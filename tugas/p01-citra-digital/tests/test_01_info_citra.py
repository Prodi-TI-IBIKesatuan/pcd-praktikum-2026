import numpy as np


def test_info_citra_warna(solusi, citra_bgr):
    assert solusi.info_citra(citra_bgr) == {"tinggi": 48, "lebar": 64, "kanal": 3, "tipe": "uint8"}


def test_info_citra_keabuan(solusi, citra_gray):
    assert solusi.info_citra(citra_gray) == {"tinggi": 40, "lebar": 52, "kanal": 1, "tipe": "uint8"}


def test_info_citra_float(solusi):
    citra = np.zeros((5, 7), dtype=np.float32)
    assert solusi.info_citra(citra)["tipe"] == "float32"
