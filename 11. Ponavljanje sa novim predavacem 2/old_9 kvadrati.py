# napraviti recnik u kome su brojevi od 0 do 10 kljucevi a vrednosti su njihvoi kvadrati


def main():
    kvadrati = {}
    for i in range(11):
        kvadrati[i] = i**2
    print(kvadrati)

    kubovi = {i:i**3 for i in range(11)}
    print(kubovi)
if __name__ == "__main__":
    main()