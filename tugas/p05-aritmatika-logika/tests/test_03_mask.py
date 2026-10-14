import numpy as np


def _mask(bentuk):
    m = np.zeros(bentuk, dtype=np.uint8)
    m[10:30, 15:40] = 255
    return m


def test_mask_keabuan(solusi, citra_gray):
    m = _mask(citra_gray.shape)
    hasil = solusi.terapkan_mask(citra_gray, m)
    np.testing.assert_array_equal(hasil, np.where(m > 0, citra_gray, 0))


def test_mask_warna(solusi, citra_bgr):
    m = _mask(citra_bgr.shape[:2])
    hasil = solusi.terapkan_mask(citra_bgr, m)
    assert hasil.shape == citra_bgr.shape and hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil[15, 20], citra_bgr[15, 20])
    np.testing.assert_array_equal(hasil[0, 0], [0, 0, 0])
