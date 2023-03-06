import os
import sys

# Questa funzione prende in ingresso i tre parametri passati dalla funzione main.
# Naviga all'interno della directory principale e di tutte le sottodirectory che trova,
# cercando ogni file dentro lungo il cammino #
def directorySelector(dirPath, oldStr, newStr):
    for dirpath, dirList, fileList in os.walk(dirPath):
        # per ogni file trovato crea il suo path assoluto
        for filename in fileList:
            filePath = os.path.join(dirpath, filename)
            # chiama la funzione di sostituzione stringa
            overwriteFileString(filePath, oldStr, newStr)

# Questa funzione prende in ingresso 3 parametri: il percorso assoluto del file, la stringa
# da sostutuire e la nuova stringa.
# Per ogni file trovato, esso viene aperto e modificato #
def overwriteFileString(filePath, oldStr, newStr):
    # apre il file corrente in lettura e ne inserisce il contenuto in una variabile per non
    # sovrascrivere subito l'originale. I parametri sono la vecchia stringa e la nuova stringa
    with open(filePath, 'r') as file:
        bodyFile = file.read()
    # apre il file in scrittura e modifica il file originale
    with open(filePath, 'w') as file:
        file.write(bodyFile.replace(oldStr, newStr))

# Funzione Main, vanno inseriti tre parametri all'avvio
# 1. la stringa da modificare
# 2. la nuova stringa
# 3. il percorso della directory principale #
if __name__ == '__main__':
    oldString = sys.argv[1]
    newString = sys.argv[2]
    directoryPath = sys.argv[3]
    directorySelector(directoryPath, oldString, newString)