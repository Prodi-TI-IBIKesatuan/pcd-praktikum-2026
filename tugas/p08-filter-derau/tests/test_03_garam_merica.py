import numpy as np


def _abu():
    return np.full((20, 25), 128, dtype=np.uint8)


def test_jumlah_piksel_berubah(solusi):
    hasil = solusi.tambah_garam_merica(_abu(), 0.1, seed=3)
    n = round(0.1 * 500)
    assert (hasil == 0).sum() == n // 2
    assert (hasil == 255).sum() == n - n // 2
    assert (hasil == 128).sum() == 500 - n


def test_asli_tidak_berubah_dan_deterministik(solusi):
    asli = _abu()
    a = solusi.tambah_garam_merica(asli, 0.2, seed=9)
    b = solusi.tambah_garam_merica(asli, 0.2, seed=9)
    c = solusi.tambah_garam_merica(asli, 0.2, seed=10)
    assert np.all(asli == 128)
    np.testing.assert_array_equal(a, b)
    assert not np.array_equal(a, c)
