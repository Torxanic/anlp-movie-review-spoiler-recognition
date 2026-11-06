# Movie Review Spoiler Detection

## Projektstruktur

- `notebooks/`: Analyse-Notebook
- `data/`: lokale Datendateien (nicht versioniert)
- `outputs/figures/` und `outputs/tables/`: exportierte Ergebnisse
- `cache/`: Joblib-Cache
- `src/movie_review_spoiler_detection/`: Python-Paketcode

## Einrichtung und Notebook ausführen

### Voraussetzungen

- Python in der in `.python-version` angegebenen Version
- [uv](https://docs.astral.sh/uv/getting-started/installation/) zur Verwaltung der Python-Umgebung und Abhängigkeiten
- VS Code mit der Python- und Jupyter-Erweiterung, wenn du das Notebook in VS Code ausführen möchtest

### Umgebung einrichten

Öffne PowerShell im Projektordner und installiere die Abhängigkeiten:

```powershell
uv sync
```

Damit erstellt uv die virtuelle Umgebung in `.venv` und installiert die im Projekt festgelegten Abhängigkeiten.

### Draft-Notebook starten

1. Öffne den Projektordner in VS Code.
2. Öffne `notebooks/spoiler_detection_draft.ipynb`.
3. Wähle im Notebook als Kernel den Python-Interpreter aus `.venv` aus. Falls er nicht angezeigt wird, wähle **Python: Select Interpreter** und dann `.venv\Scripts\python.exe`.
4. Führe die Zellen der Reihe nach aus oder wähle **Run All**.

Lege die Datei `IMDB_movie_details.json` in `data/` ab. Falls `IMDB_reviews.json` dort fehlt, versucht das Notebook, sie mit KaggleHub herunterzuladen; dafür ist Kaggle-Zugriff erforderlich. Die Daten- und Ausgabeordner werden relativ zum Projektstamm bestimmt, der über `pyproject.toml` gefunden wird.