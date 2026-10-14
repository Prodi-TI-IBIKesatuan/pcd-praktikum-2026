import cv2
import numpy as np
import pytest
from conftest import larang


@pytest.mark.parametrize("ukuran, sigma", [(3, 1.0), (5, 1.2), (7, 2.5)])
def test_kernel_gauss(solusi, ukuran, sigma):
    hasil = solusi.kernel_gauss(ukuran, sigma)
    satu_d = cv2.getGaussianKernel(ukuran, sigma)
    assert hasil.shape == (ukuran, ukuran)
    np.testing.assert_allclose(hasil, satu_d @ satu_d.T, atol=1e-9)
    assert abs(hasil.sum() - 1) < 1e-9


def test_tanpa_fungsi_siap_pakai(solusi):
    solusi.kernel_gauss(3, 1.0)
    larang("kernel_gauss", "getGaussianKernel", "GaussianBlur")


def test_ukuran_genap_ditolak(solusi):
    with pytest.raises(ValueError):
        solusi.kernel_gauss(4, 1.0)
