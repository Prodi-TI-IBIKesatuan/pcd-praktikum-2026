# Pekan 05 — Operasi aritmatika dan logika antarcitra

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-05-aritmatika-logika/latihan.ipynb) · [Materi pekan 05](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-05-aritmatika-logika)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `campur(citra_a, citra_b, alfa)`

Campur dua citra berukuran sama: alfa * A + (1 - alfa) * B.

Hasil dibulatkan, dipotong ke 0..255, uint8. Lempar ValueError bila
bentuk kedua citra berbeda atau alfa di luar 0..1.

### `selisih_absolut(citra_a, citra_b)`

|A - B| per piksel tanpa overflow, uint8 (setara cv2.absdiff).

### `terapkan_mask(citra, mask)`

Pertahankan piksel citra di posisi mask > 0, sisanya 0.

mask selalu 2D (tinggi x lebar); citra boleh keabuan atau warna.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| campur | 35 |
| selisih | 30 |
| mask | 35 |
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
