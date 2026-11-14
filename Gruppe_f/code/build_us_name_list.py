import csv
import io
import os
import re
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path


TOP_N = 1000
FIRST_YEAR = 1880
LAST_YEAR = 2024

SSA_URL = "https://www.ssa.gov/oact/babynames/names.zip"
CENSUS_URL = "https://www2.census.gov/topics/genealogy/2010surnames/names.zip"

# Auf Windows liegt der Cache unter %LOCALAPPDATA%, nicht im Abgabeordner.
CACHE_ROOT = Path(
    os.environ.get("LOCALAPPDATA", str(Path.home() / ".cache"))
)
CACHE_DIR = CACHE_ROOT / "movie-review-spoiler-recognition" / "name_sources"

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_DIR / "data" / "us_name_lists.csv"


def download_if_missing(url: str, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)

    if not destination.exists():
        print(f"Lade {url} nach {destination} …")
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "movie-review-spoiler-recognition/0.1",
                "Accept": "application/zip, application/octet-stream, */*",
            },
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            destination.write_bytes(response.read())

    return destination


def top_first_names(
    counts: Counter, sex: str
) -> list[tuple[str, int]]:
    ranked = sorted(
        (
            (name, count)
            for (name_sex, name), count in counts.items()
            if name_sex == sex
        ),
        key=lambda item: (-item[1], item[0].casefold()),
    )[:TOP_N]

    if len(ranked) != TOP_N:
        raise ValueError(f"SSA-Daten enthalten weniger als {TOP_N} Namen für {sex}.")

    return ranked


ssa_archive = download_if_missing(
    SSA_URL, CACHE_DIR / "ssa_baby_names.zip"
)
census_archive = download_if_missing(
    CENSUS_URL, CACHE_DIR / "census_2010_surnames.zip"
)

# Name, SSA-Kategorie und Geburtenzahl je Jahr aufsummieren.
first_name_counts = Counter()

with zipfile.ZipFile(ssa_archive) as archive:
    year_files = sorted(
        member
        for member in archive.namelist()
        if re.fullmatch(r"yob\d{4}\.txt", member)
        and FIRST_YEAR <= int(member[3:7]) <= LAST_YEAR
    )

    if not year_files:
        raise ValueError(
            f"SSA-Archiv enthält keine Jahresdateien für "
            f"{FIRST_YEAR}–{LAST_YEAR}."
        )

    for member in year_files:
        with archive.open(member) as source:
            for name, sex, births in csv.reader(
                io.TextIOWrapper(source, encoding="utf-8")
            ):
                if sex in {"F", "M"}:
                    first_name_counts[(sex, name)] += int(births)


rows = []

for sex, category in (
    ("F", "first_name_female"),
    ("M", "first_name_male"),
):
    for rank, (name, count) in enumerate(
        top_first_names(first_name_counts, sex), start=1
    ):
        rows.append(
            {
                "category": category,
                "name": name.title(),
                "rank": rank,
                "frequency": count,
                "source_period": f"SSA births {FIRST_YEAR}-{LAST_YEAR}",
            }
        )


# Census-Datei einlesen und Rang nach Häufigkeit bilden.
with zipfile.ZipFile(census_archive) as archive:
    with archive.open("Names_2010Census.csv") as source:
        reader = csv.DictReader(
            io.TextIOWrapper(source, encoding="utf-8-sig")
        )
        surname_counts = [
            (row["name"], int(row["count"]))
            for row in reader
        ]

top_surnames = sorted(
    surname_counts,
    key=lambda item: (-item[1], item[0].casefold()),
)[:TOP_N]

if len(top_surnames) != TOP_N:
    raise ValueError(
        f"Census-Daten enthalten weniger als {TOP_N} Nachnamen."
    )

for rank, (name, count) in enumerate(top_surnames, start=1):
    rows.append(
        {
            "category": "surname",
            "name": name.title(),
            "rank": rank,
            "frequency": count,
            "source_period": "US Census 2010",
        }
    )


OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as output:
    writer = csv.DictWriter(
        output,
        fieldnames=[
            "category",
            "name",
            "rank",
            "frequency",
            "source_period",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"{len(rows)} Einträge geschrieben: {OUTPUT_FILE}")