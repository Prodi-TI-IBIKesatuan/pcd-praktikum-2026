"""Ubah ekspor skor Classroom 50 menjadi CSV impor nilai Moodle.

Masukan:
  1. CSV skor dari Classroom 50 (tombol export CSV pada halaman submissions).
     Kolom nama pengguna GitHub dan skor dideteksi otomatis; bila nama
     kolom berbeda, sebutkan dengan --kolom-user / --kolom-skor / --kolom-maks.
  2. CSV roster (privat, jangan di-commit ke repo publik) berisi minimal kolom
     nim, nama, github (email opsional) - diisi dari formulir Moodle.

Keluaran: CSV untuk Moodle (Nilai > Impor > Berkas CSV) dengan kolom
"ID number" (= NIM), "Email address", dan satu kolom item nilai 0-100.
Petakan "ID number" ke "ID number" pengguna saat impor.

Pemakaian:
    python tools/impor_nilai.py skor-p03.csv roster.csv "Tugas Praktik P03" -o moodle-p03.csv
    python tools/impor_nilai.py skor-p03.csv roster.csv "Tugas Praktik P03" --kosong-nol
"""
from __future__ import annotations

import argparse
import csv
import io
import pathlib
import sys

CALON_USER = ["github_username", "github", "username", "login", "student", "student_username", "user"]
CALON_SKOR = ["score", "points", "points_awarded", "total", "total_score", "grade", "nilai"]
CALON_MAKS = ["max_score", "points_available", "max_points", "max", "total_points"]


def _normal(nama: str) -> str:
    return nama.strip().lower().replace(" ", "_")


def _pilih(kolom: list[str], diminta: str | None, calon: list[str], wajib: bool) -> str | None:
    peta = {_normal(k): k for k in kolom}
    if diminta:
        if _normal(diminta) not in peta:
            raise SystemExit(f"Kolom '{diminta}' tidak ada. Kolom tersedia: {', '.join(kolom)}")
        return peta[_normal(diminta)]
    for c in calon:
        if c in peta:
            return peta[c]
    if wajib:
        raise SystemExit(f"Tidak menemukan kolom ({'/'.join(calon)}). Kolom tersedia: {', '.join(kolom)}")
    return None


def _angka(teks: str) -> float | None:
    teks = (teks or "").strip().replace(",", ".")
    if not teks:
        return None
    if "/" in teks:  # format "85/100"
        a, b = teks.split("/", 1)
        return float(a) / float(b) * 100 if float(b) else 0.0
    return float(teks)


def baca_skor(teks: str, kolom_user=None, kolom_skor=None, kolom_maks=None) -> tuple[dict[str, float], list[str]]:
    pembaca = csv.DictReader(io.StringIO(teks))
    kolom = pembaca.fieldnames or []
    ku = _pilih(kolom, kolom_user, CALON_USER, True)
    ks = _pilih(kolom, kolom_skor, CALON_SKOR, True)
    km = _pilih(kolom, kolom_maks, CALON_MAKS, False)
    skor: dict[str, float] = {}
    catatan: list[str] = []
    for baris in pembaca:
        user = (baris.get(ku) or "").strip().lstrip("@").lower()
        nilai = _angka(baris.get(ks, ""))
        if not user or nilai is None:
            continue
        maks = _angka(baris.get(km, "")) if km else None
        if maks:
            nilai = nilai / maks * 100
        nilai = max(0.0, min(100.0, nilai))
        if user in skor and skor[user] != nilai:
            catatan.append(f"{user}: beberapa baris skor, diambil yang tertinggi")
        skor[user] = max(nilai, skor.get(user, 0.0))
    return skor, catatan


def baca_roster(teks: str) -> list[dict[str, str]]:
    pembaca = csv.DictReader(io.StringIO(teks))
    peta = {_normal(k): k for k in pembaca.fieldnames or []}
    for wajib in ("nim", "github"):
        if wajib not in peta:
            raise SystemExit(f"Roster wajib punya kolom '{wajib}'. Kolom tersedia: {', '.join(peta.values())}")
    hasil = []
    for baris in pembaca:
        hasil.append(
            {
                "nim": baris[peta["nim"]].strip(),
                "nama": baris.get(peta.get("nama", ""), "").strip(),
                "github": baris[peta["github"]].strip().lstrip("@").lower(),
                "email": baris.get(peta.get("email", ""), "").strip(),
            }
        )
    return hasil


def gabung(skor: dict[str, float], roster: list[dict[str, str]], item: str, kosong_nol: bool):
    keluaran = io.StringIO()
    penulis = csv.writer(keluaran)
    penulis.writerow(["ID number", "Email address", item])
    tanpa_skor, dikenal = [], set()
    for mhs in roster:
        dikenal.add(mhs["github"])
        nilai = skor.get(mhs["github"])
        if nilai is None:
            tanpa_skor.append(f"{mhs['nim']} {mhs['nama']} (@{mhs['github'] or '?'})")
            if not kosong_nol:
                continue
            nilai = 0.0
        penulis.writerow([mhs["nim"], mhs["email"], f"{nilai:.2f}"])
    tak_dikenal = sorted(set(skor) - dikenal)
    return keluaran.getvalue(), tanpa_skor, tak_dikenal


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skor", type=pathlib.Path)
    parser.add_argument("roster", type=pathlib.Path)
    parser.add_argument("item", help='nama item nilai di Moodle, mis. "Tugas Praktik P03"')
    parser.add_argument("-o", "--keluaran", type=pathlib.Path)
    parser.add_argument("--kosong-nol", action="store_true", help="mahasiswa tanpa skor diberi 0")
    parser.add_argument("--kolom-user")
    parser.add_argument("--kolom-skor")
    parser.add_argument("--kolom-maks")
    arg = parser.parse_args()

    skor, catatan = baca_skor(
        arg.skor.read_text(encoding="utf-8-sig"), arg.kolom_user, arg.kolom_skor, arg.kolom_maks
    )
    roster = baca_roster(arg.roster.read_text(encoding="utf-8-sig"))
    teks, tanpa_skor, tak_dikenal = gabung(skor, roster, arg.item, arg.kosong_nol)
    tujuan = arg.keluaran or arg.skor.with_name(f"moodle-{arg.skor.stem}.csv")
    tujuan.write_text(teks, encoding="utf-8")

    print(f"{len(roster) - len(tanpa_skor)} dari {len(roster)} mahasiswa punya skor -> {tujuan}")
    for c in catatan:
        print("  catatan:", c)
    if tanpa_skor:
        print(f"  tanpa skor ({'diberi 0' if arg.kosong_nol else 'tidak ditulis'}):")
        for t in tanpa_skor:
            print("   -", t)
    if tak_dikenal:
        print("  nama pengguna GitHub tidak ada di roster (periksa formulir Moodle):")
        for t in tak_dikenal:
            print("   -", t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
