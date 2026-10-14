import numpy as np


def test_histogram_warna(solusi, citra_bgr):
    hasil = solusi.histogram_warna(citra_bgr, 8)
    bagian = [np.bincount(citra_bgr[:, :, k].ravel().astype(int) * 8 // 256, minlength=8) for k in range(3)]
    harapan = np.concatenate(bagian) / (3 * citra_bgr.shape[0] * citra_bgr.shape[1])
    assert hasil.shape == (24,)
    np.testing.assert_allclose(hasil, harapan, atol=1e-12)
    assert abs(hasil.sum() - 1) < 1e-9


def test_citra_merah_murni(solusi):
    citra = np.zeros((4, 4, 3), dtype=np.uint8)
    citra[:, :, 2] = 255
    hasil = solusi.histogram_warna(citra, 4)
    np.testing.assert_allclose(hasil, np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]) / 3)
