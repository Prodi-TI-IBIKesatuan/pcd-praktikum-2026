"""Pekan 08 — Filter Gauss, filter median, dan derau garam-merica."""


import numpy as np


def kernel_gauss(ukuran, sigma):
    """Kernel Gauss 2D ukuran x ukuran (ganjil) yang jumlah seluruh elemennya 1.

        g(x, y) = exp(-(x^2 + y^2) / (2 sigma^2)),  x, y diukur dari pusat kernel
    Kembalikan float64. Jangan memakai cv2.getGaussianKernel.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("kernel_gauss() belum dikerjakan")


def filter_median(citra_gray, ukuran):
    """Filter median ukuran x ukuran (ganjil) untuk citra keabuan uint8.

    Tepi citra diperlakukan dengan mengulang piksel terluar (padding "edge"),
    sama dengan cv2.medianBlur. Jangan memakai cv2.medianBlur.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("filter_median() belum dikerjakan")


def tambah_garam_merica(citra_gray, proporsi, seed=0):
    """Tambahkan derau garam-merica: tepat round(proporsi * N) piksel diubah,
    separuh (dibulatkan ke bawah) menjadi 0 dan sisanya 255.

    Posisi piksel dipilih acak TANPA pengulangan memakai
    np.random.default_rng(seed). Citra asli tidak boleh ikut berubah.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("tambah_garam_merica() belum dikerjakan")
