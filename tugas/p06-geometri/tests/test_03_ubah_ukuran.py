import cv2
import numpy as np
import pytest
from conftest import larang


@pytest.mark.parametrize("skala", [2, 3, 0.5, 1.5, 0.37])
def test_ubah_ukuran_sama_dengan_opencv(solusi, citra_bgr, skala):
    hasil = solusi.ubah_ukuran_terdekat(citra_bgr, skala)
    tinggi, lebar = round(48 * skala), round(64 * skala)
    assert hasil.shape == (tinggi, lebar, 3)
    referensi = cv2.resize(citra_bgr, (lebar, tinggi), interpolation=cv2.INTER_NEAREST)
    np.testing.assert_array_equal(hasil, referensi)


def test_tanpa_cv2_resize(solusi, citra_gray):
    assert solusi.ubah_ukuran_terdekat(citra_gray, 2).shape == (80, 104)
    larang("ubah_ukuran_terdekat", "resize")
