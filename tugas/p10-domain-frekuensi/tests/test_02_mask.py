import numpy as np


def test_mask_lingkaran(solusi):
    m = solusi.mask_lingkaran((7, 9), 2)
    assert m.shape == (7, 9) and m.dtype == bool
    assert m[3, 4] and m[1, 4] and m[3, 6] and not m[1, 6] and m.sum() == 13
