import pytest


@pytest.mark.parametrize("x, y, lebar, tinggi", [(50, 0, 5, 5), (0, 38, 5, 5), (-1, 0, 3, 3), (0, 0, 0, 3)])
def test_potong_di_luar_batas(solusi, citra_gray, x, y, lebar, tinggi):
    with pytest.raises(ValueError):
        solusi.potong(citra_gray, x, y, lebar, tinggi)
