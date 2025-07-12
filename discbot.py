import asyncio
import os
import math
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('`'), intents=intents)
client.remove_command("help")

def add(x, y): return x + y
def sub(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y
def sqrt(n): return math.sqrt(n)

def inch2cm(n): return n * 2.54
def cen2mm(n): return n * 10
def cen2inc(n): return n / 2.54
def kilo2mile(n): return n / 1.609
def mile2km(n): return n * 1.609
def fttoinch(n): return n * 12
def inchtoft(n): return n / 12
def celsius2fah(n): return (n * 9/5) + 32
def fah2celsius(n): return (n - 32) * 5/9
def kg2pounds(n): return n * 2.205
def lbstokg(n): return n / 2.205
def tontokg(n): return n * 907
def kgtoton(n): return n / 907

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="my peen | `help", url='https://www.twitch.tv/amouranth'))
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", color=discord.Color.red())
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.display_avatar.url)
    em.add_field(name="Basic Math Operations", value="`help basicmath`")
    em.add_field(name="Conversion", value="`help conv`")
    em.add_field(name="Check Bot Latency", value="`ping`", inline=False)
    em.add_field(name="GitHub page", value="`github`", inline=False)
    await ctx.send(embed=em)

@help.command()
async def basicmath(ctx):
    em = discord.Embed(title="Basic Math Operations", description="Ex: `plsadd 4 3", color=discord.Color.green())
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png')
    em.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.display_avatar.url)
    em.add_field(name="Addition", value="`plsadd`", inline=False)
    em.add_field(name="Subtraction", value="`plssub`", inline=False)
    em.add_field(name="Multiplication", value="`plsmult`", inline=False)
    em.add_field(name="Division", value="`plsdiv`", inline=False)
    em.add_field(name="Square Root", value="`sqrtof`", inline=False)
    await ctx.send(embed=em)

client.help_pages = [
    discord.Embed(
        title="Conversions",
        description="Ex: `in2cm 5",
        color=discord.Color.purple()
    ).set_thumbnail(
        url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png'
    ).add_field(name="Inch to Centimeter", value="`in2cm`", inline=False)
     .add_field(name="Centimeter to Inch", value="`cm2in`", inline=False)
     .add_field(name="Centimeter to Millimetre", value="`cm2mm`", inline=False)
     .add_field(name="Kilometer to Mile", value="`km2mi`", inline=False)
     .add_field(name="Mile to Kilometer", value="`mi2km`", inline=False)
     .add_field(name="Foot to Inch", value="`ft2in`", inline=False)
     .add_field(name="Inch to Foot", value="`in2ft`", inline=False),

    discord.Embed(
        title="Temperature",
        color=discord.Color.teal()
    ).set_thumbnail(
        url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png'
    ).add_field(name="Celsius to Fahrenheit", value="`cel2fah`", inline=False)
     .add_field(name="Fahrenheit to Celsius", value="`fah2cel`", inline=False),

    discord.Embed(
        title="Mass",
        color=discord.Color.from_rgb(213, 255, 0)
    ).set_thumbnail(
        url='https://cdn.discordapp.com/attachments/840261018760380450/840825421604192256/calc.png'
    ).add_field(name="Kilogram to Pound", value="`kg2lbs`", inline=False)
     .add_field(name="Pound to Kilogram", value="`lbs2kg`", inline=False)
     .add_field(name="Kilogram to Ton", value="`kg2ton`", inline=False)
     .add_field(name="Ton to Kilogram", value="`ton2kg`", inline=False)
]

@help.command()
async def conv(ctx):
    buttons = ["⏪", "⬅", "➡", "⏩"]
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])
    for button in buttons:
        await msg.add_reaction(button)

    def check(reaction, user):
        return user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=check)
        except asyncio.TimeoutError:
            break
        else:
            previous = current
            if reaction.emoji == "⏪":
                current = 0
            elif reaction.emoji == "⬅" and current > 0:
                current -= 1
            elif reaction.emoji == "➡" and current < len(client.help_pages) - 1:
                current += 1
            elif reaction.emoji == "⏩":
                current = len(client.help_pages) - 1

            await msg.remove_reaction(reaction.emoji, ctx.author)
            if previous != current:
                await msg.edit(embed=client.help_pages[current])

@client.command()
async def ping(ctx):
    await ctx.send(f'Latency: **{round(client.latency * 1000)}ms**')

@client.command()
async def github(ctx):
    await ctx.send('https://github.com/jsphprz/Calc')

@client.command()
async def pls(ctx):
    await ctx.send("`Incomplete command! Please try again.`")

@client.command()
async def plsadd(ctx, x: float, y: float): await ctx.send(f"Result is: `{add(x, y)}`")
@client.command()
async def plssub(ctx, x: float, y: float): await ctx.send(f"Result is: `{sub(x, y)}`")
@client.command()
async def plsmult(ctx, x: float, y: float): await ctx.send(f"Result is: `{mult(x, y)}`")
@client.command()
async def plsdiv(ctx, x: float, y: float): await ctx.send(f"Result is: `{div(x, y):.2f}`")
@client.command()
async def sqrtof(ctx, x: float): await ctx.send(f"Result is: `{sqrt(x):.2f}`")

@client.command()
async def in2cm(ctx, x: float): await ctx.send(f"Result is: `{inch2cm(x):.2f} cm`")
@client.command()
async def cm2mm(ctx, x: float): await ctx.send(f"Result is: `{cen2mm(x):.2f} mm`")
@client.command()
async def cm2in(ctx, x: float): await ctx.send(f"Result is: `{cen2inc(x):.3f} in`")
@client.command()
async def km2mi(ctx, x: float): await ctx.send(f"Result is: `{kilo2mile(x):.3f} miles`")
@client.command()
async def mi2km(ctx, x: float): await ctx.send(f"Result is: `{mile2km(x):.3f} km`")
@client.command()
async def ft2in(ctx, x: float): await ctx.send(f"Result is: `{fttoinch(x)} in`")
@client.command()
async def in2ft(ctx, x: float): await ctx.send(f"Result is: `{inchtoft(x):.3f} ft`")
@client.command()
async def cel2fah(ctx, x: float): await ctx.send(f"Result is: `{celsius2fah(x):.2f} °F`")
@client.command()
async def fah2cel(ctx, x: float): await ctx.send(f"Result is: `{fah2celsius(x):.2f} °C`")
@client.command()
async def kg2lbs(ctx, x: float): await ctx.send(f"Result is: `{kg2pounds(x):.2f} lbs`")
@client.command()
async def lbs2kg(ctx, x: float): await ctx.send(f"Result is: `{lbstokg(x):.3f} kg`")
@client.command()
async def ton2kg(ctx, x: float): await ctx.send(f"Result is: `{tontokg(x):.3f} kg`")
@client.command()
async def kg2ton(ctx, x: float): await ctx.send(f"Result is: `{kgtoton(x):.3f} t`")

keep_alive()
client.run(os.getenv("TOKEN"))
