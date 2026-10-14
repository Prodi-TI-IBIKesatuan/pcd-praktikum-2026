# Pekan 08 — Filter Gauss, filter median, dan derau garam-merica

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-08-filter-derau/latihan.ipynb) · [Materi pekan 08](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-08-filter-derau)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `kernel_gauss(ukuran, sigma)`

Kernel Gauss 2D ukuran x ukuran (ganjil) yang jumlah seluruh elemennya 1.

    g(x, y) = exp(-(x^2 + y^2) / (2 sigma^2)),  x, y diukur dari pusat kernel
Kembalikan float64. Jangan memakai cv2.getGaussianKernel.

### `filter_median(citra_gray, ukuran)`

Filter median ukuran x ukuran (ganjil) untuk citra keabuan uint8.

Tepi citra diperlakukan dengan mengulang piksel terluar (padding "edge"),
sama dengan cv2.medianBlur. Jangan memakai cv2.medianBlur.

### `tambah_garam_merica(citra_gray, proporsi, seed)`

Tambahkan derau garam-merica: tepat round(proporsi * N) piksel diubah,
separuh (dibulatkan ke bawah) menjadi 0 dan sisanya 255.

Posisi piksel dipilih acak TANPA pengulangan memakai
np.random.default_rng(seed). Citra asli tidak boleh ikut berubah.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| kernel gauss | 30 |
| filter median | 40 |
| garam merica | 30 |
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
