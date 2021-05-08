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

#Conversions
def inch2cm(n: float): #inches to cm conversion
    return n * 2.54

def cen2mm(n: float): #centimeter to millimeter conversion
    return n * 10

def cen2inc(n: float): #centimeter to inch
    return n / 2.54



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('calculator | `help')) #Discord status
    print('Ready!')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", color = discord.Color.green())
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name = "Basic Math Operations", value = "`help basicmath")
    em.add_field(name = "Conversion", value = "`help conv")
    await ctx.send(embed=em)

@help.command()
async def basicmath(ctx):
    em = discord.Embed(title = "Basic Math Operations", description = "Ex: `plsadd 4 3", color = discord.Color.red())
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name = "Addition", value = "``plsadd`", inline=False)
    em.add_field(name = "Subtraction", value = "``plssub`", inline=False)
    em.add_field(name = "Multiplication", value = "``plsmult`", inline=False)
    em.add_field(name = "Division", value = "``plsdiv`", inline=False)
    em.add_field(name = "Square Root", value = "``sqrtof`", inline=False)
    await ctx.send(embed=em)

@help.command()
async def conv(ctx):
    em = discord.Embed(title = "Conversions", description = "Ex: `in2cm 5", color = discord.Color.red())
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name = "Inch to Centimeter", value = "``in2cm`", inline=False)
    em.add_field(name = "Centimeter to Inch", value = "``cm2in`", inline=False)
    em.add_field(name = "Centimeter to Millimetre", value = "``cm2mm`", inline=False)
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

#Conversion

#inch to cm
@client.command()
async def in2cm(ctx, x: float):
    res = inch2cm(x)
    await ctx.send("Result is: "  + str(res) + "cm")

#centimeter to millimetre
@client.command()
async def cm2mm(ctx, x: float):
    res = cen2mm(x)
    await ctx.send("Result is: "  + str(res) + "mm")

#centimeter to inch
@client.command()
async def cm2in(ctx, x: float):
    res = cen2inc(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: "  + str(deci) + " in")

client.run(os.getenv("TOKEN"))
