# Løsning
Underveis i implementeringen så kom jeg frem til at det ville vært snevet mer morsomt å
lage en simulering av et lite konsoll-kasino. Min løsning av alle 6 oppgavene er av den grunn
flyttet til en fil jeg har kalt 'game.py' som inneholder et objekt kalt 'Game'. 'Game' består av 
metoder jeg så på som nødvendig for å kunne gjennomføre en komplett runde med Blackjack mot en
dealer.

Filen 'program.py' inneholder derimot den overordede strukturen til mitt lille kasino hvor spilleren
i først omgang kan definere hvor mye "penger" hen ønsker å entre kasinoet med i sin "lommebok". 
Deretter så kan spilleren velge hvor mye hen vil satse per runde vedkommende spiller. 

Hvis spilleren får en blackjack/natural så vil vedkommende få tilbakebetalt med odds 3:2. Ellers,
hvis spilleren vinner mot dealeren, så vil spilleren motta tilbakebetaling med odds 1:1. Det tas
også hensyn til runder hvor det blir uavgjort mot dealeren, hvor spiller dermed vil få tilbake det
vedkommende satset.

Blir spilleren blakk så vil vedkommende bli kastet ut av kasino-spillet.

Ellers så skal alle andre funksjonaliteter være i henhold til min tolkning av oppgavene.

# Setup
Start med å åpne en konsoll, og CD deg inn til mappen med denne filen.

## Virtualenv
Alle python-prosjekter bør kjøre i sitt eget virtuelle miljø. Dette gjøres slik (eller tilsvarende, litt avhengig av hvordan python er installert):
```
python3 -m virtualenv -p python3 venv
```

og aktiveres slik:
```
[linux/mac]
source venv/bin/activate

[windows]
.\venv\Scripts\activate
``` 

## Installasjon
BlackJack for python er laget som en python-pakke, og kan installeres som dette:
```
pip install -e .
```

Kontroller at installasjonen fungerte ved å kjøre testene:
```
python setup.py test
```

## Kjør programmet
```
play
```
