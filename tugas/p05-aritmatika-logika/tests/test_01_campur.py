import cv2
import numpy as np
import pytest


def test_campur(solusi, citra_bgr):
    b = 255 - citra_bgr
    hasil = solusi.campur(citra_bgr, b, 0.3)
    harapan = np.rint(0.3 * citra_bgr.astype(float) + 0.7 * b.astype(float))
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, harapan)
    assert np.abs(hasil.astype(int) - cv2.addWeighted(citra_bgr, 0.3, b, 0.7, 0)).max() <= 1


def test_campur_ujung(solusi, citra_bgr):
    b = np.zeros_like(citra_bgr)
    np.testing.assert_array_equal(solusi.campur(citra_bgr, b, 1.0), citra_bgr)
    np.testing.assert_array_equal(solusi.campur(citra_bgr, b, 0.0), b)


def test_campur_ukuran_beda(solusi, citra_bgr, citra_gray):
    with pytest.raises(ValueError):
        solusi.campur(citra_bgr, citra_gray, 0.5)
    with pytest.raises(ValueError):
        solusi.campur(citra_bgr, citra_bgr, 1.5)
