"""Antarmuka Gradio untuk aplikasi capstone. Jalankan: python app.py

Deploy gratis ke Hugging Face Spaces (SDK: Gradio): unggah isi folder ini
beserta folder galeri/ berisi citra basis data Anda.
"""
import pathlib

import cv2
import gradio as gr

from pipeline import bangun_indeks, cari

GALERI = pathlib.Path(__file__).parent / "galeri"
BERKAS, FITUR = bangun_indeks(GALERI)


def proses(citra_rgb, k):
    if citra_rgb is None:
        return [], "Unggah citra dulu."
    hasil = cari(cv2.cvtColor(citra_rgb, cv2.COLOR_RGB2BGR), BERKAS, FITUR, int(k))
    if not hasil:
        return [], "Folder galeri/ masih kosong."
    return [(str(p), f"{p.name} — {s:.3f}") for p, s in hasil], f"{len(BERKAS)} citra di basis data."


with gr.Blocks(title="Temu Kembali Citra") as demo:
    gr.Markdown("# Temu Kembali Citra\nUnggah citra untuk mencari citra paling mirip di basis data.")
    with gr.Row():
        masukan = gr.Image(label="Citra query", type="numpy")
        with gr.Column():
            k = gr.Slider(1, 12, value=5, step=1, label="Jumlah hasil")
            tombol = gr.Button("Cari", variant="primary")
            info = gr.Markdown()
    galeri = gr.Gallery(label="Hasil", columns=5)
    tombol.click(proses, [masukan, k], [galeri, info])

if __name__ == "__main__":
    demo.launch()
