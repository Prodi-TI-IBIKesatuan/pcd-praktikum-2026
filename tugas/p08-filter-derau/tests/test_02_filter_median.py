import cv2
import numpy as np
import pytest
from conftest import larang


@pytest.mark.parametrize("ukuran", [3, 5])
def test_median_sama_dengan_opencv(solusi, citra_gray, ukuran):
    hasil = solusi.filter_median(citra_gray, ukuran)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, cv2.medianBlur(citra_gray, ukuran))


def test_median_membersihkan_derau(solusi):
    citra = np.full((15, 15), 100, dtype=np.uint8)
    citra[7, 7] = 255
    citra[3, 10] = 0
    assert np.all(solusi.filter_median(citra, 3) == 100)
    larang("filter_median", "medianBlur")
