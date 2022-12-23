import log



def write_9(date , n):
    with open('notebook-9.txt', 'a') as f:
        if n == 1:
            f.write(f'Математика:  {date}')
            log.wr2(f"учитель записывает дз по математка")
           #Math
        elif n == 2:
            f.write(f'Русский язык:  {date}')
            log.wr2(f"учитель записывает дз по русский язык")
                    #russia
        elif n == 3:
            f.write(f'География:  {date}')
            log.wr2(f"учитель записывает дз по география")
                    #geogaph
        elif n == 4:
             f.write(f'Биология :  {date}')
             log.wr2(f"учитель записывает дз по биология")
                    #biology
        elif n == 5:
            f.write(f'Химия:  {date}')
            log.wr2(f"учитель записывает дз по химия")
                    #pimia
        elif n == 6:
             f.write(f'Физика:  {date}')
             log.wr2(f"учитель записывает дз по физике")
                    #hizik
        elif n == 7:
            f.write(f'Физ-ра:  {date}')
            log.wr2(f"учитель записывает дз по физре")






def write_10(date , n):
    with open('notebook-10.txt', 'a') as f:
        if n == 1:
            f.write(f'Математика:  {date}')
            log.wr2(f"учитель записывает дз по Математика")
                    # Math
        elif n == 2:
            f.write(f'Русский язык:  {date}')
            log.wr2(f"учитель записывает дз по Русский язык")
                    # russia
        elif n == 3:
            f.write(f'География:  {date}')
            log.wr2(f"учитель записывает дз по География")
                    # geogaph
        elif n == 4:
            f.write(f'Биология:  {date}')
            log.wr2(f"учитель записывает дз по Биология")
                    # biology
        elif n == 5:
            f.write(f'Химия:  {date}')
            log.wr2(f"учитель записывает дз по Химия")
                    # pimia
        elif n == 6:
            f.write(f'Физика:  {date}')
            log.wr2(f"учитель записывает дз по Физика")
                    # hizik
        elif n == 7:
            f.write(f'Физ-ра:  {date}')
            log.wr2(f"учитель записывает дз по физре")
                    # iz-ra




def write_11(date , n):
    with open('notebook-11.txt', 'a') as f:
        if n == 1:
           f.write(f'Математика:  {date}')
           log.wr2(f"учитель записывает дз по Математика")
                # Math
        elif n == 2:
            f.write(f'Русский язык: {date}')
            log.wr2(f"учитель записывает дз по Русский язык")
                # russia
        elif n == 3:
            f.write(f'География: {date}')
            log.wr2(f"учитель записывает дз по География")
                # geogaph
        elif n == 4:
            f.write(f'Биология: {date}')
            log.wr2(f"учитель записывает дз по Биология")
                # biology
        elif n == 5:
            f.write(f'Химия: {date}')
            log.wr2(f"учитель записывает дз по Химия")
                # pimia
        elif n == 6:
            f.write(f'Физика: {date}')
            log.wr2(f"учитель записывает дз по Физика")
                # hizik
        elif n == 7:
            f.write(f'Физ-ра: {date}')
            log.wr2(f"учитель записывает дз по физре")
                # iz-ra




def read_9():
    with open('notebook-9.txt', 'r') as f:
        data = ''.join(f.read())
        log.wr2(f"прочитано дз 9 класса")
        return data

def read_10():
    with open('notebook-10.txt', 'r') as f:
        data = ''.join(f.read())
        log.wr2(f"прочитано дз 10 класса")
        return data

def read_11():
    with open('notebook-11.txt', 'r') as f:
        data = ''.join(f.read())
        log.wr2(f"прочитано дз 11 класса")
        return data


