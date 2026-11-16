Spoiler-Erkennung in Filmrezensionen
Gruppe F: Julius Drath, Roshan Raza Khalid, Konrad Krauth, Timon Gartung
Advanced NLP, Continuous Assessment 1, Prof. Dr. Kai Eckert, TH Mannheim


1. Inhalt des Ordners
---------------------

code/
  readme.txt                     diese Datei
  spoiler_erkennung.ipynb        der gesamte Code (Daten, Modelle, Hypothesen, Grafiken)
  build_us_name_list.py          erzeugt data/us_name_lists.csv neu (nur bei Bedarf)
  data/
    IMDB_reviews_example.json        Auszug aus den Rezensionen (3.200 Rezensionen)
    IMDB_movie_details_example.json  Auszug aus den Filmdaten (122 Filme)
    us_name_lists.csv                US-Vor- und Nachnamen für H2 (wird immer gebraucht)
  figures/                       wird beim Ausführen angelegt (Grafiken und CSV-Tabellen)


2. Voraussetzungen
------------------

Getestet mit Python 3.14. Benötigte Pakete:

  numpy
  pandas
  scipy
  scikit-learn
  matplotlib (mindestens 3.6)
  jupyter (oder JupyterLab)
  kagglehub (nur für den automatischen Download des vollen Datensatzes)

Installation:

  pip install numpy pandas scipy scikit-learn matplotlib jupyter kagglehub


3. Ausführen
------------

Das Notebook muss aus dem Ordner code/ gestartet werden, weil die Pfade
data/ und figures/ relativ dazu sind:

  cd code
  jupyter notebook spoiler_erkennung.ipynb

Dann alle Zellen der Reihe nach ausführen (Run All).


4. Beispieldaten oder voller Datensatz
--------------------------------------

Welche Daten genutzt werden, steht in Abschnitt 1 des Notebooks in der
Variable USE_FULL_DATASET.

Beispieldaten (schnell, ca. 2 Minuten):
  USE_FULL_DATASET = False
  Das Notebook liest data/IMDB_reviews_example.json und
  data/IMDB_movie_details_example.json. Mit so wenigen Daten sind die
  Zahlen nicht aussagekräftig. Die Beispieldaten zeigen nur, dass der
  Ablauf funktioniert.

Voller Datensatz (wie in der Dokumentation, ca. 50 Minuten):
  USE_FULL_DATASET = True
  Gebraucht werden data/IMDB_reviews.json (ca. 950 MB) und
  data/IMDB_movie_details.json (ca. 14 MB) aus dem IMDB Spoiler Dataset:
  https://www.kaggle.com/datasets/rmisra/imdb-spoiler-dataset
  Fehlen die Dateien, lädt das Notebook sie mit kagglehub automatisch
  nach data/. Dafür braucht man Internet und eventuell einen Kaggle-Login.
  Alternativ kann man beide Dateien selbst herunterladen und in data/ legen.
  Der volle Datensatz wird komplett in den Arbeitsspeicher geladen.

Die Laufzeit hängt vom Rechner ab. Zellen, die länger dauern, sind im
Notebook mit ⏳ markiert (Modellvergleich ca. 5 Min., Genre ca. 6 Min.,
Einzelfilm ca. 11 Min., H2 ca. 20 Min.).


5. Wichtige Einstellungen (Abschnitt 1 des Notebooks)
-----------------------------------------------------

  USE_FULL_DATASET  True = voller Datensatz, False = Beispieldaten
  SAMPLE_SIZE       Anzahl Rezensionen für die Modelle (Standard 100.000,
                    None = alle, dauert deutlich länger)
  SEED              fester Zufallsstartwert (42), damit die Ergebnisse
                    wiederholbar sind
  N_SEEDS           Anzahl Wiederholungen bei H2 (5)


6. Ergebnisse
-------------

Alle Grafiken der Dokumentation werden als PNG in figures/ gespeichert.
Dazu kommen diese Tabellen als CSV:

  ergebnisse.csv         Modellvergleich (alle sechs Kombinationen)
  detail_metriken.csv    die zwei besten Modelle im Detail
  genre.csv, genre_mittel.csv   Modell pro Genre
  film.csv, film_mittel.csv     Modell pro Film
  h2_figurennamen.csv    H2, F1 mit, ohne und mit ersetzten Namen
  messwerte.csv          Übersicht der wichtigsten Zahlen


7. Namenslisten für H2
----------------------

data/us_name_lists.csv enthält die 1.000 häufigsten US-Vornamen für Frauen
und Männer (Social Security Administration, Geburten 1880 bis 2024) und die
1.000 häufigsten Nachnamen (US Census 2010). Die Datei liegt bereits bei.
Nur wer sie neu erzeugen möchte, startet build_us_name_list.py. Das Skript
lädt die Rohdaten aus dem Internet.
Quellen:
  https://www.ssa.gov/oact/babynames/
  https://www.census.gov/topics/population/genealogy/data/2010_surnames.html
