# Quality Engineering Learning Hub

Repository italiana per preparare le certificazioni ISTQB e trasformare il syllabus in capacita osservabili sul campo.

[![Docs](https://img.shields.io/badge/docs-MkDocs-526CFE)](mkdocs.yml)
[![Quality gate](https://img.shields.io/badge/quality-build%20strict-0B7A53)](scripts/validate_docs.py)
[![License: MIT](https://img.shields.io/badge/license-MIT-1F2937)](LICENSE)

## Cosa offre

- percorsi guidati per Foundation, Advanced, Agile/Specialist ed Expert;
- link versionati a syllabus, glossary, sample exam e regole ufficiali;
- piani di studio, tecniche di memorizzazione e strategie d'esame;
- domande originali ed esercizi con criteri di autovalutazione;
- laboratori realistici e template pronti per progetto;
- un modello trasparente per pubblicare case study e mostrare affidabilita;
- uno spazio di contribuzione per colleghi esperti e persone in crescita.

Il progetto e indipendente e non affiliato a ISTQB. ISTQB e i relativi marchi appartengono ai rispettivi titolari. I materiali ufficiali non vengono redistribuiti: sono collegati dalle pagine dell'ente.

## Avvio rapido

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m mkdocs serve
```

Aprire `http://127.0.0.1:8000`. Per la verifica completa:

```powershell
py scripts/validate_docs.py
py -m mkdocs build --strict
```

## Da dove iniziare

- [Portale](docs/index.md)
- [Scegli il percorso](docs/percorsi/index.md)
- [Catalogo delle fonti ufficiali](docs/fonti-ufficiali.md)
- [Laboratori sul campo](docs/sul-campo/index.md)
- [Come contribuire](CONTRIBUTING.md)

## Pubblicazione

Il workflow incluso costruisce il sito e pubblica l'artefatto su GitHub Pages a ogni push su `main`. Nel repository GitHub selezionare **Settings > Pages > Source: GitHub Actions**.

