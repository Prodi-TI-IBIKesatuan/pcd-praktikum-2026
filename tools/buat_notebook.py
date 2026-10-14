"""Bangkitkan modul/pekan-NN-*/latihan.ipynb dari stub tugas/pNN-*/solusi.py.

Notebook dibuka di Google Colab (bisa dari HP) lewat tombol di README modul.
Isinya: penyiapan citra contoh, fungsi pekan itu (stub yang sama dengan repo
tugas), sel percobaan, dan petunjuk mengumpulkan.

Pemakaian:
    python tools/buat_notebook.py           # tulis ulang semua notebook
    python tools/buat_notebook.py --cek     # gagal bila ada notebook yang tidak sinkron
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

AKAR = pathlib.Path(__file__).resolve().parents[1]
REPO = "Prodi-TI-IBIKesatuan/pcd-praktikum-2026"

PENYIAPAN = '''import cv2
import numpy as np
import matplotlib.pyplot as plt

try:
    from skimage import data
    citra = cv2.cvtColor(data.astronaut(), cv2.COLOR_RGB2BGR)   # citra contoh 512x512 (BGR)
except ImportError:  # tanpa scikit-image: pakai citra sintetis
    y, x = np.mgrid[0:256, 0:256]
    citra = np.dstack([x, y, (x + y) // 2]).astype(np.uint8)
abu = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)


def tampil(*gambar, judul=None):
    """Tampilkan beberapa citra berdampingan. Citra 3 kanal dianggap BGR."""
    judul = judul or [""] * len(gambar)
    fig, ax = plt.subplots(1, len(gambar), figsize=(4 * len(gambar), 4))
    ax = np.atleast_1d(ax)
    for a, g, j in zip(ax, gambar, judul):
        if g.ndim == 3:
            a.imshow(g[:, :, ::-1])
        else:
            a.imshow(g, cmap="gray")
        a.set_title(j)
        a.axis("off")
    plt.show()


print("Citra contoh:", citra.shape, citra.dtype)'''

DEMO = {
    "p01": 'print(info_citra(citra))\nprint(info_citra(abu))\ntampil(citra, potong(citra, 180, 60, 160, 160), judul=["asli", "potongan wajah"])',
    "p02": 'g = ke_grayscale(citra)\ntampil(bgr_ke_rgb(citra)[:, :, ::-1], g, ke_biner(g, 128), judul=["warna", "keabuan", "biner > 128"])',
    "p03": 'tampil(abu, negatif(abu), atur_kecerahan(abu, 60), atur_kontras(abu, 1.8),\n       judul=["asli", "negatif", "kecerahan +60", "kontras x1.8"])',
    "p04": 'gelap = (abu // 3).astype(np.uint8)\nhasil = ekualisasi(gelap)\ntampil(gelap, hasil, judul=["gelap", "ekualisasi"])\nplt.bar(range(256), histogram(gelap), width=1, label="sebelum")\nplt.bar(range(256), histogram(hasil), width=1, alpha=0.6, label="sesudah")\nplt.legend(); plt.show()',
    "p05": 'mask = np.zeros(abu.shape, np.uint8)\ncv2.circle(mask, (256, 200), 140, 255, -1)\ntampil(campur(citra, citra[:, ::-1], 0.5), selisih_absolut(citra, citra[:, ::-1]), terapkan_mask(citra, mask),\n       judul=["campur 0.5", "selisih", "mask lingkaran"])',
    "p06": 'tampil(balik_horizontal(citra), rotasi_90(citra, 1), ubah_ukuran_terdekat(citra[200:260, 230:290], 6),\n       judul=["cermin", "rotasi 90", "perbesar 6x (terdekat)"])',
    "p07": 'tajam = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])\ntampil(abu, np.clip(konvolusi2d(abu, tajam), 0, 255).astype(np.uint8), filter_rerata(abu, 7),\n       judul=["asli", "penajaman", "rerata 7x7"])',
    "p08": 'berderau = tambah_garam_merica(abu, 0.1, seed=1)\nhalus = np.clip(cv2.filter2D(berderau.astype(float), -1, kernel_gauss(5, 1.5)), 0, 255).astype(np.uint8)\ntampil(berderau, halus, filter_median(berderau, 3), judul=["derau 10%", "Gauss 5x5", "median 3x3"])',
    "p09": 'gx, gy, mag = sobel(abu)\ntepi = tepi_canny(abu, 80, 160)\nprint("rasio tepi:", rasio_tepi(tepi))\ntampil(np.clip(mag, 0, 255).astype(np.uint8), tepi, judul=["magnitudo Sobel", "Canny"])',
    "p10": 'tampil(abu, spektrum_magnitudo(abu), np.clip(lowpass_ideal(abu, 30), 0, 255).astype(np.uint8),\n       judul=["asli", "spektrum (log)", "lolos-rendah r=30"])',
    "p11": 'biner = np.where(abu > 128, 255, 0).astype(np.uint8)\ntampil(biner, erosi(biner, 5), dilasi(biner, 5), opening(biner, 5), judul=["biner", "erosi", "dilasi", "opening"])',
    "p12": 't = ambang_otsu(abu)\nseg = segmentasi_otsu(abu)\nprint("ambang Otsu:", t, "| jumlah objek:", hitung_objek(seg))\ntampil(abu, seg, judul=["asli", f"Otsu t={t}"])',
    "p13": 'a = histogram_warna(citra, 8)\nb = histogram_warna(citra[:, ::-1], 8)\nc = histogram_warna(255 - citra, 8)\nprint("cermin  -> kosinus", kemiripan_kosinus(a, b), "euclid", jarak_euclid(a, b))\nprint("negatif -> kosinus", kemiripan_kosinus(a, c), "euclid", jarak_euclid(a, c))',
    "p14": 'potongan = [citra[y:y + 128, x:x + 128] for y in range(0, 512, 128) for x in range(0, 512, 128)]\nfitur = np.array([np.concatenate([np.bincount(p[:, :, k].ravel() // 32, minlength=8) for k in range(3)]) for p in potongan], float)\nhasil = cari_mirip(fitur[5], fitur, 4)\nprint("paling mirip dengan potongan 5:", hasil)\ntampil(*[potongan[i] for i in hasil], judul=[f"#{i}" for i in hasil])',
}


def folder_pasangan():
    for tugas in sorted((AKAR / "tugas").glob("p[0-9][0-9]-*")):
        kode = tugas.name[:3]
        modul = sorted((AKAR / "modul").glob(f"pekan-{kode[1:]}-*"))
        if modul:
            yield kode, tugas, modul[0]


def bangun(kode: str, tugas: pathlib.Path, modul: pathlib.Path) -> nbformat.NotebookNode:
    stub = (tugas / "solusi.py").read_text(encoding="utf-8").rstrip()
    judul = stub.splitlines()[0].strip('"')
    sel = [
        new_markdown_cell(
            f"# Latihan {judul}\n\n"
            "Notebook ini untuk **berlatih**, bukan untuk dikumpulkan. Jalankan sel dari atas ke bawah "
            "(Colab: *Runtime → Run all*).\n\n"
            "1. Kerjakan fungsi di sel **Fungsi pekan ini** sampai sel **Coba** menampilkan hasil yang masuk akal.\n"
            "2. Salin isi fungsi ke `solusi.py` di repo tugas Anda, lalu *commit*.\n"
            "3. Tunggu tanda hijau di GitHub: itu berarti semua tes lulus."
        ),
        new_code_cell(PENYIAPAN),
        new_markdown_cell("## Fungsi pekan ini\n\nIsi sama persis dengan `solusi.py` di repo tugas. Ganti setiap `raise NotImplementedError` dengan jawaban Anda."),
        new_code_cell(stub),
        new_markdown_cell("## Coba"),
        new_code_cell(DEMO.get(kode, "# Coba fungsi Anda di sini")),
        new_markdown_cell(
            "## Kumpulkan\n\n"
            "Buka repo tugas Anda di github.com → `solusi.py` → ikon pensil → tempel fungsi → **Commit changes**. "
            "Isi juga `CATATAN.md`. Tenggat: **Minggu 23.59 WIB**."
        ),
    ]
    for i, s in enumerate(sel):
        s["id"] = f"sel-{i:02d}"
    nb = new_notebook(cells=sel)
    nb.metadata = {
        "colab": {"provenance": [], "name": f"latihan-{modul.name}.ipynb"},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"},
    }
    nbformat.validate(nb)
    return nb


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cek", action="store_true")
    arg = parser.parse_args()
    beda = []
    for kode, tugas, modul in folder_pasangan():
        teks = nbformat.writes(bangun(kode, tugas, modul)) + "\n"
        berkas = modul / "latihan.ipynb"
        if arg.cek:
            if not berkas.exists() or berkas.read_text(encoding="utf-8") != teks:
                beda.append(str(berkas.relative_to(AKAR)))
        else:
            berkas.write_text(teks, encoding="utf-8")
            print(f"ditulis {berkas.relative_to(AKAR)}")
    if beda:
        print("Notebook tidak sinkron (jalankan tools/buat_notebook.py):\n  " + "\n  ".join(beda))
        return 1
    if arg.cek:
        print("Semua notebook sinkron.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
