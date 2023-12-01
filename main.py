def affichage_heure(horloge: tuple, alarm: tuple):
    
    horloge = list(horloge)
    alarm = list(alarm)

    while True:
        try:
            # Affichage de l'horloge
            print(f"{horloge[0]:02d}:{horloge[1]:02d}:{horloge[2]:02d}", end="\r")
            # \r pour revenir au début de la ligne (pas de nouvelle ligne)
            import time
            time.sleep(1)

            horloge[2] += 1
            if horloge[2] == 60:
                horloge[2] = 0
                horloge[1] += 1
            if horloge[1] == 60:
                horloge[1] = 0
                horloge[0] += 1
            if horloge[0] == 23:
                horloge[0] = 0
                break

            alarme_check(horloge, alarm)
            
        except KeyboardInterrupt:
            print("Arrêt de l'horloge")
            break


def alarme_check(horloge_hour: list, alarm_hour: list):
    if horloge_hour == alarm_hour:
        print("!!!!!!!!!!!!!!!!!!! DEBOUT LA-DEDANS !!!!!!!!!!!!!!!!!!!!!!!") 


horloge = (11, 59, 58)
alarme = (12, 0, 0)

affichage_heure(horloge, alarme)