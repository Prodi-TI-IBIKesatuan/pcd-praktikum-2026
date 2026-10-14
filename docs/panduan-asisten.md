# Panduan Asisten (Digital Learning Squad)

Seluruh kerja DLS tercatat sebagai issue dan *pull request* atas nama Anda di organisasi prodi. Catatan ini menjadi dasar insentif Pay-per-Video, konversi SKS magang, dan surat rekomendasi.

## Tugas rutin per pekan

| Hari | Pekerjaan |
| --- | --- |
| Senin | Impor skor pekan lalu ke Moodle (`tools/impor_nilai.py`), tandai kasus untuk dosen |
| Senin–Rabu | Kerjakan issue *Permintaan Konten* pekan depan; buka PR `Pekan NN` (alur di [CONTRIBUTING.md](../CONTRIBUTING.md)) |
| Setiap hari | Piket issue **Kendala Lab** (jawab ≤ 24 jam) dan komentar `[KEBERATAN]` (≤ 48 jam) |
| Sesi Meet | Catat pertanyaan yang belum terjawab sebagai *Discussion* |

## Standar QA video

720p/1080p, durasi 10–15 menit, audio dibersihkan (Adobe Podcast), takarir otomatis sudah dikoreksi, ukuran ramah kuota. Video final diunggah *unlisted*; hanya tautannya yang masuk README modul.

## Menangani keberatan nilai

1. Buka repo mahasiswa, jalankan `python tests/jalankan_semua.py` di Codespace untuk melihat pesan lengkap.
2. Jika mahasiswa salah: balas di PR Feedback dengan kriteria yang gagal dan petunjuk (bukan jawaban).
3. Jika tes yang salah: perbaiki tes lewat PR ke repo ini, minta dosen merge, jalankan `PERBARUI_TEMPLATE=1 bash tools/setup-github.sh`, lalu minta dosen memicu pengumpulan skor ulang di Classroom 50.

## Kasus yang ditandai untuk dosen

- Skor 0 dua pekan berturut-turut (mahasiswa mungkin tertinggal).
- Satu commit berisi seluruh jawaban menjelang tenggat tanpa riwayat percobaan.
- Ada commit yang mengubah `tests/` atau `.github/` (cek: `git log --oneline -- tests .github`).
- `CATATAN.md` kosong atau generik tiga pekan berturut-turut.

## Membuktikan kontribusi

```bash
gh search prs --owner Prodi-TI-IBIKesatuan --author <username> --merged --limit 200
gh search issues --owner Prodi-TI-IBIKesatuan --label video --assignee <username> --state closed
```

Karena repo ini publik, kontribusi Anda tampil di grafik kontribusi profil GitHub masing-masing.
