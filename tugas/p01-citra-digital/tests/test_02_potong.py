import numpy as np


def test_potong_nilai(solusi, citra_bgr):
    hasil = solusi.potong(citra_bgr, 10, 5, 20, 12)
    assert hasil.shape == (12, 20, 3)
    np.testing.assert_array_equal(hasil, citra_bgr[5:17, 10:30])


def test_potong_adalah_salinan(solusi, citra_gray):
    asli = citra_gray.copy()
    hasil = solusi.potong(citra_gray, 0, 0, 4, 4)
    hasil[:] = 0
    np.testing.assert_array_equal(citra_gray, asli), "mengubah potongan tidak boleh mengubah citra asli"


def test_potong_seluruh_citra(solusi, citra_gray):
    np.testing.assert_array_equal(solusi.potong(citra_gray, 0, 0, 52, 40), citra_gray)
