import log

base_sc_clas = {}

def read_base():
    with open('base_of_students.txt' , 'r', encoding="utf-8") as f:
        data = str(f.read()).splitlines()
        log.wr2(f"база прочтена учеников")
        for line in data:
            f1 = line.split()
            base_sc_clas[f'{f1[1]}'] = [f1[2]]
        return base_sc_clas

print(read_base())