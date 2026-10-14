"""Pekan 03 — Operasi titik: negatif, kecerahan, kontras.

Hati-hati dengan overflow uint8: 250 + 10 pada uint8 menjadi 4, bukan 260.
Hitung dalam tipe yang lebih besar, lalu potong (clip) ke rentang 0..255.
"""


import numpy as np


def negatif(citra):
    """Negatif citra: 255 - nilai piksel. Tipe hasil uint8."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("negatif() belum dikerjakan")


def atur_kecerahan(citra, delta):
    """Tambahkan delta (boleh negatif) ke semua piksel, potong ke 0..255, uint8."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("atur_kecerahan() belum dikerjakan")


def atur_kontras(citra, alfa):
    """Ubah kontras di sekitar nilai tengah 128:

        baru = alfa * (lama - 128) + 128

    dibulatkan ke bilangan bulat terdekat, dipotong ke 0..255, uint8.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("atur_kontras() belum dikerjakan")
