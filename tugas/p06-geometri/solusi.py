"""Pekan 06 — Operasi geometri: cermin, rotasi, dan ubah ukuran."""


import numpy as np


def balik_horizontal(citra):
    """Cerminkan citra kiri-kanan. Tulis sendiri dengan slicing atau indeks:
    jangan memakai cv2.flip, np.flip, atau np.fliplr."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("balik_horizontal() belum dikerjakan")


def rotasi_90(citra, k=1):
    """Putar citra 90 derajat BERLAWANAN arah jarum jam sebanyak k kali
    (k boleh negatif). Jangan memakai np.rot90 atau cv2.rotate."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("rotasi_90() belum dikerjakan")


def ubah_ukuran_terdekat(citra, skala):
    """Ubah ukuran dengan interpolasi tetangga terdekat.

    Ukuran baru = round(tinggi * skala) x round(lebar * skala).
    Piksel tujuan (b, k) mengambil piksel asal
        (floor(b * tinggi_asal / tinggi_baru), floor(k * lebar_asal / lebar_baru)).
    Jangan memakai cv2.resize.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("ubah_ukuran_terdekat() belum dikerjakan")
