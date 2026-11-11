Spoiler-Erkennung in Filmrezensionen
Gruppe F: Julius Drath, Roshan Raza Khalid, Konrad Krauth, Timon Gartung
Advanced Natural Language Processing, Continuous Assessment 1


INHALT DIESES ORDNERS

  spoiler_erkennung.ipynb    Jupyter-Notebook mit dem gesamten Code
                             (enthält bereits die Ausgaben aus unserem Lauf
                             mit dem vollen Datensatz)
  requirements.txt           benötigte Python-Pakete
  data/example/              Beispieldaten (ca. 6 MB), siehe unten
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

  Steht die Variable auf True, aber der große Datensatz fehlt, gibt das
  Notebook einen Hinweis aus und nimmt automatisch die Beispieldaten.
  Es läuft also auch ohne weitere Schritte durch.

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
  Für den vollen Lauf die beiden Dateien
    IMDB_reviews.json
    IMDB_movie_details.json
  herunterladen und in den Ordner data/ legen (neben den Ordner example/).
  Das Notebook erkennt sie automatisch.

  Beispieldaten in data/example/ (gleiches Format wie das Original):
    IMDB_reviews_example.json         3.200 Rezensionen
    IMDB_movie_details_example.json   die 122 zugehörigen Filme
  Auswahl mit Zufallsstartwert 42: 120 zufällige Filme mit je 20 zufälligen
  Rezensionen sowie 2 häufig rezensierte Filme mit je 400 Rezensionen
  (damit auch der Einzelfilm-Vergleich in Abschnitt 3.5 läuft).


VERWENDETE VERFAHREN

  Nur klassische Verfahren, keine neuronalen Netze (alles aus scikit-learn):
    Merkmale:  Bag of Words und TF-IDF über Wörter und Wortpaare
               (1- und 2-Gramme)
    Modelle:   Naive Bayes (Complement NB), logistische Regression,
               lineare SVM

  Welches Modell wo verwendet wird:
    Abschnitt 3.2/3.3 (Modellvergleich)   alle sechs Kombinationen
    Abschnitt 3.4, 3.5, 4, 5, 6           logistische Regression auf TF-IDF
