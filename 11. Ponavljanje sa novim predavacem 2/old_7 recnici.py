student = {
    "ime" : "Dusan",
    "prezime" : "Sijacic"
}

print(student)

print(student['ime']) # naziv_recnika[kljuc]
student['ime'] = "Milos"
print(student['ime']) # naziv_recnika[kljuc]
#print(student["index"])

print(student.get('index',0))
print(student)

student['index'] = 52
print(student)

kljucevi = student.keys()
print(kljucevi)
for kljuc in student.keys():
    print(kljuc,student[kljuc])
for x in student: # podrazumevano se prolazi kroz kljuceve
    print(x)
vrednosti = student.values()
print(vrednosti)
for vrednost in student.values():
    print(vrednost)

elementi = student.items()
print(elementi)
for item in student.items():
    print(item)
for kljuc,vrednost in student.items():
    print(kljuc,vrednost)

student.pop("ime")
print(student)

