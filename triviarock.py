import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'hello...purchase the subscription quickly and easily just do what bot says')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'A':
        await client.send_message(message.channel,'Price of indian is rs50.Do you Want?(Yes/No)')
    if message.content == 'B':
        await client.send_message(message.channel,'Price of international is 30.Do you Want?1 for yes and 2 for no')
    if message.content == 'C':
        await client.send_message(message.channel,'Price of both national and international is 75.Do you Want?3 for yes and 4 for no')
    if message.content == 'No':
        await client.send_message(message.channel,'ok no problem u can contact us anytime ')
    if message.content == '2':
        await client.send_message(message.channel,'ok no problem u can contact us anytime ')
    if message.content == '4':
        await client.send_message(message.channel,'ok no problem u can contact us anytime  ')
    if message.content == 'Yes':
        em = discord.Embed(description='')
        em.set_image(url='https://media.discordapp.net/attachments/545865168966647820/545875046904889345/1549700503301-1.jpg?width=168&height=301')
        await client.send_message(message.channel, embed=em)
    if message.content == '1':
        em = discord.Embed(description='')
        em.set_image(url='https://media.discordapp.net/attachments/545865168966647820/545875046904889345/1549700503301-1.jpg?width=168&height=301')
        await client.send_message(message.channel, embed=em)
    if message.content == '3':
        em = discord.Embed(description='')
        em.set_image(url='https://media.discordapp.net/attachments/545865168966647820/545875046904889345/1549700503301-1.jpg?width=168&height=301')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Yes':
        await client.send_message(message.channel,'Pay Rs50 on this code Or pay on this link https://p-y.tm/r-axjmc and give screenshot in #:moneybag:payment-proof:moneybag:')
    if message.content == '1':
        await client.send_message(message.channel,'Pay ₹30 on this code or click https://p-y.tm/BfY-er2 to pay and give screenshot in #:moneybag:payment-proof:moneybag:')
    if message.content == '3':
        await client.send_message(message.channel,'Pay ₹75 on this code OR Click https://p-y.tm/gaK-1cU and give screenshot in #:moneybag:payment-proof:moneybag:')
    if message.content == 'Help':
        await client.send_message(message.channel,'Hello:blush:..This bot helps you to buy our access of answers of all trivia just type- Subscribe')
    if message.content == 'Subscribe':
        await client.send_message(message.channel,'Thank you for contacting our subscription bot:blush: :blush: Please select one of the packages: :regional_indicator_a:For Only Indian subcription :regional_indicator_b:For international subscription :regional_indicator_c: For Both indain and international')
client.run('NTQ1ODYyNTM3OTIxNDI5NTA1.D0gOpg.omq36xbU1m8EpRth-HL1uOKWCZI')
