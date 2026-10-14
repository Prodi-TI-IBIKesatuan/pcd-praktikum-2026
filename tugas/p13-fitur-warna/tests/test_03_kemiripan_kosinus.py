def test_kemiripan_kosinus(solusi):
    assert abs(solusi.kemiripan_kosinus([1, 0], [1, 0]) - 1.0) < 1e-12
    assert abs(solusi.kemiripan_kosinus([1, 0], [0, 2])) < 1e-12
    assert abs(solusi.kemiripan_kosinus([1, 1], [-1, -1]) + 1.0) < 1e-12
    assert abs(solusi.kemiripan_kosinus([2, 0], [5, 0]) - 1.0) < 1e-12


def test_vektor_nol(solusi):
    assert solusi.kemiripan_kosinus([0, 0], [1, 2]) == 0.0
