# Esercizi CTFL

## 1. Valori limite — 20 minuti

**Scenario:** un bonifico accetta importi da 1,00 a 5.000,00 euro inclusi, con due decimali.

**Consegna:** identifica partizioni e casi per BVA a due valori; aggiungi un caso per formato non valido.

**Qualita:** ogni caso ha input, risultato atteso e confine/partizione coperta; niente duplicati senza motivazione.

## 2. Tabella delle decisioni — 35 minuti

**Scenario:** il reso e accettato entro 30 giorni, se il prodotto non e personalizzato. I clienti premium possono rendere entro 60 giorni, ma mai prodotti personalizzati.

**Consegna:** costruisci condizioni, azioni, regole e almeno un test per regola valida.

**Qualita:** regole complete, contraddizioni evidenziate, casi impossibili dichiarati.

## 3. Transizioni di stato — 35 minuti

**Scenario:** una richiesta passa tra Bozza, In revisione, Approvata, Rifiutata e Annullata. Solo Bozza puo entrare In revisione; Approvata e Rifiutata sono finali; l'autore puo annullare prima della decisione.

**Consegna:** disegna il modello e deriva test per transizioni valide e invalide.

**Qualita:** stato iniziale/finale espliciti, ruoli inclusi, oracolo per ogni test.

## 4. Review di una user story — 30 minuti

**Testo:** “Come cliente voglio ricevere velocemente una notifica quando il pagamento va male, per sapere cosa fare.”

**Consegna:** annota almeno cinque finding e riscrivi criteri di accettazione testabili.

**Qualita:** separa ambiguita, completezza, consistenza e testabilita; non inventare decisioni di business.

## 5. Portfolio finale — 90 minuti

Scegli un flusso pubblico o un'app demo. Produci rischio, charter esplorativo, cinque test derivati con almeno due tecniche, un defect report e una retrospettiva di una pagina.

Valuta l'artefatto con quattro livelli: **assente**, **parziale**, **corretto**, **corretto e motivato**. Chiedi a un collega di effettuare la stessa valutazione senza spiegazioni preventive: le differenze rivelano ambiguita.

