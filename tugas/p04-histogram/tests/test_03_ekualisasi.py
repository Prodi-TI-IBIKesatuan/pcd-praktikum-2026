import cv2
import numpy as np
from conftest import larang


def test_ekualisasi_sama_dengan_opencv(solusi, citra_gray):
    gelap = (citra_gray // 3).astype(np.uint8)
    hasil = solusi.ekualisasi(gelap)
    assert hasil.dtype == np.uint8 and hasil.shape == gelap.shape
    np.testing.assert_array_equal(hasil, cv2.equalizeHist(gelap))
    larang("ekualisasi", "equalizeHist")


def test_ekualisasi_memperlebar_rentang(solusi, citra_gray):
    sempit = (100 + citra_gray // 8).astype(np.uint8)
    hasil = solusi.ekualisasi(sempit)
    assert hasil.max() == 255 and hasil.min() == 0
