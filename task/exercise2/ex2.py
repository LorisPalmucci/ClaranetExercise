#!/usr/bin/python

import os
import sys

# crea un dizionario, ovvero una struttura dati simili ad HashMap di Java in cui ad
# ogni valore viene associata una chiave univoca
shebangSet = {}

# Questa funzione prende in ingresso il percorso principale di cui si vorrà cercare tutti i file con shebang.
# Naviga dentro ogno sotto-directory del percorso principale passato. Per ogni sotto-directory salva il relativo
# percorso in 'subPath' e ne cerca ogni file, memorizzando il suo percorso assoluto del file in 'absoluteFilePath'.
# Inoltre chiama la funzione 'calculateFile'.
def directoryNavigator(directory):
    for rootPath, subDirectory, listFiles in os.walk(directory):
        for fileName in listFiles:
            # memorizza il percorso assoluto del file attuale da passare alla funzione 'calculateFile'
            absoluteFilepath = os.path.join(rootPath, fileName)
            calculateFile(absoluteFilepath)
    
# Questa funzione prende in ingresso il percorso della sotto-directory, del file ed il file stesso attuale.
# In ogni sotto-directory ignora tutti i file che non sono degli eseguibili '.py', quindi apre gli altri
# e ne analizza la prima riga: se ha un identificatore shebang allora verrà inserito nel dizionario ed incrementato di 1,
# la cui chiave univoca è il percorso completo del file.
def calculateFile(filepath):
    # apre il file in modalità scrittura e legge la prima linea togliendo eventuali spazi
    with open(filepath, 'r') as file:
        firstLine = file.readline()
        isShebang = firstLine.strip()
        # se la prima linea è uno shebang allora lo memorizza nel dizionario e incrementa il suo conteggio
        if isShebang.startswith('#!'):
            shebangLine = isShebang
            shebangSet[shebangLine] = shebangSet.get(shebangLine, 0) + 1

# funzione main
if __name__ == '__main__':
    topLevelDirectory = sys.argv[1]
    directoryNavigator(topLevelDirectory)
    # stampa a schermo il dizionario chiave-valori dopo l'analisi
    print("File trovati in " + topLevelDirectory + ":\n")
    for shebang, count in shebangSet.items():
        print(f'"{shebang.strip()}": {count} file(s)')