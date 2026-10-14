import sys
import pathlib

import cv2
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pipeline import bangun_indeks, cari, ekstrak_fitur  # noqa: E402


def _warna(b, g, r):
    citra = np.zeros((32, 32, 3), np.uint8)
    citra[:] = (b, g, r)
    return citra


def test_fitur_ternormalisasi():
    f = ekstrak_fitur(_warna(10, 200, 30))
    assert f.shape == (512,) and abs(f.sum() - 1) < 1e-6


def test_cari_mengembalikan_warna_serupa(tmp_path):
    for nama, warna in {"merah": (0, 0, 220), "merah2": (10, 10, 200), "hijau": (0, 200, 0), "biru": (220, 0, 0)}.items():
        cv2.imwrite(str(tmp_path / f"{nama}.png"), _warna(*warna))
    berkas, fitur = bangun_indeks(tmp_path)
    assert len(berkas) == 4
    hasil = cari(_warna(5, 5, 210), berkas, fitur, k=2)
    assert {p.stem for p, _ in hasil} == {"merah", "merah2"}
    assert hasil[0][1] >= hasil[1][1]


def test_galeri_kosong(tmp_path):
    berkas, fitur = bangun_indeks(tmp_path)
    assert berkas == [] and cari(_warna(1, 2, 3), berkas, fitur) == []
