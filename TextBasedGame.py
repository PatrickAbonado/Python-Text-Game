# Patrick Abonado


# dictionary for rooms and directions
rooms = {
    'MOUNT MAUNA LOA': {'place': 'MOUNT MAUNA LOA', 'south': 'OYMYAKON',
                        'east': 'MOUNT WASHINGTON'},
    'MOUNT WASHINGTON': {'place': 'MOUNT WASHINGTON', 'west': 'MOUNT MAUNA LOA'},
    'OYMYAKON': {'place': 'OYMYAKON', 'west': 'BEDROOM', 'east': "CAMELOT",
                 'north': 'MOUNT MAUNA LOA', 'south': 'MOUNT EVEREST'},
    'BEDROOM': {'place': 'BEDROOM', 'east': 'OYMYAKON'},
    'MOUNT EVEREST': {'place': 'MOUNT EVEREST', 'north': 'OYMYAKON',
                      'east': 'MARIANA TRENCH'},
    "CAMELOT": {'place': "CAMELOT", 'west': 'OYMYAKON',
                'north': 'BURJ KHALIFA'},
    'BURJ KHALIFA': {'place': 'BURJ KHALIFA', 'south': "CAMELOT"},
    'MARIANA TRENCH': {'place': 'MARIANA TRENCH', 'west': 'MOUNT EVEREST'}
}

# list of directions
directions = ['north', 'south', 'east', 'west']


# list items needed to win game
hydra_key = ['WATER GEM', 'EARTH GEM', 'FIRE GEM', 'WIND GEM',
             'DIAMOND SWORD', 'PLANET SHIELD']

# list of collected items
inventory = []

# start location
location = rooms['BEDROOM']


# introduction
def intro_play():
    print()
    print('***************  ATTACK OF THE HYDRA!  ***************')
    print()
    print('THE HYDRA IS ATTACKING BURJ KHALIFA! YOU MUST GO ON A JOURNEY TO ')
    print('COLLECT THE ELEMENT GEMS, THE PLANET SHIELD, AND THE DIAMOND SWORD ')
    print('IN ORDER TO SLAY THE HYDRA!')


# invalid entry response
def invalid_response():
    print()
    print('NOT A POSSIBLE CHOICE.  PLEASE CHOOSE AGAIN.')


# reject add-item response
def not_accept():
    print()
    print('AS YOU WISH...')


# input options, current location, current inventory
def instructions_status():
    print()
    print('************ INPUT OPTIONS ARE PROMPTED FOR THIS INPUT TO THE LETTER, RESPECTIVELY:')
    print('************ "NORTH", "SOUTH", "EAST", "WEST", "YES", "NO" ************************')
    print()
    print('YOU ARE NOW IN {}.'.format(location['place']))
    print('INVENTORY:', inventory)


# missing any hydra key items end
def user_lose():
    print('OH NOOOOOOOOO!!!... THE HYDRA FOUND YOU!')
    print('YOU WERE EATEN BY THE HYDRA! IF ONLY YOU HAD BEEN MORE PREPARED...')
    print('GAME OVER. THANKS FOR PLAYING.')


# win game end
def defeat_hydra():
    print('THE 5-HEADED HYDRA SEES YOU AND THE BATTLE BEGINS!!')
    print()
    print('YOU BLOCK THE HYDRA"S ATTACKS WITH YOUR PLANET SHIELD. YOU THROW THE FIRE GEM ')
    print('AT THE HYDRA"S ICE HEAD, THE EARTH GEM AT THE HYDRA"S GLASS HEAD, THE WIND GEM ')
    print('AT THE HYDRA"S LAVA HEAD, AND THE WATER GEM AT THE HYDRA"S POISON HEAD WHICH CAUSES ')
    print('THEM TO EXPLODE UPON IMPACT. WITH ONLY THE LASER HEAD REMAINING YOU THRUST THE ')
    print('DIAMOND SWORD INTO THE HEART OF THE THE HYDRA CAUSING THE FINAL HYDRA ')
    print('HEAD TO FALL TO THE GROUND.  YOU HAVE SLAYED THE HYDRA!')
    print()
    print()
    print('CONGRATULATIONS YOU HAVE WON THE GAME!')
    print('THANK YOU FOR PLAYING!')


# missing key items prompt
def unprepared():
    print('YOU ARE NOT READY TO DO BATTLE WITH THE HYDRA YET! YOU MUST ESCAPE IMMEDIATELY!!')
    print()
    print('DO YOU WANT TO QUICKLY FLEE FROM BURJ KHALIFA?')


# add item to inventory
def water_gem():
    inventory.append('WATER GEM')
    print()
    print()
    print('WATER GEM HAS BEEN ADDED TO YOUR INVENTORY.')


# add item to inventory
def earth_gem():
    inventory.append('EARTH GEM')
    print()
    print()
    print('EARTH GEM HAS BEEN ADDED TO YOUR INVENTORY.')


# add item inventory
def wind_gem():
    inventory.append('WIND GEM')
    print()
    print()
    print('WIND GEM HAS BEEN ADDED TO YOUR INVENTORY.')


# add item to inventory
def fire_gem():
    inventory.append('FIRE GEM')
    print()
    print()
    print('FIRE GEM HAS BEEN ADDED TO YOUR INVENTORY.')


# add item inventory
def planet_shield():
    inventory.append('PLANET SHIELD')
    print()
    print()
    print('PLANET SHIELD HAS BEEN ADDED TO YOUR INVENTORY.')


# add item to inventory
def diamond_sword():
    inventory.append('DIAMOND SWORD')
    print()
    print()
    print('DIAMOND SWORD HAS BEEN ADDED TO YOUR INVENTORY.')


# begin program execution
if __name__ == "__main__":
    def main():
        pass


    intro_play()

# game loop
while True:
    # oymyakon game add item
    if location['place'] == 'OYMYAKON':
        if 'PLANET SHIELD' not in inventory:
            print('THE KING OF OYMYAKON WOULD LIKE TO GIVE YOU THE PLANET SHIELD.')
            choice4 = input('WILL YOU ACCEPT THE GIFT? TYPE "YES" OR "NO"')
            choice4 = choice4.lower()
            if choice4 == 'yes':
                planet_shield()
            elif choice4 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # mount mauna loa add item
    if location['place'] == 'MOUNT MAUNA LOA':
        if 'FIRE GEM' not in inventory:
            print('YOU SEE A GEM FLOATING IN THE LAVA... ')
            choice5 = input('WILL YOU TAKE THE GEM? TYPE "YES" OR "NO"')
            choice5 = choice5.lower()
            if choice5 == 'yes':
                fire_gem()
            elif choice5 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # mount washington add item
    if location['place'] == 'MOUNT WASHINGTON':
        if 'WIND GEM' not in inventory:
            print('YOU SEE A GEM FLOATING IN THE WIND SOMEHOW...  ')
            choice6 = input('DO YOU RETRIEVE THE GEM? TYPE "YES" OR "NO"')
            choice6 = choice6.lower()
            if choice6 == 'yes':
                wind_gem()
            elif choice6 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # mount everest add item
    if location['place'] == 'MOUNT EVEREST':
        if 'EARTH GEM' not in inventory:
            print('YOU SEE A GEM BURIED IN THE MOUNTAIN...')
            choice7 = input('WILL YOU DIG IT OUT? TYPE "YES" OR "NO"')
            choice7 = choice7.lower()
            if choice7 == 'yes':
                earth_gem()
            elif choice7 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # mariana trench add item
    if location['place'] == 'MARIANA TRENCH':
        if 'WATER GEM' not in inventory:
            print('IN THE DEEP HOLE YOU SEE A GLOWING GEM...')
            choice8 = input('WILL YOU REACH INSIDE TO GRAB THE GEM? '
                            'TYPE "YES" or "NO".')
            choice8 = choice8.lower()
            if choice8 == 'yes':
                water_gem()
            elif choice8 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # camelot add item
    if location['place'] == "CAMELOT":
        if 'DIAMOND SWORD' not in inventory:
            print('YOU SEE A SWORD IN A STONE...')
            choice9 = input('WILL YOU PULL THE SWORD FROM THE STONE? TYPE "YES" OR "NO"')
            choice9 = choice9.lower()
            if choice9 == 'yes':
                diamond_sword()
            elif choice9 == 'no':
                not_accept()
            else:
                invalid_response()
                continue

    # win and lose end location
    if location['place'] == 'BURJ KHALIFA':
        hydra_key.sort()
        inventory.sort()
        if hydra_key != inventory:
            unprepared()
            choice10 = input()
            choice10 = choice10.lower()
            if choice10 == 'yes' or choice10 == 'no':
                user_lose()
                break
            else:
                invalid_response()
                continue
        elif hydra_key == inventory:
            defeat_hydra()
            break

    instructions_status()

    # user input direction choice
    choice1 = input('\n WHAT DIRECTION WOULD YOU LIKE TO YOU TRAVEL?')
    choice1 = choice1.lower()

    # room change
    if choice1 in directions:
        if choice1 in location:
            location = rooms[location[choice1]]
        else:
            invalid_response()
            continue
    else:
        invalid_response()
        continue


