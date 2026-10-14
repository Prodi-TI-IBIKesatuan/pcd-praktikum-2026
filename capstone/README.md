# Capstone Praktikum PCD

Capstone menggantikan UTS (30%) dan UAS (30%). Mahasiswa mengerjakan **satu repo yang sama** sepanjang semester, dibuat dari `capstone/template` lewat assignment Classroom 50 "Capstone" (tanpa autograding nilai; tes pipeline hanya umpan balik).

| Tahap | Rilis | Isi yang dinilai | Bobot |
| --- | --- | --- | --- |
| Tahap 1 (UTS) | Release `UTS` di repo capstone | README: masalah, diagram pipeline, ≥ 20 citra, `pipeline.py` berjalan | 30% |
| Tahap 2 (UAS) | Release `UAS` di repo capstone | Aplikasi Gradio publik di Hugging Face Spaces, evaluasi presisi@k ≥ 2 fitur, video demo | 30% |

Studi kasus diambil dari tempat kerja mahasiswa (mis. pencarian foto produk gudang, pencocokan foto kerusakan barang, pencarian label kemasan) dengan **data rekaan atau foto sendiri** — tidak boleh foto/data rahasia perusahaan atau wajah orang tanpa izin.

Pengayaan untuk tahap 2: ganti `ekstrak_fitur()` dengan embedding model pralatih (mis. ResNet/CLIP lewat `torchvision` atau `transformers`) dan bandingkan dengan histogram warna. Rubrik lengkap: [RUBRIK.md](RUBRIK.md).
