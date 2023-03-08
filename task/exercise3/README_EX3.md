# Cron String

Questo progetto riguarda la creazione di un backup della directory utente che andrà poi inviata su un server remoto, utilizzando il comando cron e il protocollo SSH.

## Installazione
Per utilizzare questo script, assicurarsi di avere installato sul proprio sistema il programma cron e il client SSH. Verificare inoltre che sia stata configurata una coppia di chiavi pubbliche/ private per l'autenticazione SSH.
Copiare il file ex3.sh in una directory a scelta.

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