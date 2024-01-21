import time, math, random

player_attack = 2
player_defense = 2
player_health = 10
sleutel = 0
antaal_rupee = 0
schild = 0
bom = 1
dolk = 1
bos_key = 1

kamer_2 = 0
kamer_3 = 0
kamer_4 = 1
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
        elif spaler == 'rechtdoor':
            if bom == 1 and bos_key ==1:
                spaler = input('wat ga ik gebruiken? ')
                if spaler == 'bom':
                    bom -= 1
                    kamer_10 +=1
                elif spaler == 'zwarte sleutel':
                    print('je gebruikt de zwarte sleuten om de kamer binne te lopen')
                    bos_key -= 1
                    kamer_10 += 1
                if bom == 1 and bos_key == 0:
                    print('je gooit de bom naar de deur')
                    print('de deur gaat open!')
                    kamer_10 +=1
                    if bos_key == 1 and bom == 0:
                        print('je gebruikt de zwarte sleuten om de kamer binne te lopen')
                        kamer_10 +=1
                elif spaler == 'hek' and bom == 0 and bos_key == 1:
                    print('je probeert de deur open te krijgen maar het lukte niet')
                    print('je loopt naar de deur rechts vant je')
                    print('je gebruikt de zwarte sleutel')
                    kamer_10 += 1
                    if bom == 1:
                        print('je goot de bom naar de hek')
                        print('J eziet achter de hek een zwaard')
                        print('Je pakte het op en houdt het bij je  ')
                        player_attack += 2
                        if bos_key == 1:
                            print('je ziet nu twee deuren een met nummer 10 en andere met nummer 12')
                            spaler = input('welke deur ga je?')
                            if spaler == '12':
                                kamer_12 += 1
                                if spaler == '10':
                                    print('Na dat je de zwaard hebt gepakt je loopt naar de deur naast je met nummer 10 ')
                                    kamer_10 += 1

                            

        elif spaler == 'hek':
            print('Je proebeert het hek open te krijgen maar je grijgt hem toch niet open!!')
            player_attack +=2
            bom -= 1
            print('Je vindt zwaard je pakt hem op en je houdt hem bij je')
            spaler = input('na dat je de zwaard heeft gepakt blijft de vraag waar nu heen?')
            if spaler == 'recht':
                if bos_key == 1:
                    print('na het paken van de zwaard loop je de de groote deu')
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