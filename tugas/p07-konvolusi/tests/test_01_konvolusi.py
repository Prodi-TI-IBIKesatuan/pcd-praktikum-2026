import cv2
import numpy as np


def _referensi(citra, kernel):
    return cv2.filter2D(citra.astype(np.float64), -1, np.asarray(kernel, float), borderType=cv2.BORDER_CONSTANT)


def test_konvolusi_identitas(solusi, citra_gray):
    kernel = np.zeros((3, 3))
    kernel[1, 1] = 1
    hasil = solusi.konvolusi2d(citra_gray, kernel)
    assert hasil.dtype == np.float64 and hasil.shape == citra_gray.shape
    np.testing.assert_allclose(hasil, citra_gray)


def test_konvolusi_tajam(solusi, citra_gray):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=float)
    np.testing.assert_allclose(solusi.konvolusi2d(citra_gray, kernel), _referensi(citra_gray, kernel), atol=1e-9)


def test_kernel_5x5(solusi, citra_gray):
    kernel = np.arange(25, dtype=float).reshape(5, 5) / 25
    np.testing.assert_allclose(solusi.konvolusi2d(citra_gray, kernel), _referensi(citra_gray, kernel), atol=1e-9)
