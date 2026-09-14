# Quality Engineering Learning Hub

Knowledge base multilingue per preparare tutte le certificazioni ISTQB correnti e trasformare il syllabus in capacità osservabili sul campo.

[![Docs](https://img.shields.io/badge/web-MkDocs-18221F)](mkdocs.yml)
[![Obsidian](https://img.shields.io/badge/vault-Obsidian-2D6A58)](docs/00-Start-Here.md)
[![Container](https://img.shields.io/badge/runtime-Docker-18221F)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/license-MIT-2D6A58)](LICENSE)

## Cosa trovi

- catalogo verificato di 27 certificazioni attive: Core, Specialist ed Expert;
- link a syllabus, sample exam e regole sulle pagine ISTQB ufficiali;
- tips, domande originali ed esercizi per preparare l'esame;
- un laboratorio professionale per ogni certificazione, con criteri ed evidenze;
- template per test strategy, charter, risk register, defect report e learning log;
- un vault Obsidian e una web app generati dalla stessa sorgente Markdown.

La versione italiana offre una scheda dettagliata per ogni certificazione. Le edizioni inglese, francese, tedesca e spagnola raccolgono il catalogo completo, i percorsi, gli esercizi, i laboratori e gli strumenti essenziali. Sul sito si cambia lingua dal selettore; in Obsidian i file tradotti usano i suffissi `.en.md`, `.fr.md`, `.de.md` e `.es.md`.

Il progetto è indipendente, non affiliato a ISTQB e non è un training provider accreditato. Non contiene domande reali d'esame e non redistribuisce i PDF ufficiali.

## Avvio locale con un doppio clic

Prerequisito: [Docker Desktop](https://www.docker.com/products/docker-desktop/) avviato.

1. Esegui `start-local.bat`.
2. Attendi la build: si apre `http://127.0.0.1:8000`.
3. Esegui `stop-local.bat` per fermare il container.

Equivalente da terminale:

```powershell
docker compose up --build --detach
docker compose down
```

Il servizio gira come utente non privilegiato, espone solo l'interfaccia locale, usa un filesystem read-only e include un health check.

## Uso con Obsidian

1. Apri Obsidian.
2. Scegli **Open folder as vault**.
3. Seleziona la cartella `docs`.
4. Parti da `00-Start-Here.md`.

Il vault usa solo funzionalità core: link Markdown portabili, proprietà YAML, tag, backlink, ricerca e grafo. Le preferenze personali di workspace non vengono versionate.

## Sviluppo senza Docker

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m mkdocs serve
```

Verifica completa:

```powershell
py scripts/security_scan.py
py scripts/validate_docs.py
py -m mkdocs build --strict
docker build --tag istqb-learning-hub:local .
```

## Struttura

| Percorso | Contenuto |
|---|---|
| `docs/certificazioni/` | schede di tutte le certificazioni attive e phase-out |
| `docs/percorsi/` | piani e preparazione per livello |
| `docs/sul-campo/` | laboratori e case study verificabili |
| `docs/toolbox/` | metodo di studio e strumenti |
| `docs/assets/templates/` | template riutilizzabili |
| `docs/guide/` | edizioni consolidate in cinque lingue |
| `docs/.obsidian/` | configurazione portabile del vault |
| `mkdocs.yml` | navigazione e build della web app |

## Pubblicazione

Il workflow GitHub valida link e marker editoriali, esegue la build strict, costruisce il container e pubblica il sito su GitHub Pages a ogni push su `main`. Nel repository GitHub va selezionato **Settings > Pages > Source: GitHub Actions**.

Inizia dal [catalogo delle certificazioni](docs/certificazioni/index.md), dai [laboratori](docs/sul-campo/index.md) o dalle [linee guida per contribuire](CONTRIBUTING.md).
