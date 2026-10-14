# Pekan 04 — Histogram dan ekualisasi histogram

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-04-histogram/latihan.ipynb) · [Materi pekan 04](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-04-histogram)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `histogram(citra_gray)`

Hitung histogram citra keabuan uint8.

Kembalikan array NumPy panjang 256 berisi jumlah piksel untuk tiap
intensitas 0..255. Tulis sendiri: jangan memakai np.histogram atau cv2.calcHist.

### `ekualisasi(citra_gray)`

Ekualisasi histogram citra keabuan uint8.

Rumus (sama dengan cv2.equalizeHist):
    cdf  = jumlah kumulatif histogram
    cmin = cdf pada intensitas pertama yang muncul
    baru = round((cdf[lama] - cmin) * 255 / (N - cmin)),  N = jumlah piksel
Citra yang seluruh pikselnya sama dikembalikan apa adanya.
Tulis sendiri: jangan memakai cv2.equalizeHist.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| histogram | 35 |
| histogram manual | 15 |
| ekualisasi | 35 |
| ekualisasi khusus | 15 |
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
