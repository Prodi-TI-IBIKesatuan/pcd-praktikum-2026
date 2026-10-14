# Pekan 12 — Segmentasi: ambang Otsu dan pelabelan objek

[![Buka latihan di Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/blob/main/modul/pekan-12-segmentasi/latihan.ipynb) · [Materi pekan 12](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/tree/main/modul/pekan-12-segmentasi)

Kerjakan fungsi-fungsi berikut di **`solusi.py`**. Setiap *commit* langsung dinilai: tanda hijau di halaman repo = semua kriteria lulus. Tenggat **Minggu 23.59 WIB**.

## Fungsi yang dikerjakan

### `ambang_otsu(citra_gray)`

Hitung ambang Otsu (int 0..255) untuk citra keabuan uint8.

Pilih t yang memaksimalkan variansi antarkelas
    w0(t) * w1(t) * (mu0(t) - mu1(t))^2
dengan kelas 0 = piksel <= t dan kelas 1 = piksel > t.
Bila beberapa t sama baiknya, ambil t terkecil.
Jangan memakai cv2.threshold.

### `segmentasi_otsu(citra_gray)`

Citra biner uint8: 255 bila piksel > ambang_otsu, selain itu 0.

### `hitung_objek(citra_biner)`

Jumlah objek (komponen terhubung-8 dari piksel > 0). Anda BOLEH
memakai cv2.connectedComponents.

## Penilaian

| Kriteria | Poin |
| --- | --- |
| otsu | 45 |
| otsu manual | 20 |
| hitung objek | 35 |
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
