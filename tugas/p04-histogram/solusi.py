"""Pekan 04 — Histogram dan ekualisasi histogram."""


import numpy as np


def histogram(citra_gray):
    """Hitung histogram citra keabuan uint8.

    Kembalikan array NumPy panjang 256 berisi jumlah piksel untuk tiap
    intensitas 0..255. Tulis sendiri: jangan memakai np.histogram atau cv2.calcHist.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("histogram() belum dikerjakan")


def ekualisasi(citra_gray):
    """Ekualisasi histogram citra keabuan uint8.

    Rumus (sama dengan cv2.equalizeHist):
        cdf  = jumlah kumulatif histogram
        cmin = cdf pada intensitas pertama yang muncul
        baru = round((cdf[lama] - cmin) * 255 / (N - cmin)),  N = jumlah piksel
    Citra yang seluruh pikselnya sama dikembalikan apa adanya.
    Tulis sendiri: jangan memakai cv2.equalizeHist.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("ekualisasi() belum dikerjakan")
