class Hora:
    def __init__(self, h=0, m=0, s=0):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0
        self.set_hora(h)
        self.set_min(m)
        self.set_seg(s)

    def set_hora(self, value):
        if 0 <= value <= 23:
            self.__hora = value
        else:
            print("fail: hora invalida")
        return self

    def set_min(self, value):
        if 0 <= value <= 59:
            self.__min = value
        else:
            print("fail: minuto invalido")
        return self

    def set_seg(self, value):
        if 0 <= value <= 59:
            self.__seg = value
        else:
            print("fail: segundo invalido")
        return self

    def __str__(self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}"

    def next_second(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0
        return self


def main():
    relogio = Hora()

    while True:
        line = input()
        if not line:
            continue

        cmd = line.split()
        op = cmd[0]

        if op == "end":
            print("$end")
            break
        elif op == "show":
            print("$show")
            print(relogio)
        elif op == "set":
            h, m, s = int(cmd[1]), int(cmd[2]), int(cmd[3])
            print(f"$set {h:02d} {m:02d} {s:02d}")
            relogio.set_hora(h)
            relogio.set_min(m)
            relogio.set_seg(s)
        elif op == "init":
            h, m, s = int(cmd[1]), int(cmd[2]), int(cmd[3])
            print(f"$init {h:02d} {m:02d} {s:02d}")
            relogio = Hora()
            relogio.set_hora(h)
            relogio.set_min(m)
            relogio.set_seg(s)
        elif op == "next":
            print("$next")
            relogio.next_second()


if __name__ == "__main__":
    main()