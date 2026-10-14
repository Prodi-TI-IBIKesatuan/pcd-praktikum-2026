import cv2
import numpy as np


def test_opening_menghapus_bintik(solusi):
    citra = np.zeros((20, 20), dtype=np.uint8)
    citra[5:15, 5:15] = 255
    citra[1, 1] = 255
    hasil = solusi.opening(citra, 3)
    assert hasil[1, 1] == 0 and hasil[10, 10] == 255


def test_opening_sama_dengan_opencv(solusi):
    rng = np.random.default_rng(4)
    citra = np.where(rng.random((30, 40)) > 0.4, 255, 0).astype(np.uint8)
    referensi = cv2.morphologyEx(citra, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    np.testing.assert_array_equal(solusi.opening(citra, 3), referensi)
