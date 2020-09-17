import random


class Bcolors:
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    actions = ["Attack", "Magic", "Items"]

    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name

        self.itemname = []
        self.type1 = []
        self.description = []
        self.prop = []
        self.quantity = []
        for i in items:
            self.itemname.append(i.name)
            self.type1.append(i.type1)
            self.description.append(i.description)
            self.prop.append(i.prop)
            self.quantity.append(i.quantity)

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + self.name, "\n\tACTION:" + Bcolors.ENDC)
        i = 1
        for item in self.actions:
            print("     " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        print("\n\t\t" + Bcolors.OKBLUE + Bcolors.BOLD + "MAGIC:" + Bcolors.ENDC)
        i = 1
        for spell in self.magic:
            #if spell.type == "white":
            print("\t\t" + str(i) + ":", spell.name, ":  " + str(spell.dmg) + "( Cost:", str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        print("\n\t\t" + Bcolors.OKBLUE + Bcolors.BOLD + "ITEMS:" + Bcolors.ENDC)
        i = 1
        for items in self.items:
            print("\t\t" + str(i), ":", items.name, "{", items.description, "}" + " (x" + str(self.quantity[i-1]) + ")")
            i += 1

    def reduce_quantity(self, item_choice):
        self.quantity[item_choice] -= 1

    def get_stats(self):

        spacehp = 10
        long = len(str(self.hp)) + len(str(self.maxhp))
        spacehp -= long
        block1 = self.hp / self.maxhp

        spacemp = 5
        long = len(str(self.mp)) + len(str(self.maxmp))
        spacemp -= long
        block2 = self.mp / self.maxmp

        if self.maxhp == 40000:
            block1 = int(50 * block1)
            block2 = int(20 * block2)
            hp_block = "█" * block1 + " " * (50 - block1)
            mp_block = "█" * block2 + " " * (20 - block2)
            print("                     __________________________________________________          "
                  "  ____________________")
            print(Bcolors.BOLD + self.name + " " * spacehp, str(self.hp) + "/" + str(self.maxhp) + " |" + Bcolors.FAIL +
                  hp_block + Bcolors.ENDC + Bcolors.BOLD + "|  " + " " * spacemp + str(self.mp) + "/" + str(self.maxmp)
                  + " |" + Bcolors.OKBLUE + mp_block + Bcolors.ENDC + Bcolors.BOLD + "|" + Bcolors.ENDC)
            return

        block1 = int(block1 * 25)
        block2 = int(block2 * 10)
        hp_block = "█" * block1 + " " * (25 - block1)
        mp_block = "█" * block2 + " " * (10 - block2)
        print("                     _________________________            __________")
        print(Bcolors.BOLD + self.name + " " * spacehp, str(self.hp) + "/" + str(self.maxhp) + " |" + Bcolors.OKGREEN +
              hp_block + Bcolors.ENDC + Bcolors.BOLD + "|  " + " " * spacemp + str(self.mp) + "/" + str(self.maxmp)
              + " |" + Bcolors.OKBLUE + mp_block + Bcolors.ENDC + Bcolors.BOLD + "|" + Bcolors.ENDC)
