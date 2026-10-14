# Pekan 03 — Operasi titik: negatif, kecerahan, kontras

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-03-operasi-titik/latihan.ipynb) · [Materi pekan 03](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-03-operasi-titik)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `negatif(citra)`

Negatif citra: 255 - nilai piksel. Tipe hasil uint8.

### `atur_kecerahan(citra, delta)`

Tambahkan delta (boleh negatif) ke semua piksel, potong ke 0..255, uint8.

### `atur_kontras(citra, alfa)`

Ubah kontras di sekitar nilai tengah 128:

    baru = alfa * (lama - 128) + 128

dibulatkan ke bilangan bulat terdekat, dipotong ke 0..255, uint8.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| negatif | 25 |
| kecerahan | 40 |
| kontras | 35 |
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
