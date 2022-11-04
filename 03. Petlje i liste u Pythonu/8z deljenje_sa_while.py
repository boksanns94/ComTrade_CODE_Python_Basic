# korisnik unosi dva cela broja ,
# ispisati njihov kolicnik, ako je imenilac jednak 0, naterati korisnika
# da ispravno unese vrednost

prvi = int(input("Unesite prvi broj:"))
# drugi = int(input("Unesite drugi broj:"))

# while drugi == 0:
    # print("Doslo je do greske! Deljenje sa 0 nije definisano!!")
    # drugi = int(input("Unesite opet imenilac!!!"))

#print(f"{prvi} / {drugi} = {prvi/drugi}")
# break  - vas izbacuje iz prve spoljasnje petlje 
# continue  - continue vas vraca na pocetan sledece iteracije
while True:
    drugi = int(input("Unesite imenilac za deljenje:"))
    if drugi != 0: # provera da li je broj validan
        break # ako jeste uz pomoc break-a iskoci iz petlje
        
    #else: else nije obavezan, jer ako se desi da je uslov tacan
# uz pomoc break-a izlazimo iz petlje i sve komande nakon break-a se
# preskacu    
    #continue # zaustavlja trenutno ponavljanje petlje i vraca
    # nazad iteraciju ( ponavljanje ) na pocetak
    print("Los unos,unesite opet broj!")
    print("Kraj jednog ponavljanja petlje")
print("Komanda posle petlje")       
print(f"{prvi} / {drugi} = {prvi/drugi}")
# if 5==5:
    # break
    

