import random


class Tank:
    def __int__(self):
        self.HP = 10
        self.speed = 1
        self.Vector = "w"
        self.pos = (0, 0)

    def run(self, vec):
        if vec == "a" and self.Vector == "a":  # Проверяем направление танка, и если башня повёрнута в сторону заявленного движение, то движимся по соответствующей оси.
            self.pos[0] += (-self.speed)
        elif vec == "d" and self.Vector == "d":
            self.pos[0] += (self.speed)
        elif vec == "s" and self.Vector == "s":
            self.pos[1] += (self.speed)
        elif vec == "w" and self.Vector == "w":
            self.pos[1] += (self.speed)
        self.Vector = vec  # вне зависимости от того движимся мы или нет, мы поворачиваем башню в заявленную сторону

    def atack(self, atc):
        if atc == " ":  # Если введён пробел, то атакуем
            atack = True

    def dead(self):
        if self.HP < 1:
            # Удаляем экземпляр
            pass


class Enemy(Tank):
    def __int__(self):
        self.pos = random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)])

    def run_gen(self):
        vec = random.choice(("a", "w", "s", "d"))
        self.run(vec)

    def atack_pl(self, view):
        if view == "player":
            self.atack(" ")  # Если на линии атаки игрок, то атакуем
