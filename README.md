# Løsning
Underveis i implementeringen så kom jeg til konklusjonen om at det ville vært snevet mer morsomt å
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

# Oppgavetekst
Vedlagt ligger noen linjer av kildekoden til Blackjack. Det er en kjørende konsollapplikasjon, men uten at veldig mye virker. Gjør alle endringene du føler er nødvendig for å løse oppgavene og sikre at svarene er riktig.

## Oppgave 1:
Dersom man får over 21 poeng har man tapt og kan ikke trekke flere kort. Implementer dette

## Oppgave 2:
Kortene lagres nå som et tall fra 1 til 13. Endre dette slik at Knekt, Dame, Konge og Ess skrives ut som J, Q, K og A.

## Oppgave 3:
I Blackjack kan ess fungere både som 1 og 11 Spillet skal automatisk velge det som er det beste for spilleren. 

## Oppgave 4:
Endre så kortene trekkes fra kortstokken i tilfeldig rekkefølge

## Oppgave 5:
Blackjack spilles som regel mot en dealer. Implementer en dealer som får utdelt egne kort. Dealeren skal få utdelt ett kort opp på starten. Deretter skal spilleren spille ferdig før dealeren spiller videre. Dealeren trekker kort til han får 17 eller flere poeng

## Oppgave 6
Spillet skal skrive ut hvem som vant: Dealer eller spiller