tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    somma=0
    conta=0
    for squadra1, squadra2, num1, num2 in tupla_partite:
        somma+=num1
        somma+=num2
        conta+=1
    media=somma/conta
    return media

while True:
    squadra=input("inserisci il nome della quadra: ")
    for squadra1, squadra2, num1, num2 in tupla_partite:
        if (squadra==squadra1)or(squadra==squadra2):
            break
        else:
            print("squadra inesistente")

def media_gol_squadra(tupla_partite, squadra):
    conta=0
    somma=0
    for squadra1, squadra2, num1, num2 in tupla_partite:
        if squadra==squadra1:
            somma+=num1
            conta+=1
        if squadra==squadra2:
            somma+=num2
            conta+=1    
    media=somma/conta
    return media

def partita_con_piu_gol(tupla_partite):
    max=0
    somma=0
    risultati=[]
    for squadra1, squadra2, num1, num2 in tupla_partite:
        somma+=num1
        somma+=num2
        if somma>max:
            max=somma
            risultati.append(max)
    return max, risultati


def partita_con_meno_gol(tupla_partite):
    min=100
    somma=0
    risultati=[]
    for squadra1, squadra2, num1, num2 in tupla_partite:
        somma+=num1
        somma+=num2
        if somma<min:
            min=somma
            risultati.append(min)
    return min, risultati



def percentuale_vittorie_squadra(tupla_partite, squadra):
    somma=0
    sommaTot=0
    for squadra1, squadra2, num1, num2 in tupla_partite:
        if squadra==squadra1:
            somma+=num1
        if squadra==squadra2:
            somma+=num2
    for squadra1, squadra2, num1, num2 in tupla_partite:
        sommaTot+=num1
        sommaTot+=num2
    percentuale=(somma/sommaTot)*100
    return percentuale


while True:
    scelta=int(input("inserisci quale funzione vuoi visualizzare, (1-media dei gol totali, 2-media dei gol di una squadra, 3-partita con piu goal, 4- partite con meno goal, 5- la percentuale)"))
    if (scelta==1)or(scelta==2)or(scelta==3)or(scelta==4)or(scelta==5):
        if scelta==1:
            print(f"la media di goal di tutte le partite è di {media_gol_partite(tupla_partite)}")
        elif scelta==2:
            print(f"la media di gol di {squadra} è {media_gol_squadra(tupla_partite, squadra)}")
        elif scelta==3:
            print(f"la partita con piu punteggi è {partita_con_piu_gol(tupla_partite)}")
        elif scelta==4:
            print(f"la partita con meno punteggi è {partita_con_meno_gol(tupla_partite)}")
        elif scelta==5:
            print(f"la percentuale di {squadra} è {percentuale_vittorie_squadra(tupla_partite, squadra)}%")
        break
    else:
        print("risposta inesatta")
