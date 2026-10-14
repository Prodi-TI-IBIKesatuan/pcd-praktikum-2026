import numpy as np


def _referensi(citra, radius):
    f = np.fft.fftshift(np.fft.fft2(citra.astype(float)))
    t, l = citra.shape
    y, x = np.ogrid[:t, :l]
    f *= (y - t // 2) ** 2 + (x - l // 2) ** 2 <= radius ** 2
    return np.real(np.fft.ifft2(np.fft.ifftshift(f)))


def test_lowpass(solusi, citra_gray):
    np.testing.assert_allclose(solusi.lowpass_ideal(citra_gray, 6), _referensi(citra_gray, 6), atol=1e-8)


def test_radius_besar_mengembalikan_asli(solusi, citra_gray):
    np.testing.assert_allclose(solusi.lowpass_ideal(citra_gray, 1000), citra_gray, atol=1e-8)


def test_radius_nol_menyisakan_rerata(solusi, citra_gray):
    np.testing.assert_allclose(solusi.lowpass_ideal(citra_gray, 0), citra_gray.mean(), atol=1e-8)
