import numpy as np


def test_rasio_tepi(solusi):
    tepi = np.zeros((10, 10), dtype=np.uint8)
    tepi[0, :] = 255
    assert abs(solusi.rasio_tepi(tepi) - 0.1) < 1e-12
    assert solusi.rasio_tepi(np.zeros((4, 4), dtype=np.uint8)) == 0.0
