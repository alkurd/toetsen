
# kamer_3 = 1
# aantal_rupee = 2
# sleutel = 0
# player_defense = 0
# player_attack = 0
# if kamer_3 == 1:
#     items = ['schild', 'zwaard', 'sleutel']
#     print('Je duwt hem open en stap een hele lange kamer binnen.')
#     print(f'In deze kamer staat een tafel met daarop een {" en ".join(items)}')
#     print('Vanonder de tafel spring een gobelin en schreut ooooi!!')
#     print('De items op de tafel zijn  voor mij\nniet zo maar aan raken')
#     print('Die zijn wel te koop')
#     print(f'Ik voel dat je {aantal_rupee} rupees hebt!')
#     if aantal_rupee == 1 :
#         print('Je kan maar een item kopen')
#         player_choios =  input('Wat wil je kopen? ').lower()
#         if player_choios == 'sleutel':
#             sleutel += 1
#         elif player_choios == 'zwaard':
#             player_attack += 1
#         elif player_choios == 'schild':
#             player_defense += 1
#         aantal_rupee -= 1
#     elif aantal_rupee == 2 :
#         print('Je kan twee items kopen')
#         player_choios =  input('Wat wil je kopen? ').lower()
#         if player_choios == 'sleutel en zwaard':
#             sleutel += 1
#             player_attack += 1
#             aantal_rupee -= 2
#         elif player_choios == 'sleutel en schild':
#             sleutel += 1
#             player_defense += 1
#             aantal_rupee -= 2
#         elif player_choios == 'zwaard en schild':
#             player_attack += 1
#             player_defense += 1
#             aantal_rupee -= 2
#         elif player_choios == 'zwaard en sleutel':
#             sleutel += 1
#             player_attack += 1
#             aantal_rupee -= 2
#         elif player_choios == 'schild en zwaard':
#             player_attack += 1
#             player_defense += 1
#             aantal_rupee -= 2
#         elif player_choios == 'schild en sleutel':
#             player_defense += 1
#             sleutel += 1
#             aantal_rupee -= 2
#         elif player_choios == 'sleutel':
#             sleutel += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'zwaard':
#                     player_attack += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'schild':
#                     player_defense += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'zwaard':
#             player_attack += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'sleutel':
#                     sleutel += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'schild':
#                     player_defense += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'schild':
#             player_defense += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'sleutel':
#                     sleutel += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'zwaard':
#                     player_attack += 1
#                     aantal_rupee -= 1
#     elif aantal_rupee == 3:
#         print('Je kan drie items kopen')
#         player_choios =  input('Wat wil je kopen? ').lower()
#         if player_choios == 'alles':
#             player_attack += 1
#             aantal_rupee -= 1
#             player_defense += 1
#             aantal_rupee -= 1
#             sleutel += 1
#             aantal_rupee -= 1
#         elif player_choios == 'sleutel en zwaard':
#             sleutel += 1
#             aantal_rupee -= 1
#             player_attack += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'ja':
#                     player_defense +=1
#                     aantal_rupee -= 1
#         elif player_choios == 'sleutel en schild':
#             sleutel += 1
#             aantal_rupee -= 1
#             player_defense += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'ja':
#                     player_attack += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'zwaard en schild':
#             player_attack += 1
#             aantal_rupee -= 1
#             player_defense += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'ja':
#                     sleutel += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'zwaard en sleutel':
#             sleutel += 1
#             aantal_rupee -= 1
#             player_attack += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'ja':
#                     player_defense += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'schild en zwaard':
#             player_attack += 1
#             aantal_rupee -= 1
#             player_defense += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'ja':
#                     sleutel += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'schild en sleutel':
#             player_defense += 1
#             aantal_rupee -= 1
#             sleutel += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen? ').lower()
#                 if player_choios == 'ja':
#                     player_attack += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'sleutel':
#             sleutel += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'zwaard':
#                     player_attack += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'schild':
#                     player_defense += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'zwaard':
#             player_attack += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'sleutel':
#                     sleutel += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'schild':
#                     player_defense += 1
#                     aantal_rupee -= 1
#         elif player_choios == 'schild':
#             player_defense += 1
#             aantal_rupee -= 1
#             if aantal_rupee > 0:
#                 player_choios = input('Wil je de laatste item nog kopen?').lower()
#                 if player_choios == 'sleutel':
#                     sleutel += 1
#                     aantal_rupee -= 1
#                 elif player_choios == 'zwaard':
#                     player_attack += 1
#                     aantal_rupee -= 1
#     print('Je pakt je nieuwe items op en houd het bij je.')
#     print(f'Dapper loop je de kamer binnen.')
#     print(aantal_rupee)
#     print(player_attack)
#     print(player_defense)
#     print(sleutel)




# import time, math, random

# player_attack = 2
# player_defense = 2
# player_health = 3
# sleutel = 0
# antaal_rupee = 0
# kamer_10 = 1




# if kamer_10 == 1:
#     demon_attack = 3
#     demon_defense = 1
#     demon_health = 5
#     print('Dapper loop je de kamer binnen.')
#     print('Je loopt tegen een arch demon aan.')

#     demon_hit_damage = (demon_attack - player_defense)
#     if demon_hit_damage <= 0:
#         print('Jij hebt een te goede verdediging voor de demon, hij kan je geen schade doen.')
#     else:
#         demon_attack_amount = math.ceil(player_health / demon_hit_damage)
        
#         player_hit_damage = (player_attack - demon_defense)
#         player_attack_amount = math.ceil(demon_health / player_hit_damage)

#         if player_attack_amount < demon_attack_amount:
#             health_damage = player_attack_amount * demon_hit_damage
#             player_health -= health_damage
#             print(f'In {player_attack_amount} rondes versla je de demon.')
#             print(f'Je health is nu {player_health}.')
#             print('Je ziet een deur achter de demon.')
#             # kamer_5 += 1
#         else:
#             print('Helaas is de demon te sterk voor je.')
#             print(player_health)
#             print('Game over.')
#             exit()




# ... (previous code remains unchanged)
player_attack = 2
player_defense = 2
player_health = 3
sleutel = 0
antaal_rupee = 0
kamer_10 = 1

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
        # Player's turn
        demon_health -= max(0, player_attack - demon_defense)
        demon_health = max(0, demon_health)  # Ensure health is not negative
        print(f'Je doet {max(0, player_attack - demon_defense)} schade aan de demon. Demon health is nu {demon_health}.')

        if demon_health <= 0:
            print('Je hebt de demon verslagen!')
        else:
            # Demon's turn
            player_health -= max(0, demon_attack - player_defense)
            player_health = max(0, player_health)  # Ensure health is not negative
            print(f'De demon doet {max(0, demon_attack - player_defense)} schade. Je health is nu {player_health}.')

            if player_health <= 0:
                print('Helaas is de demon te sterk voor je.')
                print('Game over.')
            else:
                print('De strijd is voorbij.')


