import log
import notebook
import grade
import menu_students
def studies(scn):
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
