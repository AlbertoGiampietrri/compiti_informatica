class Entity:
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)

    def move(self, direction, field):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1

        if self.y > field.h:
            self.y -= 1
            print("La creatura non può andare oltre al limite del campo")
        elif self.y < 0:
            self.y += 1
            print("La creatura non può andare oltre al limite del campo")
        if self.x > field.w:
            self.x -= 1
            print("La creatura non può andare oltre al limite del campo")
        elif self.x < 0:
            self.x += 1
            print("La creatura non può andare oltre al limite del campo")
            

class Creatures(Entity):
    def __init__(self, x, y, name, damage, hp, level, field):
        super().__init__(x, y, field)
        self.name = name
        self.damage = damage + damage * (level/10)
        self.hp = hp + hp * (level/10)
        self.level = level

    def info(self):
        print("sono", self.name, "damage:", self.damage, "hp:", self.hp, "level:", self.level, "e mi trovo a", self.x, ",", self.y)

    def attack(self, enemy):
        if self.hp <= 0:
            print(self.name, "prova ad attaccare da morto con scarsi risultati")
        else:
            print(self.name, "attacca", enemy.name)

        if (enemy.hp <= 0):
            print(enemy.name, "e' morto")
        else:
            enemy.hp -= self.damage

class Field:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.entities = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities: 
                    if x == e.x and y == e.y:
                        if x <= self.w and y <= self.h:
                            print("[x]", end = "")
                            break
                else:
                    print("[ ]", end = "")
            print()
    

field = Field()
c1 = Creatures(3, 4, "Pino", 1000, 30, 1, field)
c2 = Creatures(5, 6, "Abete", 1500, 10, 2, field)
c3 = Creatures(7, 8, "Betulla", 300, 20, 3, field)

field.draw()