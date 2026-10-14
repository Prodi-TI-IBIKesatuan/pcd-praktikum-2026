import cv2
import numpy as np


def test_selisih_tanpa_overflow(solusi):
    a = np.array([[10, 200]], dtype=np.uint8)
    b = np.array([[20, 50]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.selisih_absolut(a, b), [[10, 150]])


def test_selisih_sama_dengan_absdiff(solusi, citra_bgr):
    b = np.roll(citra_bgr, 3, axis=1)
    hasil = solusi.selisih_absolut(citra_bgr, b)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, cv2.absdiff(citra_bgr, b))
