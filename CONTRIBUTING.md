# Berkontribusi (alur kerja DLS)

Semua perubahan masuk lewat *pull request* ke `main`; tidak ada yang mendorong langsung ke `main`. Setiap PR ditinjau minimal satu orang dan disetujui dosen (lihat `.github/CODEOWNERS`).

## Satu konten, dari permintaan sampai rilis

1. Dosen membuka issue **Permintaan Konten** (pekan, jenis, capaian, tenggat Kamis).
2. Asisten meng-*assign* diri, lalu membuat branch `pekan/NN-topik` dari `main`.
3. Commit kecil per langkah, pesan diawali jenisnya: `materi:`, `tugas:`, `tes:`, `perbaikan:`, `dok:`.
4. Buka PR berjudul `Pekan NN: <topik>`, tulis `Closes #<nomor issue>`, isi checklist.
5. Perbaiki sampai pemeriksaan **validasi** hijau dan dosen menyetujui; dosen menekan *Merge*.
6. Jumat 18.00 WIB materi rilis otomatis.

## Mengubah atau menambah tugas

Kunci jawaban hanya ada di repo privat `Prodi-TI-IBIKesatuan/pcd-kunci` dengan struktur `pNN/solusi.py`. **Kerangka mahasiswa selalu dibangkitkan dari kunci**, tidak ditulis tangan:

```bash
# 1. ubah ../pcd-kunci/pNN/solusi.py (nama fungsi, parameter, docstring = spesifikasi untuk mahasiswa)
# 2. ubah atau tambah tes: tugas/pNN-*/tests/test_KK_nama.py, satu berkas = satu kriteria nilai
# 3. perbarui bobot di tugas/pNN-*/tests/poin.json (total harus 100)
python tools/buat_stub.py --semua ../pcd-kunci          # kerangka solusi.py
python tools/buat_notebook.py                           # notebook Colab
python tools/buat_readme_tugas.py                       # README repo tugas
python tools/buat_konfigurasi_classroom50.py            # tabel tes Classroom 50
python tools/uji_template.py pNN --kunci ../pcd-kunci   # harus: stub 0/100, kunci 100/100
```

Aturan menulis tes:

- Tes harus **memanggil** fungsi mahasiswa, agar kerangka kosong pasti mendapat 0.
- Pesan galat ditulis dalam bahasa Indonesia yang menjelaskan apa yang salah.
- Bila sebuah fungsi wajib ditulis sendiri, pakai `larang("nama_fungsi", "cvtColor", ...)` dari `conftest.py`; pemeriksaan ini mengikuti fungsi bantu yang dipanggil.
- Gunakan citra sintetis (`citra_bgr`, `citra_gray`) atau buat dengan `np.random.default_rng(seed)` agar hasil selalu sama. Jangan menambah berkas gambar besar.
- Uji juga kesalahan umum (overflow uint8, kernel terbalik, batas citra).

Setelah merge, dorong perubahan ke repo template: `PERBARUI_TEMPLATE=1 bash tools/setup-github.sh`. Mahasiswa yang sudah menerima assignment tidak otomatis mendapat perubahan; umumkan bila tes berubah di tengah pekan.

## Yang tidak boleh masuk repo ini

Kunci jawaban, bank soal, roster, NIM, nilai, token, kata sandi, dan video mentah. Video final diunggah *unlisted* ke YouTube/Drive kampus; tautannya ditulis di README modul.
