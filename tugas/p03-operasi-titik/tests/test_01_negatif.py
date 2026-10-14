import numpy as np


def test_negatif(solusi, citra_bgr):
    hasil = solusi.negatif(citra_bgr)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, 255 - citra_bgr.astype(int))


def test_negatif_dua_kali_kembali_asli(solusi, citra_gray):
    np.testing.assert_array_equal(solusi.negatif(solusi.negatif(citra_gray)), citra_gray)
