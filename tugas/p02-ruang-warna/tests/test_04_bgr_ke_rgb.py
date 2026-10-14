import numpy as np


def test_bgr_ke_rgb(solusi, citra_bgr):
    hasil = solusi.bgr_ke_rgb(citra_bgr)
    np.testing.assert_array_equal(hasil[:, :, 0], citra_bgr[:, :, 2])
    np.testing.assert_array_equal(hasil[:, :, 2], citra_bgr[:, :, 0])
    np.testing.assert_array_equal(hasil[:, :, 1], citra_bgr[:, :, 1])
