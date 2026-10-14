# Pekan 02 — Ruang Warna, Keabuan, dan Biner

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-02-ruang-warna/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 05-03-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 14-03-2027 23.59 WIB |

## Capaian belajar

- Mengubah citra BGR ke keabuan dengan bobot luminans
- Menukar urutan kanal BGR/RGB
- Membuat citra biner dengan ambang tetap

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** model warna RGB, HSV, luminans BT.601, binarisasi.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Terima assignment pekan 02 lewat tautan Classroom 50 di Moodle. Repo `pcd-tugas-p02-ruang-warna-<username>` akan dibuat untuk Anda. Kerjakan fungsi berikut di `solusi.py`: `ke_grayscale()`, `bgr_ke_rgb()`, `ke_biner()`.

| Kriteria autograder | Poin |
| --- | --- |
| grayscale | 40 |
| grayscale manual | 20 |
| biner | 25 |
| bgr ke rgb | 15 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
