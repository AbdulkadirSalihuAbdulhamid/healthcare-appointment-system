Thesis figure assets for LaTeX / Word.

UCD diagram (Chapter 2):
  ucd-principles.png  OR  ucd-principles.pdf

Use case diagram (Chapter 4.4):
  docbook_use_case.png
  Regenerate: generate_use_case.ps1

Cloud architecture (Chapter 4, Figure 1):
  docbook_architecture.png
  Source: ../secure-cloud-based-healthcare-appointment-system/docbook_architecture.dot
  Regenerate: generate_architecture.ps1

ER diagram (Chapter 4.1, Figure 4):
  Copy from project root after running:
    python manage.py graph_models accounts bookings core -g -o docbook_erd.png
  Save here as: docbook_erd.png

Generate ER diagram (from inner project folder):
  1. Install Graphviz: https://graphviz.org/download/  (dot must be on PATH)
  2. pip install django-extensions pydot
  3. python manage.py graph_models accounts bookings core -g -o docbook_erd.png

LaTeX uses \includegraphics without extension when both .png and .pdf exist.
