# imports
import random
import time

# fish game
color = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
pattern = ('striped', 'spotted', 'splotched', 'wavy', 'leopard', 'solid')
texture = ('slimey', 'scaley', 'smooth', 'shiny', 'spiked', 'rough')

colorArray = color
patternArray = pattern
textureArray = texture

class Shop:
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots

# Shops
fishMart = Shop('Fish Mart', 3)
luresRUs = Shop('Lures R Us', 6)
captainCo = Shop('Captain Co.', 9)

# Shop Array
shopArray = (fishMart, luresRUs, captainCo)

class Hook:
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(valueMin, valueMax)
        self.color = random.choice(color)
        self.pattern = random.choice(pattern)
        self.texture = random.choice(texture)
        self.ID = f'{self.texture} {self.color} {self.pattern} {self.name}'

# Hooks
spinner = Hook('spinner', 10, 20)
jig = Hook('jig', 20, 30)
treble = Hook('treble hook', 50, 100)
single = Hook('single hook', 25, 75) 
spoon = Hook('spoon', 50, 75)
wooden = Hook('wooden lure', 70, 80)
brass = Hook('brass lure', 90, 100)
spear = Hook('spear', 100, 1000)
harpoon = Hook('harpoon', 1000, 99999)

hookArray = (spinner, jig, treble, single, spoon, wooden, brass, spear, harpoon)

class Fish:
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(valueMin, valueMax)

# Fish
trout = Fish('Trout', 1, 50)
salmon = Fish('Salmon', 5, 130)
walley = Fish('Walley', 1, 20)
burbot = Fish('Burbot', 1, 20)
minnow = Fish('Minnow', 1, 2)
sturgeon = Fish('Sturgeon', 100, 1000)
shark = Fish('Shark', 1000, 10000)
whale = Fish('Whale', 10000, 100000)
marlin = Fish('Marlin', 100, 1000)
whitefish = Fish('Whitefish', 1, 10)
lionfish = Fish('Lionfish', 1, 10)
carp = Fish('Carp', 8, 10)
pike = Fish('Pike', 1, 70)
muskie = Fish('Muskie', 5, 70)

class Other:
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(self.valueMin, self.valueMax)

boot = Other('Boot', 0, 0)
weeds = Other('Weeds', 0, 0)
jewel = Other('Jewel', 25, 50)
line = Other('Old Line', 0, 0)

otherArray = (boot, weeds, jewel, line)

lakeArray = (trout, pike, walley, minnow, burbot, muskie, boot, weeds, jewel, treble, single, spoon, spinner, jig)
oceanArray = (salmon, marlin, lionfish, shark, whale, harpoon, spear)
riverArray = (trout, whitefish, salmon, minnow, pike, sturgeon, muskie, weeds, treble, spoon, jig, brass, wooden)
rapidsArray = (trout, salmon, sturgeon, single, treble)
pondArray = (minnow, carp, boot, weeds, jewel, line, spinner, spoon, jig)

class Location:
    def __init__(self, name, fee, items):
        self.name = name
        self.fee = fee
        self.items = items

lake = Location('lake', 10, lakeArray)
ocean = Location('ocean', 1500, oceanArray)
river = Location('river', 150, riverArray)
rapids = Location('rapids', 250, rapidsArray)
pond = Location('pond', 5, pondArray)

locationArray = [lake, ocean, river, rapids, pond]

def Slots(shop, hook, gold):
    time.sleep(0.5)
    print('\n')
    print(f'Current Shop: {shop.name}\n')
    shopList = []
    counter = 0
    while counter < shop.slots:
        counter += 1
        slotItem = random.choice(hookArray)
        shopList.append(slotItem)
    for item in shopList:
        time.sleep(0.5)
        print(f'{item.ID} (${item.value})')
    print('\n')
    time.sleep(1)
    print(f'Current Gold: (${gold})')
    print('Your current hook:')
    print(f'{hook.ID} ({hook.value} dmg)')
    print('Choose item or leave?\n')

    loop = 'none'
    while loop == 'none':
        choice = input()
        for item in shopList:
            if choice == item.ID:
                if gold > item.value:
                    loop = 'done'
                    oldHook = hook
                    hook = item
                    gold -= hook.value
                    time.sleep(0.5)
                    print(f'You got rid of the: {oldHook.ID}\n')
                    time.sleep(0.5)
                    print(f'You now have the: {hook.ID}\n')
                    time.sleep(0.5)
                    print(f'You now have {gold} gold.\n')
                    time.sleep(0.5)
                    Choose(gold, hook)
                else:
                    loop = 'done'
                    print('You do not have sufficient funds.\n')
                    time.sleep(0.5)
                    Choose(gold, hook)
            elif choice == 'leave':
                loop = 'done'
                Choose(gold, hook)

def Spot(gold, hook):
    print('\n   Fishing Destinations:\n')
    for location in locationArray:
        time.sleep(0.5)
        print(f'{location.name} (${location.fee})')
    time.sleep(1)
    print('\n')
    print(f'Current Gold: (${gold})')
    print('Which do you choose?\n')

    loop = 'none'
    while loop == 'none':
        choice = input()
        for location in locationArray:
            if choice == location.name:
                if gold > location.fee:
                    loop = 'done'
                    destination = location
                    gold -= destination.fee
                    time.sleep(0.5)
                    print(f'You now have {gold} gold.\n')
                    Fishing(destination, gold, hook)
                else:
                    loop = 'done'
                    print('You do not have sufficient funds.\n')
                    time.sleep(0.5)
                    Choose(gold, hook)

def Fishing(location, gold, hook):
    time.sleep(0.5)
    print('\n')
    print(f'Current Fishing Spot: {location.name}\n')
    fish = 'fish'
    while gold > 0 and fish == 'fish':
        outcome = random.choice(location.items)
        if outcome in hookArray:
            time.sleep(0.5)
            print(f'You found a:\n{outcome.ID} ({outcome.value} dmg)\n')
            time.sleep(0.5)
            print(f'Your current hook:\n{hook.ID} ({hook.value} dmg)\n')
            time.sleep(1)
            print('   switch or keep?')
            choice = input()
            if choice == 'switch':
                oldHook = hook
                hook = outcome
        elif outcome in otherArray:
            outcome.value = random.randint(outcome.valueMin, outcome.valueMax)
            print(f'\nYou found: {outcome.name} ({outcome.value} lbs.)')
            gold += outcome.value
            print(f'Your gold: (${gold})')
            time.sleep(1)
            print('   fish or leave?')
            fish = input()
            if fish == 'leave':
                Choose(gold, hook)
        elif hook.value > outcome.value:
            outcome.value = random.randint(outcome.valueMin, outcome.valueMax)
            print(f'\nYou found: {outcome.name} ({outcome.value} lbs.)')
            gold += outcome.value
            print(f'Your gold: (${gold})')
            time.sleep(1)
            print('   fish or leave?')
            fish = input()
            if fish == 'leave':
                Choose(gold, hook)
        else:
            print(f'\nYour {hook.ID} broke from a {outcome.name} ({outcome.value} lbs.)')
            break

def Intro():
    global gold
    gold = 1000
    global hook
    startArray = (jig, spinner)
    hook = random.choice(startArray)
    time.sleep(0.5)
    print('\n---Fishing Adventure!---\n')
    time.sleep(0.5)
    print('   RULES:')
    time.sleep(0.5)
    print('   Earn Money.')
    print('   Find Hooks.')
    print('   Catch Fish.')
    time.sleep(1)
    print('\n')
    print('Your current hook:')
    print(f'{hook.ID} ({hook.value} dmg)')
    time.sleep(1)
    print('\n')

def Choose(gold, hook):
    print('   Choose: fishing or shop')
    loop = 'none'
    while loop == 'none':
        go = input()
        if go == 'shop':
            loop = 'done'
            shop = random.choice(shopArray)
            Slots(shop, hook, gold)
        elif go == 'fishing':
            loop = 'done'
            Spot(gold, hook)
        else:
            loop = 'none'
            print('\nPlease enter a valid response.\n')

def Game():
    Intro()
    Choose(gold, hook)

# Run the game
Game()
