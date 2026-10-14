"""Pekan 09 — Deteksi tepi: Sobel dan Canny."""


import cv2
import numpy as np


SOBEL_X = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
SOBEL_Y = SOBEL_X.T


def sobel(citra_gray):
    """Kembalikan (gx, gy, magnitudo), semuanya float64 berukuran sama dengan citra.

    - gx memakai kernel SOBEL_X, gy memakai SOBEL_Y (korelasi, kernel tidak dibalik).
    - Tepi citra dipantulkan TANPA mengulang piksel tepi (np.pad mode="reflect"),
      sama dengan bawaan cv2.Sobel.
    - magnitudo = sqrt(gx^2 + gy^2).
    Jangan memakai cv2.Sobel atau cv2.filter2D.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("sobel() belum dikerjakan")


def tepi_canny(citra_gray, ambang_rendah, ambang_tinggi):
    """Deteksi tepi Canny. Di sini Anda BOLEH memakai cv2.Canny.
    Kembalikan citra biner uint8 (0 atau 255)."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("tepi_canny() belum dikerjakan")


def rasio_tepi(citra_tepi):
    """Proporsi piksel tepi (nilai > 0) terhadap seluruh piksel, float 0..1."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("rasio_tepi() belum dikerjakan")
