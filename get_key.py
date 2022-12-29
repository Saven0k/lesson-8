import log


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    log.wr2("Взят ключ")