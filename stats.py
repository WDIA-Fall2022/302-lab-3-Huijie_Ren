import pylightxl as xl
from collections import OrderedDict

with open('students.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=15)[1:])

d ={}
for el in l:
    EL = el.upper()
    if EL in d:
        d[EL]=d[EL]+1
    else:
        d[EL]=1


l1=list(db.ws(ws='Sheet1').col(col=16)[1:])
nInternational = 0
for el in l1:
    if el == 'Y':
        nInternational += 1
print("{} International Students".format(nInternational))

l1=list(db.ws(ws='Sheet1').col(col=5)[1:])
nFemales = 0
nStudents = len(l1)

for el in l1:
    if el == 'Female':
        nFemales += 1
print("{} Female Students".format(nFemales))
print("{} Male Students".format(nStudents - nFemales))


d1 = dict(sorted(d.items(), key=lambda item: item[1]))
print("{:<18} | {:>15}".format("COUNTRY","STUDENTS"))
print("-"*36)
for k,v in d1.items():
    print("{:<18} {:>15}".format(k,v))

