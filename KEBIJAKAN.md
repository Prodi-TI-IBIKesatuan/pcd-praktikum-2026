# Kebijakan praktikum

## Keamanan

- Semua anggota organisasi wajib memakai autentikasi dua faktor (2FA).
- Token (Moodle, Classroom 50, `KUNCI_TOKEN`) hanya disimpan sebagai *Actions secret*, berjenis *fine-grained*, berlaku satu semester.
- Rahasia yang sempat ter-*commit* dianggap bocor: cabut, buat ulang, laporkan ke Kepala Lab. Menghapus commit saja tidak cukup.

## Privasi

- Repo tugas dan capstone mahasiswa privat selama semester.
- Pemetaan NIM ↔ nama pengguna GitHub hanya disimpan di Moodle dan berkas lokal dosen, tidak pernah di repo (UU No. 27/2022 tentang Pelindungan Data Pribadi).
- Citra untuk capstone: foto sendiri atau data terbuka. Dilarang memakai foto/data rahasia perusahaan atau wajah orang tanpa izin.

## Penggunaan AI (termasuk GitHub Copilot gratis untuk mahasiswa terverifikasi)

| Pekerjaan | AI boleh? | Syarat |
| --- | --- | --- |
| Memahami materi, menjelaskan pesan galat | Ya | — |
| Tugas praktik mingguan | Ya, terbatas | Tulis di `CATATAN.md` bagian mana yang dibantu AI dan apa yang Anda ubah |
| Capstone | Ya, terbatas | Wajib lulus verifikasi lisan: bisa menjelaskan setiap fungsi |
| Kuis mikro Moodle | Tidak | — |
| Kerja DLS (materi, tes, soal) | Ya | Centang bagian AI di template PR; diperiksa manusia sebelum merge |

Tes tertentu memeriksa bahwa fungsi ditulis sendiri (tanpa fungsi siap pakai OpenCV/NumPy yang disebut di docstring). Sinyal yang ditinjau dosen: satu commit berisi jawaban lengkap tanpa riwayat percobaan, `CATATAN.md` kosong berulang, dan hasil verifikasi lisan acak di sesi Meet.

Sanksi: pelanggaran pertama berarti nilai 0 untuk tugas tersebut dan wajib mengulang dengan verifikasi lisan; pelanggaran kedua diteruskan ke Kaprodi.
