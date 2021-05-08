from asyncio import sleep
import os
import discord
from discord.ext import commands
import math
from dotenv import load_dotenv

load_dotenv()

client = commands.AutoShardedBot(commands.when_mentioned_or('`'))
client.remove_command("help")

def add(x: float, y: float): #Addition
    return x + y

def sub(x: float, y: float): #Subtraction
    return x-y

def mult(x: float, y: float): #Multiplication
    return x * y

def div(x: float, y: float): #Division
    return x / y

def sqrt(n: float): #Square root of n
    return math.sqrt(n)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('calculator | `help')) #Discord status
    print('Ready!')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help")
    em.add_field(name = "Addition", value = "`plsadd")
    em.add_field(name = "Subtraction", value = "`plssub")
    em.add_field(name = "Multiplication", value = "`plsmult")
    em.add_field(name = "Division", value = "`plsdiv")
    em.add_field(name = "Square Root", value = "`sqrtof")

    await ctx.send(embed=em)

#Commands

@client.command()
async def pls(ctx):
    await ctx.send("``Incomplete command! Please try again.``")

@client.command()
async def plsadd(ctx, x: float, y: float):
    res = add(x,y)
    await ctx.send("Result is: " + str(res))

@client.command()
async def plssub(ctx, x: float, y: float):
    res = sub(x,y)
    await ctx.send("Result is: " + str(res))

@client.command()
async def plsdiv(ctx, x: float, y: float):
    res = div(x,y)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: " + str(deci))

@client.command()
async def plsmult(ctx, x: float, y: float):
    res = mult(x,y)
    await ctx.send("Result is: " + str(res))

@client.command()
async def sqrtof(ctx, x: float):
    res = sqrt(x)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: " + str(deci))

client.run(os.getenv("TOKEN"))
