"""Jalankan semua tes tugas dan hitung skor.

Pemakaian:
    python tests/jalankan_semua.py          # semua kriteria
    python tests/jalankan_semua.py 02       # hanya kriteria berawalan test_02

Bobot tiap berkas tes ada di tests/poin.json. Skrip keluar dengan kode 0
hanya bila skor penuh, sehingga tanda di GitHub hijau = semua tes lulus.
Bila dijalankan di GitHub Actions, tabel skor ditulis ke ringkasan workflow.
"""
from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

TES = pathlib.Path(__file__).resolve().parent
AKAR = TES.parent


def jalankan(berkas: pathlib.Path) -> tuple[bool, str]:
    proses = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--no-header", "-p", "no:cacheprovider", str(berkas)],
        cwd=AKAR,
        capture_output=True,
        text=True,
        timeout=120,
    )
    keluaran = proses.stdout + proses.stderr
    return proses.returncode == 0, keluaran


def ringkas_galat(keluaran: str) -> str:
    baris = [b for b in keluaran.splitlines() if b.startswith("E ") or "Error" in b or "assert" in b]
    return "\n".join(baris[:4])


def main(argv: list[str]) -> int:
    poin: dict[str, int] = json.loads((TES / "poin.json").read_text(encoding="utf-8"))
    awalan = argv[1] if len(argv) > 1 else ""
    total = maks = 0
    tabel = ["| Kriteria | Hasil | Poin |", "| --- | --- | --- |"]
    for nama, bobot in poin.items():
        if awalan and not nama.startswith(f"test_{awalan}"):
            continue
        berkas = TES / f"{nama}.py"
        maks += bobot
        lulus, keluaran = jalankan(berkas)
        if lulus:
            total += bobot
            print(f"LULUS  {nama} (+{bobot})")
            tabel.append(f"| {nama} | lulus | {bobot}/{bobot} |")
        else:
            print(f"GAGAL  {nama} (0/{bobot})")
            for baris in ringkas_galat(keluaran).splitlines():
                print(f"       {baris}")
            tabel.append(f"| {nama} | gagal | 0/{bobot} |")
    print(f"SKOR: {total} / {maks}")
    ringkasan = os.environ.get("GITHUB_STEP_SUMMARY")
    if ringkasan:
        with open(ringkasan, "a", encoding="utf-8") as f:
            f.write(f"### Skor: {total} / {maks}\n\n" + "\n".join(tabel) + "\n")
    return 0 if total == maks and maks > 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
