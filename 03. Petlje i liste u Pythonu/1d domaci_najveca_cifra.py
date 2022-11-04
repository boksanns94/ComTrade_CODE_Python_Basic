# korisnik unosi neki trocifreni broj,
# ispisati njegovu najvecu cifru 

broj = int(input("Unesite broj:"))

if broj < 100 or broj > 999:
    print("Los unos broja,unesite trocifren")
    exit()
    
# 123 : 10 = 12 (3)
# 12  : 10 = 1  (2)
# 1   : 10 = 0  (1)

jedinice = broj % 10
desetice = broj // 10 % 10
stotine = broj // 10 // 10 % 10
print(f"Jedinice:{jedinice},desetice:{desetice},stotine:{stotine}")

if jedinice > desetice and jedinice > stotine:
    print(f"Najveci je {jedinice}")

elif desetice > stotine:
    print(f"Najveci je {desetice}")
    
else:
    print(f"Najveci je {stotine}")
    

trenutni_maksimum = jedinice # privremena promenljiva koja je proglasena
# za trenutni maksimum 
# nakon toga proveravamo za svaki od brojeva,
# da li je veci od trenutnog maksimuma ako jeste
#
if desetice > trenutni_maksimum:
    trenutni_maksimum = desetice # menjamo trenutni maksimum na tu vrednost

if stotine > trenutni_maksimum:
    trenutni_maksimum = stotine
    
print(f"Najveca cifra je {trenutni_maksimum}")


