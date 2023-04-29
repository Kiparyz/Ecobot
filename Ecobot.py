import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет! Хочешь почувствовать себя на месте директора экологии? $ecoyes - да / $econo - нет.")


@bot.command()
async def eco_yes(ctx):
    await ctx.send(f"https://dialogs.yandex.ru/store/skills/d4d7dec6-sohrani-ekologiyu - Почувствуй себя на месте директора экологии и реши глобальную проблему")


@bot.command()
async def eco_no(ctx):
    await ctx.send(f"Ну как хочешь")



bot.run("MTA5MjAzNDQ2MzkwMDM3MzA2Mg.GjLMCz.FomU5uwHJJMzkXOmTpv3iWwY9klHfUUAf_cz8g")