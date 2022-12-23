import log
import security
import notebook
import menu_teahers
import grade
import menu_students
import base_of_studets
import get_key


log.wr("start")




def work():
    print("Кто вы?:)")
    print(("1 - Учитель\n2 - Ученик"))
    data = int(input(":  "))
    password = 0
    while data != 0:
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
                print("Добро пожаловать , какую операцию хотите выбрать\n1 - Записать дз\n2 - Поставь оценки \n3 - Посмотреть какие классы у меня")
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
                        work()
                    elif pp == 2:
                        predmet = int(input(": "))
                        date = input("Пишите: ")
                        notebook.write_10(date, predmet)
                        work()

                    elif pp == 3:
                        predmet = int(input(": "))
                        date = input("Пишите: ")
                        notebook.write_11(date, predmet)
                        work()
                    else:
                        quit()
                elif oper == 2:
                    log.wr2("Учить выбрал поставить оценку ")
                    bg= []
                    pred_nm = int(input('Выберете предмет по которому хотите поставить оценку\n1  - математика \n2 - русский языык\n3 - география\n4 - биология\n5 - химия\n6 - физика\n7 - физ-ра'))
                    clas_nm = int(input("Ученику какого класса хотите поставить оценку: "))
                    bg.append(get_key.get_key(menu_students.children(), clas_nm))
                    print(bg)
                    name_ch = input("Выберете фамилию ученика, которому будете  ставить оценку: ")
                    print('Какую оценку хотите поставить?')
                    grades = int((input(":")))
                    grade.write(name_ch, pred_nm, grades)


                elif oper == 3:
                    log.wr2("Учить выбрал посмотреть на его учеников ")
                    if lg in security.ap():
                        pg = security.teacher_clas[lg]
                        classs = ' '.join(pg)
                        print(classs)
                else:
                    quit()
                log.wr2(f"Учитель ввел пароль {pd}")
            else:
                print("неверный пароль введите снова: ")
                password = int(input())
                if pd == password:
                    log.wr2("Учитель успешно вошел")
                    print("Добро пожаловать , какую операцию хотите выбрать\n1 - Записать дз\n2 - Поставь оценки \n3 - Посмотреть какие классы у меня")
                    oper = int(input(': '))
                    if oper == 1:
                        log.wr2("Учить выбрал записать дз")
                        pp = int(input("1 - 9 классам\n2 - 10 классам\n3 - 11 классам\n              \nКаким классам: "))
                        print('Выберете предмет\n 1 - математика \n2 - русский языык\n3 - география\n4 - биология\n5 - химия\n6 - физика\n7 - физ-ра')
                        if pp == 1:
                            predmet = input(": ")
                            date = input("Пишите: ")
                            notebook.write_9(date , predmet)
                            continue
                        elif pp == 2:
                            predmet = input(": ")
                            date = input("Пишите: ")
                            notebook.write_10(date, predmet)
                            continue
                        elif pp == 3:
                            predmet = input(": ")
                            date = input("Пишите: ")
                            notebook.write_11(date, predmet)
                            work()
                        else:
                            quit()
                    elif oper == 2:
                        log.wr2("Учить выбрал поставить оценку ")
                        bg = []
                        pred_nm = int(input(
                            'Выберете предмет по которому хотите поставить оценку\n1  - математика \n2 - русский языык\n3 - география\n4 - биология\n5 - химия\n6 - физика\n7 - физ-ра'))
                        clas_nm = int(input("Ученику какого класса хотите поставить оценку"))
                        for i in base_of_studets.base_sc_clas:
                            if clas_nm in base_of_studets.base_sc_clas:
                                bg.append(base_of_studets.base_sc_clas[clas_nm])
                        print(*bg)
                        name_ch = input("Выберете фамилиө ученика, которому будете  ставить оценку: ")
                        if name_ch in bg:
                            print('Какую оценку хотите поставить?')
                            grades = int((input(":")))
                        grade.write(name_ch, clas_nm, pred_nm, grades)

                    elif oper == 3:
                        log.wr2("Учить выбрал посмотреть на его учеников ")
                        if lg in security.ap():
                            pg = security.teacher_clas[lg]
                            classs = ' '.join(pg)
                            print(classs)
                    else:
                        quit()
                    log.wr2(f"Учитель ввел пароль {pd}")

        elif data == 2:
            scn = input("Фамилия: ")

            if scn in menu_students.children():
                log.wr2(f"Фамилия ученика {scn}")
                clas = input("В каком ты классе: ")

                if clas == menu_students.chil_class[scn]:
                    log.wr2(f"Заходит ученик {clas} класса")
                    print('Выбери нужную операцию')

                    print('1 - Посмотреть дз\n2 - Посмотреть оценки')

                    mn = int(input(': '))
                    if mn == 1:
                        log.wr2(f"Ученик хочет посмотреть дз")

                        if int(clas) == 9:
                            print(notebook.read_9())

                        elif int(clas) == 10:
                            print(notebook.read_10())

                        elif int(clas) == 11:
                            print(notebook.read_11())

                    elif mn == 2:
                        log.wr2(f"Ученик хочет посмотреть оценки")
                        print(grade.read(scn))
                    else:
                        quit()

                quit()

            else:
                quit()

        elif data == 0:
            data = 0
            quit()

            log.wr2('end')



work()
log.wr2("end")
