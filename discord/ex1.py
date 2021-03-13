import discord
from discord.ext import commands,tasks
import random
import pandas as pd
import numpy as np
from tabulate import tabulate

bot = commands.Bot(command_prefix=['fennekon ','fenn '])
bot_token = 'ODEzMjc3NDMyNjQyNzk3NjA4.YDM9oQ.xvyyFovonSvOniAuLNjFQQsjl6c'


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to The Black Ocean! , please read the rules first. After you understand the rules We recommend you to go to the general-and-lession room.'
    )

@bot.event    
async def on_message(message):
    if message.author == bot.user:
        return

    if '  ' in message.content and 'fennekon' in message.content:
        await message.channel.send(f"Do not double-space to command me , I'm very confused (@ o @)")

    elif (any([True for x in ('thx','thk','thank') if x in message.content]) and (str(message.author) == "KuugenFox#5233") and ('fennekon' in message.content)):
        await message.channel.send(f'= w = :ok_hand:')

    elif ((('fennekon' in message.content) or ('fenn' in message.content)) and (random.randint(1,2)>=2)):
        await message.channel.send(f'= w =')
    
    await bot.process_commands(message)

@bot.command()
async def hello_test(ctx):
    #KuugenFox#5233 only can be use command
    if str(ctx.message.channel)!='KuugenFox#5233':
        return
    await ctx.send(f"```{pd.DataFrame({'a':[1,2],'b':[2,3]})}```")

@bot.command(aliases=['dicetrade','roll dicetrade'])
async def roll_dice(ctx):
    dice = ['buy','hold','sell']
    await ctx.send(f'dice result = {dice[random.randint(0,2)]} :laughing:')

@bot.command(aliases=['price','weight'])
async def price_weight(ctx,*,args):
    message = ctx.message.content

    if(len(args.split()[1].split(',')) % 2 != 0):
        raise commands.CommandNotFound
    
    if(message.startswith('fenn price weight') or message.startswith('fenn weight price')):
        vol_arr = np.array([float(i) for c,i in enumerate(args.split()[1].split(',')) if c%2!=0])
        price_arr = np.array([float(i) for c,i in enumerate(args.split()[1].split(',')) if c%2==0])
        price_weight = (sum(price_arr * vol_arr)+(sum(price_arr * vol_arr)*(.172128/100)))/sum(vol_arr)
        await ctx.send(f'{ctx.message.author.mention} your price is approx {round(price_weight,3)}')

    elif(message.startswith('fennekon price weight') or message.startswith('fennekon weight price')):
        vol_arr = np.array([float(i) for c,i in enumerate(args.split()[1].split(',')) if c%2!=0])
        price_arr = np.array([float(i) for c,i in enumerate(args.split()[1].split(',')) if c%2==0])
        price_weight = (sum(price_arr * vol_arr)+(sum(price_arr * vol_arr)*(.172128/100)))/sum(vol_arr)
        await ctx.send(f'{ctx.message.author.mention} your price is approx {round(price_weight,3)}')

    else:
        raise commands.CommandNotFound

#error handle triggered after clear.error
@bot.event
async def on_command_error(ctx,error):
    if(isinstance(error,commands.MissingRequiredArgument)):
        await ctx.send(f'{ctx.message.author.mention} command missing argument.')
    elif(isinstance(error,commands.CommandNotFound)):
        await ctx.send(f"{ctx.message.author.mention} sorry I don't understand your command.")
    else:
        print(error)
        await ctx.send(f"{ctx.message.author.mention} sorry I don't understand your command.")

bot.run(bot_token)

