# Pekan 01 — Citra digital sebagai array NumPy

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-01-citra-digital/latihan.ipynb) · [Materi pekan 01](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-01-citra-digital)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `info_citra(citra)`

Kembalikan dict {"tinggi", "lebar", "kanal", "tipe"} dari sebuah citra.

- kanal = 1 untuk citra 2D (keabuan), 3 untuk citra warna.
- tipe = nama tipe data sebagai string, misalnya "uint8".

### `potong(citra, x, y, lebar, tinggi)`

Potong citra mulai kolom x dan baris y sebesar lebar x tinggi piksel.

Kembalikan SALINAN (bukan view) potongan tersebut. Lempar ValueError bila
area potongan keluar dari batas citra atau ukurannya tidak positif.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| info citra | 35 |
| potong | 40 |
| potong batas | 25 |
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
