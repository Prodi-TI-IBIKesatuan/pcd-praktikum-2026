import numpy as np
from conftest import larang


def test_biner(solusi, citra_gray):
    hasil = solusi.ke_biner(citra_gray, 100)
    assert hasil.dtype == np.uint8
    np.testing.assert_array_equal(hasil, np.where(citra_gray > 100, 255, 0))
    larang("ke_biner", "threshold")


def test_biner_tepat_di_ambang(solusi):
    citra = np.array([[99, 100, 101]], dtype=np.uint8)
    np.testing.assert_array_equal(solusi.ke_biner(citra, 100), [[0, 0, 255]])
