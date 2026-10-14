# Pekan 10 — Domain Frekuensi

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-10-domain-frekuensi/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 07-05-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 16-05-2027 23.59 WIB |

## Capaian belajar

- Menampilkan spektrum magnitudo Fourier
- Membuat mask lingkaran di domain frekuensi
- Menerapkan filter lolos-rendah ideal

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** FFT 2D, fftshift, efek ringing.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Terima assignment pekan 10 lewat tautan Classroom 50 di Moodle. Repo `pcd-tugas-p10-domain-frekuensi-<username>` akan dibuat untuk Anda. Kerjakan fungsi berikut di `solusi.py`: `spektrum_magnitudo()`, `mask_lingkaran()`, `lowpass_ideal()`.

| Kriteria autograder | Poin |
| --- | --- |
| spektrum | 35 |
| mask | 20 |
| lowpass | 45 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
