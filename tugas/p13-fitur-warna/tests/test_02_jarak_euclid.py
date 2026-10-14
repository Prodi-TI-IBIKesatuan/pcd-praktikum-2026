def test_jarak_euclid(solusi):
    assert abs(solusi.jarak_euclid([0, 0], [3, 4]) - 5.0) < 1e-12
    assert solusi.jarak_euclid([1, 2, 3], [1, 2, 3]) == 0.0
