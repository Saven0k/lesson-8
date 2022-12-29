import teacher
import log
import studies
import security

log.wr("start")

print("Кто вы?:)")
print(("1 - Учитель\n2 - Ученик"))
data = int(input(":  "))

def work(data):
    password = 0
    if data == 1:
        lg = input("Введите свою фамилию: ")
        log.wr2(f"Заходит учитель с фамилией {lg}")
        if lg in security.op():
            ps = security.login_password_teacher[lg]
            password = ' '.join(ps)
        pds = list(input("Введите пароль учителя для проверки: "))
        pd = ''.join(pds)
        if pd == password:
            log.wr2("Учить успешно вошел")
            teacher.teacher(lg)
            print("Хотите продолжить или выйти\n1 - продолжить \n2 - выйти")
            st = int(input(": "))
            if st == 1:
                teacher.teacher(lg)
            elif st == 2:
                print("Кто вы?:)")
                print(("1 - Учитель\n2 - Ученик"))
                data1 = int(input(":  "))
                work(data1)
        else:
            while password != pd:
                ps = security.login_password_teacher[lg]
                password = ' '.join(ps)
                print("неверный пароль введите снова: ")
                log.wr2("Невернеый пароль , производиться новый ввод")
                password = int(input())
            log.wr2(f"Учитель ввел пароль {pd}")
            teacher.teacher(lg)
    elif data == 2:
        scn = input("Фамилия: ")
        studies.studies(scn)
    else:
        print("Error")
        log.wr2("Errror\nEnd")


work(data)