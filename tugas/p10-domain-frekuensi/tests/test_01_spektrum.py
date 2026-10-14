import numpy as np


def test_spektrum(solusi, citra_gray):
    hasil = solusi.spektrum_magnitudo(citra_gray)
    harapan = np.log1p(np.abs(np.fft.fftshift(np.fft.fft2(citra_gray.astype(float)))))
    assert hasil.shape == citra_gray.shape
    np.testing.assert_allclose(hasil, harapan, rtol=1e-9)


def test_puncak_di_tengah(solusi, citra_gray):
    hasil = solusi.spektrum_magnitudo(citra_gray)
    assert np.unravel_index(np.argmax(hasil), hasil.shape) == (20, 26)
