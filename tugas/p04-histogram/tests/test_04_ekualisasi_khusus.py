import numpy as np


def test_citra_seragam_tidak_rusak(solusi):
    citra = np.full((6, 6), 77, dtype=np.uint8)
    np.testing.assert_array_equal(solusi.ekualisasi(citra), citra)


def test_dua_nilai(solusi):
    citra = np.array([[10, 10, 200, 200]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.ekualisasi(citra), [[0, 0, 255, 255]])
