import numpy as np
from conftest import larang


def test_balik_horizontal(solusi, citra_bgr):
    np.testing.assert_array_equal(solusi.balik_horizontal(citra_bgr), citra_bgr[:, ::-1])
    larang("balik_horizontal", "flip", "fliplr")


def test_balik_dua_kali(solusi, citra_gray):
    np.testing.assert_array_equal(solusi.balik_horizontal(solusi.balik_horizontal(citra_gray)), citra_gray)
