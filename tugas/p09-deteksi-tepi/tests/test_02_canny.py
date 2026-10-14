import cv2
import numpy as np


def test_canny(solusi, citra_gray):
    hasil = solusi.tepi_canny(citra_gray, 50, 150)
    assert hasil.dtype == np.uint8 and set(np.unique(hasil)) <= {0, 255}
    np.testing.assert_array_equal(hasil, cv2.Canny(citra_gray, 50, 150))
