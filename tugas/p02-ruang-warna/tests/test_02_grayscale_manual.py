import numpy as np
from conftest import larang


def test_tanpa_cvtcolor(solusi, citra_bgr):
    assert solusi.ke_grayscale(citra_bgr).dtype == np.uint8
    larang("ke_grayscale", "cvtColor")


def test_putih_dan_hitam(solusi):
    citra = np.zeros((2, 2, 3), dtype=np.uint8)
    citra[0, 0] = 255
    hasil = solusi.ke_grayscale(citra)
    assert hasil[0, 0] == 255 and hasil[1, 1] == 0
