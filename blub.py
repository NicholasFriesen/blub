#imports
import random
import time

#fish game
color = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
pattern = ('striped', 'spotted', 'splotched', 'wavy', 'leopard', 'solid')
texture = ('slimey', 'scaley', 'smooth', 'shiny', 'spiked', 'rough')

colorArray = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
patternArray = ('striped', 'spotted', 'splotched', 'wavy', 'leopard', 'solid')
textureArray = ('slimey', 'scaley', 'smooth', 'shiny', 'spiked', 'rough')


class Shop:
#shop attributes and traits  
                 
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots

#Shops
fishMart = Shop('Fish Mart', 3)
luresRUs = Shop('Lures R Us', 6)
captainCo = Shop('Captain Co.', 9)

#Shop Array
shopArray = (fishMart, luresRUs, captainCo)

class Hook:
#hook attributes and traits  
                 
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(valueMin, valueMax)
        self.color = random.choice(color)
        self.pattern = random.choice(pattern)
        self.texture = random.choice(texture)
        self.ID = str(self.texture) + ' ' + str(self.color) + ' ' + str(self.pattern) + ' ' + str(self.name)

#Hooks
spinner = Hook('spinner', 10, 20)
jig = Hook('jig', 20, 30)
treble = Hook('treble hook', 50, 100)
single = Hook('single hook', 25, 75) 
spoon = Hook('spoon', 50, 75)
wooden = Hook('wooden lure', 70, 80)
brass = Hook('brass lure', 90, 100)
spear = Hook('spear', 100, 1000)
harpoon = Hook('harpoon', 1000, 99999)

#Hook Array
hookArray = (spinner, jig, treble, single, spoon, wooden, brass, spear, harpoon)

class Fish:
#fish attributes and traits  
                 
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(valueMin, valueMax)

#Fish
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
#other attributes and traits  
                 
    def __init__(self, name, valueMin, valueMax):
        self.name = name
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.value = random.randint(self.valueMin, self.valueMax)
#Other
boot = Other('Boot', 0, 0)
weeds = Other('Weeds', 0, 0)
jewel = Other('Jewel', 25, 50)
line = Other('Old Line', 0, 0) 

#Other Array
otherArray = (boot, weeds, jewel, line)

#Location Arrays
lakeArray = (trout, pike, walley, minnow, burbot, muskie, boot, weeds, jewel, treble, single, spoon, spinner, jig)
oceanArray = (salmon, marlin, lionfish, shark, whale, harpoon, spear)
riverArray = (trout, whitefish, salmon, minnow, pike, sturgeon, muskie, weeds, treble, spoon, jig, brass, wooden)
rapidsArray = (trout, salmon, sturgeon, single, treble)
pondArray = (minnow, carp, boot, weeds, jewel, line, spinner, spoon, jig)

class Location:
#location attributes and traits  
                 
    def __init__(self, name, fee, items):
        self.name = name
        self.fee = fee
        self.items = items

#Locations
lake = Location('lake', 10, lakeArray)
ocean = Location('ocean', 1500, oceanArray)
river = Location('river', 150, riverArray)
rapids = Location('rapids', 250, rapidsArray)
pond = Location('pond', 5, pondArray)

#Location Array
locationArray = [lake, ocean, river, rapids, pond]    

def Slots(shop, hook, gold):
    time.sleep(.5)
    print ' '
    print ('Current Shop: ' + shop.name) 
    print ' '
    shopList = []
    counter = 0
    while counter < shop.slots:
        counter = counter + 1
        slotItem = random.choice(hookArray)
        shopList.append(slotItem)
    for item in shopList: 
        time.sleep(.5)
        #item.color = random.choice(color)
        #item.pattern = random.choice(pattern)
        #item.texture = random.choice(texture)
        #item.value = random.randint(item.valueMin, item.valueMax)
        #item.ID = str(item.texture) + ' ' + str(item.color) + ' ' + str(item.pattern) + ' ' + str(item.name)
        print str(item.ID) + '($' + str(item.value) + ')'
    print ' '
    time.sleep(1)
    print ('Current Gold: ($' + str(gold) + ')')
    print ('Your current hook:')
    print (hook.ID + '(' + str(hook.value) + ' dmg)')       
    print ('Choose item or leave?')
    print ' '
    loop = 'none' 
    while loop == 'none':        
        choice = raw_input()
        for item in shopList:
            if choice == item.ID: 
                if gold > item.value:
                    loop = 'done'
                    oldHook = hook
                    hook = item         
                    gold = gold - hook.value 
                    time.sleep(.5)
                    print ('You got rid of the:')
                    print oldHook.ID
                    print ' '
                    time.sleep(.5)
                    print ('You now have the:')
                    print hook.ID
                    print ' '
                    time.sleep(.5)
                    print ('You now have ' + str(gold) + ' gold.')
                    print ' '
                    time.sleep(.5)
                    Choose(gold, hook)
                else:
                    loop = 'done'
                    print ('You do not have sufficient funds.')
                    print ' '
                    time.sleep(.5)
                    Choose(gold, hook)
            elif choice == 'leave':
                loop = 'none'
                Choose(gold, hook)
            else:
                loop = 'none'
                print ' '
            
def Spot(gold, hook):
    print ' ' 
    print ('   Fishing Destinations:')  
    print ' '
    for location in locationArray: 
        time.sleep(.5)
        print str(location.name) + '($' + str(location.fee) + ')'
    time.sleep(1)
    print ' '
    print ('Current Gold: ($' + str(gold) + ')')       
    print ('Which do you choose?')    
    print ' '
    loop = 'none' 
    while loop == 'none':        
        choice = raw_input()
        for location in locationArray:
            if choice == location.name: 
                if gold > location.fee:
                    loop = 'done'                    
                    destination = location
                    gold = gold - destination.fee
                    time.sleep(.5)
                    print ('You now have ' + str(gold) + ' gold.')
                    print ' '
                    Fishing(destination, gold, hook)
                else:
                    loop = 'done'
                    print ('You do not have sufficient funds.')
                    print ' '
                    time.sleep(.5)
                    Choose(gold, hook)
            else:
                loop = 'none'         
    
def Fishing(location, gold, hook):
    time.sleep(.5)
    print ' '
    print ('Current Fishing Spot: ' + location.name) 
    print ' '
    while gold > 0 or fish == 'fish':
       outcome = random.choice(location.items)  
       #outcome.value = random.randint(outcome.valueMin, outcome.valueMax)   
       if outcome in hookArray:
           #outcome.color = random.choice(color)
           #outcome.pattern = random.choice(pattern)
           #outcome.texture = random.choice(texture)
           #outcome.ID = str(outcome.texture) + ' ' + str(outcome.color) + ' ' + str(outcome.pattern) + ' ' + str(outcome.name)
           time.sleep(.5)
           print ('You found a:')
           print (outcome.ID + '(' + str(outcome.value) + ' dmg)')
           time.sleep(.5)
           print ' '
           print ('Your current hook:')
           print (hook.ID + '(' + str(hook.value) + ' dmg)')       
           time.sleep(1)
           print ('   switch or keep?')
           choice = raw_input()
           if choice == 'switch':
               oldHook = hook
               hook = outcome
               location = location   
       elif outcome in otherArray:
           outcome.value = random.randint(outcome.valueMin, outcome.valueMax)   
           print ' '
           time.sleep(.5)
           print ('you found: ' + outcome.name + '(' + str(outcome.value) + ' lbs.)')
           gold = gold + outcome.value
           print ('your gold: ($' + str(gold) + ')')
           time.sleep(1)
           print ('   fish or leave?')
           fish = raw_input()
           outcome = random.choice(location.items)     
           if fish == 'leave':
               Choose(gold, hook)
                      
       elif hook.value > outcome.value:
           outcome.value = random.randint(outcome.valueMin, outcome.valueMax)   
           print ' '
           time.sleep(.5)
           print ('you found: ' + outcome.name + '(' + str(outcome.value) + ' lbs.)')
           gold = gold + outcome.value           
           print ('your gold: ($' + str(gold) + ')')
           time.sleep(1)           
           print ('   fish or leave?')
           fish = raw_input()
           if fish == 'leave':
               Choose(gold, hook)
       else: 
           print ' '
           time.sleep(.5)
           print ('your ' + hook.ID + ' broke from a ' + outcome.name + '(' + str(outcome.value) + 'lbs.)') 
           break  
    
def Intro():
    global gold
    gold = 1000
    global hook
    startArray = (jig, spinner)
    hook = random.choice(startArray)        
    time.sleep(.5)
    print ' '
    print ('---Fishing Adventure!---')
    time.sleep(.5)
    print ' '
    print ('   RULES:')
    time.sleep(.5)
    print ('   Earn Money.')
    print ('   Find Hooks.')
    print ('   Catch Fish.')
    time.sleep(1)
    print ' '

    print ('Your current hook:')
    print (hook.ID + '(' + str(hook.value) + ' dmg)')       
    time.sleep(1)
    print ' '
    
def Choose(gold, hook): 
 
    print ('   Choose: fishing or shop')
    loop = 'none'
    while loop == 'none':
        go = raw_input()
    
        if go == 'shop':
            loop = 'done'
            shop = random.choice(shopArray)
            Slots(shop, hook, gold)  
        elif go == 'fishing':
            loop = 'done'
            Spot(gold, hook)
        else:  
            loop = 'none'
            print ' '
            print ('Please enter a valid response.')      
            print ' '

def Game():
    Intro()
    Choose(gold, hook)

print spinner
print spinner.color
spinner.color = random.choice(color)
print spinner
print spinner.color
spinner.color = random.choice(colorArray)
print spinner
print spinner.color
print jig
print jig.color
test = jig
print test
print test.color
jig.color = random.choice(colorArray)
print jig
print jig.color
test.color = random.choice(colorArray)
print test
print test.color

Game()
