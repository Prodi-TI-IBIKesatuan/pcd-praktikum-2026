import cv2
import numpy as np
import pytest
from conftest import larang


def _biner(seed):
    rng = np.random.default_rng(seed)
    return np.where(rng.random((30, 40)) > 0.55, 255, 0).astype(np.uint8)


@pytest.mark.parametrize("ukuran", [3, 5])
@pytest.mark.parametrize("seed", [1, 2])
def test_erosi_sama_dengan_opencv(solusi, ukuran, seed):
    citra = _biner(seed)
    hasil = solusi.erosi(citra, ukuran)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, cv2.erode(citra, np.ones((ukuran, ukuran), np.uint8)))


def test_erosi_ditulis_sendiri(solusi):
    solusi.erosi(_biner(3), 3)
    larang("erosi", "erode", "dilate", "morphologyEx")
