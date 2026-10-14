"""Pekan 07 — Konvolusi (korelasi) 2D dan filter rerata."""


import numpy as np


def konvolusi2d(citra_gray, kernel):
    """Korelasi 2D seperti cv2.filter2D dengan padding nol.

    - kernel berukuran ganjil (mis. 3x3, 5x5), TIDAK dibalik.
    - hasil berukuran sama dengan citra, bertipe float64.
    Tulis sendiri: jangan memakai cv2.filter2D atau fungsi convolve/correlate.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("konvolusi2d() belum dikerjakan")


def filter_rerata(citra_gray, ukuran):
    """Filter rerata ukuran x ukuran memakai konvolusi2d (padding nol).

    Hasil dibulatkan, dipotong ke 0..255, uint8.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("filter_rerata() belum dikerjakan")
