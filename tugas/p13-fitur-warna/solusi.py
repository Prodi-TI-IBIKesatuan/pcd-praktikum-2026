"""Pekan 13 — Ekstraksi fitur warna dan ukuran kemiripan."""


import numpy as np


def histogram_warna(citra_bgr, bins):
    """Vektor fitur histogram warna.

    - Tiap kanal (urutan B, G, R) dibagi menjadi `bins` kelompok sama lebar:
      indeks kelompok = nilai * bins // 256.
    - Gabungkan ketiga histogram menjadi satu vektor panjang 3 * bins.
    - Normalisasi sehingga jumlah seluruh elemen = 1. Kembalikan float64.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("histogram_warna() belum dikerjakan")


def jarak_euclid(a, b):
    """Jarak Euclid antara dua vektor (float)."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("jarak_euclid() belum dikerjakan")


def kemiripan_kosinus(a, b):
    """Kemiripan kosinus a.b / (|a| |b|) sebagai float. Bila salah satu vektor
    nol, kembalikan 0.0."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("kemiripan_kosinus() belum dikerjakan")
