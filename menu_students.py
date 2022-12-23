import log
chil_class = {}
def children():
    with open('base_of_students.txt', 'r' , encoding="utf-8") as f:
        data = str(f.read()).splitlines()
        log.wr2("Сформировалась  база учеников")
        for line in data:
            f1 = line.split()
            chil_class[f1[1]] = f1[2]
        return chil_class
children()







