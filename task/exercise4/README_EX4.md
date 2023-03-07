# INTRODUZIONE

## Scenario:
   Dopo la scoperta del Covid che ha interessato l'intero globo e dopo aver fatto fronte alla prima emergenza sanitaria, 
   il governo Italiano ha deciso di mettere in piedi un sito in cui i cittadini possano informarsi su norme comportamentali
   sull'andamento della pandemia nella nazione, in quali comuni e regioni entrano in vigore le norme di contenimento e molte
   altri informazioni a riguardo.
   Del deploy se ne occupa Claranet, che incarica i suoi Flower di scegliere i tool e dare vita al sito.

### Quali tool sono stati scelti e perché:
- Per l'automatizzazione dell'infrastruttura si è scelto di usare Ansible:
  - Ansible permette di gestire un grande numero di server e può essere usato su svariati dispositivi fisici o virtuali,
    cloud e dispositivi di rete

- Per il setup dell'applicazione invece si è scelto di usare Docker:
  - Permette di usare immagini di applicazioni indipendentemente dal sistema operativo sottostante, isola i vari ambienti
    di lavoro garantendo sicurezza e affidabilità, a basso impatto sulle prestazione della macchina ed efficiente nella
    distribuzione e gestione dell'applicazione

- Come server Web si è scelto di usare Nginx:
  -- Essendo un sito a scopo prettamente informativo Nginx si dimostra all'altezza nel gestire un gran numero di richieste 
    da parte dei client, grazie alla sua capacità di Reverse Proxy è protetto da attacchi informatici garantendo sicurezza
    al sito, inoltre è facile da configurare

    Nel caso in cui divenisse neccessaria l'acquisizione di dati personali di utenti, sposterei la mia scelta su Apache,
    che garantisce stabilità e protezione avantate di autenticazione ecrittografia oltre ad avere una nutrita comunity di
    supporto

- Per creare l'infrastruttura si è scelto di usare CloudFormation visto che il sito sarà messo su un Cloud AWS:
  -- Facilità di gestione delle delle risorse dello stack AWS che consente di modificarle, aggiornarle o eliminarle
    quando necessario, sicurezza grazie alle autorizzazioni di accesso alle risorse, rollback in caso di problemi grazie
    alla gestione di più versioni delle definizioni dello stack, possibilità di riprodurre l'infrastruttura su più
    account AWS

## CLOUDFORMATION
Grazie alla possibilità di eseguire la propria infrastruttura come codice, è possibile descrivere le risorse che si intende
creare con le loro porpietà in un file YAML.
Come primo passo verrà istanziato un ambiente sul cloud AWS in particolare potremmo definire un'istanza per Docker in 
modo che venga eseguito uno script che lo installi nello stac EC2:

    yaml:
    #
      configurazione stack EC2
    #

      # Definizione della risorsa
    Risorsa Docker:
      Type: AWS::EC2::Instance
      Properties:
        ImageId: tipo di AMI che si vuole usare come base
        InstanceType: tipo di istanza da inizializzare
        KeyName: chiave SSH
        SecurityGroupIds:
          - sg-1234567890abcdef

        UserData:
          Fn::Base64: !Sub |
            #!/bin/bash
            apt-get update
            apt-get install -y docker.io
            docker run -d -p 80:80 --name my_nginx nginx

dove in UserData specificheremo di eseguire lo script o comandi da per configurare Docker.
Inoltre nel container di Docker si è deciso di istanziare anche il server Web Nginx, in modo tale che nella stessa macchina
si possano avere server Web diversi (Apache ad esempio) containerizzati in altre applicazioni.

## ANSIBLE
Grazie ad Ansible possiamo gestire la creazione dell'infrastruttura su un Cloud AWS.
Nell'architettura pensata si è deciso di far gestire l'automazione ad Ansible facendo in modo che le configurazioni
per la creazione dello stack EC2 vengano eseguite su macchine remote.
Una volta creato il file di configurazione YAML, esso può essere mandato in esecuzione su diversi host con il comando

  > ansible-playbook -i inventory.ini aws.yml

dove  inventory.ini non è altro che una lista di host su cui eseguire il playbook aws.yml.
Si può aggiungere al comando anche la seguente condizione

  > ask-become-pass con cui chiederemo le credenziali dell'utente remoto

una ulteriore precauzione per la sicurezza.

Si è scelto di usare Ansible anche per comandare il Docker Client che gira su una macchina diversa dal container 
dell'applicazione in modo da avere i file di configurazione separati dal container in modo da aumentare l'affidabilità
e poter rimettere in piedi il container in tempi ragionevoli.
Utilizzando il modulo docker_container è possibile gestire il Client_Docker situato su una macchina diversa dal container
stesso. Questo modulo verrà impostato nel nodo di Controllo di Ansible

In questo modo possiamo centralizzare la gestione sia di AWS che di Docker.

## DOCKER
Come detto in precedenza useremo una tecnica di containerizzazione delle applicazioni usando Docker.
Si è scelto questo approccio per fare in modo che sulla stessa macchina si possano avere più applicazioni, anche con
funzionalità diverse.

Avremo che il client_docker girerà su un host diverso da quello del container poiché avremo alcuni benefici:
  - gestione centralizzata sui container in esecuzione su molte macchine
  - maggiore sicurezza, evitando di esporre il client sulla macchina remota proteggeremo anche i container
  - possibilità di eseguire il client anche su S.O. diverso da quello del container
  - migliore gestione delle risorse dato che non avremo un client per ogni container separato

Nel file di configurazione YAML possiamo specificare il tipo di istanza di WordPress che vogliamo installare, mettendo
come dipendenza la risorsa Wordpress nella risorsa Docker.

All'interno di Docker istanzieremo anche il web server scelto che andrà anch'esso come dipendenza della risorsa Docker nel
file YAML. Anche qui ci sono alcuni vantaggi:
  - essendo un ambiente isolato, avremo che il webserver sarà meno soggetto ad attacchi dall'esterno
  - sempre grazie alla concezione di isolamento, se il webserver andasse fuori servizio, avremo che solo l'applicazione
    di quel container smetta di funzionare, a differenza di un web server istanziato in maniera classica che renderebbe
    inaccessibile qualsiasi processo fino al completo ripristino
  - è possibile creare un'immagine del webserver e riprodurla su un altro container

Inoltre il container di Docker sarà correlato anche di un DB. Anche qui la scelta di includere un DB all'interno è analoga
ai motivi sopracitati. E' anche possibile aggiungere estensioni e plugin in base alle necessità del sito.

## NGINX
Si è scelto questo tipo di Web Server per la possibilità di scalare orizzontalmente la struttura in modo da poter distribuire
il carico dati su più server, per la sua capacità di gestire grandi quantità di connessioni contemporaneamente e flusso dati.
Essendo lo scenario un sito avente contenuti statici con un probabile alto afflusso di richieste, Nginx si presta bene a
gestire queste esigenze. Inoltre avendo un più basso consumo di RAM rispetto ad Apache lo rende ottimo nel caso si abbiano
svariati container nella stessa macchina.

POST-DEPLOY
Una volta deployata l'applicazione dovrebbe essere:
1. Sicura:
    - uso di HTTPS per la comunicazione 
    - crittografia di dati sensibili
    - uso di firewall per limitare l'accesso ai servizi e alle porte

2. Veloce:
    - utilizzo di cache
    - usare tecniche per distribuire il traffico su più server

3. Tollerante ai Guasti:
    - usare un approccio a sistemi distribuiti

4. Adattabilità al carico Medio
    - auto-scaling per adattare le risorse in base al traffico
    - utilizzo di cache

## CONCLUSIONI
Per deployare un sito per prima cosa andremo ad analizzare le possibilità di richieste ed il tipo di contenuti in modo da
farsi un visione generale di quali tool usare. Una volta concretizzata questa visione passeremo a strutturare
l'intera architettura.

Per prima cosa istanzieremo un ambiente EC2 per AWS. In questo ambiente andremo a mettere tutte le componenti di cui
abbiamo bisogno. Per semplificare il più possibile l'architettura, si è deciso di applicare un sistema centralizzato in cui
nell'ambiente AWS avremo soltanto i container Docker istanziati. Il client_docker ed il nodo di controllo di Ansible
saranno in funzione su una macchina separata, per alleggerire il l'ambiente AWS e proteggere i container da attacchi esterni.

Una volta istanziato l'ambiente AWS, andremo a creare il container di Docker in cui al suo interno verrano inserite le immagini
del Web Server, del DB ed altre funzionalità.

Per automatizzare il tutto faremo uso di Ansible che ci permette di gestire da remoto ogni singola parte che abbiamo istanziato,
dall'ambiente AWS al container ed i suoi componenti interni.

Una volta eseguito il deploy proteggremo l'applicativo con firewall e connessioni HTTPS, useremo delle cache per velocizzare
e gestire l'alto flusso di dati ed infine potremmo usare più container della stessa applicazione, anche su host diversi, per
avere un sistema distribuito resistente ai guasti.