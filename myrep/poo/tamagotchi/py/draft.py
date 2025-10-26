class Tamagotchi:
    def __init__(self, energyMax, cleanMax):
        self.energyMax = energyMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.clean = cleanMax
        self.age = 0
        self.alive = True
        self.death_reason = None  # motivo da morte

    def set_energy(self, value):
        if not self.alive:
            return
        if value <= 0:
            self.energy = 0
            self.alive = False
            self.death_reason = "fraqueza"
        else:
            self.energy = min(value, self.energyMax)

    def set_clean(self, value):
        if not self.alive:
            return
        if value <= 0:
            self.clean = 0
            self.alive = False
            self.death_reason = "sujeira"
        else:
            self.clean = min(value, self.cleanMax)

    def set_age(self, value):
        if not self.alive:
            return
        self.age = value

    def get_energy(self):
        return self.energy

    def get_clean(self):
        return self.clean

    def get_age(self):
        return self.age

    def is_alive(self):
        return self.alive

    def __str__(self):
        return f"E:{self.energy}/{self.energyMax}, L:{self.clean}/{self.cleanMax}, I:{self.age}"

class Game:
    def __init__(self):
        self.pet = None

    def init(self, energy, clean):
        self.pet = Tamagotchi(energy, clean)

    def show(self):
        print(self.pet)

    def play(self):
        if not self.pet.is_alive():
            print("fail: pet esta morto")
            return
        self.pet.set_energy(self.pet.get_energy() - 2)
        self.pet.set_clean(self.pet.get_clean() - 3)
        self.pet.set_age(self.pet.get_age() + 1)
        if not self.pet.is_alive():
            if self.pet.death_reason == "fraqueza":
                print("fail: pet morreu de fraqueza")
            else:
                print("fail: pet morreu de sujeira")

    def shower(self):
        if not self.pet.is_alive():
            print("fail: pet esta morto")
            return
        self.pet.set_energy(self.pet.get_energy() - 3)
        self.pet.set_clean(self.pet.cleanMax)  # limpeza no máximo
        self.pet.set_age(self.pet.get_age() + 2)
        if not self.pet.is_alive():
            if self.pet.death_reason == "fraqueza":
                print("fail: pet morreu de fraqueza")
            else:
                print("fail: pet morreu de sujeira")

    def sleep(self):
        if not self.pet.is_alive():
            print("fail: pet esta morto")
            return
        if self.pet.get_energy() > self.pet.energyMax - 5:
            print("fail: nao esta com sono")
            return
        lost_energy = self.pet.energyMax - self.pet.get_energy()
        self.pet.set_energy(self.pet.energyMax)
        self.pet.set_age(self.pet.get_age() + lost_energy)


# Código principal para ler os comandos:
game = Game()
while True:
    try:
        line = input()
    except EOFError:
        break

    if line == "$end":
        break

    parts = line.split()
    cmd = parts[0]

    if cmd == "$init":
        energy = int(parts[1])
        clean = int(parts[2])
        game.init(energy, clean)
    elif cmd == "$show":
        game.show()
    elif cmd == "$play":
        game.play()
    elif cmd == "$shower":
        game.shower()
    elif cmd == "$sleep":
        game.sleep()

