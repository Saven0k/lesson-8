import log
import security
import notebook
import grade
import menu_students
import get_key
def teacher(lg):
    print(
        "Добро пожаловать , какую операцию хотите выбрать\n1 - Записать дз\n2 - Поставь оценки \n3 - Посмотреть какие классы у меня")
    oper = int(input(': '))
    if oper == 1:
        log.wr2("Учить выбрал записать дз")
        pp = int(input("1 - 9 классам\n2 - 10 классам\n3 - 11 классам\n              \nКаким классам: "))
        print(
            'Выберете предмет\n1  - математика \n2 - русский языык\n3 - география\n4 - биология\n5 - химия\n6 - физика\n7 - физ-ра')
        if pp == 1:
            predmet = int(input(": "))
            date = input("Пишите: ")
            notebook.write_9(date, predmet)
            teacher(lg)
        elif pp == 2:
            predmet = int(input(": "))
            date = input("Пишите: ")
            notebook.write_10(date, predmet)
            teacher(lg)
        elif pp == 3:
            predmet = int(input(": "))
            date = input("Пишите: ")
            notebook.write_11(date, predmet)
            teacher(lg)
        else:
            quit()
    elif oper == 2:
        log.wr2("Учить выбрал поставить оценку ")
        bg = []
        pred_nm = int(input(
            'Выберете предмет по которому хотите поставить оценку\n1  - математика \n2 - русский языык\n3 - география\n4 - биология\n5 - химия\n6 - физика\n7 - физ-ра'))
        clas_nm = int(input("Ученику какого класса хотите поставить оценку: "))
        bg.append(get_key.get_key(menu_students.children(), clas_nm))
        name_ch = input("Выберете фамилию ученика, которому будете  ставить оценку: ")
        print('Какую оценку хотите поставить?')
        grades = int((input(": ")))
        grade.write(name_ch, pred_nm, grades)
        print("Хотите продолжить или выйти\n1 - продолжить \n2 - выйти")
        st = int(input(": "))
        if st == 1:
            teacher(lg)
        elif st == 2:
            quit()
    elif oper == 3:
        log.wr2("Учить выбрал посмотреть на его учеников ")
        if lg in security.ap():
            pg = security.teacher_clas[lg]
            classs = ' '.join(pg)
            print(classs)
        print("Хотите продолжить или выйти\n1 - продолжить \n2 - выйти")
        st = int(input(": "))
        if st == 1:
            teacher(lg)
        elif st == 2:
            quit()

    else:
        quit()