# Pekan 07 — Konvolusi dan Filter Spasial

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-07-konvolusi/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 09-04-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 18-04-2027 23.59 WIB |

## Capaian belajar

- Menulis korelasi 2D dengan padding nol
- Membedakan korelasi dan konvolusi
- Menerapkan filter rerata

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** kernel, padding, korelasi vs konvolusi.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Klik tautan assignment pekan 07 di Moodle lalu tekan *Accept*. Classroom 50 membuatkan repo privat `<kelas>-p07-<username>` (mis. `pcd-karyawan-a-p07-budisantoso`) di organisasi kelas. Kerjakan fungsi berikut di `solusi.py`: `konvolusi2d()`, `filter_rerata()`.

| Kriteria autograder | Poin |
| --- | --- |
| konvolusi | 40 |
| konvolusi manual | 15 |
| kernel asimetris | 20 |
| filter rerata | 25 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
