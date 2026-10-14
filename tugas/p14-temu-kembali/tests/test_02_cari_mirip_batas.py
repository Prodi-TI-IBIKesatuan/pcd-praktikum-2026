import numpy as np
import pytest


def test_k_tidak_valid(solusi):
    basis = np.eye(3)
    for k in (0, 4):
        with pytest.raises(ValueError):
            solusi.cari_mirip([1, 0, 0], basis, k)


def test_seri_indeks_kecil_dulu(solusi):
    basis = np.array([[0, 1], [1, 0], [2, 0], [0, 3]], dtype=float)
    assert list(solusi.cari_mirip([1, 0], basis, 2)) == [1, 2]
