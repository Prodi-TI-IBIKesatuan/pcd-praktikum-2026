"""Pekan 11 — Morfologi citra biner: erosi, dilasi, opening.

Citra biner bernilai 0 (latar) atau 255 (objek). Elemen penstruktur berupa
bujur sangkar ukuran x ukuran (ganjil). Piksel di luar citra dianggap TIDAK
mempengaruhi hasil (sama dengan bawaan cv2.erode / cv2.dilate).
"""


import numpy as np


def erosi(citra_biner, ukuran):
    """Erosi: piksel menjadi 255 hanya bila SEMUA tetangga dalam jendela 255.
    Jangan memakai cv2.erode atau cv2.morphologyEx."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("erosi() belum dikerjakan")


def dilasi(citra_biner, ukuran):
    """Dilasi: piksel menjadi 255 bila ADA tetangga dalam jendela bernilai 255.
    Jangan memakai cv2.dilate atau cv2.morphologyEx."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("dilasi() belum dikerjakan")


def opening(citra_biner, ukuran):
    """Opening = dilasi(erosi(citra)). Menghapus bintik objek kecil."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("opening() belum dikerjakan")
