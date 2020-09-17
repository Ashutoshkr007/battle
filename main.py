from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.Inventory import Item
import random

# player options
option = ['1', '2', '3']
option1 = ['1', '2', '3', '4', '5', '6']
option2 = ['1', '2', '3', '4', '5', '6', '7']
# These are Black magic

fire = Spell("Fire", 17, 700, "Dark")
thunder = Spell("Thunder", 22, 850, "Dark")
blizzard = Spell("Blizzard", 20, 800, "Dark")
meteor = Spell("Meteor", 30, 1200, "Dark")
quake = Spell("Quake", 14, 440, "Dark")

# white spell

cure = Spell("Cure", 12, 750, "white")
cura = Spell("Cura", 18, 1500, "white")

# Create some Items
potion = Item("potion", "potion", "Heals 50 HP", 50, 15)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100, 5)
superpotion = Item("Super potion", "potion", "Heals 500 HP", 500, 2)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999, 1)
megaelixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of whole party", 9999, 1)
grenade = Item("Grenade", "attack", "Deals 3000 damage", 3000, 1)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, megaelixer, grenade]

enemy_spell = [cure, cura]
# Instantiate peoples

player1 = Person("Bot1  :", 4600, 165, 130, 34, player_spells, player_items)
player2 = Person("Bot2  :", 3060, 175, 100, 34, player_spells, player_items)
player3 = Person("Bot3  :", 3710, 165, 120, 34, player_spells, player_items)
enemy = Person("Enemy :", 40000, 365, 350, 525, enemy_spell, [])

players = [player1, player2, player3]

running = True

while running:
    print("================================")
    print(Bcolors.BOLD + "Name                 HP                                 MP")

    for player in players:
        player.get_stats()
    enemy.get_stats()

    for player in players:
        player.choose_action()
        choice = input("\tChoose an action: ")
        if choice not in option:
            print(Bcolors.FAIL + Bcolors.BOLD + "Never do that again and you loose your chance\n\t " + Bcolors.ENDC)
            continue
        index = int(choice) - 1

        if index >= 3:
            print(Bcolors.FAIL + Bcolors.BOLD + "Never do that again and you loose your chance\n\t " + Bcolors.ENDC)
            continue
# For attack
        elif index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(Bcolors.BOLD + Bcolors.WARNING + "You attacked for", dmg, "points of damage" + Bcolors.ENDC)
# For spells
        elif index == 1:
            player.choose_magic()
            magic_choice = input("\t\tChoose spell: ")
            if magic_choice not in option1:
                print(Bcolors.FAIL + Bcolors.BOLD + "Never do that again and you loose your chance")
                continue
            magic_choice = int(magic_choice) - 1
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\n Not enough MP!\n" + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " heals for"
                      , magic_dmg, "points " + Bcolors.ENDC)

            elif spell.type == "Dark":
                enemy.take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals", magic_dmg,
                      "points of damage" + Bcolors.ENDC)
# Items
        elif index == 2:
            player.choose_items()
            item_choose = input("\t\tChoose Item: ")

            if item_choose not in option2:
                print(Bcolors.FAIL + Bcolors.BOLD + "Never do that again and you loose your chance")
                continue

            item_choose = int(item_choose) - 1
            if item_choose == -1:
                continue
            elif item_choose > 5:
                print(Bcolors.FAIL + Bcolors.BOLD + "Never do that again and you loose your chance")
                continue
            item = player.items[item_choose]
# potion items
            if player.type1[item_choose] == 'potion':

                if player.quantity[item_choose] == 0:
                    print(Bcolors.BOLD + Bcolors.FAIL + "\n" + player.itemname[item_choose] + ", None left....")
                    continue

                player.heal(item.prop)
                player.reduce_quantity(item_choose)
                print(Bcolors.OKGREEN + "\n" + player.itemname[item_choose] + " heals for", player.prop[item_choose], Bcolors.ENDC)
# Elixer items
            elif player.type1[item_choose] == 'elixer':

                if player.quantity[item_choose] == 0:
                    print(Bcolors.BOLD + Bcolors.FAIL + "\n" + player.itemname[item_choose] + " is out of stock")
                    continue
                elif player.itemname[item_choose] == 'MegaElixer':
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(Bcolors.BOLD + "Name                 HP                                 MP")
                        i.get_stats()
                        continue

                player.mp = player.maxmp
                player.hp = player.maxhp
                player.reduce_quantity(item_choose)
                print(Bcolors.OKBLUE + "\n", player.itemname[item_choose] + " has fully restored your MP/HP" + Bcolors.ENDC)
# Attack items
            elif player.type1[item_choose] == 'attack':

                if player.quantity[item_choose] == 0:
                    print(Bcolors.BOLD + Bcolors.FAIL + "\n" + player.itemname[item_choose] + " is out of stock" +
                          Bcolors.ENDC)
                    continue

                enemy.take_damage(item.prop)
                player.reduce_quantity(item_choose)
                print(Bcolors.FAIL + "\n" + player.itemname[item_choose] + " deals", player.prop[item_choose],
                      " amounts of damage" + Bcolors.ENDC)
# check if enemy is alive
        if enemy.get_hp() == 0:
            print(Bcolors.OKGREEN + "You win" + Bcolors.ENDC)
            running = False
            break
# Enemy chance
        enemy_choice = random.randint(0, 1)

        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            player.take_damage(enemy_dmg)
            print(Bcolors.WARNING + Bcolors.BOLD + "Enemy attacked for", enemy_dmg, "points\n" + Bcolors.ENDC)
            print(Bcolors.BOLD + "Name                 HP                                 MP")
            player.get_stats()
            enemy.get_stats()

        elif enemy_choice == 1:
            magic_choice = random.randint(0, 1)
            spell = enemy.magic[magic_choice]
            enemy.heal(spell.dmg)
            enemy.mp -= spell.cost
            print(Bcolors.BOLD + Bcolors.FAIL + "Enemy heals for" , spell.dmg, "by spell", spell.name, Bcolors.ENDC)
        if player.get_hp() == 0:
            print(Bcolors.FAIL + "Your enemy has defeated you!" + Bcolors.ENDC)
            players.remove(player)

        elif len(players) == 0:
            print(Bcolors.BOLD + Bcolors.FAIL + "All of the party members are dead!\n\t Game Over" + Bcolors.ENDC)
            running = False
