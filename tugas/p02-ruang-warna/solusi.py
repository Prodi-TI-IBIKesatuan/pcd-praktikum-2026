"""Pekan 02 — Ruang warna, keabuan, dan citra biner."""


import numpy as np


def ke_grayscale(citra_bgr):
    """Ubah citra BGR menjadi keabuan dengan bobot luminans ITU-R BT.601:

        abu = 0.299 R + 0.587 G + 0.114 B

    Hasil dibulatkan ke bilangan bulat terdekat, bertipe uint8, berbentuk 2D.
    Tulis sendiri: jangan memakai cv2.cvtColor.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("ke_grayscale() belum dikerjakan")


def bgr_ke_rgb(citra_bgr):
    """Tukar urutan kanal BGR menjadi RGB (untuk ditampilkan matplotlib)."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("bgr_ke_rgb() belum dikerjakan")


def ke_biner(citra_gray, ambang):
    """Citra biner uint8: piksel > ambang menjadi 255, sisanya 0.

    Tulis sendiri: jangan memakai cv2.threshold.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("ke_biner() belum dikerjakan")
