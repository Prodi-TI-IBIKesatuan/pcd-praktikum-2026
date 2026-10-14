"""Bangkitkan tugas/pNN-*/README.md (halaman depan repo tugas mahasiswa).

Isi diambil dari solusi.py (judul, daftar fungsi + docstring) dan poin.json,
sehingga README tidak pernah berbeda dari tes.

Pemakaian:
    python tools/buat_readme_tugas.py          # tulis ulang
    python tools/buat_readme_tugas.py --cek    # gagal bila tidak sinkron
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import sys

AKAR = pathlib.Path(__file__).resolve().parents[1]
REPO = "Prodi-TI-IBIKesatuan/pcd-praktikum-2026"


def bangun(tugas: pathlib.Path) -> str:
    sumber = (tugas / "solusi.py").read_text(encoding="utf-8")
    pohon = ast.parse(sumber)
    judul = (ast.get_docstring(pohon) or tugas.name).splitlines()[0].rstrip(".")
    pekan = tugas.name[1:3]
    modul = next(iter(sorted((AKAR / "modul").glob(f"pekan-{pekan}-*"))), None)
    poin = json.loads((tugas / "tests" / "poin.json").read_text(encoding="utf-8"))
    fungsi = [n for n in pohon.body if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")]

    baris = [f"# {judul}", ""]
    if modul:
        colab = f"https://colab.research.google.com/github/{REPO}/blob/main/modul/{modul.name}/latihan.ipynb"
        baris += [
            f"[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab})"
            f" · [Materi pekan {pekan}](https://github.com/{REPO}/tree/main/modul/{modul.name})",
            "",
        ]
    baris += [
        "Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai:"
        " tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.",
        "",
        "## Fungsi yang dikerjakan",
        "",
    ]
    for f in fungsi:
        argumen = ", ".join(a.arg for a in f.args.args)
        doc = ast.get_docstring(f) or ""
        baris += [f"### `{f.name}({argumen})`", "", doc, ""]
    baris += ["## Penilaian", "", "| Kriteria | Poin |", "| --- | --- |"]
    baris += [f"| {k.split('_', 2)[-1].replace('_', ' ')} | {v} |" for k, v in poin.items()]
    baris += [
        f"| **Total** | **{sum(poin.values())}** |",
        "",
        "## Cara mengerjakan dari HP",
        "",
        "1. Berlatih di notebook Colab (tombol di atas) sampai hasilnya benar.",
        "2. Di halaman repo ini buka `solusi.py` → ikon pensil → tempel jawaban → hapus baris"
        " `raise NotImplementedError` → **Commit changes**.",
        "3. Tunggu tanda kuning berubah hijau/merah. Merah? Ketuk tanda → *Details* untuk melihat kriteria yang gagal.",
        "4. Isi `CATATAN.md` dan unggah tangkapan layar hasil ke folder `bukti/`.",
        "",
        "## Cara mengerjakan dari laptop",
        "",
        "Tekan **Code → Codespaces → Create codespace on main**, atau di komputer sendiri:",
        "",
        "```bash",
        "pip install -r requirements.txt",
        "python tests/jalankan_semua.py        # semua kriteria + skor",
        "python -m pytest -q tests/test_01_*.py  # satu kriteria",
        "```",
        "",
        "Jangan mengubah isi folder `tests/` dan `.github/`; perubahan di sana tidak dihitung dan dapat dianggap pelanggaran.",
        "",
    ]
    return "\n".join(baris)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cek", action="store_true")
    arg = parser.parse_args()
    beda = []
    for tugas in sorted((AKAR / "tugas").glob("p[0-9][0-9]-*")):
        teks = bangun(tugas)
        berkas = tugas / "README.md"
        if arg.cek:
            if not berkas.exists() or berkas.read_text(encoding="utf-8") != teks:
                beda.append(str(berkas.relative_to(AKAR)))
        else:
            berkas.write_text(teks, encoding="utf-8")
            print(f"ditulis {berkas.relative_to(AKAR)}")
    if beda:
        print("README tugas tidak sinkron (jalankan tools/buat_readme_tugas.py):\n  " + "\n  ".join(beda))
        return 1
    if arg.cek:
        print("Semua README tugas sinkron.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
