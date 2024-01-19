import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
sleutel = 0
antaal_rupee = 0

kamer_2 = 0
kamer_3 = 0
kamer_4 = 0
kamer_5 = 0
kamer_6 = 0
kamer_7 = 0
kamer_8 = 0

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
kamer_7 += 1
print('')
time.sleep(1)

# === [kamer 7] === #
if kamer_7 == 1:
    print ('Je vindt een rupee in het kamer je pakt hem op en\nLoop door naar de volgende deur')
    antaal_rupee += 1
    print('In het kamer zie je twee deuren.')
    spaler_1 = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
    if spaler_1 == 'rechts':
        kamer_8 +=1
    elif spaler_1 == 'rechtdoor':
        kamer_2 +=1

# === [kamer 2] === #
if kamer_2 == 1:
    RANDOM_0 = random.randint(10, 25)
    RANDOM_1 = random.randint(-5, 76)
    antwoord_1 = RANDOM_0 + RANDOM_0
    antwoord_2 = RANDOM_1 - RANDOM_1
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    vraag_1_input = int(input(f'Daarboven zie je een som staan {RANDOM_0} + {RANDOM_0} = ? '))
    vraag_2_input = int(input(f'Daarboven zie je een som staan {RANDOM_1} - {RANDOM_1} = ? '))
    if vraag_1_input == antwoord_1 and vraag_2_input == antwoord_2:
        sleutel += 1
        print('Het standbeeld laat de sleutel vallen en je pakt het op.')
    else:
        print('Er gebeurt niets....')
    print('In het kamer zie je twee deuren.')
    spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
    if spaler == 'rechts':
        kamer_8 +=1
    elif 'recht door':
        kamer_6 +=1
    # time.sleep(1)
        print('')
    time.sleep(1)

# === [kamer 6] === #
if kamer_6 == 1:
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print(f'Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            kamer_8 += 1
            print('Je zie een deur achter het standbeeld.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()  
print('')
time.sleep(1)

# == [kamer 8] == #
if kamer_8 == 1:
    kamer_3 +=1
    dobelsteen_1 = random.randint(1,6)
    dobelsteen_2 = random.randint(1,6)
    print('Je de duwt de deur open en loopt een lange kamer binne')
    print('in het lange kamer is er een goblin')
    black_goblin =input('Hij vraagt jou als je met hem wilt gokken? ').lower()
    if black_goblin == 'ja':
        print('Laat we dan gelijk beginnen')
        print('Laten we de win of door gokerij spelen')
        print('Je gooit me de dobelsteens')
        if dobelsteen_1 + dobelsteen_2 > 7:
            antaal_rupee * 2
            print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
            print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
        elif dobelsteen_1 + dobelsteen_2 == 7:
            print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
            print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
            antaal_rupee += 1
            player_health += 4
        elif dobelsteen_1 + dobelsteen_2 < 7:
            print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
            print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
            player_health -+ 1
    elif black_goblin == 'nee':
        print('Je loopt door naar de volgende deur')

# === [kamer 3] === #
if kamer_3 == 1:
    items = ['schild', 'zwaard']
    # chosen_item = random.choice(items)
    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een{" en ".join(items)}')
    print('Vanonder de tafel spring een goblin en schreut ooooi!!')
    print('De items op de tafel zijn  voor mij\nniet zo maar aan raken')
    print('Die zijn wel te koop')
    print('een rupee voor elk van de items')
    if antaal_rupee >= 2:
        print(f'Ik voel dat je {antaal_rupee} rupees hebt!')
        schild_zwaard = input('Wil je een Schild een Zwaard').lower()
        if schild_zwaard == 'ja':
            player_defense += 1
            antaal_rupee -= 1
            player_attack += 2
            antaal_rupee -= 1
        elif schild_zwaard == 'nee':
            player_choios = input(f'Welke wil je dan hebben de {" of ".join(items)}? ')
            if player_choios == 'schild':
                player_defense += 1
                antaal_rupee -= 1
                print(f'Je pakt het {player_choios} op en houd het bij je.')
            elif player_choios == 'zwaard':
                player_attack += 2
                antaal_rupee -= 1
                print(f'Je pakt het {player_choios} op en houd het bij je.')
    elif antaal_rupee == 1:
        player_choios = input(f'Welke wil je hebben de {" of ".join(items)}? ')
        if player_choios == 'schild':
            player_defense += 1
            antaal_rupee -= 1
            print(f'Je pakt het {player_choios} op en houd het bij je.')
        elif player_choios == 'zwaard':
            player_attack += 2
            antaal_rupee -= 1
            print(f'Je pakt het {player_choios} op en houd het bij je.')
    else:
        print('Je hebt niet genoeg rupees!')
    print('Op naar de volgende deur.')
    kamer_3 -=1
    kamer_4 +=1
    print('')
    time.sleep(1)

# === [kamer 4] === #
if kamer_4 ==1:
    zombie_attack = 2
    zombie_defense = 0
    zombie_health = 3
    print(f'Dapper met je nieuwe {player_choios} loop je de kamer binnen.')
    print('Je loopt tegen een zombie bos aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            print('Je zie een deur achter het standbeeld.')
            kamer_5 += 1
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)

# === [kamer 5] === #
if kamer_5 == 1:
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if sleutel == 1:
        print('met de sleutel open je de kist en versla je de Dungeon')
    else:
        print ('je kon de Dungeon niet verslan\n""""""""""GAMEOVER""""""""""')
