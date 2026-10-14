# Pekan 14 — Temu kembali citra berbasis isi (CBIR)

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-14-temu-kembali/latihan.ipynb) · [Materi pekan 14](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-14-temu-kembali)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `cari_mirip(fitur_query, fitur_basis_data, k)`

Indeks k citra paling mirip dengan query berdasarkan kemiripan kosinus.

- Urutkan dari paling mirip; bila sama, indeks lebih kecil lebih dulu.
- Kembalikan list of int panjang k.
- Lempar ValueError bila k < 1 atau k > jumlah citra di basis data.

### `presisi_pada_k(indeks_hasil, label_query, label_basis_data)`

Presisi@k: proporsi hasil yang labelnya sama dengan label query (float).

## Penilaian

| Kriteria | Poin |
| --- | --- |
| cari mirip | 45 |
| cari mirip batas | 20 |
| presisi | 35 |
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
