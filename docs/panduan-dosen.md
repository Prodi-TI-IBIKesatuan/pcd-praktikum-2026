# Panduan Dosen

Penyiapan dilakukan sekali (±4 jam, sebagian besar bisa didelegasikan ke DLS); selama semester berjalan dosen cukup **±80 menit per minggu**.

## Penyiapan awal semester

1. **Verifikasi GitHub Education sebagai Teacher**, lalu upgrade organisasi kelas ke GitHub Team (gratis). Disarankan memakai organisasi terpisah untuk repo mahasiswa (mis. `Prodi-TI-IBIKesatuan-Kelas`), karena token Classroom 50 punya akses baca-tulis ke semua repo di organisasinya.
2. **Jalankan skrip penyiapan** dari akar repo ini (gh CLI login sebagai owner):
   ```bash
   DRY_RUN=1 bash tools/setup-github.sh   # tinjau dulu
   bash tools/setup-github.sh             # label, tim, ruleset main, 14 repo template, tag v1
   ```
   Tambahkan diri Anda ke tim `dosen-pcd` dan asisten ke tim `dls`.
3. **Kunci jawaban:** buat repo privat `pcd-kunci` (isi `pNN/solusi.py`), lalu simpan *fine-grained token* baca-saja ke repo itu sebagai secret `KUNCI_TOKEN` di repo ini. Validasi otomatis kemudian memastikan setiap tugas bisa mencapai 100.
4. **Classroom 50:** masuk classroom50.org, jalankan *organization setup* untuk organisasi kelas, buat classroom (mis. `pcd-karyawan-a`, term `2026-genap`), lalu buat 14 assignment + 1 assignment Capstone. Beri slug assignment `p01`…`p14` dan `capstone` agar repo mahasiswa bernama `<kelas>-pNN-<username>`; pilih template `pcd-tugas-pNN-…`, visibilitas privat, dan isi *release date* Jumat 18.00 WIB sesuai KALENDER agar assignment baru terlihat saat rilis. Salin tes dari [classroom50-tes.md](classroom50-tes.md). Di pengaturan lanjutan, batasi berkas yang dinilai hanya `solusi.py` agar perubahan mahasiswa pada `tests/` dan `.github/` diabaikan.
5. **Roster:** ekspor mahasiswa dari Moodle, gabungkan dengan formulir nama pengguna GitHub (kolom `nim,nama,github,email`), unggah ke Classroom 50. Simpan berkas roster di komputer Anda, **bukan** di repo.
6. **Moodle:** restore blueprint kelas, tempel *accept link* tiap assignment (halaman submissions → **Share** → **Copy accept link**) sebagai aktivitas URL di pekan yang sesuai, plus tautan README modul. Moodle hanya menyimpan tautan; repo mahasiswa dibuat oleh Classroom 50 saat mahasiswa menekan *Accept*. Opsional: isi secret `MOODLE_TOKEN`, variable `MOODLE_URL`, dan `MODUL_P01`…`MODUL_P14` (cmid aktivitas) agar rilis Jumat ikut menampilkan aktivitas Moodle.
7. **Sesuaikan [KALENDER.csv](../KALENDER.md)** dengan kalender akademik.
8. **Uji ujung ke ujung** dengan satu akun mahasiswa uji: terima assignment P01, commit jawaban salah lalu benar, pastikan skor terbaca.

## Alokasi 80 menit per minggu

| Kegiatan | Caranya | Menit |
| --- | --- | --- |
| Rilis materi | Tinjau PR `Pekan NN` dari DLS di GitHub (browser cukup), *Approve* dan *Merge*. Rilis berjalan sendiri Jumat 18.00 WIB | 5 |
| Sesi Meet | 5 menit ringkasan tes paling banyak gagal (dasbor Classroom 50) → 20 menit *live coding* di Colab/Codespaces → 15 menit dua mahasiswa acak menjelaskan commit mereka → 5 menit tanya jawab | 45 |
| Verifikasi tugas | Tinjau daftar yang ditandai DLS: skor 0, commit tunggal mencurigakan, keberatan | 30 |

## Memindahkan nilai ke Moodle (Senin)

```bash
python tools/impor_nilai.py skor-p03.csv ~/rahasia/roster.csv "Tugas Praktik P03" -o moodle-p03.csv
```

Skrip mendeteksi kolom Classroom 50 otomatis, menskalakan ke 0–100, dan melaporkan mahasiswa tanpa skor serta nama pengguna yang tidak ada di roster. Impor `moodle-p03.csv` di Moodle (*Nilai → Impor → Berkas CSV*), petakan "ID number" ke "ID number". Tugas ini bisa didelegasikan ke DLS dengan peran *Non-editing teacher*.

## Komposisi nilai

| Komponen | Bobot | Sumber |
| --- | --- | --- |
| Presensi | 10% | Moodle |
| Kuis mikro | 10% | Moodle |
| Tugas praktik | 20% | Rata-rata 14 skor autograder |
| UTS | 30% | Capstone tahap 1, [rubrik](../capstone/RUBRIK.md) |
| UAS | 30% | Capstone tahap 2, rubrik + demo |

## Akhir semester

Arsipkan repo tugas mahasiswa, keluarkan anggota yang tidak lanjut, rekap kontribusi DLS (lihat panduan asisten), dan perbarui blueprint Moodle.
