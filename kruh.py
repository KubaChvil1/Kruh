'''
Program pro vypocet obvodu a obsahu kruhu se vstupem z klavesnice uzivatele
Vytvoril Jakub Chvilicek v roce 2024
'''

while True:
    try:
        polomer = float(input("Zadejte poloměr kruhu: ")) #uzivatel zada vstup - polomer kruhu, ktery se ulozi jako float

        obvod = 2 * polomer * 3.1415926 #vypocet obvodu
        obsah = 3.1415926 * polomer ** 2 #vypocet obsahu

        print("Obvod kruhu s poloměrem " + str(polomer) + " je " + str(obvod) + " a jeho obsah je " + str(obsah) + ".") #vypis informaci o kruhu (polomer, obvod, obsah)

    except ValueError:
        print("Neplatná hodnota poloměru!") #kdyz zadam string
    except:
        print("Neznámá chyba!") #kdyz dostanu jinou chybu
    
    

    