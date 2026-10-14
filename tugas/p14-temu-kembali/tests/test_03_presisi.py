def test_presisi(solusi):
    label = ["kucing", "anjing", "kucing", "burung", "kucing"]
    assert abs(solusi.presisi_pada_k([0, 2, 3, 4], "kucing", label) - 0.75) < 1e-12
    assert solusi.presisi_pada_k([1, 3], "kucing", label) == 0.0
    assert solusi.presisi_pada_k([], "kucing", label) == 0.0
