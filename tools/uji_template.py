"""Uji template tugas sebelum dirilis ke mahasiswa.

Untuk setiap tugas, repo template dirakit ke folder sementara lalu diuji:
  1. solusi.py bawaan (stub) HARUS mendapat skor 0   -> tes tidak bocor jawaban
  2. kunci jawaban (bila tersedia) HARUS mendapat 100 -> tes benar dan bisa dicapai
  3. poin.json total 100 dan setiap berkas tes punya bobot, begitu pula sebaliknya

Pemakaian:
    python tools/uji_template.py                         # semua tugas, tanpa kunci
    python tools/uji_template.py --kunci ../pcd-kunci     # semua tugas, dengan kunci
    python tools/uji_template.py p07 --kunci ../pcd-kunci
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from rakit_template import daftar_tugas, rakit  # noqa: E402

SKOR = re.compile(r"SKOR: (\d+) / (\d+)")


def skor(folder: pathlib.Path) -> tuple[int, int, str]:
    proses = subprocess.run(
        [sys.executable, "tests/jalankan_semua.py"], cwd=folder, capture_output=True, text=True, timeout=600
    )
    cocok = SKOR.search(proses.stdout)
    if not cocok:
        return -1, -1, proses.stdout + proses.stderr
    return int(cocok.group(1)), int(cocok.group(2)), proses.stdout


def cek_poin(folder: pathlib.Path) -> list[str]:
    masalah = []
    poin = json.loads((folder / "tests" / "poin.json").read_text(encoding="utf-8"))
    berkas = {p.stem for p in (folder / "tests").glob("test_*.py")}
    if sum(poin.values()) != 100:
        masalah.append(f"total poin {sum(poin.values())}, seharusnya 100")
    if set(poin) != berkas:
        masalah.append(f"poin.json dan berkas tes tidak cocok: {sorted(set(poin) ^ berkas)}")
    return masalah


def uji(folder_tugas: pathlib.Path, kunci: pathlib.Path | None) -> bool:
    kode = folder_tugas.name[:3]
    with tempfile.TemporaryDirectory() as tmp:
        repo = rakit(folder_tugas, pathlib.Path(tmp))
        masalah = cek_poin(repo)
        nilai, maks, log = skor(repo)
        status_stub = f"stub: {nilai}/{maks}"
        if nilai != 0:
            masalah.append(f"stub mendapat {nilai}/{maks}, seharusnya 0\n{log}")
        status_kunci = "kunci: dilewati"
        berkas_kunci = kunci / kode / "solusi.py" if kunci else None
        if berkas_kunci and berkas_kunci.exists():
            shutil.copy(berkas_kunci, repo / "solusi.py")
            nilai, maks, log = skor(repo)
            status_kunci = f"kunci: {nilai}/{maks}"
            if (nilai, maks) != (100, 100):
                masalah.append(f"kunci mendapat {nilai}/{maks}, seharusnya 100/100\n{log}")
        elif kunci:
            masalah.append(f"kunci {berkas_kunci} tidak ditemukan")
    hasil = "OK   " if not masalah else "GAGAL"
    print(f"{hasil} {folder_tugas.name:28s} {status_stub}  {status_kunci}")
    for m in masalah:
        print("      - " + m.replace("\n", "\n        "))
    return not masalah


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kode", nargs="?", help="mis. p07; kosongkan untuk semua tugas")
    parser.add_argument("--kunci", type=pathlib.Path, help="folder berisi pNN/solusi.py")
    arg = parser.parse_args()
    folder = [f for f in daftar_tugas() if not arg.kode or f.name.startswith(f"{arg.kode}-")]
    if not folder:
        print("Tidak ada tugas yang cocok.")
        return 1
    hasil = [uji(f, arg.kunci) for f in folder]
    print(f"\n{sum(hasil)}/{len(hasil)} template siap rilis.")
    return 0 if all(hasil) else 1


if __name__ == "__main__":
    sys.exit(main())
