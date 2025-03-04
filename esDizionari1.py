dizionario={
    "Mario Rossi":[("Antipasti",(8,7,9),"Junior Chef"),("Primi",(7,8,9),"Junior Chef"), ("Secondi",(9,9,8),"Junior Chef"),("Dessert",(8,8,9),"Junior Chef"),],
    "Luigi Bianchi":[("Antipasti",(7,7,8),"Senior Chef"),("Primi",(8,9,7),"Senior Chef"),("Secondi",(7,8,7),"Senior Chef"),("Dessert",(9,8,8),"Senior Chef")],
    "Giulia Verdi":[("Antipasti",(9,8,8),"Junior Chef"),("Primi",(8,7,9),"Junior Chef"),("Secondi",(8,8,8),"Junior Chef"),("Dessert",(7,9,8),"Junior Chef")],
    "Nicole Tuzzeo":[("Antipasti",(5,6,7),"Junior Chef"),("Primi",(0,1,0),"Junior Chef"),("Secondi",(8,3,4),"Junior Chef"),("Dessert",(7,6,8),"Junior Chef")]

}
import random
def aggiuntaCategoria():
    for chiavi, valori in dizionario.items():
        for valore in valori:
            piatto,punti, categoria=valore
            n1=random.randint(1,10)
            n2=random.randint(1,10)
            n3=random.randint(1,10)
            list=[]
            if categoria=="Junior Chef":
                list.append(("Piatti unici",(n1,n2,n3),"Junior Chef"))
            else:
                list.append(("Piatti unici",(n1,n2,n3),"Junior Chef"))
    dizionario[chiavi].append(list)
    print(f"punto3: \n {dizionario}")
aggiuntaCategoria()
print(dizionario)
    
def stampaDati(nome):
    for chiavi, valori in dizionario.items():
       for valore in valori:
            piatto,(creativita,gusto,presentazione),categoria=valore
            if nome==chiavi:
                print(f"Categoria di Chef:{categoria}")
                print(f"nome e cognome: {nome}")
                print("piatto: {piatto}")
                print(f"pnteggi:")
                print(creativita)
                print(gusto)
                print(presentazione)
while True:
    nome=input("inserisci il nome: ")
    if (nome=="Mario Rossi" or nome=="Luigi Bianchi" or nome=="Giulia Verdi" or nome=="Nicole Tuzzeo"):  
        stampaDati(nome)
        break
    else:
        print(f"errore")

def stampaPiatti(categoriaPiatto):
     for chiavi, valori in dizionario.items():
        for valore in valori:
            piatto,(creativita,gusto,presentazione),categoria=valore
            if categoriaPiatto==piatto:
                print(f"Categoria di Chef:{categoria}")
                print(f"nome e cognome: {chiavi}")
                print(f"pnteggi:")
                print(creativita)
                print(gusto)
                print(presentazione)
while True:
    categoriaPiatto=input("inserisci la categoria paitto: ")
    if (categoriaPiatto=="Primi"or categoriaPiatto=="Secondi" or categoriaPiatto=="Dessert" or categoriaPiatto=="Dessert"or categoriaPiatto=="Antipasti" or categoriaPiatto=="Piatti unici"):  
        stampaPiatti(categoriaPiatto)
        break
    else:
        print(f"errore")

def totale(dizionario,categoriaPiatto2, categoriaChef):
    totali=[]
    for chiavi, valori in dizionario.items():
       for valore in valori:
            piatto,(creativita,gusto,presentazione),categoria=valore
            if (categoriaPiatto2==piatto and categoriaChef==categoria):    
                totale=creativita+gusto+presentazione
                totali.append(totale)
    maxtotale=max(totali)
    print(f"totale massimo{maxtotale}")

while True:
    categoriaPiatto2=input("inserisci la categoria paitto: ")
    categoriaChef=input("insrisci la categoria dello chef: ")
    if (categoriaPiatto2=="Primi"or categoriaPiatto2=="Secondi" or categoriaPiatto2=="Dessert" or categoriaPiatto2=="Dessert"or categoriaPiatto2=="Antipasti" or categoriaPiatto2=="Piatti unici")and(categoriaChef=="Junior Chef" or categoriaChef=="Senior Chef"):  
        totale(dizionario,categoriaPiatto2, categoriaChef)
        break
    else:
        print(f"errore")

def mediaPunteggiTot(dizionario,categoriaPiatto3, categoriaChef2):
    for chiavi, valori in dizionario.items():
       for valore in valori:
            piatto,(creativita,gusto,presentazione),categoria=valore
            if (categoriaPiatto3==piatto and categoriaChef2==categoria):
                totale=creativita+gusto+presentazione
    media=totale/len(dizionario)
    print(media)


while True:
    categoriaPiatto=input("inserisci la categoria paitto: ")
    categoriaChef2=input("insrisci la categoria dello chef: ")
    if (categoriaPiatto3=="Primi"or categoriaPiatto3=="Secondi" or categoriaPiatto3=="Dessert" or categoriaPiatto3=="Dessert"or categoriaPiatto3=="Antipasti" or categoriaPiatto3=="Piatti unici")and(categoriaChef2=="Junior Chef" or categoriaChef2=="Senior Chef"):  
        mediaPunteggiTot(dizionario,categoriaPiatto3, categoriaChef2)
        break
    else:
        print(f"errore")
           
           



