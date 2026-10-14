# Pekan 12 — Segmentasi Citra

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-12-segmentasi/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 21-05-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 30-05-2027 23.59 WIB |

## Capaian belajar

- Menghitung ambang Otsu secara manual
- Mensegmentasi citra dengan ambang Otsu
- Menghitung objek dengan pelabelan komponen terhubung

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** variansi antarkelas, konektivitas-4 dan -8.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Klik tautan assignment pekan 12 di Moodle lalu tekan *Accept*. Classroom 50 membuatkan repo privat `<kelas>-p12-<username>` (mis. `pcd-karyawan-a-p12-budisantoso`) di organisasi kelas. Kerjakan fungsi berikut di `solusi.py`: `ambang_otsu()`, `segmentasi_otsu()`, `hitung_objek()`.

| Kriteria autograder | Poin |
| --- | --- |
| otsu | 45 |
| otsu manual | 20 |
| hitung objek | 35 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
