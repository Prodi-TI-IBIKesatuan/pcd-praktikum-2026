import cv2
import numpy as np


def test_filter_rerata(solusi, citra_gray):
    hasil = solusi.filter_rerata(citra_gray, 3)
    assert hasil.dtype == np.uint8
    referensi = cv2.blur(citra_gray, (3, 3), borderType=cv2.BORDER_CONSTANT)
    assert np.abs(hasil.astype(int) - referensi).max() <= 1


def test_filter_rerata_citra_datar(solusi):
    citra = np.full((9, 9), 90, dtype=np.uint8)
    assert solusi.filter_rerata(citra, 3)[4, 4] == 90
