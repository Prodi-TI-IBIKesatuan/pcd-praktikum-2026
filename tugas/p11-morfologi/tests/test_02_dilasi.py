import cv2
import numpy as np
import pytest
from conftest import larang


def _biner(seed):
    rng = np.random.default_rng(seed)
    return np.where(rng.random((30, 40)) > 0.55, 255, 0).astype(np.uint8)


@pytest.mark.parametrize("ukuran", [3, 5])
@pytest.mark.parametrize("seed", [1, 2])
def test_dilasi_sama_dengan_opencv(solusi, ukuran, seed):
    citra = _biner(seed)
    hasil = solusi.dilasi(citra, ukuran)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, cv2.dilate(citra, np.ones((ukuran, ukuran), np.uint8)))


def test_dilasi_ditulis_sendiri(solusi):
    solusi.dilasi(_biner(3), 3)
    larang("dilasi", "erode", "dilate", "morphologyEx")
