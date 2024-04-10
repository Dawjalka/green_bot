import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('Hej'):
        await message.channel.send("Cześć! Napisz z jakimi odpadami masz największy problem, a ja dam ci rozwiązanie! Wybierz: Plastik, Papier, Szkło lub Organiczne.")
    if message.content.startswith('Plastik'):
        await message.channel.send("Zamist plasktikowych butelek używaj butelek z filtrem. Z platikowych butelek można zrobić np. doniczki, karmnik, pojemnik.")
    if message.content.startswith('Papier'):
        await message.channel.send("Nie wyrzucaj kartek popisanych z jednej strony. Z role po papierze toaletowym można zrobić np: armatka konfetti, doniczki, zabawkę dla zwięrząt.")
    if message.content.startswith('Szkło'):
        await message.channel.send("Ogranicz kupowanie szklanych butelek. Ze szkła można zrobić: świeczniki, dozownik do mydła, po rozpuszczeniu szkła można użyć ponownie.")
    if message.content.startswith('Organiczne'):
        await message.channel.send("Można użyć je jako nawóz lub wrzucić do segregowanych odpadów bio, skąd trafią do biogazowni, gdzie zostaną przetworzone w energię.")

client.run(token['TU WPISZ SWÓJ TOKEN'])
