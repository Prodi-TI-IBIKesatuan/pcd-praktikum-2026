import numpy as np
from conftest import larang


def test_konvolusi_ditulis_sendiri(solusi, citra_gray):
    assert solusi.konvolusi2d(citra_gray, np.ones((3, 3)) / 9).shape == citra_gray.shape
    larang("konvolusi2d", "filter2D", "convolve", "correlate", "convolve2d", "correlate2d", "blur", "boxFilter")
