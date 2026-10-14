"""Pekan 05 — Operasi aritmatika dan logika antarcitra."""


import numpy as np


def campur(citra_a, citra_b, alfa):
    """Campur dua citra berukuran sama: alfa * A + (1 - alfa) * B.

    Hasil dibulatkan, dipotong ke 0..255, uint8. Lempar ValueError bila
    bentuk kedua citra berbeda atau alfa di luar 0..1.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("campur() belum dikerjakan")


def selisih_absolut(citra_a, citra_b):
    """|A - B| per piksel tanpa overflow, uint8 (setara cv2.absdiff)."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("selisih_absolut() belum dikerjakan")


def terapkan_mask(citra, mask):
    """Pertahankan piksel citra di posisi mask > 0, sisanya 0.

    mask selalu 2D (tinggi x lebar); citra boleh keabuan atau warna.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("terapkan_mask() belum dikerjakan")
