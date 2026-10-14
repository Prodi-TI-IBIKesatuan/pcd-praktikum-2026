# Pekan 11 — Morfologi citra biner: erosi, dilasi, opening

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-11-morfologi/latihan.ipynb) · [Materi pekan 11](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-11-morfologi)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `erosi(citra_biner, ukuran)`

Erosi: piksel menjadi 255 hanya bila SEMUA tetangga dalam jendela 255.
Jangan memakai cv2.erode atau cv2.morphologyEx.

### `dilasi(citra_biner, ukuran)`

Dilasi: piksel menjadi 255 bila ADA tetangga dalam jendela bernilai 255.
Jangan memakai cv2.dilate atau cv2.morphologyEx.

### `opening(citra_biner, ukuran)`

Opening = dilasi(erosi(citra)). Menghapus bintik objek kecil.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| erosi | 35 |
| dilasi | 35 |
| opening | 30 |
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
