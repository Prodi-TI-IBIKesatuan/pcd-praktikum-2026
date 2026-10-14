import numpy as np


BASIS = np.array([[1, 0, 0], [0.9, 0.1, 0], [0, 1, 0], [0, 0, 1], [0.5, 0.5, 0], [2, 0, 0]], dtype=float)


def test_urutan_kemiripan(solusi):
    hasil = solusi.cari_mirip([1, 0, 0], BASIS, 3)
    assert [int(i) for i in hasil] == [0, 5, 1]


def test_skala_tidak_berpengaruh(solusi):
    assert list(solusi.cari_mirip([0, 3, 0], BASIS, 2)) == [2, 4]


def test_acak_konsisten_dengan_kosinus(solusi):
    rng = np.random.default_rng(11)
    basis = rng.random((50, 16))
    q = rng.random(16)
    skor = basis @ q / (np.linalg.norm(basis, axis=1) * np.linalg.norm(q))
    assert list(solusi.cari_mirip(q, basis, 5)) == list(np.argsort(-skor, kind="stable")[:5])
