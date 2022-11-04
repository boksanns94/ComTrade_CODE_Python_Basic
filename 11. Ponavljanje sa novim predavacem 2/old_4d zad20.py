def izbaci_duplikate(brojevi):
    # [1,1,1,2,3,4,3,3,4] -> [1,2,3,4]
    resenje = []
    for broj in brojevi:
        if broj not in resenje:
            resenje.append(broj)
    return resenje
brojevi = [1,1,1,2,3,4,3,3,4]
print(izbaci_duplikate(brojevi))

# setovi- odnosno skupovi predstavljaju kolekciju koja ne dozvoljava ponavljanje u sebi
skup = {1,2,3,4,2,2,2,2,2} # 
# postoje dva nacina da se deklarise skup
skup = {}
skup = set([1,2,3,3,3,3])
print(skup)
