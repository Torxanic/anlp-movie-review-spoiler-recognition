Spoiler-Erkennung in Filmrezensionen
Gruppe F: Julius Drath, Roshan Raza Khalid, Konrad Krauth, Timon Gartung
Advanced Natural Language Processing, Continuous Assessment 1


INHALT DIESES ORDNERS

  spoiler_erkennung.ipynb    Jupyter-Notebook mit dem gesamten Code
                             (enthält bereits die Ausgaben aus unserem Lauf
                             mit dem vollen Datensatz)
  build_us_name_list.py     Skript zur Reproduktion der Namenslisten
  requirements.txt           benötigte Python-Pakete
  data/example/              Beispieldaten (ca. 6 MB), siehe unten
  data/us_name_lists.csv     kompakte Namenslisten für die Figurenheuristik
  figures/                   Abbildungen (300 dpi) und Ergebnistabellen (CSV)
                             aus unserem Lauf mit dem vollen Datensatz


VORAUSSETZUNGEN

  Python 3.10 oder neuer und Jupyter Lab (oder Jupyter Notebook).

  Getestet mit:
    Python        3.13
    numpy         2.5.3
    pandas        3.0.5
    scipy         1.18.1
    scikit-learn  1.9.1
    matplotlib    3.11.2
    jinja2        3.1.6   (für die farbige Ergebnistabelle)

  Installation:
    pip install -r requirements.txt
    pip install jupyterlab


AUSFÜHREN

  1. In diesen Ordner (code/) wechseln.
  2. "jupyter lab" starten und spoiler_erkennung.ipynb öffnen.
  3. "Run > Run All Cells" wählen.

  Welche Daten verwendet werden, legt eine Variable in der zweiten
  Code-Zelle des Notebooks fest:

    USE_FULL_DATASET = True    ganzer Datensatz aus data/
    USE_FULL_DATASET = False   Beispieldaten aus data/example/

  Steht die Variable auf True, lädt das Notebook fehlende Dateien
  IMDB_reviews.json und/oder IMDB_movie_details.json automatisch mit
  KaggleHub nach data/ herunter. Dafür werden Internetzugriff und
  gegebenenfalls eine Kaggle-Anmeldung benötigt. Bei einem Downloadfehler
  wird eine Fehlermeldung angezeigt; es wird nicht still auf Beispieldaten
  gewechselt.

  Mit den Beispieldaten dauert ein Durchlauf etwa 2 Minuten. Die Zahlen
  sind dann nur eine Demonstration des Vorgehens.

  Für die Ergebnisse aus unserer Dokumentation wird der volle Datensatz
  benötigt (siehe unten). Dann dauert ein Durchlauf etwa 40 Minuten und
  braucht etwa 4 GB Arbeitsspeicher. Zellen mit längerer Laufzeit sind im
  Notebook mit einer Sanduhr markiert.

  Mit SAMPLE_SIZE (gleiche Zelle) lässt sich einstellen, wie viele
  Rezensionen für die Modelle gezogen werden (Standard: 100.000,
  None = alle).

  Alle Zufallsentscheidungen verwenden den festen Startwert 42. Die
  Abbildungen und Tabellen werden beim Ausführen in figures/ neu erzeugt,
  jede Abbildung als eigene PNG-Datei mit 300 dpi.


DATEN

  Originaldaten: IMDB Spoiler Dataset (Rishabh Misra)
    https://www.kaggle.com/datasets/rmisra/imdb-spoiler-dataset

  Der Datensatz ist etwa 970 MB groß und liegt deshalb nicht bei.
  Bei USE_FULL_DATASET = True lädt das Notebook fehlende Dateien automatisch
  über KaggleHub aus dem Datensatz
    rmisra/imdb-spoiler-dataset
  nach data/ herunter. Es wird jeweils nur eine Datei geladen, wenn sie
  fehlt; vorhandene Dateien bleiben unberührt. Alternativ können die beiden Dateien
    IMDB_reviews.json
    IMDB_movie_details.json
  manuell in den Ordner data/ gelegt werden.

  Beispieldaten in data/example/ (gleiches Format wie das Original):
    IMDB_reviews_example.json         3.200 Rezensionen
    IMDB_movie_details_example.json   die 122 zugehörigen Filme
  Auswahl mit Zufallsstartwert 42: 120 zufällige Filme mit je 20 zufälligen
  Rezensionen sowie 2 häufig rezensierte Filme mit je 400 Rezensionen
  (damit auch der Einzelfilm-Vergleich in Abschnitt 3.5 läuft).

NAMENSLISTEN REPRODUZIEREN

  Die Datei data/us_name_lists.csv enthält je 1.000 Vornamen aus den
  SSA-Kategorien F und M sowie die 1.000 häufigsten Nachnamen aus dem
  US Census 2010. Die Vornamen-Häufigkeiten sind für die Jahre 1880–2024
  je Name und Kategorie aufsummiert. Bei Gleichständen entscheidet die
  alphabetische Reihenfolge; dadurch ist die Auswahl reproduzierbar.

  Zum Neuerstellen in einer PowerShell im Ordner code/ ausführen:

    python build_us_name_list.py

  Das Skript benötigt keine zusätzlichen Python-Pakete, aber Internetzugriff.
  Es lädt bei Bedarf die öffentlichen Quelldateien herunter und speichert
  sie außerhalb des Abgabeordners im Cache:

    %LOCALAPPDATA%\movie-review-spoiler-recognition\name_sources\

  Verwendete Quellen:
    SSA Baby Names
      https://www.ssa.gov/oact/babynames/
    US Census 2010 Surnames
      https://www.census.gov/topics/population/genealogy/data/2010_surnames.html

  Ein API-Key ist nicht erforderlich. Die fertige CSV ist etwa 150 KB groß.
  Falls die Downloads fehlschlagen, können die Archive manuell von den Quellen
  geladen und mit den Dateinamen ssa_baby_names.zip und census_2010_surnames.zip
  in %LOCALAPPDATA%\movie-review-spoiler-recognition\name_sources\ abgelegt
  werden. Unter Windows ist %LOCALAPPDATA% normalerweise
  C:\Users\<Benutzername>\AppData\Local.

VERWENDETE VERFAHREN

  Nur klassische Verfahren, keine neuronalen Netze (alles aus scikit-learn):
    Merkmale:  Bag of Words und TF-IDF über Wörter und Wortpaare
               (1- und 2-Gramme)
    Modelle:   Naive Bayes (Complement NB), logistische Regression,
               lineare SVM

  Welches Modell wo verwendet wird:
    Abschnitt 3.2/3.3 (Modellvergleich)   alle sechs Kombinationen
    Abschnitt 3.4, 3.5, 4, 5, 6           logistische Regression auf TF-IDF
