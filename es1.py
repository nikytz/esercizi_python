tupla=(
    ("Milano", [("gennaio", "N/D"),("febbraio", 23),("marzo", 21),("aprile", 13),("maggio", 32),("giugno", "N/D"),("luglio", 14),("agosto", 35),("setembre", 11),("ottobre", "N/D"),("novembre", 10),("dicembre", 5)]),
    ("Novara", [("gennaio", 34),("febbraio", 23),("marzo", "N/D"),("aprile", 31),("maggio", 2),("giugno", "N/D"),("luglio", 11),("agosto", 0),("setembre", "N/D"),("ottobre",11 ),("novembre", 3),("dicembre", 5)])
    )

def calcola(nomeCitta):
    somma=0
    conta=0
    tempMax=-100
    tempMin=100
    meseMax=[]
    meseMin=[]
    for citta,rilevazioni in tupla:
        if nomeCitta==citta: 
            for mese,valore in rilevazioni:
                if valore!="N/D":
                    conta+=1
                    somma+=valore
        media=somma/conta
    
    for citta,rilevazioni in tupla:
        if nomeCitta==citta: 
            for mese,valore in rilevazioni:
                if valore!="N/D":
                    if valore>tempMax:
                        tempMax=valore
                        meseMax=[mese]
                    if valore<tempMin:
                        tempMin=valore
                        meseMin=[mese]
    for citta, rilevazioni in tupla:
        if mese==tempMax:
            meseMax.append(mese)
        if mese==tempMin:
            meseMin.append(mese)
    return((media,(tempMax, meseMax), (tempMin, meseMin)))


while True:
    nomeCitta=str(input("inserisci il nome della citta: "))
    cittaTrovata=False
    for citta, rilevazioni in tupla:
        if nomeCitta in citta:
            cittaTrovata=True
    if cittaTrovata==True:
        break
    else:
        print("citta non valida")

print(calcola(nomeCitta))
   

