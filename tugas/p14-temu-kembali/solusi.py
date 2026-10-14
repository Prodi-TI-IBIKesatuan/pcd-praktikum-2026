"""Pekan 14 — Temu kembali citra berbasis isi (CBIR).

Basis data citra direpresentasikan sebagai matriks fitur (n x d): satu baris
per citra. Fitur bisa dari histogram warna (pekan 13) atau embedding model
pralatih (lihat pengayaan di README).
"""


import numpy as np


def cari_mirip(fitur_query, fitur_basis_data, k):
    """Indeks k citra paling mirip dengan query berdasarkan kemiripan kosinus.

    - Urutkan dari paling mirip; bila sama, indeks lebih kecil lebih dulu.
    - Kembalikan list of int panjang k.
    - Lempar ValueError bila k < 1 atau k > jumlah citra di basis data.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("cari_mirip() belum dikerjakan")


def presisi_pada_k(indeks_hasil, label_query, label_basis_data):
    """Presisi@k: proporsi hasil yang labelnya sama dengan label query (float)."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("presisi_pada_k() belum dikerjakan")
