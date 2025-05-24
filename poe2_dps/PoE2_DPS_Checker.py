
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a decimal number.")

def dps_calc(physical_damage, total_elemental_damage, atk_speed):
   
    elemental_dps = total_elemental_damage * atk_speed
    physical_dps = physical_damage * atk_speed
    total_weapon_damage = elemental_dps + physical_dps

    return total_weapon_damage

weapon_list = {}

power_on = True
while power_on:

    damage_values = True

    elemental_damage = {}

    physical_damage = 0

    low_phy = get_int_input("Low end physical damage value: ")
    high_phy = get_int_input("High end physical damage value: ")
    physical_damage = (low_phy + high_phy)/2

    while damage_values:
        more_dmg = input("Are there any other damage types? y or n: ").lower()
        
        if more_dmg == "y":
            new_dmg_type = input("Fire, Cold, Lightning or Chaos? (F, C, L, CH): ").strip().lower()

            if new_dmg_type in ["fire", "f"]:
                low = get_int_input("Low end Fire damage value: ")
                high = get_int_input("High end Fire damage value: ")
                elemental_damage["Fire Damage"] = (low + high)/2

            elif new_dmg_type in ["cold", "c"]:
                low = get_int_input("Low end Cold damage value: ")
                high = get_int_input("High end Cold damage value: ")
                elemental_damage["Cold Damage"] = (low + high)/2

            elif new_dmg_type in ["lightning", "l"]:
                low = get_int_input("Low end Lightning damage value: ")
                high = get_int_input("High end Lightning damage value: ")
                elemental_damage["Lightning Damage"] = (low + high)/2

            elif new_dmg_type in ["chaos", "ch"]:
                low = get_int_input("Low end Chaos damage value: ")
                high = get_int_input("High end Chaos damage value: ")
                elemental_damage["Chaos Damage"] = (low + high)/2

            else:
                print("Invalid damage type.")
            
        
        else:
            damage_values = False

    total_elemental_dmg = sum(elemental_damage.values())

    atk_speed = get_float_input("What is the weapon's attack speed? ")

    weapon_dps = round(dps_calc(physical_damage, total_elemental_dmg, atk_speed), 2)   

    weapon_name = input("What is the name of this weapon? ").capitalize()

    weapon_list[weapon_name] = weapon_dps

    print(f"{weapon_name}'s DPS is {weapon_dps}")


    run_input = True

    while run_input:
        run_again = input("would you like to calculate another weapon or see the list of calculated weapons DPS? (y = yes, n = no, l = list: ").lower()

        if run_again == "l":
            print(weapon_list)
        elif run_again == "y":
            run_input = False
        elif run_again == "n":
            print("Thank you for using the Path of Exile 2 DPS calculator")
            run_input = False
            power_on = False
        else:
            print("Invalid input. please enter 'y', 'n' or 'l'")
        






