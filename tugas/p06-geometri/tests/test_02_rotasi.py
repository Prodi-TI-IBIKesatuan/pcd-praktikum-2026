import numpy as np
import pytest
from conftest import larang


@pytest.mark.parametrize("k", [1, 2, 3, 4, -1, 5])
def test_rotasi(solusi, citra_bgr, k):
    np.testing.assert_array_equal(solusi.rotasi_90(citra_bgr, k), np.rot90(citra_bgr, k))


def test_rotasi_arah(solusi):
    citra = np.array([[1, 2], [3, 4]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.rotasi_90(citra, 1), [[2, 4], [1, 3]])
    larang("rotasi_90", "rot90", "rotate")
