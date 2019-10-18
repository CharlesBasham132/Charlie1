#ask user to input lives, energy and shield data
print("please enter the number of lives")
bot_lives = int(input())

print("please enter the energy level")
bot_energy_level = int(input())

print("please enter the sheild level")
bot_sheild_level = int(input())
#print levels
print("lives:", "♥" * bot_lives)
print("energy level:", "☼" * bot_energy_level)
print("shield level:", "♦" * bot_sheild_level)