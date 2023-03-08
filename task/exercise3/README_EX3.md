# Cron String

Questo progetto riguarda la creazione di un backup della directory utente che andrà poi inviata su un server remoto, utilizzando il comando cron e il protocollo SSH.

## Installazione
Per utilizzare questo script, assicurarsi di avere installato sul proprio sistema il programma cron e il client SSH. Verificare inoltre che sia stata configurata una coppia di chiavi pubbliche/ private per l'autenticazione SSH.
Copiare il file ex3.sh in una directory a scelta.

## Configurazione Cron String
E' possibile configurare la pianificazione del job modificando una particolare stringa.
Aprire il file ex3.sh con l'editor preferito e modificare la seguente sezione del codice:

> echo " [* * * * *] [some_command]" >> /home/user/newCrontabJob

dove [* * * * *] verrà inserito l'arco temporale in accordo con la sintassi della cron string e [some_command] verrà sostituito con i comandi desiderati per eseguire il job

- Esempio:
    Supponiamo di volere che ogni sera alle 21 venga creata la copia di un archivio. Modificheremo lo script nel seguente modo:

    > echo "0 21 * * 0 tar -czvf /home/user/archive_name.tar.gz /path/to/directory_to_compress" >> /home/user/newCrontabJob

Il comando verrà inserito in un file che poi verrà schedulato per la pinaificazione dei job, salvare e chiudere il file.
Questo produrrà ogni sera alle 21.00, un archivio in /home/user denominato archive_name.tar.gz compresso da una specifica directory o file.



## Utilizzo
E' possibile eseguire lo script per verificare che funzioni correttamente. Aprire un terminale e navigare nella directory in cui è stato salvato il file ex3.sh.sh. Quindi, eseguire il comando seguente:

- bash

    > ./ex3.sh

Questo creerà un un file in /home/user in cui verrà scritta una copia di tutti i job precedentemente pianificati.
Verrà poi fatto un append della stringa contenente la nuova pianificazione ed il file verrà memorizzato dal daemon Crontab.d
in modo da avere tutti i job precedenti più il nuovo job pianificato.
Infine la copia di questo file precedentemente creata verrà eliminata.

Ora il backup ed invio all'host specificato verrà eseguito automaticamente ogni domenica notte.

## Nota
E' buona norma di verificare regolarmente la riuscita del backup. Inoltre, se la directory di destinazione sul server remoto non esiste, assicurarsi di crearla prima di eseguire lo script.