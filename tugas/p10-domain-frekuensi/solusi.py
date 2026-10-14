"""Pekan 10 — Domain frekuensi dengan transformasi Fourier."""


import numpy as np


def spektrum_magnitudo(citra_gray):
    """Spektrum magnitudo terpusat dalam skala log:

        log(1 + |fftshift(fft2(citra))|)
    Kembalikan float64 berukuran sama dengan citra.
    """
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("spektrum_magnitudo() belum dikerjakan")


def mask_lingkaran(bentuk, radius):
    """Mask boolean (tinggi x lebar): True bila jarak Euclid dari titik pusat
    (tinggi // 2, lebar // 2) <= radius."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("mask_lingkaran() belum dikerjakan")


def lowpass_ideal(citra_gray, radius):
    """Filter lolos-rendah ideal: pertahankan frekuensi di dalam mask_lingkaran
    pada spektrum terpusat, lalu kembalikan bagian riil hasil invers
    (ifft2(ifftshift(...))) sebagai float64."""
    # TODO: tulis jawaban Anda di sini, lalu hapus baris raise di bawah.
    raise NotImplementedError("lowpass_ideal() belum dikerjakan")
