# Konfigurasi tes Classroom 50

Berkas ini dibangkitkan otomatis oleh `tools/buat_konfigurasi_classroom50.py` dari `tests/poin.json`. Jangan diedit manual.

Pengaturan umum setiap assignment: template repo `Prodi-TI-IBIKesatuan/pcd-tugas-<folder>`, tipe individu, tenggat **Minggu 23.59 WIB**, *feedback pull request* aktif. Setiap baris di bawah = satu tes bertipe **Run command** (lulus bila kode keluar 0), *setup command* `python -m pip install -q -r requirements.txt`, timeout 2 menit.

## p01-citra-digital

Pekan 01 — Citra digital sebagai array NumPy. Repo template: `pcd-tugas-p01-citra-digital`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| info citra | `python -m pytest -q tests/test_01_info_citra.py` | 35 |
| potong | `python -m pytest -q tests/test_02_potong.py` | 40 |
| potong batas | `python -m pytest -q tests/test_03_potong_batas.py` | 25 |
| **Total** | | **100** |

## p02-ruang-warna

Pekan 02 — Ruang warna, keabuan, dan citra biner. Repo template: `pcd-tugas-p02-ruang-warna`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| grayscale | `python -m pytest -q tests/test_01_grayscale.py` | 40 |
| grayscale manual | `python -m pytest -q tests/test_02_grayscale_manual.py` | 20 |
| biner | `python -m pytest -q tests/test_03_biner.py` | 25 |
| bgr ke rgb | `python -m pytest -q tests/test_04_bgr_ke_rgb.py` | 15 |
| **Total** | | **100** |

## p03-operasi-titik

Pekan 03 — Operasi titik: negatif, kecerahan, kontras. Repo template: `pcd-tugas-p03-operasi-titik`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| negatif | `python -m pytest -q tests/test_01_negatif.py` | 25 |
| kecerahan | `python -m pytest -q tests/test_02_kecerahan.py` | 40 |
| kontras | `python -m pytest -q tests/test_03_kontras.py` | 35 |
| **Total** | | **100** |

## p04-histogram

Pekan 04 — Histogram dan ekualisasi histogram. Repo template: `pcd-tugas-p04-histogram`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| histogram | `python -m pytest -q tests/test_01_histogram.py` | 35 |
| histogram manual | `python -m pytest -q tests/test_02_histogram_manual.py` | 15 |
| ekualisasi | `python -m pytest -q tests/test_03_ekualisasi.py` | 35 |
| ekualisasi khusus | `python -m pytest -q tests/test_04_ekualisasi_khusus.py` | 15 |
| **Total** | | **100** |

## p05-aritmatika-logika

Pekan 05 — Operasi aritmatika dan logika antarcitra. Repo template: `pcd-tugas-p05-aritmatika-logika`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| campur | `python -m pytest -q tests/test_01_campur.py` | 35 |
| selisih | `python -m pytest -q tests/test_02_selisih.py` | 30 |
| mask | `python -m pytest -q tests/test_03_mask.py` | 35 |
| **Total** | | **100** |

## p06-geometri

Pekan 06 — Operasi geometri: cermin, rotasi, dan ubah ukuran. Repo template: `pcd-tugas-p06-geometri`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| balik | `python -m pytest -q tests/test_01_balik.py` | 25 |
| rotasi | `python -m pytest -q tests/test_02_rotasi.py` | 35 |
| ubah ukuran | `python -m pytest -q tests/test_03_ubah_ukuran.py` | 40 |
| **Total** | | **100** |

## p07-konvolusi

Pekan 07 — Konvolusi (korelasi) 2D dan filter rerata. Repo template: `pcd-tugas-p07-konvolusi`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| konvolusi | `python -m pytest -q tests/test_01_konvolusi.py` | 40 |
| konvolusi manual | `python -m pytest -q tests/test_02_konvolusi_manual.py` | 15 |
| kernel asimetris | `python -m pytest -q tests/test_03_kernel_asimetris.py` | 20 |
| filter rerata | `python -m pytest -q tests/test_04_filter_rerata.py` | 25 |
| **Total** | | **100** |

## p08-filter-derau

Pekan 08 — Filter Gauss, filter median, dan derau garam-merica. Repo template: `pcd-tugas-p08-filter-derau`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| kernel gauss | `python -m pytest -q tests/test_01_kernel_gauss.py` | 30 |
| filter median | `python -m pytest -q tests/test_02_filter_median.py` | 40 |
| garam merica | `python -m pytest -q tests/test_03_garam_merica.py` | 30 |
| **Total** | | **100** |

## p09-deteksi-tepi

Pekan 09 — Deteksi tepi: Sobel dan Canny. Repo template: `pcd-tugas-p09-deteksi-tepi`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| sobel | `python -m pytest -q tests/test_01_sobel.py` | 50 |
| canny | `python -m pytest -q tests/test_02_canny.py` | 30 |
| rasio tepi | `python -m pytest -q tests/test_03_rasio_tepi.py` | 20 |
| **Total** | | **100** |

## p10-domain-frekuensi

Pekan 10 — Domain frekuensi dengan transformasi Fourier. Repo template: `pcd-tugas-p10-domain-frekuensi`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| spektrum | `python -m pytest -q tests/test_01_spektrum.py` | 35 |
| mask | `python -m pytest -q tests/test_02_mask.py` | 20 |
| lowpass | `python -m pytest -q tests/test_03_lowpass.py` | 45 |
| **Total** | | **100** |

## p11-morfologi

Pekan 11 — Morfologi citra biner: erosi, dilasi, opening. Repo template: `pcd-tugas-p11-morfologi`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| erosi | `python -m pytest -q tests/test_01_erosi.py` | 35 |
| dilasi | `python -m pytest -q tests/test_02_dilasi.py` | 35 |
| opening | `python -m pytest -q tests/test_03_opening.py` | 30 |
| **Total** | | **100** |

## p12-segmentasi

Pekan 12 — Segmentasi: ambang Otsu dan pelabelan objek. Repo template: `pcd-tugas-p12-segmentasi`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| otsu | `python -m pytest -q tests/test_01_otsu.py` | 45 |
| otsu manual | `python -m pytest -q tests/test_02_otsu_manual.py` | 20 |
| hitung objek | `python -m pytest -q tests/test_03_hitung_objek.py` | 35 |
| **Total** | | **100** |

## p13-fitur-warna

Pekan 13 — Ekstraksi fitur warna dan ukuran kemiripan. Repo template: `pcd-tugas-p13-fitur-warna`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| histogram warna | `python -m pytest -q tests/test_01_histogram_warna.py` | 40 |
| jarak euclid | `python -m pytest -q tests/test_02_jarak_euclid.py` | 25 |
| kemiripan kosinus | `python -m pytest -q tests/test_03_kemiripan_kosinus.py` | 35 |
| **Total** | | **100** |

## p14-temu-kembali

Pekan 14 — Temu kembali citra berbasis isi (CBIR). Repo template: `pcd-tugas-p14-temu-kembali`.

| Nama tes | Perintah | Poin |
| --- | --- | --- |
| cari mirip | `python -m pytest -q tests/test_01_cari_mirip.py` | 45 |
| cari mirip batas | `python -m pytest -q tests/test_02_cari_mirip_batas.py` | 20 |
| presisi | `python -m pytest -q tests/test_03_presisi.py` | 35 |
| **Total** | | **100** |
