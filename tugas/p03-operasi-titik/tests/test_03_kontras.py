import numpy as np


def test_kontras(solusi, citra_gray):
    hasil = solusi.atur_kontras(citra_gray, 1.5)
    harapan = np.clip(np.rint(1.5 * (citra_gray.astype(float) - 128) + 128), 0, 255)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, harapan)


def test_kontras_satu_tidak_berubah(solusi, citra_gray):
    np.testing.assert_array_equal(solusi.atur_kontras(citra_gray, 1.0), citra_gray)


def test_kontras_nol_menjadi_abu(solusi, citra_gray):
    assert np.all(solusi.atur_kontras(citra_gray, 0.0) == 128)
