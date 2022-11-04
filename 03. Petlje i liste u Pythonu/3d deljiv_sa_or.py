# treba da se proveri da li je broj deljiv ili sa 5 ili sa 23.

broj = int(input("Unesite broj:"))

if broj % 5 == 0 or broj % 23 == 0:
    print(f"{broj} je deljiv sa 5 ili sa 23")
else:
    print(f"{broj} nije deljiv sa 5 ili sa 23")