"""Pekan 01 — Citra digital sebagai array NumPy.

Citra keabuan = array 2D (tinggi x lebar); citra warna = array 3D
(tinggi x lebar x 3) berurutan kanal BGR seperti di OpenCV.
"""


import numpy as np


def info_citra(citra):
    """Kembalikan dict {"tinggi", "lebar", "kanal", "tipe"} dari sebuah citra.

    - kanal = 1 untuk citra 2D (keabuan), 3 untuk citra warna.
    - tipe = nama tipe data sebagai string, misalnya "uint8".
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("info_citra() belum dikerjakan")


def potong(citra, x, y, lebar, tinggi):
    """Potong citra mulai kolom x dan baris y sebesar lebar x tinggi piksel.

    Kembalikan SALINAN (bukan view) potongan tersebut. Lempar ValueError bila
    area potongan keluar dari batas citra atau ukurannya tidak positif.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("potong() belum dikerjakan")
