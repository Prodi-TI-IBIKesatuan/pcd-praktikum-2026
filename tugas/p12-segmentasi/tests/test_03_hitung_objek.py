import numpy as np


def test_hitung_objek(solusi):
    citra = np.zeros((20, 20), dtype=np.uint8)
    citra[1:4, 1:4] = 255
    citra[10:12, 10:15] = 255
    citra[17, 2] = 255
    citra[18, 3] = 255  # bersinggungan diagonal dengan (17, 2): satu objek
    assert solusi.hitung_objek(citra) == 3


def test_citra_kosong(solusi):
    assert solusi.hitung_objek(np.zeros((5, 5), dtype=np.uint8)) == 0
