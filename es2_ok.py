tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("febbraio", ("elettrico", 453))
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("gennaio", ("gas", 234))
    ]),
    ("Novara", [
        ("febbraio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("gennaio", ("gas", 260)),
        ("febbraio", ("gas", 245)),
        ("febbraio", ("elettrico", 234))
    ])
    
)
while True:
    nomeCitta=input("inserisci il nome dell citta: ")
    for (citta,(mese,(risorsa,consumo)))in tupla_consumi_energetici:
        if nomeCitta==citta:
            break
        else:
            ("nome sbagliato")
while True:
    nomeRisorsa=input("inserisci il nome dell citta: ")
    for (citta,(mese,(risorsa,consumo)))in tupla_consumi_energetici:
        if nomeRisorsa==risorsa:
            break
        else:
            ("nome sbagliato")

def analizza_consumi_energetici(tupla_consumi_energetici, nomeCitta, nomeRisorsa):
    somma=0
    conta=0
    max=0
    meseA=[]
    for (citta,(mese,(risorsa,consumo)))in tupla_consumi_energetici:
        if (nomeCitta==citta)and(nomeRisorsa==risorsa):
            somma+=consumo
            conta+=1
    media_risorsa=somma/conta
    for (citta,(mese,(risorsa,consumo)))in tupla_consumi_energetici:
        if (nomeCitta==citta)and(nomeRisorsa==risorsa):
            if consumo>max:
                max=consumo
                maseA=[mese]
            elif consumo==max:
                meseA.append(mese)
    return (media_risorsa,(max,meseA))
print(analizza_consumi_energetici(tupla_consumi_energetici, nomeCitta, nomeRisorsa))


        