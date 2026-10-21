from FortniteBot import FortniteBot

bot1 = FortniteBot("Chat")
bot2 = FortniteBot("R2-D2")
bot3 = FortniteBot("AM")

bot1.take_damage(5)
bot2.take_damage(10)

print(bot1.health)  # Output: 95
print(bot2.health)  # Output: 90
print(bot3.health)  # Output: 100