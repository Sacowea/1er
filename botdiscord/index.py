import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';', description = 'im chuerking.')

@bot.command()
async def hola(ctx):
    await ctx.send('SAL DE MI PANTANO')

#Evento
@bot.event
async def on_ready():
    print('CHUERK IS READY ')
    await bot.change_presence(activity=discord.Streaming(name='CHUERKEANDO', url='www.twitch.tv/bgamerz4'))


bot.run('Njg2Mzc5NTY3NTY0NTg3MTM3.XmWXOg.buY-uxKVCvxer2PKdD7fyTn9rf4')


