"""Pekan 12 — Segmentasi: ambang Otsu dan pelabelan objek."""


import cv2
import numpy as np


def ambang_otsu(citra_gray):
    """Hitung ambang Otsu (int 0..255) untuk citra keabuan uint8.

    Pilih t yang memaksimalkan variansi antarkelas
        w0(t) * w1(t) * (mu0(t) - mu1(t))^2
    dengan kelas 0 = piksel <= t dan kelas 1 = piksel > t.
    Bila beberapa t sama baiknya, ambil t terkecil.
    Jangan memakai cv2.threshold.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("ambang_otsu() belum dikerjakan")


def segmentasi_otsu(citra_gray):
    """Citra biner uint8: 255 bila piksel > ambang_otsu, selain itu 0."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("segmentasi_otsu() belum dikerjakan")


def hitung_objek(citra_biner):
    """Jumlah objek (komponen terhubung-8 dari piksel > 0). Anda BOLEH
    memakai cv2.connectedComponents."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("hitung_objek() belum dikerjakan")
