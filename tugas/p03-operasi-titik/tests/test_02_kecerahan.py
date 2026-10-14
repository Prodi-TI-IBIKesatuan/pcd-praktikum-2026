import numpy as np


def test_kecerahan_naik_tanpa_overflow(solusi):
    citra = np.array([[0, 100, 250, 255]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.atur_kecerahan(citra, 10), [[10, 110, 255, 255]])


def test_kecerahan_turun_tanpa_underflow(solusi):
    citra = np.array([[0, 5, 100, 255]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.atur_kecerahan(citra, -10), [[0, 0, 90, 245]])


def test_kecerahan_citra_warna(solusi, citra_bgr):
    hasil = solusi.atur_kecerahan(citra_bgr, 40)
    assert hasil.dtype == np.uint8 and hasil.shape == citra_bgr.shape
    np.testing.assert_array_equal(hasil, np.clip(citra_bgr.astype(int) + 40, 0, 255))
