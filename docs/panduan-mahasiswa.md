# Panduan Mahasiswa

Setiap tugas dikumpulkan sebagai *commit* ke repo GitHub pribadi Anda dan langsung dinilai otomatis. Semua langkah bisa dikerjakan dari smartphone.

## Persiapan pekan pertama (sekali, ±30 menit)

1. Buat akun di github.com memakai **email kampus**, aktifkan 2FA.
2. Ajukan GitHub Education sebagai *Student* di education.github.com (gratis Copilot dan Codespaces).
3. Pasang aplikasi **GitHub Mobile** untuk notifikasi hasil tes dan komentar dosen.
4. Isi formulir **Nama Pengguna GitHub** di Moodle. Tanpa ini nilai Anda tidak bisa dicocokkan dengan NIM.
5. Terima undangan organisasi kelas dari email/notifikasi GitHub.

## Alur tugas mingguan

1. **Jumat malam:** buka Moodle, klik tautan assignment pekan ini, tekan *Accept*. Repo `pcd-tugas-pNN-…-<username>` dibuat untuk Anda.
2. **Sabtu–Minggu:** tonton video, lalu buka README modul dan tekan **Buka di Colab**. Kerjakan fungsi di notebook sampai sel *Coba* menampilkan hasil yang benar.
3. **Kumpulkan:** di github.com buka repo tugas → `solusi.py` → ikon pensil → tempel fungsi Anda → **Commit changes**.
4. **Lihat nilai:** tanda kuning = sedang dinilai, hijau = semua kriteria lulus, merah = ada yang gagal. Ketuk tanda itu → *Details* untuk melihat kriteria yang gagal dan pesannya. Perbaiki dan commit lagi sesering yang Anda mau sebelum tenggat.
5. **Isi `CATATAN.md`** (3–5 kalimat) dan unggah tangkapan layar hasil di Colab ke folder `bukti/`.
6. **Minggu 23.59 WIB:** tenggat. Commit setelahnya tidak dihitung.

## Pilih alat sesuai perangkat

| Perangkat | Alat | Catatan |
| --- | --- | --- |
| Smartphone | Google Colab + editor web github.com + GitHub Mobile | Cukup untuk semua tugas mingguan |
| Laptop/PC | GitHub Codespaces (*Code → Codespaces → Create*) | VS Code + Python siap pakai; hentikan Codespace setelah selesai agar jatah 180 jam/bulan awet |
| Laptop + Python lokal | `pip install -r requirements.txt` lalu `python tests/jalankan_semua.py` | Melihat skor sebelum commit |

## Kebiasaan commit yang dinilai baik

- Commit setiap kali satu fungsi selesai, bukan sekali di akhir. Riwayat bertahap adalah bukti Anda mengerjakan sendiri.
- Pesan commit menjelaskan perubahan: `tugas: ekualisasi histogram`, bukan `update`.
- Jangan menulis token, kata sandi, atau NIM di repo.
- Tidak sempat karena lembur? Commit apa pun yang sudah ada: nilai sebagian lebih baik dari nol.

## Keberatan nilai

Tulis komentar di *pull request* bernama **Feedback** di repo tugas Anda, diawali `[KEBERATAN]`, paling lambat Rabu setelah tenggat. Jelaskan kriteria mana dan mengapa. DLS menjawab dalam 48 jam; bila tes terbukti salah, tes diperbaiki untuk semua dan skor dikumpulkan ulang.

## Troubleshooting

| Gejala | Penyebab umum | Solusi |
| --- | --- | --- |
| Tautan assignment "tidak punya akses" | Undangan organisasi belum diterima | Buka email/notifikasi GitHub, terima undangan, ulangi tautan |
| Nilai di Moodle 0 padahal tanda hijau | Nama pengguna GitHub belum/salah diisi di Moodle | Perbaiki formulir; DLS mengimpor ulang |
| `NotImplementedError ... belum dikerjakan` | Baris `raise NotImplementedError` belum dihapus | Hapus baris itu setelah menulis jawaban |
| "harus ditulis sendiri, tetapi memakai: …" | Memakai fungsi siap pakai yang dilarang di docstring | Tulis ulang dengan NumPy/loop sendiri |
| Benar di Colab, gagal di tes | Tipe data atau pembulatan berbeda (mis. hasil float, bukan uint8) | Baca docstring: tipe dan cara pembulatan ikut dinilai |
| `ModuleNotFoundError: solusi` | Berkas `solusi.py` diganti nama atau dipindah | Kembalikan nama dan letaknya di akar repo |
| Codespace gagal dibuat | Benefit Education belum aktif atau jatah habis | Cek education.github.com; pakai Colab sementara |

Masalah lain: buka issue **Kendala Lab** di repo materi (jangan tempel kode jawaban).

## Capstone (UTS & UAS)

Lihat [capstone/README.md](../capstone/README.md) dan [rubriknya](../capstone/RUBRIK.md). Setelah nilai keluar, repo capstone boleh Anda jadikan publik dan disematkan di profil GitHub sebagai portofolio.
