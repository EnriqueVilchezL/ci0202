"""Empaqueta el material descargable (PDF y notebooks) en un .zip.

Lee la tabla de contenidos (`project.toc`) de `myst.yml` para saber qué
páginas están efectivamente publicadas, y por cada una incluye:

- el archivo `.ipynb`, si la página es un notebook.
- el `.pdf` con el mismo nombre en la misma carpeta, si la página es un
  Markdown que tiene un PDF asociado.

No se incluye Markdown ni páginas que no aparezcan en el `toc`, para que
el contenido del zip sea siempre consistente con lo que está publicado
en el sitio.
"""

import zipfile
from pathlib import Path

import yaml

BOOK_DIR = Path(__file__).resolve().parent.parent
MYST_YML = BOOK_DIR / "myst.yml"
OUTPUT_ZIP = BOOK_DIR / "resources" / "material_teorico.zip"


def toc_entries(toc: list[dict]) -> list[str]:
    entries = []
    for entry in toc:
        if "file" in entry:
            entries.append(entry["file"])
        for child in entry.get("children", []):
            if "file" in child:
                entries.append(child["file"])
    return entries


def archivos_descargables() -> list[Path]:
    config = yaml.safe_load(MYST_YML.read_text(encoding="utf-8"))
    toc = config["project"]["toc"]

    archivos = []
    for relative_path in toc_entries(toc):
        page = BOOK_DIR / relative_path
        if page.suffix == ".ipynb":
            if page.is_file():
                archivos.append(page)
        elif page.suffix == ".md":
            pdf = page.with_suffix(".pdf")
            if pdf.is_file():
                archivos.append(pdf)
    return archivos


def generar_zip() -> None:
    OUTPUT_ZIP.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for archivo in archivos_descargables():
            zf.write(archivo, archivo.relative_to(BOOK_DIR))
    print(f"Zip generado: {OUTPUT_ZIP}")


if __name__ == "__main__":
    generar_zip()
