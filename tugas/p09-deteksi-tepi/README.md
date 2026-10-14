# Pekan 09 — Deteksi tepi: Sobel dan Canny

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-09-deteksi-tepi/latihan.ipynb) · [Materi pekan 09](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-09-deteksi-tepi)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `sobel(citra_gray)`

Kembalikan (gx, gy, magnitudo), semuanya float64 berukuran sama dengan citra.

- gx memakai kernel SOBEL_X, gy memakai SOBEL_Y (korelasi, kernel tidak dibalik).
- Tepi citra dipantulkan TANPA mengulang piksel tepi (np.pad mode="reflect"),
  sama dengan bawaan cv2.Sobel.
- magnitudo = sqrt(gx^2 + gy^2).
Jangan memakai cv2.Sobel atau cv2.filter2D.

### `tepi_canny(citra_gray, ambang_rendah, ambang_tinggi)`

Deteksi tepi Canny. Di sini Anda BOLEH memakai cv2.Canny.
Kembalikan citra biner uint8 (0 atau 255).

### `rasio_tepi(citra_tepi)`

Proporsi piksel tepi (nilai > 0) terhadap seluruh piksel, float 0..1.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| sobel | 50 |
| canny | 30 |
| rasio tepi | 20 |
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
