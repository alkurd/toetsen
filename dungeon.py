import time, math, random

player_attack = 1
player_defense = 0
player_health = 10
sleutel = 0
antaal_rupee = 0
schild = 0
bom = 0
dolk = 0
bos_key = 0

kamer_2 = 0
kamer_3 = 0
kamer_4 = 0
kamer_5 = 0
kamer_6 = 0
kamer_7 = 0
kamer_8 = 0
kamer_9 = 0
kamer_10 = 0
kamer_11 = 0
kamer_12 = 0
kamer_13 = 0
kamer_14 = 0
kamer_15 = 0

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
kamer_7 += 1
print('')
time.sleep(1)

# === [kamer 7] === #
if kamer_7 == 1:
    betoverde_kamer = random.randint(1,10)
    print('Je loopt binne je voet magie in de lucht')
    print('Blijkbaar heeft een euwen oud tovenaar heeft de kamer  betoverd')
    if betoverde_kamer != 5:
        print ('Je vindt een rupee in het kamer je pakt hem op en\nLoop door naar de volgende deur')
        antaal_rupee += 1
        print(f'Je hebt nu {antaal_rupee} rupees')
    else:
        print('Je loop met lege handen door') 
    print('In het kamer zie je twee deuren.')
    spaler_1 = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
    if spaler_1 == 'rechts':
        kamer_8 +=1
    elif spaler_1 == 'rechtdoor':
        kamer_2 +=1

# === [kamer 2] === #
if kamer_2 == 1:
    RANDOM_0 = random.randint(10, 25)
    RANDOM_01 = random.randint(10, 25)
    RANDOM_1 = random.randint(-5, 76)
    RANDOM_10 = random.randint(-5, 76)
    antwoord_1 = RANDOM_0 + RANDOM_01
    antwoord_2 = RANDOM_1 - RANDOM_10
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    vraag_1_input = int(input(f'Daarboven zie je een som staan {RANDOM_0} + {RANDOM_01} = ? {antwoord_1} '))
    vraag_2_input = int(input(f'Daarboven zie je een som staan {RANDOM_1} - {RANDOM_10} = ? {antwoord_2} '))
    if vraag_1_input == antwoord_1 and vraag_2_input == antwoord_2:
        antaal_rupee += 1
        print(f'Je hebt nu {antaal_rupee} rupees')
        print('Het standbeeld laat de rupee vallen en je pakt het op.')
    else:
        print('Er gebeurt niets....')
    print('In het kamer zie je twee deuren.')
    spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
    if spaler == 'rechts':
        kamer_8 +=1
    elif spaler == 'rechtdoor':
        kamer_6 +=1
    # time.sleep(1)
        print('')
    time.sleep(1)

# === [kamer 6] === #
if kamer_6 == 1:
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            health_damig = player_attack_amount * zombie_hit_damage
            player_health -= health_damig

            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            print('Na dat je de zombie verslaat krijg je een drop item')
            print('"""""""""""""Dlek""""""""""""""')
            dolk += 1
            if dolk == 1:
                player_attack += 1
            spaler = input('Je ziet twee deuren een is recht en ander is rechtdoor? ').lower()
            if spaler == 'rechts':
                kamer_8 +=1
            elif spaler == 'rechtdoor':
                kamer_3 +=1
            print('Je zie een duer verschijnen na dat je de zombie heeft verslaan.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()  
print('')
time.sleep(1)

# == [kamer 8] == #
if kamer_8 == 1:
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
            rupee_verdubeling = (antaal_rupee * 2)
            antaal_rupee = rupee_verdubeling
            print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
            print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
            print(f'Je heb nu {antaal_rupee} rupes')
            print(f'Met {antaal_rupee} rupes loop je weg')
            print('In het kamer zie je twee deuren.')
            spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
            if spaler == 'eerste deur':
                kamer_3 +=1
            elif spaler == 'tweede deur':
                kamer_9 +=1
            elif spaler == 'rechts':
                kamer_14 += 1
        elif dobelsteen_1 + dobelsteen_2 == 7:
            print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
            print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
            antaal_rupee += 1
            player_health += 4
            print(f'Je heb nu {antaal_rupee} rupes')
            print(f'Met {antaal_rupee} rupes loop je weg')
            spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
            if spaler == 'eerste deur':
                kamer_3 +=1
            elif spaler == 'tweede deur':
                kamer_9 +=1
            elif spaler == 'rechts' :
                kamer_14 += 1
        elif dobelsteen_1 + dobelsteen_2 < 7:
            player_health -= 1
            if player_health <= 0:
                print('""""""""""""Game over""""""""""""')
                exit()
            else:
                print(f"Je hebt bij de eerste dobelsteen {dobelsteen_1} gerold")
                print(f"Je hebt bij de tweede dobelsteen {dobelsteen_2} gerold")
                print(f'Maar je health is vermindert met 1 punt!')
                print(f'Je heb nu {antaal_rupee} rupes')
                print(f'Met {antaal_rupee} rupes loop je weg')
                spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
                if spaler == 'eerste deur':
                    kamer_3 +=1
                elif spaler == 'tweede deur':
                    kamer_9 +=1
                elif spaler == 'rechts':
                    kamer_14 += 1
    elif black_goblin == 'nee':
        print('Je loopt door naar de volgende deur')
        spaler = input('welke kant ga je rechts naar de eerste deur of recht door naar het tweede deur?').lower()
        if spaler == 'eerste deur':
            kamer_3 +=1
        elif spaler == 'tweede deur':
            kamer_9 +=1
        elif spaler == 'rechts':
            kamer_14 += 1

# == [kamer 14] == #
if kamer_14 == 1:
    print('je dwut de deur open en loopt binnen')
    print('Mindden in de kamer zweveft een zwarte sleutel')
    print ('je pakt hem op en je houdt hem bij')
    bos_key += 1
    kamer_9 += 1

# == [kamer 9] == #
if kamer_9 == 1:
    blessings = ['defense', 'health']
    random_blessing = random.choice(blessings)
    print('Je duwt de deur open en loopt een lange kamer binnen.')
    print('Aan het einde van de kamer zie je een glanzende witte deur.')
    print('Het glanst zo fel dat je het van ver kunt zien.')
    print('Je rent daarheen.')
    print('Je duwt de deur open.')
    if random_blessing == 'defense':
        defense_value = 1
        player_defense += defense_value
        print(f'Je voelt een kracht om je heen die je verdediging versterkt. Verdediging +{defense_value}')
    elif random_blessing == 'health':
        health_value = 2
        player_health += health_value
        print(f'Je voelt een genezende kracht die je gezondheid herstelt. Gezondheid +{health_value}')
    print('je ziet twee deuren een is liks en de ander is rechtdoor')
    spaler = input('door welke deur zou je gaan de likere of die rechtdoor? ')
    if spaler == 'links':
        kamer_3 += 1
    elif spaler == 'rechtdoor':
        kamer_4 += 1



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
        schild_zwaard = input('Wil je alle items kopen ').lower()
        if schild_zwaard == 'ja':
            sleutel += 1
            player_defense += 1
            schild += 1
            antaal_rupee -= 1
            player_attack += 2
            antaal_rupee -= 1
    elif antaal_rupee == 2:
        player_choios = input('welke 2 itms wil je hebbe? ').lower()
        if player_choios == 'bom en schild':
            player_defense += 1
            schild += 1
            antaal_rupee -= 1
            bom += 1
            antaal_rupee -= 1
        if player_choios == 'schild en bom':
            player_defense += 1
            schild += 1
            antaal_rupee -= 1
            bom += 1
            antaal_rupee -= 1
        elif player_choios == 'schild en sleutel':
            player_defense += 1
            schild += 1
            antaal_rupee -= 1
            sleutel += 1
            antaal_rupee -= 1
        elif player_choios == "sleutel en schild":
            player_defense += 1
            schild += 1
            antaal_rupee -= 1
            sleutel += 1
            antaal_rupee -= 1
        elif player_choios == 'sleutel en bom':
            sleutel += 1
            antaal_rupee -= 1
            bom += 1
            antaal_rupee -= 1
        elif player_choios == 'bom en sleutel':
            sleutel += 1
            antaal_rupee -= 1
            bom += 1
            antaal_rupee -= 1
        elif player_choios == 'nee':
            player_choios = input(f'Welke wil je dan hebben de {" of ".join(items)}? ')
            if player_choios == 'sleutel':
                sleutel += 1
                antaal_rupee -= 1
            elif player_choios == 'schild':
                player_defense += 1
                schild += 1
                antaal_rupee -= 1
            elif player_choios == 'bom':
                bom += 1
                antaal_rupee -= 1
                print(f'Je pakt het {player_choios} op en houd het bij je.')
    elif antaal_rupee == 1:
        print('1 rupee voor elk van de items')
        player_choios = input(f'Welke wil je hebben de {" of ".join(items)}? ')
        if player_choios == 'schild':
            schild += 1
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
        
    else:
        print('Je hebt niet genoeg rupees!')
    print('Op een verscheint nog een deur in het kamer')
    spaler = input('Welke deur ga je paken de eerte of de tweede deur? ').lower()
    if spaler == 'eerste deur':
        kamer_4 +=1
    elif spaler == 'tweede deur':
        kamer_11 +=1
    print('')
    time.sleep(1)

# === [kamer 11] === #
if kamer_11 == 1:
    print('Je dewt de deur open')
    print('Je ziet een hele lange kamergevoeld met stambelden')
    print('je loopt je stapte binde de kamer en de deuren sleuten van zicht achter ')
    if schild == 1:
        print('je loopt door en op eens beginne de stambelden pijlen te schiten tegen jou')
        print('Je denkt gelukig heb ik de schild gekoscht ')
        print('Anders was ik nu al dood')
        print('Je ziet lange duer en je dwut hem open')
        kamer_10 += 1
    elif schild < 1:
        print('Je loopt binnen')
        print('je voelt dat de kamer is te rustig')
        print('je begint door het kamer te lopen')
        print('na enkel stapen bigenne de stambelden te bewgen')
        print('ze beginnen jou te bekogelen met pijlen')
        print('je probiert te renen maar ...')
        print('je wordt geschoten in je been en in arm')
        print('je denkt ik ben nu al dood\nIk heb geen kans meer')
        print('""""""""""""""" Game Over """""""""""""""')
        exit()

# === [kamer 4] === #
if kamer_4 ==1:
    zombie_bos_attack = 2
    zombie_bos_defense = 0
    zombie_bos_health = 3
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een zombie bos aan.')

    zombie_bos_hit_damage = (zombie_bos_attack - player_defense)
    if zombie_bos_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        print ("je ziet twee deruen en een hek")
        spaler = input('Je denkt wat nou? ').lower()
        if spaler == 'recht':
            kamer_12 += 1
        elif spaler == 'hek':
            print('Je proebeert het hek open te krijgen maar je grijgt hem toch niet open!!')
            spaler = input('je denkt denkt zou ik de bom gebruiken? ').lower()
            if spaler == 'ja':
                player_attack +=2
                bom -= 1
                print('Je vindt zwaard je pakt hem op en je houdt hem bij je')
        elif spaler == 'rechtdoor':
            if bos_key == 1 and bom == 1:
                spaler = input('Welke ga je gebruiken? ').lower()
                if spaler == 'bos key':
                    print('Je gebruikt de zwarte sleutel om de deur te openen ')
                    kamer_10 += 1
                    bos_key -= 1
                elif spaler == 'bom':
                    print('Je gooit de bom naar de deur en de deur barst open')
                    kamer_10 += 1
                    bom -= 1
            if bos_key == 1:
                print('Je gebruikt de zwarte sleutel om de deur te openen ')
                kamer_10 += 1
                bos_key -= 1
    else:
        zombie_bos_attack_amount = math.ceil(player_health / zombie_bos_hit_damage)
        
        player_hit_damage = (player_attack - zombie_bos_defense)
        player_attack_amount = math.ceil(zombie_bos_health / player_hit_damage)

        if player_attack_amount < zombie_bos_attack_amount:
            health_damig = player_attack_amount * zombie_bos_hit_damage
            player_health -= health_damig
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print ("je ziet twee deruen en een hek")
            spaler = input('Je denkt wat nou? ').lower()
            if spaler == 'recht':
                kamer_12 += 1
            elif spaler == 'hek':
                print('Je proebeert het hek open te krijgen maar je grijgt hem toch niet open!!')
                spaler = input('je denkt denkt zou ik de bom gebruiken? ').lower()
                if spaler == 'ja':
                    player_attack +=2
                    bom -= 1
                    print('Je vindt zwaard je pakt hem op en je houdt hem bij je')
            elif spaler == 'rechtdoor':
                if bos_key == 1 and bom == 1:
                    spaler = input('Welke ga je gebruiken? ').lower()
                    if spaler == 'bos key':
                        print('Je gebruikt de zwarte sleutel om de deur te openen ')
                        kamer_10 += 1
                        bos_key -= 1
                    elif spaler == 'bom':
                        print('Je gooit de bom naar de deur en de deur barst open')
                        kamer_10 += 1
                        bom -= 1
                if bos_key == 1:
                    print('Je gebruikt de zwarte sleutel om de deur te openen ')
                    kamer_10 += 1
                    bos_key -= 1
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)

# == [kamer 12] == #
if kamer_12 == 1:
    print('Zodra dat je de deur opent voel je gelijk dat je in de lucht hangt')
    print('En hier bij val je tot je dood')
    print(""""""""""""" Game Over """"""""""""")
    exit()


# == [kamer 10] == #
if kamer_10 == 1:
    demon_attack = 3
    demon_defense = 1
    demon_health = 5
    print('Dapper loop je de kamer binnen.')
    print('Je loopt tegen een arch demon aan.')

    demon_hit_damage = max(0, demon_attack - player_defense)
    if demon_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de demon, hij kan je geen schade doen.')
    else:
        while player_health > 0 and demon_health > 0:
            
            demon_health -= max(0, player_attack - demon_defense)
            demon_health = max(0, demon_health)
            print(f'Je doet {max(0, player_attack - demon_defense)} schade aan de demon. Demon health is nu {demon_health}.')

            if demon_health <= 0:
                print('Je hebt de demon verslagen!')
                kamer_5 +=1
                print(player_attack)
                print(player_defense)
                print(player_health)
                break
            player_health -= max(0, demon_attack - player_defense)
            player_health = max(0, player_health)
            print(f'De demon doet {max(0, demon_attack - player_defense)} schade. Je health is nu {player_health}.')

            if player_health <= 0:
                print('Helaas is de demon te sterk voor je.')
                print('Game over.')
                exit()
                
                


# === [kamer 5] === #
if kamer_5 == 1:
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if sleutel == 1:
        print('met de sleutel open je de kist en versla je de Dungeon')
    elif bom == 1:
        print('Je gooit de bom naar de kist ')
        print('De kist kraakt open!!')
        print('Je overleeft de Dungeon ')
    else:
        print ('je kon de Dungeon niet verslan\n""""""""""GAMEOVER""""""""""')


# if kamer_11 == 1:
#     print('Je dewt de deur open')
#     print('Je ziet een hele lange kamergevoeld met stambelden')
#     print('je loopt je stapte binde de kamer en de deuren sleuten van zicht achter ')
#     if schild == 1:
#         print('je loopt door en op eens beginne de stambelden pijlen te schiten tegen jou')
#         print('Je denkt gelukig heb ik de schild gekoscht ')
#         print('Anders was ik nu al dood')
#         print('Je ziet lange duer en je dwut hem open')
#         kamer_4 += 1
#     elif schild < 1:
#         print('Je loopt binnen')
#         print('je voelt dat de kamer is te rustig')
#         print('je begint door het kamer te lopen')
#         print('na enkel stapen bigenne de stambelden te bewgen')
#         print('ze beginnen jou te bekogelen met pijlen')
#         print('je probiert te renen maar ...')
#         print('je wordt geschoten in je been en in arm')
#         print('je denkt ik ben nu al dood\nIk heb geen kans meer')
#         print('""""""""""""""" Game Over """""""""""""""')
#         exit()