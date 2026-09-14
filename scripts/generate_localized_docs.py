"""Generate the compact multilingual ISTQB editions from reviewed source copy."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GUIDE = DOCS / "guide"
VERIFIED = "2026-09-14"

CERTIFICATIONS = (
    ("core", "CTFL v4.0", "Foundation Level", "https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/"),
    ("core", "CTAL-AT v2.0", "Agile Tester", "https://istqb.org/certifications/certified-tester-advanced-level-agile-tester-ctal-at/"),
    ("core", "CTAL-TA v4.0", "Test Analyst", "https://istqb.org/certifications/certified-tester-advanced-level-test-analyst/"),
    ("core", "CTAL-TAE v2.0", "Test Automation Engineering", "https://istqb.org/certifications/certified-tester-advanced-level-test-automation-engineering-ctal-tae-v2-0/"),
    ("core", "CTAL-TM v3.0", "Test Management", "https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/"),
    ("core", "CTAL-TTA", "Technical Test Analyst", "https://istqb.org/certifications/certified-tester-advanced-level-technical-test-analyst-ctal-tta/"),
    ("technology", "CT-AI v2.0", "AI Testing", "https://istqb.org/certifications/certified-tester-ai-testing-ct-ai/"),
    ("technology", "CT-QDO", "Quality in DevOps", "https://istqb.org/certifications/certified-tester-quality-in-devops-ct-qdo/"),
    ("technology", "CT-GenAI", "Testing with Generative AI", "https://istqb.org/certifications/gen-ai/"),
    ("technology", "CT-MAT", "Mobile Application Testing", "https://istqb.org/certifications/certified-tester-mobile-application-testing-ct-mat/"),
    ("technology", "CT-MBT", "Model-Based Testing", "https://istqb.org/certifications/certified-tester-model-based-tester-ct-mbt/"),
    ("technology", "CT-TAS", "Test Automation Strategy", "https://istqb.org/certifications/certified-tester-test-automation-strategy-ct-tas/"),
    ("technology", "CT-ATLaS", "Agile Test Leadership at Scale", "https://istqb.org/certifications/certified-tester-agile-test-leadership-at-scale-ct-atlas/"),
    ("quality", "CT-AcT", "Acceptance Testing", "https://istqb.org/certifications/certified-tester-acceptance-testing/"),
    ("quality", "CT-PT", "Performance Testing", "https://istqb.org/certifications/certified-tester-performance-testing-ct-pt/"),
    ("quality", "CT-SEC", "Security Tester", "https://istqb.org/certifications/certified-tester-security-tester-ct-sec/"),
    ("quality", "CT-STE", "Security Test Engineer", "https://istqb.org/certifications/certified-tester-security-test-engineer/"),
    ("quality", "CT-UT", "Usability Testing", "https://istqb.org/certifications/certified-tester-usability-testing-ct-ut/"),
    ("domain", "CT-FT", "Finance Testing", "https://istqb.org/certifications/certified-tester-finance-testing-ct-ft/"),
    ("domain", "CT-AuT", "Automotive Software Tester", "https://istqb.org/certifications/certified-tester-automotive-software-tester-ct-aut/"),
    ("domain", "CT-GaMe", "Game Testing", "https://istqb.org/certifications/certified-tester-game-testing-ct-game/"),
    ("domain", "CT-GT", "Gambling Industry Tester", "https://istqb.org/certifications/certified-tester-gambling-industry-tester-ct-gt/"),
    ("expert", "CTEL-ITP-ATP", "Assessing Test Processes", "https://istqb.org/certifications/certified-tester-expert-level-assessing-test-processes-ctel-itp-atp/"),
    ("expert", "CTEL-ITP-ITPI", "Implementing Test Process Improvement", "https://istqb.org/certifications/certified-tester-expert-level-implementing-test-process-improvement-ctel-itp-itpi/"),
    ("expert", "CTEL-TM-SM", "Strategic Test Management", "https://istqb.org/certifications/certified-tester-expert-level-test-management-strategic-test-management-ctel-tm-sm/"),
    ("expert", "CTEL-TM-OTM", "Operational Test Management", "https://istqb.org/certifications/certified-tester-expert-level-test-management-operational-test-management-ctel-tm-otm/"),
    ("expert", "CTEL-TM-MTT", "Managing the Test Team", "https://istqb.org/certifications/certified-tester-expert-level-test-management-managing-the-test-team-ctel-tm-mtt/"),
)

GROUPS = {
    "it": {"core": "Core", "technology": "Tecnologie e approcci", "quality": "Caratteristiche di qualità e livelli", "domain": "Domini", "expert": "Expert"},
    "en": {"core": "Core", "technology": "Technologies and approaches", "quality": "Quality characteristics and test levels", "domain": "Domains", "expert": "Expert"},
    "fr": {"core": "Core", "technology": "Technologies et approches", "quality": "Caractéristiques qualité et niveaux de test", "domain": "Domaines", "expert": "Expert"},
    "de": {"core": "Core", "technology": "Technologien und Ansätze", "quality": "Qualitätsmerkmale und Teststufen", "domain": "Domänen", "expert": "Expert"},
    "es": {"core": "Core", "technology": "Tecnologías y enfoques", "quality": "Características de calidad y niveles de prueba", "domain": "Dominios", "expert": "Expert"},
}

COPY = {
    "it": {
        "catalog_title": "Catalogo ISTQB verificato",
        "catalog_intro": "Il catalogo internazionale comprende **27 certificazioni attive** alla data indicata. I nomi ufficiali restano in inglese per evitare ambiguità. Apri sempre la pagina ufficiale prima di acquistare un esame.",
        "status_title": "Percorsi in phase-out",
        "status": "CTFL Agile Tester (CTFL-AT) e Agile Technical Tester (CT-ATT) sono in sunset: gli esami inglesi terminano il 6 maggio 2027 e quelli non inglesi il 6 novembre 2027. CTAL-AT v2.0 è il percorso agile corrente. Anche le vecchie versioni CTAL-TA, CTAL-TM, CT-TAE e CT-AI sono in transizione o ritirate.",
        "study": dedent("""
            # Percorsi di studio, tips ed esercizi

            ## Scegli il livello

            | Obiettivo | Percorso | Evidenza pratica |
            |---|---|---|
            | Linguaggio e tecniche comuni | CTFL | test design e defect report |
            | Specializzazione operativa | Advanced o Specialist | strategia o laboratorio di dominio |
            | Leadership e miglioramento | Expert | assessment, roadmap e metriche |

            ## Ciclo di preparazione in sei settimane

            1. Mappa learning objective, termini e peso dei capitoli.
            2. Studia un capitolo alla volta e crea esempi tuoi.
            3. Trasforma ogni tecnica in un artefatto verificabile.
            4. Rispondi a domande a tempo e annota il motivo degli errori.
            5. Esegui un sample exam ufficiale nelle condizioni reali.
            6. Ripassa solo i gap misurati e completa il portfolio.

            ## Tips e trick

            - Distingui definizioni, applicazione e analisi usando i livelli K.
            - Elimina le risposte incompatibili con il contesto prima di scegliere.
            - Crea una scheda per ogni tecnica: quando usarla, input, output e limite.
            - Alterna richiamo attivo, esercizi e revisione dilazionata.
            - Non memorizzare domande: spiega perché le alternative sono errate.

            ## Domande originali

            1. Quale evidenza dimostra che una tecnica è stata applicata correttamente?
            2. Come cambia la priorità quando impatto e probabilità divergono?
            3. Quando una metrica di copertura può dare falsa sicurezza?
            4. Quale informazione rende un defect report riproducibile?
            5. Come distingui monitoraggio, controllo e completamento del test?
            6. Quale rischio introduce l'automazione non manutenibile?

            ## Esercizi

            - Deriva partizioni, valori limite e una decision table da una regola di checkout.
            - Costruisci un risk register e giustifica l'ordine dei test.
            - Conduci una review di una user story e registra i difetti statici.
            - Disegna una strategia di regressione con criteri di selezione misurabili.
            - Simula una retrospettiva e collega ogni azione a un indicatore.
        """),
        "practice": dedent("""
            # Dall'esame al lavoro sul campo

            Ogni laboratorio produce evidenze utilizzabili in portfolio. Anonimizza sempre persone, clienti, sistemi e dati.

            | Laboratorio | Scenario | Consegna | Criteri | Evidenza |
            |---|---|---|---|---|
            | Test design | checkout con sconti e pagamenti | partizioni, limiti, decision table | tracciabilità e copertura | test set revisionato |
            | Risk-based testing | rilascio con tempo limitato | risk register e ordine di esecuzione | impatto, probabilità, mitigazioni | decision log |
            | Automazione | suite di regressione instabile | strategia e proof of concept | valore, manutenibilità, feedback | trend prima/dopo |
            | DevOps quality | pipeline con feedback tardivo | quality gates e osservabilità | tempi, ownership, falsi positivi | dashboard minima |
            | Test management | programma multi-team | test strategy e reporting | obiettivi, stakeholder, metriche | review firmata |
            | Process improvement | processo con difetti ricorrenti | assessment e roadmap | baseline, priorità, outcome | retrospettiva misurata |

            ## Definition of done del laboratorio

            - decisioni collegate a rischi e requisiti;
            - dati riproducibili e nessun dato sensibile;
            - criteri di qualità espliciti;
            - limiti e assunzioni dichiarati;
            - feedback di un pari e azione di miglioramento.
        """),
        "toolbox": dedent("""
            # Toolbox di apprendimento e lavoro

            ## Metodo

            - **Syllabus map:** learning objective, livello K, esempio e dubbio aperto.
            - **Learning log:** data, attività, risultato, errore e prossima azione.
            - **Spaced review:** ripasso dopo 1, 3, 7, 14 e 30 giorni.
            - **Teach-back:** spiega il concetto senza note in meno di tre minuti.
            - **Evidence review:** fai revisionare un artefatto, non solo la risposta.

            ## Strumenti consigliati

            Usa Obsidian per backlink e note atomiche, un foglio di calcolo per score e gap, Git per versionare gli artefatti, un issue tracker per difetti ed evidenze, e gli strumenti di test già approvati dal tuo contesto aziendale. Non caricare dati riservati su servizi esterni.

            ## Template inclusi

            - [Test charter](../assets/templates/test-charter.md)
            - [Defect report](../assets/templates/defect-report.md)
            - [Risk register](../assets/templates/risk-register.md)
            - [Test strategy](../assets/templates/test-strategy.md)
            - [Learning log](../assets/templates/learning-log.md)
        """),
        "sources": dedent("""
            # Fonti ufficiali e controllo versione

            Usa il [catalogo ISTQB](https://istqb.org/certifications/) come fonte primaria e il [glossario ISTQB](https://glossary.istqb.org/) per i termini. Syllabus, sample exam, risposte e regole devono essere scaricati dalla pagina ufficiale della certificazione.

            ## Checklist prima dell'esame

            1. Conferma versione del syllabus, prerequisiti e lingua.
            2. Verifica struttura, durata e punteggio con l'exam provider.
            3. Controlla eventuali sunset date.
            4. Usa solo sample exam ufficiali o domande originali dichiarate.
            5. Non redistribuire PDF o domande d'esame riservate.
        """),
    },
    "en": {
        "catalog_title": "Verified ISTQB certification catalogue",
        "catalog_intro": "The international catalogue contains **27 active certifications** on the stated date. Official titles remain in English. Always open the official page before purchasing an exam.",
        "status_title": "Paths being phased out",
        "status": "Foundation Level Agile Tester (CTFL-AT) and Agile Technical Tester (CT-ATT) are in sunset: English exams end on 6 May 2027 and non-English exams on 6 November 2027. CTAL-AT v2.0 is the current Agile path. Older CTAL-TA, CTAL-TM, CT-TAE and CT-AI versions are also transitioning or retired.",
        "study": dedent("""
            # Study paths, tips and exercises

            ## Choose the level

            | Goal | Path | Practical evidence |
            |---|---|---|
            | Shared language and techniques | CTFL | test design and defect report |
            | Operational specialisation | Advanced or Specialist | strategy or domain lab |
            | Leadership and improvement | Expert | assessment, roadmap and metrics |

            ## Six-week preparation cycle

            1. Map learning objectives, terms and chapter weight.
            2. Study one chapter at a time and create your own examples.
            3. Turn every technique into a reviewable artefact.
            4. Answer timed questions and record why errors occurred.
            5. Run an official sample exam under realistic conditions.
            6. Review measured gaps only and complete the portfolio.

            ## Tips and tricks

            - Separate recall, application and analysis through the K-levels.
            - Remove answers that conflict with the scenario before choosing.
            - Give each technique a card: use, input, output and limitation.
            - Alternate active recall, practice and spaced review.
            - Do not memorise questions; explain why alternatives are wrong.

            ## Original practice questions

            1. What evidence proves that a technique was applied correctly?
            2. How does priority change when impact and likelihood diverge?
            3. When can a coverage metric create false confidence?
            4. Which information makes a defect report reproducible?
            5. How do monitoring, control and test completion differ?
            6. Which risk is introduced by unmaintainable automation?

            ## Exercises

            - Derive partitions, boundaries and a decision table from checkout rules.
            - Build a risk register and justify the execution order.
            - Review a user story and record static defects.
            - Design a regression strategy with measurable selection criteria.
            - Run a retrospective and connect every action to an indicator.
        """),
        "practice": dedent("""
            # From the exam to professional practice

            Every lab produces portfolio-ready evidence. Always anonymise people, clients, systems and data.

            | Lab | Scenario | Deliverable | Quality criteria | Evidence |
            |---|---|---|---|---|
            | Test design | checkout with discounts and payments | partitions, boundaries, decision table | traceability and coverage | reviewed test set |
            | Risk-based testing | time-constrained release | risk register and execution order | impact, likelihood, mitigations | decision log |
            | Automation | unstable regression suite | strategy and proof of concept | value, maintainability, feedback | before/after trend |
            | DevOps quality | pipeline with late feedback | quality gates and observability | speed, ownership, false positives | minimal dashboard |
            | Test management | multi-team programme | test strategy and reporting | goals, stakeholders, metrics | signed review |
            | Process improvement | recurring defects | assessment and roadmap | baseline, priorities, outcomes | measured retrospective |

            ## Lab definition of done

            - decisions trace to risks and requirements;
            - reproducible data with no sensitive information;
            - explicit quality criteria;
            - stated limitations and assumptions;
            - peer feedback and one improvement action.
        """),
        "toolbox": dedent("""
            # Learning and field toolbox

            ## Method

            - **Syllabus map:** learning objective, K-level, example and open question.
            - **Learning log:** date, activity, result, error and next action.
            - **Spaced review:** revisit after 1, 3, 7, 14 and 30 days.
            - **Teach-back:** explain the concept without notes in under three minutes.
            - **Evidence review:** ask a peer to review an artefact, not only an answer.

            ## Recommended tools

            Use Obsidian for backlinks and atomic notes, a spreadsheet for scores and gaps, Git for versioning artefacts, an issue tracker for defects and evidence, and testing tools approved in your organisation. Never upload confidential data to external services.

            ## Included templates

            - [Test charter](../assets/templates/test-charter.md)
            - [Defect report](../assets/templates/defect-report.md)
            - [Risk register](../assets/templates/risk-register.md)
            - [Test strategy](../assets/templates/test-strategy.md)
            - [Learning log](../assets/templates/learning-log.md)
        """),
        "sources": dedent("""
            # Official sources and version control

            Use the [ISTQB catalogue](https://istqb.org/certifications/) as the primary source and the [ISTQB glossary](https://glossary.istqb.org/) for terminology. Download syllabi, sample exams, answers and rules from each certification's official page.

            ## Checklist before the exam

            1. Confirm syllabus version, prerequisites and language.
            2. Verify structure, duration and score with the exam provider.
            3. Check any sunset dates.
            4. Use official sample exams or clearly labelled original questions only.
            5. Do not redistribute PDFs or confidential exam questions.
        """),
    },
}


COPY["fr"] = {
    "catalog_title": "Catalogue vérifié des certifications ISTQB",
    "catalog_intro": "Le catalogue international comprend **27 certifications actives** à la date indiquée. Les intitulés officiels restent en anglais. Consultez toujours la page officielle avant d'acheter un examen.",
    "status_title": "Parcours en retrait progressif",
    "status": "Foundation Level Agile Tester (CTFL-AT) et Agile Technical Tester (CT-ATT) sont en phase de retrait : les examens en anglais se terminent le 6 mai 2027 et les autres langues le 6 novembre 2027. CTAL-AT v2.0 est le parcours Agile actuel. Les anciennes versions CTAL-TA, CTAL-TM, CT-TAE et CT-AI sont également en transition ou retirées.",
    "study": dedent("""
        # Parcours d'étude, conseils et exercices

        ## Choisir le niveau

        | Objectif | Parcours | Preuve pratique |
        |---|---|---|
        | Langage commun et techniques | CTFL | conception de tests et rapport d'anomalie |
        | Spécialisation opérationnelle | Advanced ou Specialist | stratégie ou laboratoire métier |
        | Leadership et amélioration | Expert | évaluation, feuille de route et métriques |

        ## Cycle de préparation en six semaines

        1. Cartographier les objectifs d'apprentissage, les termes et le poids des chapitres.
        2. Étudier un chapitre à la fois et créer ses propres exemples.
        3. Transformer chaque technique en livrable révisable.
        4. Répondre à des questions chronométrées et noter la cause des erreurs.
        5. Réaliser un examen blanc officiel dans des conditions réalistes.
        6. Revoir uniquement les lacunes mesurées et terminer le portfolio.

        ## Conseils pratiques

        - Distinguer mémorisation, application et analyse à l'aide des niveaux K.
        - Éliminer d'abord les réponses incompatibles avec le scénario.
        - Créer une fiche par technique : usage, entrée, sortie et limite.
        - Alterner rappel actif, pratique et révision espacée.
        - Ne pas mémoriser les questions : expliquer pourquoi les autres réponses sont fausses.

        ## Questions originales d'entraînement

        1. Quelle preuve montre qu'une technique a été correctement appliquée ?
        2. Comment la priorité change-t-elle lorsque l'impact et la probabilité divergent ?
        3. Quand une métrique de couverture peut-elle donner une fausse confiance ?
        4. Quelles informations rendent un rapport d'anomalie reproductible ?
        5. En quoi le suivi, le contrôle et la clôture des tests diffèrent-ils ?
        6. Quel risque une automatisation difficile à maintenir introduit-elle ?

        ## Exercices

        - Déduire les partitions, les valeurs limites et une table de décision de règles de paiement.
        - Construire un registre des risques et justifier l'ordre d'exécution.
        - Réviser une user story et consigner les défauts statiques.
        - Concevoir une stratégie de régression avec des critères de sélection mesurables.
        - Mener une rétrospective et relier chaque action à un indicateur.
    """),
    "practice": dedent("""
        # De l'examen à la pratique professionnelle

        Chaque laboratoire produit une preuve utilisable dans un portfolio. Anonymisez toujours les personnes, clients, systèmes et données.

        | Laboratoire | Scénario | Livrable | Critères de qualité | Preuve |
        |---|---|---|---|---|
        | Conception de tests | paiement avec remises et moyens multiples | partitions, limites, table de décision | traçabilité et couverture | jeu de tests révisé |
        | Tests fondés sur les risques | livraison sous contrainte de temps | registre des risques et ordre d'exécution | impact, probabilité, mesures | journal des décisions |
        | Automatisation | suite de régression instable | stratégie et preuve de concept | valeur, maintenabilité, feedback | tendance avant/après |
        | Qualité DevOps | pipeline au retour tardif | quality gates et observabilité | rapidité, responsabilité, faux positifs | tableau de bord minimal |
        | Gestion des tests | programme multi-équipes | stratégie de test et reporting | objectifs, parties prenantes, métriques | revue approuvée |
        | Amélioration du processus | défauts récurrents | évaluation et feuille de route | référence, priorités, résultats | rétrospective mesurée |

        ## Critères de fin du laboratoire

        - décisions reliées aux risques et aux exigences ;
        - données reproductibles sans information sensible ;
        - critères de qualité explicites ;
        - limites et hypothèses déclarées ;
        - retour d'un pair et une action d'amélioration.
    """),
    "toolbox": dedent("""
        # Boîte à outils pour apprendre et pratiquer

        ## Méthode

        - **Carte du syllabus :** objectif d'apprentissage, niveau K, exemple et question ouverte.
        - **Journal d'apprentissage :** date, activité, résultat, erreur et prochaine action.
        - **Révision espacée :** revoir après 1, 3, 7, 14 et 30 jours.
        - **Restitution :** expliquer le concept sans notes en moins de trois minutes.
        - **Revue des preuves :** faire réviser un livrable, pas seulement une réponse.

        ## Outils recommandés

        Utilisez Obsidian pour les liens et les notes atomiques, un tableur pour les scores et les lacunes, Git pour versionner les livrables, un outil de suivi pour les anomalies et les preuves, ainsi que les outils de test approuvés par votre organisation. Ne chargez jamais de données confidentielles sur des services externes.

        ## Modèles inclus

        - [Charte de test](../assets/templates/test-charter.md)
        - [Rapport d'anomalie](../assets/templates/defect-report.md)
        - [Registre des risques](../assets/templates/risk-register.md)
        - [Stratégie de test](../assets/templates/test-strategy.md)
        - [Journal d'apprentissage](../assets/templates/learning-log.md)
    """),
    "sources": dedent("""
        # Sources officielles et contrôle des versions

        Utilisez le [catalogue ISTQB](https://istqb.org/certifications/) comme source principale et le [glossaire ISTQB](https://glossary.istqb.org/) pour la terminologie. Téléchargez syllabus, examens blancs, réponses et règles depuis la page officielle de chaque certification.

        ## Checklist avant l'examen

        1. Confirmer la version du syllabus, les prérequis et la langue.
        2. Vérifier la structure, la durée et le score auprès du fournisseur d'examen.
        3. Contrôler les éventuelles dates de retrait.
        4. Utiliser uniquement les examens blancs officiels ou des questions originales clairement signalées.
        5. Ne pas redistribuer de PDF ni de questions d'examen confidentielles.
    """),
}

COPY["de"] = {
    "catalog_title": "Geprüfter ISTQB-Zertifizierungskatalog",
    "catalog_intro": "Der internationale Katalog umfasst zum angegebenen Datum **27 aktive Zertifizierungen**. Die offiziellen Titel bleiben auf Englisch. Prüfe vor dem Kauf einer Prüfung immer die offizielle Seite.",
    "status_title": "Auslaufende Pfade",
    "status": "Foundation Level Agile Tester (CTFL-AT) und Agile Technical Tester (CT-ATT) laufen aus: englische Prüfungen enden am 6. Mai 2027, nicht-englische am 6. November 2027. CTAL-AT v2.0 ist der aktuelle Agile-Pfad. Ältere Versionen von CTAL-TA, CTAL-TM, CT-TAE und CT-AI befinden sich ebenfalls im Übergang oder sind eingestellt.",
    "study": dedent("""
        # Lernpfade, Tipps und Übungen

        ## Niveau auswählen

        | Ziel | Pfad | Praktischer Nachweis |
        |---|---|---|
        | Gemeinsame Sprache und Techniken | CTFL | Testentwurf und Fehlerbericht |
        | Operative Spezialisierung | Advanced oder Specialist | Strategie oder Domänenlabor |
        | Führung und Verbesserung | Expert | Bewertung, Roadmap und Metriken |

        ## Sechswöchiger Vorbereitungszyklus

        1. Lernziele, Begriffe und Kapitelgewichtung abbilden.
        2. Jeweils ein Kapitel bearbeiten und eigene Beispiele erstellen.
        3. Jede Technik in ein prüfbares Arbeitsergebnis überführen.
        4. Fragen unter Zeitvorgabe beantworten und Fehlerursachen notieren.
        5. Eine offizielle Musterprüfung unter realistischen Bedingungen durchführen.
        6. Nur gemessene Lücken nacharbeiten und das Portfolio abschließen.

        ## Tipps und Tricks

        - Erinnern, Anwenden und Analysieren anhand der K-Stufen trennen.
        - Antworten ausschließen, die dem Szenario widersprechen.
        - Für jede Technik eine Karte anlegen: Zweck, Eingabe, Ausgabe und Grenze.
        - Aktives Abrufen, Üben und verteiltes Wiederholen abwechseln.
        - Fragen nicht auswendig lernen; erklären, warum Alternativen falsch sind.

        ## Eigene Übungsfragen

        1. Welcher Nachweis zeigt, dass eine Technik korrekt angewendet wurde?
        2. Wie ändert sich die Priorität, wenn Auswirkung und Eintrittswahrscheinlichkeit auseinanderliegen?
        3. Wann kann eine Überdeckungsmetrik falsche Sicherheit erzeugen?
        4. Welche Angaben machen einen Fehlerbericht reproduzierbar?
        5. Wie unterscheiden sich Überwachung, Steuerung und Testabschluss?
        6. Welches Risiko entsteht durch schlecht wartbare Automatisierung?

        ## Übungen

        - Äquivalenzklassen, Grenzwerte und eine Entscheidungstabelle aus Checkout-Regeln ableiten.
        - Ein Risikoregister erstellen und die Ausführungsreihenfolge begründen.
        - Eine User Story prüfen und statische Fehler dokumentieren.
        - Eine Regressionsteststrategie mit messbaren Auswahlkriterien entwerfen.
        - Eine Retrospektive durchführen und jede Maßnahme mit einem Indikator verbinden.
    """),
    "practice": dedent("""
        # Von der Prüfung in die Praxis

        Jedes Labor erzeugt einen portfoliofähigen Nachweis. Personen, Kunden, Systeme und Daten müssen immer anonymisiert werden.

        | Labor | Szenario | Ergebnis | Qualitätskriterien | Nachweis |
        |---|---|---|---|---|
        | Testentwurf | Checkout mit Rabatten und Zahlungen | Klassen, Grenzen, Entscheidungstabelle | Rückverfolgbarkeit und Überdeckung | geprüfter Testsatz |
        | Risikobasiertes Testen | Release unter Zeitdruck | Risikoregister und Ausführungsreihenfolge | Auswirkung, Wahrscheinlichkeit, Maßnahmen | Entscheidungsprotokoll |
        | Automatisierung | instabile Regressionstests | Strategie und Proof of Concept | Nutzen, Wartbarkeit, Feedback | Vorher-nachher-Trend |
        | DevOps-Qualität | Pipeline mit spätem Feedback | Quality Gates und Beobachtbarkeit | Geschwindigkeit, Verantwortung, Fehlalarme | minimales Dashboard |
        | Testmanagement | Programm mit mehreren Teams | Teststrategie und Berichtswesen | Ziele, Stakeholder, Metriken | freigegebene Prüfung |
        | Prozessverbesserung | wiederkehrende Fehler | Bewertung und Roadmap | Ausgangslage, Prioritäten, Ergebnisse | gemessene Retrospektive |

        ## Definition of Done für das Labor

        - Entscheidungen sind auf Risiken und Anforderungen zurückführbar;
        - reproduzierbare Daten enthalten keine sensiblen Informationen;
        - Qualitätskriterien sind ausdrücklich benannt;
        - Grenzen und Annahmen sind dokumentiert;
        - Peer-Feedback und eine Verbesserungsmaßnahme liegen vor.
    """),
    "toolbox": dedent("""
        # Werkzeugkasten für Lernen und Praxis

        ## Methode

        - **Syllabus-Karte:** Lernziel, K-Stufe, Beispiel und offene Frage.
        - **Lernprotokoll:** Datum, Aktivität, Ergebnis, Fehler und nächster Schritt.
        - **Verteilte Wiederholung:** nach 1, 3, 7, 14 und 30 Tagen wiederholen.
        - **Teach-back:** das Konzept ohne Notizen in weniger als drei Minuten erklären.
        - **Nachweisprüfung:** ein Arbeitsergebnis prüfen lassen, nicht nur eine Antwort.

        ## Empfohlene Werkzeuge

        Nutze Obsidian für Rückverweise und atomare Notizen, eine Tabelle für Ergebnisse und Lücken, Git zur Versionierung von Arbeitsergebnissen, einen Issue-Tracker für Fehler und Nachweise sowie die in deiner Organisation freigegebenen Testwerkzeuge. Lade keine vertraulichen Daten zu externen Diensten hoch.

        ## Enthaltene Vorlagen

        - [Test-Charter](../assets/templates/test-charter.md)
        - [Fehlerbericht](../assets/templates/defect-report.md)
        - [Risikoregister](../assets/templates/risk-register.md)
        - [Teststrategie](../assets/templates/test-strategy.md)
        - [Lernprotokoll](../assets/templates/learning-log.md)
    """),
    "sources": dedent("""
        # Offizielle Quellen und Versionskontrolle

        Nutze den [ISTQB-Katalog](https://istqb.org/certifications/) als Primärquelle und das [ISTQB-Glossar](https://glossary.istqb.org/) für Fachbegriffe. Syllabi, Musterprüfungen, Antworten und Regeln werden von der offiziellen Seite der jeweiligen Zertifizierung heruntergeladen.

        ## Checkliste vor der Prüfung

        1. Syllabus-Version, Voraussetzungen und Sprache bestätigen.
        2. Aufbau, Dauer und Punktzahl beim Prüfungsanbieter prüfen.
        3. Mögliche Auslaufdaten kontrollieren.
        4. Nur offizielle Musterprüfungen oder klar gekennzeichnete eigene Fragen verwenden.
        5. Keine PDFs oder vertraulichen Prüfungsfragen weitergeben.
    """),
}

COPY["es"] = {
    "catalog_title": "Catálogo verificado de certificaciones ISTQB",
    "catalog_intro": "El catálogo internacional contiene **27 certificaciones activas** en la fecha indicada. Los títulos oficiales se mantienen en inglés. Consulta siempre la página oficial antes de comprar un examen.",
    "status_title": "Rutas en retirada",
    "status": "Foundation Level Agile Tester (CTFL-AT) y Agile Technical Tester (CT-ATT) están en retirada: los exámenes en inglés terminan el 6 de mayo de 2027 y los de otros idiomas el 6 de noviembre de 2027. CTAL-AT v2.0 es la ruta Agile actual. Las versiones anteriores de CTAL-TA, CTAL-TM, CT-TAE y CT-AI también están en transición o retiradas.",
    "study": dedent("""
        # Rutas de estudio, consejos y ejercicios

        ## Elegir el nivel

        | Objetivo | Ruta | Evidencia práctica |
        |---|---|---|
        | Lenguaje común y técnicas | CTFL | diseño de pruebas e informe de defecto |
        | Especialización operativa | Advanced o Specialist | estrategia o laboratorio de dominio |
        | Liderazgo y mejora | Expert | evaluación, hoja de ruta y métricas |

        ## Ciclo de preparación de seis semanas

        1. Mapear objetivos de aprendizaje, términos y peso de los capítulos.
        2. Estudiar un capítulo cada vez y crear ejemplos propios.
        3. Convertir cada técnica en un entregable revisable.
        4. Responder preguntas cronometradas y registrar la causa de los errores.
        5. Realizar un examen de muestra oficial en condiciones realistas.
        6. Repasar solo las carencias medidas y completar el porfolio.

        ## Consejos y trucos

        - Separar recuerdo, aplicación y análisis mediante los niveles K.
        - Descartar primero las respuestas incompatibles con el escenario.
        - Crear una ficha por técnica: uso, entrada, salida y limitación.
        - Alternar recuerdo activo, práctica y repaso espaciado.
        - No memorizar preguntas; explicar por qué las alternativas son incorrectas.

        ## Preguntas originales de práctica

        1. ¿Qué evidencia demuestra que una técnica se aplicó correctamente?
        2. ¿Cómo cambia la prioridad cuando impacto y probabilidad divergen?
        3. ¿Cuándo puede una métrica de cobertura generar falsa confianza?
        4. ¿Qué información hace reproducible un informe de defecto?
        5. ¿En qué se diferencian seguimiento, control y finalización de pruebas?
        6. ¿Qué riesgo introduce una automatización difícil de mantener?

        ## Ejercicios

        - Derivar particiones, límites y una tabla de decisión de reglas de compra.
        - Crear un registro de riesgos y justificar el orden de ejecución.
        - Revisar una historia de usuario y registrar defectos estáticos.
        - Diseñar una estrategia de regresión con criterios de selección medibles.
        - Realizar una retrospectiva y vincular cada acción con un indicador.
    """),
    "practice": dedent("""
        # Del examen a la práctica profesional

        Cada laboratorio produce evidencias aptas para un porfolio. Anonimiza siempre personas, clientes, sistemas y datos.

        | Laboratorio | Escenario | Entregable | Criterios de calidad | Evidencia |
        |---|---|---|---|---|
        | Diseño de pruebas | compra con descuentos y pagos | particiones, límites, tabla de decisión | trazabilidad y cobertura | conjunto de pruebas revisado |
        | Pruebas basadas en riesgos | entrega con tiempo limitado | registro de riesgos y orden de ejecución | impacto, probabilidad, mitigaciones | registro de decisiones |
        | Automatización | suite de regresión inestable | estrategia y prueba de concepto | valor, mantenibilidad, feedback | tendencia antes/después |
        | Calidad DevOps | pipeline con feedback tardío | quality gates y observabilidad | velocidad, responsabilidad, falsos positivos | panel mínimo |
        | Gestión de pruebas | programa con varios equipos | estrategia de pruebas e informes | objetivos, interesados, métricas | revisión aprobada |
        | Mejora de procesos | defectos recurrentes | evaluación y hoja de ruta | línea base, prioridades, resultados | retrospectiva medida |

        ## Definición de terminado del laboratorio

        - las decisiones se vinculan con riesgos y requisitos;
        - los datos reproducibles no contienen información sensible;
        - los criterios de calidad son explícitos;
        - las limitaciones y suposiciones están declaradas;
        - existe revisión de un compañero y una acción de mejora.
    """),
    "toolbox": dedent("""
        # Herramientas para aprender y trabajar

        ## Método

        - **Mapa del syllabus:** objetivo de aprendizaje, nivel K, ejemplo y duda abierta.
        - **Diario de aprendizaje:** fecha, actividad, resultado, error y próxima acción.
        - **Repaso espaciado:** revisar después de 1, 3, 7, 14 y 30 días.
        - **Teach-back:** explicar el concepto sin notas en menos de tres minutos.
        - **Revisión de evidencias:** pedir que revisen un entregable, no solo una respuesta.

        ## Herramientas recomendadas

        Usa Obsidian para enlaces y notas atómicas, una hoja de cálculo para resultados y carencias, Git para versionar entregables, un gestor de incidencias para defectos y evidencias, y las herramientas de prueba aprobadas por tu organización. No subas datos confidenciales a servicios externos.

        ## Plantillas incluidas

        - [Charter de pruebas](../assets/templates/test-charter.md)
        - [Informe de defecto](../assets/templates/defect-report.md)
        - [Registro de riesgos](../assets/templates/risk-register.md)
        - [Estrategia de pruebas](../assets/templates/test-strategy.md)
        - [Diario de aprendizaje](../assets/templates/learning-log.md)
    """),
    "sources": dedent("""
        # Fuentes oficiales y control de versiones

        Usa el [catálogo ISTQB](https://istqb.org/certifications/) como fuente principal y el [glosario ISTQB](https://glossary.istqb.org/) para la terminología. Descarga syllabus, exámenes de muestra, respuestas y reglas desde la página oficial de cada certificación.

        ## Lista de comprobación antes del examen

        1. Confirmar la versión del syllabus, los prerrequisitos y el idioma.
        2. Verificar estructura, duración y puntuación con el proveedor del examen.
        3. Comprobar posibles fechas de retirada.
        4. Usar solo exámenes de muestra oficiales o preguntas originales claramente indicadas.
        5. No redistribuir PDF ni preguntas de examen confidenciales.
    """),
}

HOME = {
    "en": ("Quality Engineering Learning Hub", "Prepare for ISTQB certifications and turn syllabus concepts into observable professional skills.", "Start with the verified catalogue, choose a study path, practise with original questions and produce reviewable evidence.", "Open the certification catalogue", ("Study paths", "Professional practice", "Learning toolbox", "Official sources"), "This is an independent project, not affiliated with ISTQB and not an accredited training provider. It contains no real exam questions or confidential material."),
    "fr": ("Centre d'apprentissage Quality Engineering", "Préparez les certifications ISTQB et transformez le syllabus en compétences professionnelles observables.", "Commencez par le catalogue vérifié, choisissez un parcours, entraînez-vous avec des questions originales et produisez des preuves révisables.", "Ouvrir le catalogue des certifications", ("Parcours d'étude", "Pratique professionnelle", "Boîte à outils", "Sources officielles"), "Ce projet indépendant n'est ni affilié à ISTQB ni un organisme de formation accrédité. Il ne contient aucune question d'examen réelle ni aucun contenu confidentiel."),
    "de": ("Quality Engineering Lernplattform", "Bereite dich auf ISTQB-Zertifizierungen vor und überführe Syllabus-Konzepte in beobachtbare berufliche Fähigkeiten.", "Beginne mit dem geprüften Katalog, wähle einen Lernpfad, übe mit eigenen Fragen und erstelle prüfbare Nachweise.", "Zertifizierungskatalog öffnen", ("Lernpfade", "Berufliche Praxis", "Lernwerkzeuge", "Offizielle Quellen"), "Dieses unabhängige Projekt ist weder mit ISTQB verbunden noch ein akkreditierter Schulungsanbieter. Es enthält keine echten Prüfungsfragen oder vertraulichen Inhalte."),
    "es": ("Centro de aprendizaje de Quality Engineering", "Prepara las certificaciones ISTQB y convierte los conceptos del syllabus en competencias profesionales observables.", "Empieza con el catálogo verificado, elige una ruta, practica con preguntas originales y produce evidencias revisables.", "Abrir el catálogo de certificaciones", ("Rutas de estudio", "Práctica profesional", "Herramientas de aprendizaje", "Fuentes oficiales"), "Este proyecto independiente no está afiliado a ISTQB ni es un proveedor de formación acreditado. No contiene preguntas de examen reales ni material confidencial."),
}

TABLE_HEADERS = {
    "it": ("Codice", "Certificazione ufficiale", "Fonte"),
    "en": ("Code", "Official certification", "Source"),
    "fr": ("Code", "Certification officielle", "Source"),
    "de": ("Code", "Offizielle Zertifizierung", "Quelle"),
    "es": ("Código", "Certificación oficial", "Fuente"),
}


def frontmatter(title: str, locale: str) -> str:
    return f"---\ntitle: {title}\nlang: {locale}\nlast_verified: {VERIFIED}\n---\n\n"


def localized_path(base: Path, locale: str) -> Path:
    if locale == "it":
        return base
    return base.with_name(f"{base.stem}.{locale}{base.suffix}")


def render_catalog(locale: str) -> str:
    copy = COPY[locale]
    code_label, certification_label, source_label = TABLE_HEADERS[locale]
    lines = [frontmatter(copy["catalog_title"], locale), f"# {copy['catalog_title']}\n", copy["catalog_intro"] + "\n"]
    for group in ("core", "technology", "quality", "domain", "expert"):
        lines.extend((f"## {GROUPS[locale][group]}\n", f"| {code_label} | {certification_label} | {source_label} |\n", "|---|---|---|\n"))
        for cert_group, code, name, url in CERTIFICATIONS:
            if cert_group == group:
                lines.append(f"| {code} | {name} | [ISTQB]({url}) |\n")
        lines.append("\n")
    lines.extend((f"## {copy['status_title']}\n", copy["status"] + "\n"))
    return "".join(lines)


def render_home(locale: str) -> str:
    title, intro, body, action, links, disclaimer = HOME[locale]
    study, practice, toolbox, sources = links
    return frontmatter(title, locale) + dedent(f"""
        # {title}

        {intro}

        {body}

        [{action}](guide/certifications.md)

        - [{study}](guide/study.md)
        - [{practice}](guide/practice.md)
        - [{toolbox}](guide/toolbox.md)
        - [{sources}](guide/sources.md)

        {disclaimer}
    """)


def write() -> None:
    GUIDE.mkdir(parents=True, exist_ok=True)
    for locale in COPY:
        catalog = localized_path(GUIDE / "certifications.md", locale)
        catalog.write_text(render_catalog(locale), encoding="utf-8", newline="\n")
        for key in ("study", "practice", "toolbox", "sources"):
            path = localized_path(GUIDE / f"{key}.md", locale)
            title = COPY[locale][key].lstrip().splitlines()[0].removeprefix("# ")
            path.write_text(frontmatter(title, locale) + COPY[locale][key].lstrip(), encoding="utf-8", newline="\n")

    for locale in HOME:
        localized_path(DOCS / "index.md", locale).write_text(render_home(locale), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    write()
