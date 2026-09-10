# Domande originali CTFL

Queste domande sono create per il repository: non sono domande ISTQB e non predicono l'esame. Copri la colonna delle risposte mentre lavori.

## Quiz

1. Un team esegue test per mostrare che tutte le combinazioni possibili funzionano. Quale principio mette in discussione l'obiettivo?
2. Durante una review, un requisito ambiguo viene corretto prima dello sviluppo. Quale beneficio del testing si osserva?
3. Un campo accetta eta da 18 a 65 incluse. Quale set minimo copre i confini con BVA a due valori?
4. Una regola concede sconto se il cliente e premium **e** l'ordine supera 100 euro. Quale tecnica rappresenta meglio le combinazioni?
5. Una transizione `Bozza → Approvato` e consentita solo a un revisore. Quale tecnica e piu adatta?
6. 9 statement su 10 sono eseguiti. Che copertura statement e stata raggiunta?
7. Quale informazione rende un difetto piu riproducibile: priorita, titolo creativo, risultato atteso/osservato con passi, o nome del tester?
8. Perche test indipendenti possono trovare difetti diversi rispetto all'autore?
9. Un rischio ha alta probabilita e basso impatto; un altro bassa probabilita e impatto catastrofico. Qual e il primo passo corretto?
10. Una suite UI automatizzata e lenta e fragile. Qual e la decisione piu coerente con benefici e rischi dei tool?
11. Dopo una modifica fiscale, quali test sono rilevanti oltre alla verifica della correzione?
12. Il numero di difetti aperti cala, ma cresce il tempo medio di risoluzione. Qual e la lettura migliore?

## Risposte ragionate

1. Il testing esaustivo e impossibile: bisogna selezionare in base a rischio e priorita.
2. Prevenzione/rilevazione anticipata dei difetti e riduzione del costo di correzione.
3. `17, 18, 65, 66`: per ciascun confine, il valore sul confine e quello adiacente esterno.
4. Tabella delle decisioni, per rendere esplicite le combinazioni delle condizioni.
5. Testing delle transizioni di stato.
6. 90%.
7. Passi, precondizioni/dati, risultato atteso e osservato.
8. Prospettive e bias diversi aumentano la probabilita di rilevare categorie differenti di difetti.
9. Definire un metodo coerente di valutazione/esposizione e discutere il contesto con gli stakeholder; non basta ordinare una sola dimensione.
10. Analizzare cause e livelli piu adatti, ridurre test UI ridondanti e migliorare manutenibilita; non automatizzare di piu per compensare.
11. Confirmation testing e regression testing mirato alle aree impattate.
12. Le metriche vanno lette insieme: meno aperti non implica flusso migliore; servono aging, severita, arrivi/chiusure e cause del tempo crescente.

## Autovalutazione

Assegna 0 se hai indovinato, 1 se sai spiegare, 2 se sai produrre un esempio nuovo. Obiettivo: almeno 20/24, con nessuna risposta a 0.

