"""Bangkitkan docs/classroom50-tes.md: daftar tes autograding per assignment.

Dosen/DLS menyalin isi tabel ini ke formulir assignment di Classroom 50
(tipe tes "Run command", kode keluar 0 = lulus). Sumber kebenaran adalah
tests/poin.json di setiap tugas, jadi tabel tidak pernah berbeda dari tes.

Pemakaian:
    python tools/buat_konfigurasi_classroom50.py         # tulis ulang
    python tools/buat_konfigurasi_classroom50.py --cek   # gagal bila tidak sinkron
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

AKAR = pathlib.Path(__file__).resolve().parents[1]
TUJUAN = AKAR / "docs" / "classroom50-tes.md"
TIMEOUT_MENIT = 2


def bangun() -> str:
    baris = [
        "# Konfigurasi tes Classroom 50",
        "",
        "Berkas ini dibangkitkan otomatis oleh `tools/buat_konfigurasi_classroom50.py` dari `tests/poin.json`."
        " Jangan diedit manual.",
        "",
        "Pengaturan umum setiap assignment: template repo `Prodi-TI-IBIKesatuan/pcd-tugas-<folder>`, tipe individu,"
        " tenggat **Minggu 23.59 WIB**, *feedback pull request* aktif. Setiap baris di bawah = satu tes bertipe"
        f" **Run command** (lulus bila kode keluar 0), *setup command* `python -m pip install -q -r requirements.txt`,"
        f" timeout {TIMEOUT_MENIT} menit.",
        "",
    ]
    for tugas in sorted((AKAR / "tugas").glob("p[0-9][0-9]-*")):
        poin = json.loads((tugas / "tests" / "poin.json").read_text(encoding="utf-8"))
        judul = (tugas / "solusi.py").read_text(encoding="utf-8").splitlines()[0].strip('"').rstrip(".")
        baris += [f"## {tugas.name}", "", f"{judul}. Repo template: `pcd-tugas-{tugas.name}`.", ""]
        baris += ["| Nama tes | Perintah | Poin |", "| --- | --- | --- |"]
        for nama, bobot in poin.items():
            label = nama.split("_", 2)[-1].replace("_", " ")
            baris.append(f"| {label} | `python -m pytest -q tests/{nama}.py` | {bobot} |")
        baris += [f"| **Total** | | **{sum(poin.values())}** |", ""]
    return "\n".join(baris)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cek", action="store_true")
    arg = parser.parse_args()
    teks = bangun()
    if arg.cek:
        if not TUJUAN.exists() or TUJUAN.read_text(encoding="utf-8") != teks:
            print("docs/classroom50-tes.md tidak sinkron; jalankan tools/buat_konfigurasi_classroom50.py")
            return 1
        print("Konfigurasi Classroom 50 sinkron.")
        return 0
    TUJUAN.parent.mkdir(exist_ok=True)
    TUJUAN.write_text(teks, encoding="utf-8")
    print(f"ditulis {TUJUAN.relative_to(AKAR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
