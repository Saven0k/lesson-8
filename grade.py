import log
def write(sc ,predmet , gr):
    with open('ggrade.txt', 'a' , encoding="utf-8") as f:
        f.write(f"{sc} {predmet} {gr}\n")
        log.wr2("Учитель сделал запись")

grades = {}
def read(sc):
    with open('ggrade.txt', 'r' , encoding="utf-8") as f:
        data = str(f.read()).splitlines()
        for line in data:
            f1 = line.split()
            grades[f'{f1[0]}'] = [f1[2]]
        if sc in grades:
            return grades[sc]
        log.wr2("Оценки были прочитаны")


