# Pekan 02 — Ruang warna, keabuan, dan citra biner

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-02-ruang-warna/latihan.ipynb) · [Materi pekan 02](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-02-ruang-warna)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `ke_grayscale(citra_bgr)`

Ubah citra BGR menjadi keabuan dengan bobot luminans ITU-R BT.601:

    abu = 0.299 R + 0.587 G + 0.114 B

Hasil dibulatkan ke bilangan bulat terdekat, bertipe uint8, berbentuk 2D.
Tulis sendiri: jangan memakai cv2.cvtColor.

### `bgr_ke_rgb(citra_bgr)`

Tukar urutan kanal BGR menjadi RGB (untuk ditampilkan matplotlib).

### `ke_biner(citra_gray, ambang)`

Citra biner uint8: piksel > ambang menjadi 255, sisanya 0.

Tulis sendiri: jangan memakai cv2.threshold.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| grayscale | 40 |
| grayscale manual | 20 |
| biner | 25 |
| bgr ke rgb | 15 |
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
