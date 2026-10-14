"""Tes untuk alat bantu di folder tools/."""
import ast
import pathlib
import sys

import pytest

ALAT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ALAT))

import buat_stub  # noqa: E402
import impor_nilai  # noqa: E402

KUNCI_CONTOH = '''"""Pekan 99 - contoh."""
import numpy as np

KONSTANTA = 3
_RAHASIA = 42


def _bantu(x):
    return x * _RAHASIA


def tambah(a, b=1):
    """Jumlahkan a dan b."""
    return _bantu(a) + b


def kali(
    a,
    b,
):
    return a * b
'''


def test_stub_tidak_membocorkan_jawaban():
    stub = buat_stub.stub_dari_kunci(KUNCI_CONTOH)
    assert "_RAHASIA" not in stub and "_bantu" not in stub and "return" not in stub
    assert "KONSTANTA = 3" in stub and "import numpy as np" in stub
    assert '"""Jumlahkan a dan b."""' in stub
    pohon = ast.parse(stub)
    fungsi = {n.name: n for n in pohon.body if isinstance(n, ast.FunctionDef)}
    assert set(fungsi) == {"tambah", "kali"}
    assert [a.arg for a in fungsi["kali"].args.args] == ["a", "b"]


def test_stub_melempar_not_implemented():
    ruang = {}
    exec(buat_stub.stub_dari_kunci(KUNCI_CONTOH), ruang)  # noqa: S102
    with pytest.raises(NotImplementedError):
        ruang["tambah"](1)


ROSTER = "nim,nama,github,email\n2401,Budi,BudiS,budi@kampus.ac.id\n2402,Sari,@sari-dev,sari@kampus.ac.id\n2403,Dewi,dewi99,\n"


def test_impor_nilai_kolom_otomatis_dan_skala():
    skor_csv = "Student Username,Points Awarded,Points Available\nbudis,45,50\nsari-dev,100,100\norang-asing,70,100\n"
    skor, _ = impor_nilai.baca_skor(skor_csv)
    assert skor == {"budis": 90.0, "sari-dev": 100.0, "orang-asing": 70.0}
    teks, tanpa, asing = impor_nilai.gabung(skor, impor_nilai.baca_roster(ROSTER), "Tugas P03", False)
    baris = teks.strip().splitlines()
    assert baris[0] == "ID number,Email address,Tugas P03"
    assert baris[1:] == ["2401,budi@kampus.ac.id,90.00", "2402,sari@kampus.ac.id,100.00"]
    assert tanpa == ["2403 Dewi (@dewi99)"] and asing == ["orang-asing"]


def test_impor_nilai_kosong_nol_dan_duplikat():
    skor_csv = "login,score\ndewi99,40\ndewi99,85/100\n"
    skor, catatan = impor_nilai.baca_skor(skor_csv)
    assert skor == {"dewi99": 85.0} and catatan
    teks, _, _ = impor_nilai.gabung(skor, impor_nilai.baca_roster(ROSTER), "P03", True)
    assert "2401,budi@kampus.ac.id,0.00" in teks and "2403,,85.00" in teks


def test_impor_nilai_kolom_tidak_ada():
    with pytest.raises(SystemExit):
        impor_nilai.baca_skor("nama,nilai_akhir\nbudi,90\n")
