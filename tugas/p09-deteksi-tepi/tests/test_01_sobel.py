import cv2
import numpy as np
from conftest import larang


def test_sobel_sama_dengan_opencv(solusi, citra_gray):
    gx, gy, mag = solusi.sobel(citra_gray)
    f = citra_gray.astype(np.float64)
    rx = cv2.Sobel(f, cv2.CV_64F, 1, 0, ksize=3)
    ry = cv2.Sobel(f, cv2.CV_64F, 0, 1, ksize=3)
    np.testing.assert_allclose(gx, rx, atol=1e-9)
    np.testing.assert_allclose(gy, ry, atol=1e-9)
    np.testing.assert_allclose(mag, np.hypot(rx, ry), atol=1e-9)


def test_sobel_tepi_vertikal(solusi):
    citra = np.zeros((10, 10), dtype=np.uint8)
    citra[:, 5:] = 200
    gx, gy, _ = solusi.sobel(citra)
    assert np.abs(gx[:, 4:6]).min() > 0 and np.allclose(gy, 0)
    larang("sobel", "Sobel", "filter2D", "Scharr", "convolve", "correlate")
