"""Rakit satu folder tugas menjadi repo template mandiri yang siap di-push.

Isi repo template = berkas bersama tugas/_umum + isi folder tugas/pNN-*.
Berkas di folder tugas menimpa berkas bersama bila namanya sama.

Pemakaian:
    python tools/rakit_template.py p03 build/            # -> build/pcd-tugas-p03-operasi-titik/
    python tools/rakit_template.py --semua build/
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import sys

AKAR = pathlib.Path(__file__).resolve().parents[1]
TUGAS = AKAR / "tugas"
UMUM = TUGAS / "_umum"
ABAIKAN = shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc")


def daftar_tugas() -> list[pathlib.Path]:
    return sorted(p for p in TUGAS.glob("p[0-9][0-9]-*") if p.is_dir())


def cari(kode: str) -> pathlib.Path:
    for folder in daftar_tugas():
        if folder.name.startswith(f"{kode}-"):
            return folder
    raise SystemExit(f"Tugas {kode} tidak ditemukan")


def nama_repo(folder: pathlib.Path) -> str:
    return f"pcd-tugas-{folder.name}"


def rakit(folder: pathlib.Path, keluaran: pathlib.Path) -> pathlib.Path:
    tujuan = keluaran / nama_repo(folder)
    if tujuan.exists():
        shutil.rmtree(tujuan)
    shutil.copytree(UMUM, tujuan, ignore=ABAIKAN)
    shutil.copytree(folder, tujuan, dirs_exist_ok=True, ignore=ABAIKAN)
    return tujuan


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kode", nargs="?", help="mis. p03")
    parser.add_argument("keluaran", type=pathlib.Path)
    parser.add_argument("--semua", action="store_true")
    arg = parser.parse_args()
    arg.keluaran.mkdir(parents=True, exist_ok=True)
    folder = daftar_tugas() if arg.semua else [cari(arg.kode)]
    for f in folder:
        print(rakit(f, arg.keluaran))
    return 0


if __name__ == "__main__":
    sys.exit(main())
