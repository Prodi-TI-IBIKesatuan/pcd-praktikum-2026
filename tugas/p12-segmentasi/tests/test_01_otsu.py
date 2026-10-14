import cv2
import numpy as np
import pytest


def _bimodal(seed):
    rng = np.random.default_rng(seed)
    nilai = np.concatenate([rng.normal(60, 15, 1000), rng.normal(170, 20, 1000)])
    return np.clip(nilai, 0, 255).astype(np.uint8).reshape(40, 50)


@pytest.mark.parametrize("seed", [0, 1, 2, 3])
def test_otsu_sama_dengan_opencv(solusi, seed):
    citra = _bimodal(seed)
    ambang, _ = cv2.threshold(citra, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    assert solusi.ambang_otsu(citra) == int(ambang)


def test_segmentasi(solusi):
    citra = _bimodal(5)
    t = solusi.ambang_otsu(citra)
    np.testing.assert_array_equal(solusi.segmentasi_otsu(citra), np.where(citra > t, 255, 0))
