import numpy as np


def test_histogram(solusi, citra_gray):
    hasil = np.asarray(solusi.histogram(citra_gray))
    assert hasil.shape == (256,)
    np.testing.assert_array_equal(hasil, np.bincount(citra_gray.ravel(), minlength=256))
    assert hasil.sum() == citra_gray.size
