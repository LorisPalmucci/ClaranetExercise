# Shebang-Counter Script

Questo script Python o Bash conta il numero di file script presenti in una directory e li suddivide in base all'interprete Shebang specificato all'inizio di ciascun file. L'interprete Shebang è la riga di commento che indica quale interprete di comandi deve essere utilizzato per eseguire lo script.

## Installazione
Per utilizzare lo script, assicurarsi di avere Python installato sul proprio sistema. Quindi, scaricare il file dello script e salvarlo in una posizione a scelta.

## Utilizzo
Per eseguire lo script, aprire un terminale e navigare nella directory in cui è salvato lo script. Quindi, utilizzare il seguente comando:

Per utilizzare la versione Python dello script, esegui il seguente comando:

> python ex1.py [nome_directory]

Sostituire [nome_directory] con il nome della directory che si desidera controllare.

- Esempio
    Supponiamo che si voglia contare il numero di script presenti nella directory "/percorso/alla/mia_directory". Per fare ciò utilizzando la versione Python dello script, eseguire il seguente comando:

    > python ex1.py [percorso/alla/mia_directory]

Ciò restituirà un elenco delle varie interpretazioni Shebang e il numero di file script che utilizzano ciascuna interprete.

## Nota
Questo script conta i file script presenti nella directory specificata, ed i file nelle eventuali sotto-directory. Inoltre, l'interprete Shebang deve essere indicato all'inizio di ogni file script, altrimenti lo script non verrà contato.

Si consiglia di verificare attentamente i risultati e di esaminare i file script per assicurarsi che siano stati contati correttamente.