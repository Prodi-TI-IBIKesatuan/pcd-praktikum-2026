import numpy as np
from conftest import larang


def test_histogram_tanpa_fungsi_siap_pakai(solusi, citra_gray):
    assert len(solusi.histogram(citra_gray)) == 256
    larang("histogram", "calcHist", "histogram", "bincount", "unique")
