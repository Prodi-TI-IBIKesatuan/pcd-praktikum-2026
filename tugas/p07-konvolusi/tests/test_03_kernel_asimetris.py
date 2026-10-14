import cv2
import numpy as np


def test_kernel_tidak_dibalik(solusi, citra_gray):
    """Kernel tak simetris membedakan korelasi (benar) dari konvolusi terbalik."""
    kernel = np.array([[1, 2, 0], [0, -1, 3], [4, 0, -2]], dtype=float)
    referensi = cv2.filter2D(citra_gray.astype(np.float64), -1, kernel, borderType=cv2.BORDER_CONSTANT)
    np.testing.assert_allclose(solusi.konvolusi2d(citra_gray, kernel), referensi, atol=1e-9)
