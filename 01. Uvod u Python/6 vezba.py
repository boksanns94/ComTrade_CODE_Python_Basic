#1. Korisnik unosi poluprecnik kruga kao decimalan broj
# izracunati obim i povrsinu kruga.
# i ispisati poruke u formatu: Obim kruga: _____
# Povrsina: _____
poluprecnik_kruga = float(input("Unesite poluprecnik:"))

obim = 2 * poluprecnik_kruga * 3.14
povrsina = poluprecnik_kruga ** 2 * 3.14
print("Obim:",obim)
print("Povrsina:",povrsina)

# 2. Korisnik unosi neki ceo broj sekundi, konvertovati te sekunde
# u format broj minuta : broj_sekundi
# 400 -> 6min 40sec
# 400 // 60 = 6
# 400 %  60 = 40
ukupno_sekundi = int(input("Unesite broj sekundi:"))
minuti = ukupno_sekundi // 60 # 
sekunde = ukupno_sekundi % 60
print(minuti,"min",sekunde,"sec")