##########################################################################################################################################################################################################################################
help = '''``b뽑기`` ``[번호1]`` ``[번호2]`` ----- ``번호1`` ~ ``번호2``까지 수 중 하나를 뽑습니다.
``b청소`` ----- 채팅창을 깨끗하게 청소합니다.
``b색깔뽑기`` ----- 모든 색깔중 하나를 뽑습니다.
``b주사위`` ``[주사위갯수]`` ----- 주사위를 ``[주사위갯수]``만큼 굴립니다'''
##########################################################################################################################################################################################################################################
import discord
import random
import os
import re
import datetime
from openpyxl import load_workbook
from openpyxl import Workbook
import asyncio
import openpyxl
import requests
from json import loads
import time

col = 0x5cdd33
client = discord.Client()
now = datetime.datetime.now()
now_time = str(now.year) + '년 ' + str(now.month) + '월 ' + str(now.day) + '일  ' + str(now.hour) + '시 ' + str(now.minute) + '분 ' + str(now.second) + '초'

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game('"b도움" 입력 ㄱ')
    await client.change_presence(status = discord.Status.online, activity = game)

@client.event
async def on_message(message):
    a = message.author.id
    mention = '<@' + str(a) + '>'
    now = datetime.datetime.now()

    #도움말
    if message.content == 'b도움':
        embed = discord.Embed(title = ':orange_book:도움말',
                              description = help, color = col)
        embed.set_footer(text = now_time)
        await message.channel.send(mention, embed = embed)

    #뽑기
    if message.content.startswith('b뽑기'):
        drawing = message.content
        drawing = drawing.split(' ')
        if drawing[1] > drawing[2]:
            drawing3 = random.randint(int(drawing[2]), int(drawing[1]))
        else:
            drawing3 = random.randint(int(drawing[1]), int(drawing[2]))
        embed = discord.Embed(title = ':gift:뽑기결과', description = '**' + str(drawing3) + '**', color = col)
        embed.set_footer(text = now_time)
        await message.channel.send(mention, embed = embed)

    #청소
    if message.content == 'b청소':
        embed = discord.Embed(title = '채팅청소', description = '.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n.', color = col)
        embed.set_footer(text = now_time)
        await message.channel.send(embed = embed)

    #색깔뽑기
    if message.content == 'b색깔뽑기':
        random_col = random.randint(0x000000, 0xffffff)
        embed = discord.Embed(title = ':gift:색깔뽑기결과', description = '**' + str(hex(random_col)) + '**', color = random_col)
        embed.set_footer(text = now_time)
        await message.channel.send(mention, embed = embed)

    #주사위
    if message.content.startswith('b주사위'):
        a = 0
        dice_sum = 0
        random_dice = []
        dice_output = ''
        dice = message.content
        dice = dice.split(' ')
        dice_count = int(dice[1])
        for i in range(0, dice_count):
            random_dice.append(random.randint(1,6))
            dice_sum += random_dice[a]
        for i in range(0, dice_count):
            dice_output += '``' + str(i+1) + '번째 주사위 : ``' + str(random_dice[i]) + '\n'
        embed = discord.Embed(title = ':game_die:뽑은 주사위', description = dice_output + ':game_die:주사위 총합 : ' + str(dice_sum) + '\n:game_die:주사위 평균 : ' + str(float(dice_sum/dice_count)), color = col)
        embed.set_footer(text = now_time)
        await message.channel.send(mention, embed = embed)
        
client.run('NTAzODYyMDQyMTg5NjI3Mzkz.XODfDQ.w4PjJPZz5MTHMUO-KV7becZHFiM')










#if message.content.startswith('안녕'):
#        await message.channel.send('ㅎㅇ')
#if message.contet == '안녕':
#        await message.channel.send('ㅎㅇ')
#'<@' + str(a) + '>'
