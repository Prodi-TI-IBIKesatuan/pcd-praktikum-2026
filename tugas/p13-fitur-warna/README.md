# Pekan 13 — Ekstraksi fitur warna dan ukuran kemiripan

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-13-fitur-warna/latihan.ipynb) · [Materi pekan 13](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-13-fitur-warna)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `histogram_warna(citra_bgr, bins)`

Vektor fitur histogram warna.

- Tiap kanal (urutan B, G, R) dibagi menjadi `bins` kelompok sama lebar:
  indeks kelompok = nilai * bins // 256.
- Gabungkan ketiga histogram menjadi satu vektor panjang 3 * bins.
- Normalisasi sehingga jumlah seluruh elemen = 1. Kembalikan float64.

### `jarak_euclid(a, b)`

Jarak Euclid antara dua vektor (float).

### `kemiripan_kosinus(a, b)`

Kemiripan kosinus a.b / (|a| |b|) sebagai float. Bila salah satu vektor
nol, kembalikan 0.0.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| histogram warna | 40 |
| jarak euclid | 25 |
| kemiripan kosinus | 35 |
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
