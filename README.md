# Praktikum Pengolahan Citra Digital 2026


[![Validasi tugas](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/actions/workflows/validasi-tugas.yml/badge.svg)](https://github.com/Prodi-TI-IBIKesatuan/pcd-praktikum-2026/actions/workflows/validasi-tugas.yml)

## Mulai dari sini

| Saya… | Baca |
| --- | --- |
| Mahasiswa | [docs/panduan-mahasiswa.md](docs/panduan-mahasiswa.md) |
| Asisten Digital Learning Squad (DLS) | [docs/panduan-asisten.md](docs/panduan-asisten.md) dan [CONTRIBUTING.md](CONTRIBUTING.md) |
| Dosen pengampu | [docs/panduan-dosen.md](docs/panduan-dosen.md) |
| Semua | [KEBIJAKAN.md](KEBIJAKAN.md) — keamanan, privasi, dan penggunaan AI |

## Siklus mingguan

| Hari | Yang terjadi |
| --- | --- |
| Senin–Kamis | DLS menyiapkan materi pekan depan lewat *pull request*; dosen meninjau dan merge |
| Jumat 18.00 WIB | Workflow **Weekend Release** menerbitkan Release `PNN` sesuai [KALENDER.csv](KALENDER.md) |
| Sabtu–Minggu | Mahasiswa menonton video, berlatih di Colab, mengerjakan repo tugas; autograder menilai tiap *commit* |
| Minggu 23.59 WIB | Tenggat tugas; Classroom 50 mengumpulkan skor |
| Senin–Jumat 19.30 WIB | Sesi Meet 45 menit: *live coding* dan membahas tes yang paling sering gagal |

## Isi repo

```text
modul/pekan-NN-*/      README materi + latihan.ipynb (tombol "Buka di Colab")
tugas/_umum/           berkas bersama semua repo tugas (autograder, Codespaces, workflow)
tugas/pNN-*/           solusi.py (kerangka) + tests/ + poin.json untuk 14 tugas
capstone/              template proyek UTS/UAS (aplikasi Gradio) + rubrik
docs/                  panduan per peran + konfigurasi tes Classroom 50
tools/                 alat bantu: rakit & uji template, stub, notebook, impor nilai, setup GitHub
.github/workflows/     weekend-release, validasi-tugas, autograde-python (reusable)
```

## Pemeriksaan mutu

Setiap *pull request* menjalankan [validasi-tugas](.github/workflows/validasi-tugas.yml): kerangka `solusi.py` harus mendapat **0**, kunci jawaban (repo privat `pcd-kunci`) harus mendapat **100**, dan notebook serta tabel Classroom 50 harus sinkron dengan tes. Jalankan lokal:

```bash
pip install -r requirements-dev.txt
python tools/uji_template.py --kunci ../pcd-kunci
```

## Lisensi

Kode: MIT. Materi ajar: CC BY-SA 4.0. Lihat [LICENSE-MATERI.md](LICENSE-MATERI.md).
