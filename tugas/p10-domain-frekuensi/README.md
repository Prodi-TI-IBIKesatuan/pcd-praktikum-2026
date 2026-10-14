# Pekan 10 — Domain frekuensi dengan transformasi Fourier

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-10-domain-frekuensi/latihan.ipynb) · [Materi pekan 10](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-10-domain-frekuensi)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `spektrum_magnitudo(citra_gray)`

Spektrum magnitudo terpusat dalam skala log:

    log(1 + |fftshift(fft2(citra))|)
Kembalikan float64 berukuran sama dengan citra.

### `mask_lingkaran(bentuk, radius)`

Mask boolean (tinggi x lebar): True bila jarak Euclid dari titik pusat
(tinggi // 2, lebar // 2) <= radius.

### `lowpass_ideal(citra_gray, radius)`

Filter lolos-rendah ideal: pertahankan frekuensi di dalam mask_lingkaran
pada spektrum terpusat, lalu kembalikan bagian riil hasil invers
(ifft2(ifftshift(...))) sebagai float64.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| spektrum | 35 |
| mask | 20 |
| lowpass | 45 |
| **Total** | **100** |

## Cara mengerjakan dari HP

1. Berlatih di notebook Colab (tombol di atas) sampai hasilnya benar.
2. Di halaman repo ini buka `solusi.py` → ikon pensil → tempel jawaban → hapus baris `raise NotImplementedError` → **Commit changes**.
3. Tunggu tanda kuning berubah hijau/merah. Merah? Ketuk tanda → *Details* untuk melihat kriteria yang gagal.
4. Isi `CATATAN.md` dan unggah tangkapan layar hasil ke folder `bukti/`.

## Cara mengerjakan dari laptop

Tekan **Code → Codespaces → Create codespace on main**, atau di komputer sendiri:

```bash
pip install -r requirements.txt
python tests/jalankan_semua.py        # semua kriteria + skor
python -m pytest -q tests/test_01_*.py  # satu kriteria
```

Jangan mengubah isi folder `tests/` dan `.github/`; perubahan di sana tidak dihitung dan dapat dianggap pelanggaran.
