import cv2
import numpy as np


def test_grayscale_rumus(solusi, citra_bgr):
    hasil = solusi.ke_grayscale(citra_bgr)
    b, g, r = (citra_bgr[:, :, i].astype(float) for i in range(3))
    harapan = np.rint(0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
    assert hasil.shape == (48, 64) and hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, harapan)


def test_grayscale_mendekati_opencv(solusi, citra_bgr):
    referensi = cv2.cvtColor(citra_bgr, cv2.COLOR_BGR2GRAY).astype(int)
    assert np.abs(solusi.ke_grayscale(citra_bgr).astype(int) - referensi).max() <= 1
