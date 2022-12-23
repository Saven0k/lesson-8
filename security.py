
import log

teacher_clas = {}
login_password_teacher = {}

def op():
    with open('base_of_teacher.txt', 'r',  encoding="utf-8") as f:
        data = str(f.read()).splitlines()
        log.wr2(f"база прочтена под пароль")
        for line in data:
            f1 = line.split()
            login_password_teacher[f'{f1[0]}'] = [f1[1]]
        return login_password_teacher
op()

def ap():
    with open('base_of_teacher.txt', 'r',  encoding="utf-8") as f:
        data = str(f.read()).splitlines()
        log.wr2(f"База под классы прочтена")
        for line in data:
            f2 = line.split()
            teacher_clas[f'{f2[0]}'] = [f'{f2[2]}', f'{f2[3]}', f'{f2[4]}']


        log.wr2(f"классы у учителя")
        return teacher_clas

ap()

