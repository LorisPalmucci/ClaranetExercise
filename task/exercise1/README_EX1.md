## Substring substitution script

Questo script prende tre parametri:

- stringa da sostituire
- nuova stringa
- il percorso di una directory

e sostituisce in modo ricorsivo ogni occorrenza della prima stringa con la seconda stringa in tutti i file presenti nella directory.

# Installazione
Per utilizzare lo script, assicurati di avere Python 3 installato sul tuo sistema. Quindi, scarica il file dello script e salvalo in una posizione a tua scelta.

# Utilizzo
Per eseguire lo script, apri un terminale e naviga nella directory in cui è salvato lo script. Quindi, utilizza il seguente comando:

css
Copy code
python3 sostituzione_sottostringhe.py [prima_stringa] [seconda_stringa] [nome_directory]
Sostituisci [prima_stringa] con la stringa che desideri sostituire, [seconda_stringa] con la stringa di sostituzione e [nome_directory] con il nome della directory che desideri cercare.

Esempio
Supponiamo che tu voglia sostituire tutte le occorrenze della stringa "foo" con la stringa "bar" in tutti i file presenti nella directory "mia_directory". Per fare ciò utilizzando la versione Python dello script, esegui il seguente comando:

python3 sostituzione_sottostringhe.py foo bar mia_directory
Ciò sostituirà tutte le occorrenze di "foo" con "bar" in tutti i file presenti nella directory "mia_directory", in modo ricorsivo. Lo stesso risultato può essere ottenuto utilizzando la versione Bash dello script eseguendo il comando equivalente:

Nota
Fai attenzione quando utilizzi questo script, in quanto esso apporterà modifiche ai file nella directory specificata. Si consiglia di creare un backup dei file prima di eseguire lo script, nel caso in cui si verifichino cambiamenti imprevisti.