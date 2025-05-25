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

def get_string_input(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("That is not a valid input")

def get_weapon_type(prompt):
    valid_types = ["Bow", "Crossbow", "Quarterstaff", "Spear", "One Handed Mace", "Two Handed Mace"]
    while True:
        user_input = input(prompt).strip()
        normalized_input = user_input.lower()
        valid_lower = [v.lower() for v in valid_types]
        
        if normalized_input in valid_lower:
            index = valid_lower.index(normalized_input)
            return valid_types[index]
        else:
            print(f"Invalid weapon type. Please enter one of: {', '.join(valid_types)}")

def dps_calc(physical_damage, total_elemental_damage, attacks_per_second):
    elemental_dps = total_elemental_damage * attacks_per_second
    physical_dps = physical_damage * attacks_per_second
    total_weapon_damage = elemental_dps + physical_dps
    return total_weapon_damage

class Weapon:
    def __init__(self, type, name, dps, critical_chance, attacks_per_second, quality, item_level, required_level, rarity):
        self.type = type
        self.name = name
        self.dps = dps
        self.critical_chance = critical_chance
        self.attacks_per_second = attacks_per_second
        self.quality = quality
        self.item_level = item_level
        self.required_level = required_level
        self.rarity = rarity

    def critical_chance_str(self):
        return f"{self.critical_chance}%"
    
    def quality_str(self):
        return f"{self.quality}%"

    def __str__(self):
        return (f"{self.name}\n Type: {self.type}\n DPS: {self.dps}\n "
                f"Crit Chance: {self.critical_chance_str()}\n "
                f"Attacks/Sec: {self.attacks_per_second}\n Quality: {self.quality_str()}\n "
                f"Item Level: {self.item_level}\n Required Level: {self.required_level}\n Rarity: {self.rarity}\n")

class Crossbow(Weapon):
    def __init__(self, type, name, dps, critical_chance, attacks_per_second, reload_time, quality, item_level, required_level, rarity):
        super().__init__(type, name, dps, critical_chance, attacks_per_second, quality, item_level, required_level, rarity)
        self.reload_time = reload_time

    def __str__(self):
        return super().__str__() + f" Reload Time: {self.reload_time}"

weapon_list = {}

power_on = True
while power_on:

    elemental_damage = {}

    type = get_weapon_type("Enter weapon type (Bow, Crossbow, Quarterstaff, Spear, one handed Mace, two handed Mace): ").capitalize()

    low_phy = get_int_input("Low end physical damage value: ")
    high_phy = get_int_input("High end physical damage value: ")
    physical_damage = (low_phy + high_phy) / 2

    damage_values = True
    while damage_values:
        more_dmg = input("Are there any other damage types? (y/n): ").lower()
        
        if more_dmg == "y":
            new_dmg_type = input("Fire, Cold, Lightning or Chaos? (F, C, L, CH): ").strip().lower()

            if new_dmg_type in ["fire", "f"]:
                low = get_int_input("Low end Fire damage value: ")
                high = get_int_input("High end Fire damage value: ")
                elemental_damage["Fire Damage"] = (low + high) / 2

            elif new_dmg_type in ["cold", "c"]:
                low = get_int_input("Low end Cold damage value: ")
                high = get_int_input("High end Cold damage value: ")
                elemental_damage["Cold Damage"] = (low + high) / 2

            elif new_dmg_type in ["lightning", "l"]:
                low = get_int_input("Low end Lightning damage value: ")
                high = get_int_input("High end Lightning damage value: ")
                elemental_damage["Lightning Damage"] = (low + high) / 2

            elif new_dmg_type in ["chaos", "ch"]:
                low = get_int_input("Low end Chaos damage value: ")
                high = get_int_input("High end Chaos damage value: ")
                elemental_damage["Chaos Damage"] = (low + high) / 2

            else:
                print("Invalid damage type.")
        else:
            damage_values = False

    total_elemental_dmg = sum(elemental_damage.values())

    attacks_per_second = get_float_input("What is the weapon's attacks per second value? ")

    dps = round(dps_calc(physical_damage, total_elemental_dmg, attacks_per_second), 2)   

    critical_chance = get_float_input("What is the critical hit chance? (e.g. 5.00 for 5%): ")

    quality = get_int_input("What is the weapon's quality? (0 - 20): ")

    item_level = get_int_input("What is the item level? ")

    required_level = get_int_input("What is the required level? ")

    rarity = get_string_input("What is the weapon's rarity? (normal, magic, rare, unique): ").capitalize()

    name = input("What is the name of this weapon? ").capitalize()

    
    if type == "Crossbow":
        reload_time = get_float_input("Enter reload time: ")
        weapon = Crossbow(type, name, dps, critical_chance, attacks_per_second, reload_time, quality, item_level, required_level, rarity)
    else:
        weapon = Weapon(type, name, dps, critical_chance, attacks_per_second, quality, item_level, required_level, rarity)

    weapon_list[name] = weapon

    print(f"{name}'s DPS is {dps} and Critical Chance is {weapon.critical_chance_str()}")

    run_input = True
    while run_input:
        run_again = input("Would you like to calculate another weapon or see the list of calculated weapons DPS? (y = yes, n = no, l = list): ").lower()
        if run_again == "l":
            for w in weapon_list.values():
                print(w)
        elif run_again == "y":
            run_input = False
        elif run_again == "n":
            print("Thank you for using the Path of Exile 2 DPS calculator")
            run_input = False
            power_on = False
        else:
            print("Invalid input. Please enter 'y', 'n', or 'l'.")