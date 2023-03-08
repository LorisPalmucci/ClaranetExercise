## Substring substitution script

Questo script prende tre parametri:

- stringa da sostituire
- nuova stringa
- il percorso di una directory

e sostituisce in modo ricorsivo ogni occorrenza della prima stringa con la seconda stringa in tutti i file presenti nella directory.

# Installazione
Per utilizzare lo script, assicurarsi di avere Python installato sul proprio sistema. Quindi, scaricare il file dello script e salvarlo in una posizione a scelta.

# Utilizzo
Per eseguire lo script, aprire un terminale e navigare nella directory in cui è salvato lo script. Quindi, utilizzare il seguente comando:

> python ex1.py [prima_stringa] [seconda_stringa] [nome_directory]

Sostituire [prima_stringa] con la stringa che si desidera sostituire, [seconda_stringa] con la stringa di sostituzione e [nome_directory] con il nome della directory in cui si desidera eseguire la modifica.

Esempio:
Supponiamo che si voglia sostituire tutte le occorrenze della stringa "ciao mondo" con la stringa "hello world!" in tutti i file presenti nella directory "/percorso/alla/mia_directory". Per fare ciò utilizzando la versione Python dello script, eseguire il seguente comando:

> python ex1.py 'ciao mondo' 'hello world!' percorso/alla/mia_directory

Ciò sostituirà tutte le occorrenze di "ciao mondo" con "hello world!" in tutti i file presenti nella directory "percorso/alla/mia_directory", in modo ricorsivo.

# Nota
Fare attenzione quando si utilizza questo script, in quanto esso apporterà modifiche ai file nella directory specificata. Si consiglia di creare un backup dei file prima di eseguire lo script, nel caso in cui si verifichino cambiamenti imprevisti.