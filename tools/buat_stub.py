"""Bangkitkan solusi.py untuk mahasiswa dari berkas kunci jawaban.

Setiap fungsi publik di kunci dipertahankan nama, parameter, dan docstring-nya,
tetapi isinya diganti dengan petunjuk dan `raise NotImplementedError`.
Fungsi/konstanta berawalan garis bawah dan isi fungsi tidak ikut tersalin,
sehingga stub tidak pernah membocorkan jawaban.

Pemakaian:
    python tools/buat_stub.py <kunci/pNN/solusi.py> <tugas/pNN-.../solusi.py>
    python tools/buat_stub.py --semua <folder-kunci>      # semua pekan
    python tools/buat_stub.py --cek <folder-kunci>        # gagal bila ada yang tidak sinkron
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import sys

AKAR = pathlib.Path(__file__).resolve().parents[1]
TUGAS = AKAR / "tugas"


def stub_dari_kunci(sumber: str) -> str:
    pohon = ast.parse(sumber)
    baris_sumber = sumber.splitlines()
    keluaran: list[str] = []

    docstring_modul = ast.get_docstring(pohon, clean=False)
    if docstring_modul is not None:
        keluaran.append(f'"""{docstring_modul}"""')

    impor = [n for n in pohon.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    if impor:
        keluaran.append("\n".join(ast.get_source_segment(sumber, n) for n in impor))

    konstanta = [
        n
        for n in pohon.body
        if isinstance(n, ast.Assign)
        and all(isinstance(t, ast.Name) and not t.id.startswith("_") for t in n.targets)
    ]
    if konstanta:
        keluaran.append("\n".join(ast.get_source_segment(sumber, n) for n in konstanta))

    for node in pohon.body:
        if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
            continue
        kepala = baris_sumber[node.lineno - 1 : node.body[0].lineno - 1]
        # Kepala fungsi bisa beberapa baris; buang baris docstring bila ikut terambil.
        kepala_teks = "\n".join(kepala).rstrip()
        doc = ast.get_docstring(node, clean=False)
        badan = []
        if doc is not None:
            badan.append(f'    """{doc}"""')
        badan.append("    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.")
        badan.append(f'    raise NotImplementedError("{node.name}() belum dikerjakan")')
        keluaran.append(kepala_teks + "\n" + "\n".join(badan))

    return "\n\n\n".join(keluaran) + "\n"


def folder_tugas(kode: str) -> pathlib.Path:
    cocok = sorted(TUGAS.glob(f"{kode}-*"))
    if len(cocok) != 1:
        raise SystemExit(f"Folder tugas untuk {kode} tidak ditemukan (atau ganda) di {TUGAS}")
    return cocok[0]


def pasangan(folder_kunci: pathlib.Path):
    for kunci in sorted(folder_kunci.glob("p[0-9][0-9]/solusi.py")):
        yield kunci, folder_tugas(kunci.parent.name) / "solusi.py"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("sumber")
    parser.add_argument("tujuan", nargs="?")
    parser.add_argument("--semua", action="store_true")
    parser.add_argument("--cek", action="store_true")
    arg = parser.parse_args()

    if arg.semua or arg.cek:
        beda = []
        for kunci, tujuan in pasangan(pathlib.Path(arg.sumber)):
            stub = stub_dari_kunci(kunci.read_text(encoding="utf-8"))
            if arg.cek:
                if not tujuan.exists() or tujuan.read_text(encoding="utf-8") != stub:
                    beda.append(str(tujuan.relative_to(AKAR)))
            else:
                tujuan.write_text(stub, encoding="utf-8")
                print(f"ditulis {tujuan.relative_to(AKAR)}")
        if beda:
            print("Stub tidak sinkron dengan kunci (jalankan --semua):\n  " + "\n  ".join(beda))
            return 1
        if arg.cek:
            print("Semua stub sinkron dengan kunci.")
        return 0

    if not arg.tujuan:
        parser.error("sebutkan berkas tujuan")
    stub = stub_dari_kunci(pathlib.Path(arg.sumber).read_text(encoding="utf-8"))
    pathlib.Path(arg.tujuan).write_text(stub, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
