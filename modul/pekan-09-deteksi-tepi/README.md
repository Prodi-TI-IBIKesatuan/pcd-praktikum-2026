# Pekan 09 — Deteksi Tepi

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-09-deteksi-tepi/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 30-04-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 09-05-2027 23.59 WIB |

## Capaian belajar

- Menghitung gradien Sobel
- Menerapkan detektor Canny
- Mengukur kerapatan tepi

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** gradien dan magnitudo, non-maximum suppression, ambang histeresis.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Klik tautan assignment pekan 09 di Moodle lalu tekan *Accept*. Classroom 50 membuatkan repo privat `<kelas>-p09-<username>` (mis. `pcd-karyawan-a-p09-budisantoso`) di organisasi kelas. Kerjakan fungsi berikut di `solusi.py`: `sobel()`, `tepi_canny()`, `rasio_tepi()`.

| Kriteria autograder | Poin |
| --- | --- |
| sobel | 50 |
| canny | 30 |
| rasio tepi | 20 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
