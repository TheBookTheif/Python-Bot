import random
import discord
from discord.ext import commands

class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'EVENT : Welcome {0.mention} to this cursed shithole called {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

    async def on_member_remove(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'EVENT : The ass of {0.mention} was hardcore kicked !'.format(member,guild)
            await guild.system_channel.send(to_send)


bot = MyClient(command_prefix='?')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Latency -  {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball','8bal','ball8','ball'])
async def _8ball(ctx, *, _8ball_question):
    _8ball_responses = ['Yes','No','Kachow Da','Kachow Ne','Madjarova taka kaza','EI JINA','Ako kihnesh shte te izritam ot chas','badumc','Teo e straight','thats what she said','wow>liga','Vreme ti e za boomer doomer','kus ti e jivei s tva','dobre ama nqma da e dobre','tiho tam','margulan perma ban pls']
    await ctx.send(f'Question: {_8ball_question}\nAnswer: {random.choice(_8ball_responses)}')

@bot.command()
async def rnd(ctx, *, rnd_s):
    print("+"+rnd_s+"+")
    print(len(rnd_s))
    tmp = 0
    rnd_list = []
    for i in range(0,len(rnd_s)):
        if(rnd_s[i].isdigit()):
            tmp*=10;
            tmp+=int(rnd_s[i])
        else:
            rnd_list.append(tmp)
            print(tmp)
            tmp = 0
    if(tmp!=0):
        rnd_list.append(tmp)
        print(tmp)
        tmp = 0
    if(len(rnd_list)!=2):
        await ctx.send(f'Probably invalid')
    else:
        numbers_to_choose = []
        for i in range(rnd_list[0],rnd_list[1]+1):
            numbers_to_choose.append(i)
        await ctx.send(f'I have chosen the legendary number = {random.choice(numbers_to_choose)}')

@bot.command()
async def command(ctx, member: discord.Member):
    await ctx.send(member.avatar_url)

@bot.command()
async def say(ctx,text_to_send):
    await ctx.send(text_to_send)

@bot.command()
async def choose_random_5(ctx):
    people = {1:"Aleks",2:'Simo',3:'Valeri',4:'Koko',5:'Paraskov',6:'Deni',7:'Botko',8:'Dumo',9:'Teo',10:'Bisera'}
    teams = []
    for i in range(1,11):
        teams.append(i)

    await ctx.send(f'Team 1 : ')
    for i in range(1,6):
        key = random.choice(teams)
        result = people.pop(key, None)
        while result==None:
            key = random.choice(teams)
            result = people.pop(key, None)
        await ctx.send(f'{result}')
        #del people[key]

    await ctx.send(f'Team 2 : ')
    for i in range(6, 11):
        key = random.choice(teams)
        result = people.pop(key, None)
        while result == None:
            key = random.choice(teams)
            result = people.pop(key, None)
        await ctx.send(f'{result}')
        #del people[key]

bot.run('NjkyNDU4NzEwNjM0ODU2NTQ4.Xn0YkQ.kQtCDYMxAAXIpi-scTpacnbZySo')

