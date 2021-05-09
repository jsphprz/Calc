import asyncio
import os
import discord
from discord.ext import commands
import math
from dotenv import load_dotenv

load_dotenv()

client = commands.AutoShardedBot(commands.when_mentioned_or('`'))
client.remove_command("help")

def add(x: float, y: float): 
    return x + y

def sub(x: float, y: float): 
    return x-y

def mult(x: float, y: float): 
    return x * y

def div(x: float, y: float): 
    return x / y

def sqrt(n: float): 
    return math.sqrt(n)

def inch2cm(n: float): 
    return n * 2.54

def cen2mm(n: float):
    return n * 10

def cen2inc(n: float):
    return n / 2.54

def kilo2mile(n: float): 
    return n / 1.609

def mile2km(n: float):  
    return n * 1.609

def fttoinch(n: float): 
    return n * 12

def inchtoft(n: float): 
    return n / 12

def celsius2fah(n: float): 
    return (n * 9/5) + 32

def fah2celsius(n: float): 
    return (n - 32) * 5/9

def kg2pounds(n: float):
    return n * 2.205

def lbstokg(n: float): 
    return n / 2.205

def tontokg(n: float): 
    return n * 907

def kgtoton(n: float):
    return n / 907


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('calculator | `help')) 
    print('Ready!')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", color = discord.Color.from_rgb(255,0,0))
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
    em.set_footer(text=f'Requested By - {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name = "Basic Math Operations", value = "``help basicmath`")
    em.add_field(name = "Conversion", value = "``help conv`")
    em.add_field(name = "Check Bot Latency", value = "``ping`", inline=False)
    await ctx.send(embed=em)

@help.command()
async def basicmath(ctx):
    em = discord.Embed(title = "Basic Math Operations", description = "Ex: `plsadd 4 3", color = discord.Color.from_rgb(118,247,140))
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name = "Addition", value = "``plsadd`", inline=False)
    em.add_field(name = "Subtraction", value = "``plssub`", inline=False)
    em.add_field(name = "Multiplication", value = "``plsmult`", inline=False)
    em.add_field(name = "Division", value = "``plsdiv`", inline=False)
    em.add_field(name = "Square Root", value = "``sqrtof`", inline=False)
    await ctx.send(embed=em)

page1 = discord.Embed(title = "Conversions", description="Ex: `in2cm 5",color = discord.Color.from_rgb(179,0,255))
page1.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
page1.add_field(name = "__**Length**__ \n Inch to Centimeter", value = "``in2cm`", inline=False)
page1.add_field(name = "Centimeter to Inch", value = "``cm2in`", inline=False)
page1.add_field(name = "Centimeter to Millimetre", value = "``cm2mm`", inline=False)
page1.add_field(name = "Centimeter to Inch", value = "``cm2in`", inline=False)
page1.add_field(name = "Kilometer to Mile", value = "``km2mi`", inline=False)
page1.add_field(name = "Mile to Kilometer", value = "``mi2km`", inline=False)
page1.add_field(name = "Foot to Inch", value = "``ft2in`", inline=False)
page1.add_field(name = "Inch to Foot", value = "``in2ft`", inline=False)

page2 = discord.Embed(title="Temperature", colour=discord.Colour.from_rgb(0,247,255))
page2.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
page2.add_field(name = "Celsius to Fahrenheit", value = "``cel2fah`", inline=False)
page2.add_field(name = "Fahrenheit to Celsius", value = "``fah2cel`", inline=False)

page3 = discord.Embed(title="Mass", colour=discord.Colour.from_rgb(213,255,0))
page3.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
page3.add_field(name = "Kilogram to Pound", value = "``kg2lbs`", inline=False)
page3.add_field(name = "Pound to Kilogram", value ="``lbs2kg`", inline=False)
page3.add_field(name = "Kilogram to Ton", value = "``kg2ton`", inline=False)
page3.add_field(name = "Ton to Kilogram", value = "``ton2kg`", inline=False)

client.help_pages = [page1, page2, page3]
@help.command()
async def conv(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] 
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=20.0)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0

            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])

#Commands

@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Latancy: {round(client.latency * 1000)}ms')

@client.command()
async def pls(ctx):
    await ctx.send("``Incomplete command! Please try again.``")

@client.command()
async def plsadd(ctx, x: float, y: float):
    res = add(x,y)
    await ctx.send("Result is: `" + str(res) +"`")

@client.command()
async def plssub(ctx, x: float, y: float):
    res = sub(x,y)
    await ctx.send("Result is: `" + str(res) +"`")

@client.command()
async def plsdiv(ctx, x: float, y: float):
    res = div(x,y)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: `" + str(deci) +"`")

@client.command()
async def plsmult(ctx, x: float, y: float):
    res = mult(x,y)
    await ctx.send("Result is: `" + str(res) +"`")

@client.command()
async def sqrtof(ctx, x: float):
    res = sqrt(x)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: `" + str(deci) +"`")

@client.command()
async def in2cm(ctx, x: float):
    res = inch2cm(x)
    await ctx.send("Result is: `"  + str(res) + "cm`")

@client.command()
async def cm2mm(ctx, x: float):
    res = cen2mm(x)
    await ctx.send("Result is: `"  + str(res) + "mm`")

@client.command()
async def cm2in(ctx, x: float):
    res = cen2inc(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `"  + str(deci) + " in`")

@client.command()
async def km2mi(ctx, x: float):
    res = kilo2mile(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " miles`")

@client.command()
async def mi2km(ctx, x: float):
    res = mile2km(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " km`")

@client.command()
async def ft2in(ctx, x: float):
    res = fttoinch(x)
    await ctx.send("Result is: `" + str(res) + " in`")

@client.command()
async def in2ft(ctx, x: float):
    res = inchtoft(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " ft`")

@client.command()
async def cel2fah(ctx, x: float):
    res = celsius2fah(x)
    await ctx.send("Result is: `"  + str(res) + "`°F`")

@client.command()
async def fah2cel(ctx, x: float):
    res = fah2celsius(x)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: `"  + str(deci) + "°C`")

@client.command()
async def kg2lbs(ctx, x: float):
    res = kg2pounds(x)
    deci = "{:.2f}".format(res)
    await ctx.send("Result is: `"  + str(deci) + " lbs`")

@client.command()
async def lbs2kg(ctx, x: float):
    res = lbstokg(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " kg`")

@client.command()
async def ton2kg(ctx, x: float):
    res = tontokg(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " kg`")

@client.command()
async def kg2ton(ctx, x: float):
    res = kgtoton(x)
    deci = "{:.3f}".format(res)
    await ctx.send("Result is: `" + str(deci) + " t`")

client.run(os.getenv("TOKEN"))
