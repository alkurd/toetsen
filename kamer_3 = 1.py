kamer_3 = 1
antaal_rupee = 2
sleutel = 0
player_defense = 0
player_attack = 0
import time
# === [kamer 3] === #
if kamer_3 == 1:
    
    items = ['schild', 'zwaard', 'sleutel']
    # items1 = list.pop('sleutel')
    # chosen_item = random.choice(items)
    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {" en ".join(items)}')
    print('Vanonder de tafel spring een goblin en schreut ooooi!!')
    print('De items op de tafel zijn  voor mij\nniet zo maar aan raken')
    print('Die zijn wel te koop')
    print(f'Ik voel dat je {antaal_rupee} rupees hebt!')
    if antaal_rupee >= 3:
        # print('1 rupee voor elk van de items')
        player_choios = input('Wil je alle items kopen ').lower()
        if player_choios == 'ja':
            sleutel += 1
            antaal_rupee -= 1
            player_defense += 1
            antaal_rupee -= 1
            player_attack += 2
            antaal_rupee -= 1
    elif antaal_rupee == 2:
        # print('1 rupee voor elk van de items')
        player_choios = input('welke itms wil je hebbe? ').lower()
        if player_choios == 'schild en zwaard':
            player_defense += 1
            antaal_rupee -= 1
            player_attack += 2
            antaal_rupee -= 1
        elif player_choios == 'schild en sleutel':
            player_defense += 1
            antaal_rupee -= 1
            sleutel += 1
            antaal_rupee -= 1
        elif player_choios == 'sleutel en zwaard':
            sleutel += 1
            antaal_rupee -= 1
            player_attack += 1
            antaal_rupee -= 1
        elif player_choios == 'nee':
            player_choios = input(f'Welke wil je dan hebben de {" of ".join(items)}? ')
            if player_choios == 'sleutel':
                sleutel += 1
                antaal_rupee -= 1
            elif player_choios == 'schild':
                player_defense += 1
                antaal_rupee -= 1
                print(f'Je pakt het {player_choios} op en houd het bij je.')
            elif player_choios == 'zwaard':
                player_attack += 2
                antaal_rupee -= 1
                print(f'Je pakt het {player_choios} op en houd het bij je.')
    elif antaal_rupee == 1:
        print('1 rupee voor elk van de items')
        player_choios = input(f'Welke wil je hebben de {" of ".join(items)}? ')
        if player_choios == 'schild':
            player_defense += 1
            antaal_rupee -= 1
            print(f'Je pakt het {player_choios} op en houd het bij je.')
        elif player_choios == 'zwaard':
            player_attack += 2
            antaal_rupee -= 1
        elif player_choios == 'sleutel':
            sleutel += 1
            antaal_rupee -= 1
            print(f'Je pakt het {player_choios} op en houd het bij je.')
            print(f'Dapper met je nieuwe {player_choios} loop je de kamer binnen.')
    else:
        print('Je hebt niet genoeg rupees!')
    print('Op naar de volgende deur.')
    # kamer_4 +=1
    print('')
    time.sleep(1)

print(sleutel)
print(player_attack)
print(player_defense)
print(antaal_rupee)
print(f'{player_choios}')