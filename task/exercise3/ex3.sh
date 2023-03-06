#!/bin/sh

# crea un nuovo file nella specifica directory in cui verrà memorizzata una copia dei job pianificati
crontab -l > /home/user/newCrontabJob

# 1. Imposta come tempo di esecuzione del job, ogni domenica sera alle ore 21.00 
# 2. Usa il comando 'tar' per creare un archivio della directory.
#       c --> crea il nuovo archivio
#       z --> è il metodo di compressione
#       v --> aggiunge ogni elemento presente nella cartella all'archio
#       f --> specifica il nome dell'archivio
# 3. Usa il comando scp -i per copiare l'archivio compresso sulla directory del server remoto
#    usando la chiave privata contenuta nella specifica directory
# 4. Infine salva l'intera stringa in coda al file precedentemente creato
echo "0 21 * * 0 
      tar -czvf /home/user/folder.tar.gz 
      scp -i /percorso della chiave privata 
             /path/to/archive.tar.gz user@192.168.1.100:/path/on/remote_host" >> /home/user/newCrontabJob

# Il file viene messo nel CronTab del sistema con il nuovo job pianificato
crontab /home/user/newCrontabJob

# Rimuove la copia di 'newCrontabJob' precedentemente creata
rm /home/user/newCrontabJob