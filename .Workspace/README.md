Denis Ameti, December 2024, denis.ameti@stud.hslu.ch, https://github.com/LeMagiD
# Inhalte und deren Funktionen

---
## Ordner 
* .envs:
    - die yml files mit den in Anaconda installierten Packages/Libraries
    - verwende nach Intallation von Anaconda (hier miniconda ohne Navigator verwendet) den Befehl `conda create --name my_env --file env.yml`
* data:
    - alle Bilder und Annotationen der Datensätze TUC, ICARUS und [coco](https://cocodataset.org/#download), die für diese Arbeit verwendet wurden.
    - pred_img: zufällige Bilder aus den vorher erwähnten Datensätzen für Testing.
    - roboflow: selbst annotierte Bilder aus dem ICARUS Datensatz, annotiert mit [roboflow](https://roboflow.com/).
    - constellations: Welche Bilder genau für die jeweiligen Projekte P1 bis Pn verwendet wurden (für Reproduzierbarkeit)
* my_libs:
    - Eigene und Ultralytics Bibliotheken, welche in andere Files/Skripts/Programme verwendet werden
* P1_catforg-eval:
    - Das erste Projekt, bei dem getestet wurde, ab wievielen Epochen das catastrophic forgetting eintritt
    - Dazu zugehörig die predictions im Projekt P1-1
* P2_e4train:
    - In diesem Projekt wurde ermittelt, wie sich das ändern der Lernrate auf die Resultate auswirkt
    - Dazu zugehörig die predictions im Projekt P2-1
    - Das Training und die predictions wurden mit den Gewichten best.pt aus den Projekt P1 nach 4 Epochen genommen (etwa der Zeitpunkt vor dem catastrophic forgetting)
* P3_coco_mix(2):
    - Hier wurden alle verfügbaren und annotierten Daten verwendet, um zu sehen, wie sich zusätzliche reale Bilder (aus dem coco Datensatz) ohne Fischaugen-Perspektive auf das Training auswirken, im Vergleich zu Training nur mit synthetischen Bildern aus dem TUC Datensatz und 10 annotierten Bildern aus dem ICARUS Datensatz
    - Die Predictions sind im gleichen Ordner unter predict
* P4_matri4x4:
    - Enthält die Validierungen der Baseline und der Projekte P5 bis P8 im Unterordner ./val
	- 

## Files
Die meisten Files hier nehmen Optionen entgegen, verwende `python <filename>.py -h` für genauere Infos
* coco1k.py:
    - Ein Python Skript, welche die ersten 1000 Bilder aus dem coco Datensatz herunterlädt. Annotierungen sind jedoch alles vorhanden (unter ./data/coco/labels/.all)
* datasplit.py:
    - Das wichtigste Skript hier
    - Erstellt die Training splits, schreibt die constellations, schreibt das data.yaml file in die Projektordner usw. Siehe File selber für genaueres
* import_img.py
    - importiert Bilder (eigentlich allgemein files mit demselben filetype) von einem Ort zu einem anderen
    - Wurde verwendet um alles Datensätze zu zentralisieren
* my_coco.py:
    - konvertiert mithilfe der Library von Ultralytics die Annotationen der coco Bilder aus dem coco Format zum yolo Format
* predict.py 
    - Ist eine Vorlage, für die eigentlichen predict.py in den Projektordner, führe dieses File also NICHT hier aus. Ist auch nicht ganz up to date, verwende besser diejenigen aus den Projekten P3 und neuer
    - Führt ein inference/predict mit dem gewünschten Modell auf die Bilder in ./data/pred_img durch und speichert sie im selben Projektordner under ./predict
* slave.py
    - Eine erste (Teil)Version von datasplit.py welche zu Beginn der Arbeit verwendet wurde
    - Wurde beibehalten um einzelne Funktionen zu kopieren 

* Irrelevante Ordner und Files welche zu Testzwecken existieren
    - ./screenshots
    - ./test
    - path_test.py
    - test.py

