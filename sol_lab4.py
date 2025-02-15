
list = ['Alex' , ['SkyN11', 'TestNet4', 'TestNet6'],
        'Bob'  , ['SuperM', 'TestNet6'],
        'ANN'  , ['Global13'],
        'Elena', ['Area5', 'TestNet4', 'Global13'],
        'sam'  , ['superm', 'skyn11', 'testNet4'] ]

n = len(list) // 2
names = [ str.capitalize(x) for x in list[0::2] ]
#print(names)

projects = list[1::2]
for i in range(n):
    projects[i] = [ str.lower(x) for x in projects[i] ]
#print(projects)

# Найти сотрудников, которые работают только в двух проектах
list2 = [ names[i] for i in range(n) if len(projects[i])==2 ]
print(list2)

# Список оригинальных проектов
originProj = []
for i in range(n):
    for x in projects[i]:
        if x not in originProj: originProj.append(x)
#print(originProj)

# Список-списков ( имя проекта, список сотрудников )
listProj = [ [x,[]] for x in originProj ]
#print(listProj)

# Добавляем имена сотрудников
for x in listProj:
    for i in range(n):
        if x[0] in projects[i]: x[1].append(names[i])

for item in listProj: print(item)

