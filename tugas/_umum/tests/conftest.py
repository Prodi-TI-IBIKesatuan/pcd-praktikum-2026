"""Perlengkapan bersama untuk semua tes tugas praktikum PCD.

Berkas ini disalin ke setiap repo tugas oleh tools/rakit_template.py.
Jangan diubah oleh mahasiswa.
"""
from __future__ import annotations

import ast
import pathlib
import sys

import numpy as np
import pytest

AKAR = pathlib.Path(__file__).resolve().parents[1]
if str(AKAR) not in sys.path:
    sys.path.insert(0, str(AKAR))


@pytest.fixture(scope="session")
def solusi():
    """Modul solusi.py milik mahasiswa."""
    import solusi as modul  # noqa: WPS433

    return modul


@pytest.fixture()
def citra_bgr() -> np.ndarray:
    """Citra warna sintetis 48x64 (BGR, uint8) yang selalu sama."""
    rng = np.random.default_rng(2026)
    return rng.integers(0, 256, size=(48, 64, 3), dtype=np.uint8)


@pytest.fixture()
def citra_gray() -> np.ndarray:
    """Citra keabuan sintetis 40x52 (uint8) dengan gradasi + derau."""
    rng = np.random.default_rng(7)
    y, x = np.mgrid[0:40, 0:52]
    dasar = (x * 3 + y * 2) % 256
    derau = rng.integers(-20, 21, size=dasar.shape)
    return np.clip(dasar + derau, 0, 255).astype(np.uint8)


def _nama_panggilan(node: ast.Call) -> str:
    fungsi = node.func
    if isinstance(fungsi, ast.Attribute):
        return fungsi.attr
    if isinstance(fungsi, ast.Name):
        return fungsi.id
    return ""


def panggilan_dalam(nama_fungsi: str, berkas: pathlib.Path | None = None) -> set[str]:
    """Semua nama fungsi yang dipanggil oleh `nama_fungsi` di solusi.py,
    termasuk lewat fungsi bantu lain yang didefinisikan di berkas yang sama."""
    berkas = berkas or AKAR / "solusi.py"
    pohon = ast.parse(berkas.read_text(encoding="utf-8"))
    definisi = {
        n.name: n for n in ast.walk(pohon) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    if nama_fungsi not in definisi:
        raise AssertionError(f"Fungsi {nama_fungsi}() tidak ditemukan di solusi.py")
    terkunjungi: set[str] = set()
    hasil: set[str] = set()
    antrean = [nama_fungsi]
    while antrean:
        nama = antrean.pop()
        if nama in terkunjungi:
            continue
        terkunjungi.add(nama)
        for node in ast.walk(definisi[nama]):
            if isinstance(node, ast.Call):
                dipanggil = _nama_panggilan(node)
                hasil.add(dipanggil)
                if dipanggil in definisi:
                    antrean.append(dipanggil)
    return hasil


def larang(nama_fungsi: str, *terlarang: str) -> None:
    """Gagalkan tes bila `nama_fungsi` memakai fungsi siap pakai yang dilarang."""
    dipakai = panggilan_dalam(nama_fungsi) & set(terlarang)
    assert not dipakai, (
        f"{nama_fungsi}() harus ditulis sendiri, tetapi memakai: {', '.join(sorted(dipakai))}"
    )
