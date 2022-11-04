tekst='''John,Doe,120 jefferson st.,Riverside, NJ, 08075
        Jack,McGinnis,220 hobo Av.,Phila, PA,09119
        "John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
        Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
        Dusan,Blankman,,SomeTown, SD, 00298
"Joan ""the bone"", Anne",Jet,"9th, at Terrace plc",Desert City,CO,00123
        '''
print(tekst)

redovi = tekst.split("\n")
print(redovi)

imena = []
for red in redovi:
    delovi_reda = red.split(',')
    print(delovi_reda[0])
    delovi_reda[0] = delovi_reda[0].strip()
    imena.append(delovi_reda[0])

rec = "            test           "
rec=rec.strip()
print(len(rec))

print(imena)
poslednja_kolona = [red.split(',')[-1] for red in tekst.split('\n')]
print(poslednja_kolona)