import numpy as np
from conftest import larang


def test_otsu_ditulis_sendiri(solusi, citra_gray):
    assert 0 <= solusi.ambang_otsu(citra_gray) <= 255
    larang("ambang_otsu", "threshold", "threshold_otsu")
