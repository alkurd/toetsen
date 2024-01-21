import time, math, random

player_attack = 2
player_defense = 2
player_health = 10
sleutel = 0
antaal_rupee = 0
schild = 0
bom = 1
dolk = 1
bos_key = 0

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
        print ("Je ziet drie deuren elke met zijn nummer der boven op 10/12/13")
        spaler = input('Je denkt welke kant nou? ').lower()
        if spaler == '12' :
            kamer_12 += 1
        elif spaler == '13' and bom == 1 :
            print('Je makt de hek open met een bom naar toe te gooien')
            print('Je vindt binne een zwaard je pakt hem houdt hem bij je')
            player_attack += 2
            if bos_key == 1:
                print('Na dat je de zwaard hebt gepakt loop je de kleine kamer der uit')
                print('je ziet nu twee deuren een met nummer 10 en andere met nummer 12')
                spaler = input('welke deur ga je?')
                if spaler == '10':
                    print('Na dat je de zwaard hebt gepakt je loopt naar de deur naast je met nummer 10 ')
                    kamer_10 += 1
                elif spaler == '12':
                    kamer_12 += 1
            elif bos_key == 0 :
                print('Je loopt naar deur rechts van je met nummer 10 ')
                print('Je probeert de deur open te maken maar krijg je hem toch niet open')
                print('Dus je loopt naar de ander deur met nummer 12')
                print('Je dwut de deur open')
                kamer_12 +=1
        elif spaler == '10':
            if bos_key == 1:
                print('Je dewt de deur open')
                kamer_10 += 1
            elif bos_key == 0 and bom == 1 :
                print('Je probeert de deur open te maken maar het lukt je niet')
                print('Je loopt paar stapen naar acht en gooit met de bom naar de deur!')
                print('......Boooom!!!!')
                print('De deur gaat open en je loopt naar binne')
                kamer_10 += 1
    else:
        zombie_bos_attack_amount = math.ceil(player_health / zombie_bos_hit_damage)
        
        player_hit_damage = (player_attack - zombie_bos_defense)
        player_attack_amount = math.ceil(zombie_bos_health / player_hit_damage)

        if player_attack_amount < zombie_bos_attack_amount:
            health_damig = player_attack_amount * zombie_bos_hit_damage
            player_health -= health_damig
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print ("Je ziet drie deuren elke met zijn nummer der boven op 10/12/13")
            spaler = input('Je denkt welke kant nou? ').lower()    
            if spaler == '12' :
                kamer_12 += 1
            elif spaler == '13' and bom == 1 :
                print('Je makt de hek open met een bom naar toe te gooien')
                player_attack += 2
                if bos_key == 1:
                    print('je ziet nu twee deuren een met nummer 10 en andere met nummer 12')
                    spaler = input('welke deur ga je?')
                    if spaler == '10':
                        print('Na dat je de zwaard hebt gepakt je loopt naar de deur naast je met nummer 10 ')
                        kamer_10 += 1
                    elif spaler == '12':
                        kamer_12 += 1
                elif bos_key == 0 :
                    print('Je loopt naar deur rechts van je met nummer 10 ')
                    print('Je probeert de deur open te maken maar krijg je hem toch niet open')
                    print('Dus je loopt naar de ander deur met nummer 12')
                    print('Je dwut de deur open')
                    kamer_12 +=1
            elif spaler == '10':
                if bos_key == 1:
                    print('Je dewt de deur open')
                    kamer_10 += 1
                elif bos_key == 0 and bom == 1 :
                    print('Je probeert de deur open te maken maar het lukt je niet')
                    print('Je loopt paar stapen naar acht en gooit met de bom naar de deur!')
                    print('......Boooom!!!!')
                    print('De deur gaat open en je loopt naar binne')
                    kamer_10 += 1    
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)

