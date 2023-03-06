
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
    for rootPath, subDirectory, pathFiles in os.walk(directory):
        for dir in subDirectory:
            # memorizza il percorso della sotto-directory attuale
            subpath = os.path.join(rootPath, dir)
        for fileName in pathFiles:
            # memorizza il percorso assoluto del file attuale da passare alla funzione 'calculateFile'
            absoluteFilepath = os.path.join(rootPath, fileName)
            calculateFile(subpath, absoluteFilepath, pathFiles)
    
# Questa funzione prende in ingresso il percorso della sotto-directory, del file ed il file stesso attuale.
# In ogni sotto-directory ignora tutti i file che non sono degli eseguibili '.py', quindi apre gli altri
# e ne analizza la prima riga: se ha un identificatore shebang allora verrà inserito nel dizionario ed incrementato di 1,
# la cui chiave univoca è il percorso completo del file.
def calculateFile(subpath, filepath, files):
    for filename in files:
        # controlla che sia un eseguibile .py. La scelta è stata fatta ipotizzando che quest sia il tipo
        # di file che ci interessa analizzare in modo da velociazzare la ricerca.
        if not (filename.endswith('.py')):
                continue
        # se il file è un eseguibile python allora lo apre e analizza la prima riga. Se ha uno shebang
        # allora lo aggiunge al dizionario
        with open(filepath, 'r') as f:
            first_line = f.readline()
            isShebang = first_line.strip()
            if isShebang.startswith('#!'):
                shebangLine = subpath + "  ---->  " + isShebang
                shebangSet[shebangLine] = shebangSet.get(shebangLine, 0) + 1

# funzione main
if __name__ == '__main__':
    topLevelDirectory = sys.argv[1]
    directoryNavigator(topLevelDirectory)
    # stampa a schermo il dizionario chiave-valori dopo l'analisi
    for shebang, count in shebangSet.items():
        print(f'"{shebang.strip()}": {count} file(s)')