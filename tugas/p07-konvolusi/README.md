# Pekan 07 — Konvolusi (korelasi) 2D dan filter rerata

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-07-konvolusi/latihan.ipynb) · [Materi pekan 07](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-07-konvolusi)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `konvolusi2d(citra_gray, kernel)`

Korelasi 2D seperti cv2.filter2D dengan padding nol.

- kernel berukuran ganjil (mis. 3x3, 5x5), TIDAK dibalik.
- hasil berukuran sama dengan citra, bertipe float64.
Tulis sendiri: jangan memakai cv2.filter2D atau fungsi convolve/correlate.

### `filter_rerata(citra_gray, ukuran)`

Filter rerata ukuran x ukuran memakai konvolusi2d (padding nol).

Hasil dibulatkan, dipotong ke 0..255, uint8.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| konvolusi | 40 |
| konvolusi manual | 15 |
| kernel asimetris | 20 |
| filter rerata | 25 |
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
