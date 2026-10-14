# Pekan 03 — Operasi Titik

[![Buka di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-03-operasi-titik/latihan.ipynb)

| Rilis | Sesi Meet | Tenggat tugas |
| --- | --- | --- |
| Jumat 12-03-2027 18.00 WIB | Senin–Jumat 19.30 WIB, 45 menit | Minggu 21-03-2027 23.59 WIB |

## Capaian belajar

- Menghitung negatif citra
- Mengatur kecerahan tanpa overflow uint8
- Mengatur kontras terhadap nilai tengah

## Belajar mandiri (Sabtu–Minggu)

1. **Video** (10–15 menit): _tautan diisi DLS sebelum rilis_
2. **Konsep kunci:** transformasi intensitas, overflow dan clipping, pembulatan.
3. **Latihan:** tekan tombol *Buka di Colab* di atas. Notebook berjalan di browser HP tanpa instalasi.

## Tugas praktik

Klik tautan assignment pekan 03 di Moodle lalu tekan *Accept*. Classroom 50 membuatkan repo privat `<kelas>-p03-<username>` (mis. `pcd-karyawan-a-p03-budisantoso`) di organisasi kelas. Kerjakan fungsi berikut di `solusi.py`: `negatif()`, `atur_kecerahan()`, `atur_kontras()`.

| Kriteria autograder | Poin |
| --- | --- |
| negatif | 25 |
| kecerahan | 40 |
| kontras | 35 |

Setiap *commit* langsung dinilai; tanda hijau di GitHub = semua kriteria lulus. Isi juga `CATATAN.md` (3–5 kalimat).

## Rujukan

- Gonzalez, R. C. & Woods, R. E. *Digital Image Processing*, 4th ed. Pearson.
- Dokumentasi OpenCV: https://docs.opencv.org/4.x/
- Modul praktikum Pengolahan Citra Digital, Prodi TI IBI Kesatuan.
