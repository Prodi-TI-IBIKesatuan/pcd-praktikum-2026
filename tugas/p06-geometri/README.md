# Pekan 06 — Operasi geometri: cermin, rotasi, dan ubah ukuran

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-06-geometri/latihan.ipynb) · [Materi pekan 06](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-06-geometri)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `balik_horizontal(citra)`

Cerminkan citra kiri-kanan. Tulis sendiri dengan slicing atau indeks:
jangan memakai cv2.flip, np.flip, atau np.fliplr.

### `rotasi_90(citra, k)`

Putar citra 90 derajat BERLAWANAN arah jarum jam sebanyak k kali
(k boleh negatif). Jangan memakai np.rot90 atau cv2.rotate.

### `ubah_ukuran_terdekat(citra, skala)`

Ubah ukuran dengan interpolasi tetangga terdekat.

Ukuran baru = round(tinggi * skala) x round(lebar * skala).
Piksel tujuan (b, k) mengambil piksel asal
    (floor(b * tinggi_asal / tinggi_baru), floor(k * lebar_asal / lebar_baru)).
Jangan memakai cv2.resize.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| balik | 25 |
| rotasi | 35 |
| ubah ukuran | 40 |
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
