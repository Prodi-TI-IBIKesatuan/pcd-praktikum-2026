"""Inti aplikasi capstone: pengindeksan dan pencarian citra (CBIR).

Semua logika ada di sini agar bisa diuji tanpa antarmuka. app.py hanya
membungkusnya dengan Gradio. Ganti `ekstrak_fitur` dengan fitur Anda sendiri
(histogram warna, tekstur, atau embedding model pralatih) — tahap 2 menilai
seberapa baik pilihan fitur Anda dijelaskan dan dievaluasi.
"""
from __future__ import annotations

import pathlib

import cv2
import numpy as np

EKSTENSI = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def ekstrak_fitur(citra_bgr: np.ndarray, bins: int = 8) -> np.ndarray:
    """Fitur bawaan: histogram HSV 3D yang dinormalisasi (panjang bins**3)."""
    hsv = cv2.cvtColor(citra_bgr, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, [bins] * 3, [0, 180, 0, 256, 0, 256]).ravel()
    total = hist.sum()
    return hist / total if total else hist


def bangun_indeks(folder: str | pathlib.Path) -> tuple[list[pathlib.Path], np.ndarray]:
    """Baca semua citra di folder (rekursif) dan kembalikan (daftar_berkas, matriks_fitur)."""
    berkas = sorted(p for p in pathlib.Path(folder).rglob("*") if p.suffix.lower() in EKSTENSI)
    fitur, terbaca = [], []
    for p in berkas:
        citra = cv2.imread(str(p))
        if citra is None:
            continue
        terbaca.append(p)
        fitur.append(ekstrak_fitur(citra))
    if not fitur:
        return [], np.zeros((0, 0))
    return terbaca, np.vstack(fitur)


def cari(citra_query: np.ndarray, berkas: list[pathlib.Path], fitur: np.ndarray, k: int = 5):
    """Kembalikan list (path, skor_kosinus) k citra paling mirip, terurut menurun."""
    if len(berkas) == 0:
        return []
    q = ekstrak_fitur(citra_query)
    norma = np.linalg.norm(fitur, axis=1) * np.linalg.norm(q)
    skor = np.divide(fitur @ q, norma, out=np.zeros(len(berkas)), where=norma > 0)
    urutan = np.lexsort((np.arange(len(skor)), -skor))[: min(k, len(berkas))]
    return [(berkas[i], float(skor[i])) for i in urutan]
