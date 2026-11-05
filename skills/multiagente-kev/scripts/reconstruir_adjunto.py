"""Reconstruye un archivo adjuntado desde el Tablero de agentes.

El tablero guarda cada archivo partido en documentos de la colección
`adjuntos_partes` (campo `datos` en base64, campo `n` con el orden).
Uso:
    python3 -I reconstruir_adjunto.py <carpeta_out_dir> <id_adjunto> <ruta_salida>
<carpeta_out_dir> es la que se pasó como `out_dir` a ArtifactData al leer
`adjuntos_partes` filtrado por `adjunto == <id_adjunto>`.
"""
import base64
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    carpeta, adjunto, salida = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    partes = []
    for archivo in carpeta.rglob(f"{adjunto}--*.json"):
        obj = json.loads(archivo.read_text(encoding="utf-8"))
        datos = obj.get("data", obj)
        if datos.get("adjunto") != adjunto:
            continue
        partes.append((int(datos["n"]), datos["datos"]))
    if not partes:
        print(f"No encontré partes del adjunto {adjunto} en {carpeta}")
        return 1
    partes.sort()
    esperadas = list(range(len(partes)))
    if [n for n, _ in partes] != esperadas:
        print("Faltan partes del adjunto; vuelvan a leer la colección completa.")
        return 1
    contenido = base64.b64decode("".join(d for _, d in partes))
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_bytes(contenido)
    print(f"Listo: {salida} ({len(contenido)} bytes, {len(partes)} partes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
