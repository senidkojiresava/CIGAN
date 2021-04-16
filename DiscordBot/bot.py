import discord
from discord.ext import commands
from random import randint


client =commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Volim cigane")

@client.command()
async def cigan(x):
    await x.send("Mama ti je grda")
@client.command()
async def kac(y):
    await y.send("kac ima maloga")
@client.command()
async def random(c):
    a=randint(0,100)
    await c.send(a)
@client.command()
async def stefan(slika):
    ime="stefan"
    ime+=str(randint(1,7))
    ime+=".png"
    await slika.send(file=discord.File(ime))
@client.command()
async def vito(slika):
    ime1="vito"
    ime1+=str(randint(1,6))
    ime1+=".png"
    await slika.send(file=discord.File(ime1))
client.run("ODMyNTc1ODY1MTQxMDY3Nzc2.YHlysg.tJhOYkqmWqcP6uZGcPNQ0RWHLFY")
