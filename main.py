### IMPORTS ###
import discord
from random import randint
from discord.ext import commands
from discord import User
from discord.ext.commands import *
from discord.ext import tasks
import datetime
import json
import timefetch
from keep_alive import keep_alive
from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')

### STARTUP VARIABLES (and arrays ofc) ###
errorHandler_path = "logs/errors.txt"
loggerHandler_path = "logs/actions.txt"
theme_color = 0x89CFF0
mainmenu = [
  'donut',
  'cake',
  'cookie',
  'bagel',
  'sandwich'
]
barmenu = [
  'coffee',
  'plain water',
  'cappucchino',
  'cappucino',
  'cold brew coffee',
  'coldbrew coffee',
  'coldbrewcoffee',
  'coldbrew',
  'cold brew'
  'latte',
  'mocha',
  'chocolate milkshake',
  'chocomilkshake',
  'chocolatemilkshake',
  'choco milkshake',
  'boba',
  'boba tea',
  'boba milo'
]
## ITEMS ##
with open('db/currency.json', 'r') as f:
  global cc
  cc = json.load(f)
with open('db/inventory/cafe/bagel.json', 'r') as f:
  global bagel
  bagel = json.load(f)
with open('db/inventory/cafe/cake.json', 'r') as f:
  global cake
  cake = json.load(f)
with open('db/inventory/cafe/cookies.json', 'r') as f:
  global cookies
  cookies = json.load(f)
with open('db/inventory/cafe/donut.json', 'r') as f:
  global donut
  donut = json.load(f)
with open('db/inventory/cafe/sandwich.json', 'r') as f:
  global sandwich
  sandwich = json.load(f)
with open('db/inventory/cafe/bananas.json', 'r') as f:
  global bananas
  bananas = json.load(f)

with open('db/inventory/bar/coffee.json', 'r') as f:
  global coffee
  coffee = json.load(f)
with open('db/inventory/bar/plain_water.json', 'r') as f:
  global water
  water = json.load(f)
with open('db/inventory/bar/boba.json', 'r') as f:
  global boba
  boba = json.load(f)
with open('db/inventory/bar/choco_milkshake.json', 'r') as f:
  global chocomilkshake
  chocomilkshake = json.load(f)
with open('db/inventory/bar/mocha.json', 'r') as f:
  global mocha
  mocha = json.load(f)
with open('db/inventory/bar/coldbrew_coffee.json', 'r') as f:
  global coldbrew
  coldbrew = json.load(f)
with open('db/inventory/bar/cappucino.json', 'r') as f:
  global cappucino
  cappucino = json.load(f)
with open('db/inventory/bar/latte.json', 'r') as f:
  global latte
  latte = json.load(f)

## USERDB ##
with open('db/users.json', 'r') as f:
  global users
  users = json.load(f)
## CONFIG ##
with open('db/config.json', 'r') as f:
  global config
  config = json.load(f)

def save_data():
  with open(f'db/currency.json', 'w+') as f:
    json.dump(cc, f, indent=2)
  with open(f'db/inventory/cafe/cookies.json', 'w+') as f:
    json.dump(cookies, f, indent=2)
  with open(f'db/inventory/cafe/cake.json', 'w+') as f:
    json.dump(cake, f, indent=2)
  with open(f'db/inventory/cafe/bagel.json', 'w+') as f:
    json.dump(bagel, f, indent=2)
  with open(f'db/inventory/cafe/donut.json', 'w+') as f:
    json.dump(donut, f, indent=2)
  with open(f'db/inventory/cafe/sandwich.json', 'w+') as f:
    json.dump(sandwich, f, indent=2)
  with open(f'db/inventory/cafe/bananas.json', 'w+') as f:
    json.dump(bananas, f, indent=2)

  with open(f'db/inventory/bar/coffee.json', 'w+') as f:
    json.dump(coffee, f, indent=2)
  with open(f'db/inventory/bar/boba.json', 'w+') as f:
    json.dump(boba, f, indent=2)
  with open(f'db/inventory/bar/cappucino.json', 'w+') as f:
    json.dump(cappucino, f, indent=2)
  with open(f'db/inventory/bar/choco_milkshake.json', 'w+') as f:
    json.dump(chocomilkshake, f, indent=2)
  with open(f'db/inventory/bar/coldbrew_coffee.json', 'w+') as f:
    json.dump(coldbrew, f, indent=2)
  with open(f'db/inventory/bar/latte.json', 'w+') as f:
    json.dump(latte, f, indent=2)
  with open(f'db/inventory/bar/mocha.json', 'w+') as f:
    json.dump(mocha, f, indent=2)
  with open(f'db/inventory/bar/plain_water.json', 'w+') as f:
    json.dump(water, f, indent=2)
  
  with open(f'db/config.json', 'w+') as f:
    json.dump(config, f, indent=2)

### DEFINE CLASSES ###
class colors:
  cyan = '\033[96m'
  red = '\033[91m'
  green = '\033[92m'
  end = '\033[0m'

### ON_START ###
@client.event
async def on_ready():
  print('Έχουμε κατέχει {0.user}. Αυτό το sUssY bAkA (μπίνγκο στον Ίαν Μπογκς!) θα χρησιμοποιηθεί για το τελετουργικό της θυσίας για να ξυπνήσει τη κληρονόμο Γαία πριν από τα εφτά πανιά.'.format(client))
  print('==================================')
  print('Among us is not meta:')
  print(f'  Αφάνεια: {round(client.latency * 1000)}')
  print('==================================')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"customers | Type !help"))

### ERROR HANDLER ###
@client.event
async def on_command_error(ctx, error):
    current_time = timefetch.timenow
    if isinstance(error, CommandNotFound):
        await ctx.message.add_reaction('❔')
        with open(errorHandler_path, 'a') as f:
            f.write(f'[{current_time}] Ignoring exception at CommandNotFound. Details: This command does not exist.\n')
            f.close()
        print(f'[{current_time}] Ignoring exception at {colors.red}CommandNotFound{colors.end}. See {colors.green}"{errorHandler_path}"{colors.end} for more info.')
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f':warning: Don\'t use this command too fast! Please try again after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**')
        with open(errorHandler_path, 'a') as f:
            f.write(f'[{current_time}] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.\n')
            f.close()
        print(f'[{current_time}] Ignoring exception at {colors.red}CommandOnCooldown{colors.end}. See {colors.green}"{errorHandler_path}"{colors.end} for more info.')
    if isinstance(error, MissingRequiredArgument):
        await ctx.send(':warning: Your command has missing required argument(s)', delete_after=8)
        with open(errorHandler_path, 'a') as f:
            f.write(f'[{current_time}] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
            f.close()
        print(f'[{current_time}] Ignoring exception at {colors.red}MissingRequiredArgument{colors.end}. See {colors.green}"{errorHandler_path}"{colors.end} for more info.')
    if isinstance(error, MissingPermissions):
        await ctx.send(':x: You don\'t have permissions to use this command.', delete_after=8)
        with open(errorHandler_path, 'a') as f:
            f.write(f'[{current_time}] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
            f.close()
        print(f'[{current_time}] Ignoring exception at {colors.red}MissingPermissions{colors.end}. See {colors.green}"{errorHandler_path}"{colors.end} for more info.')
    if isinstance(error, BadArgument):
        await ctx.send(':x: Invalid argument.', delete_after=8)
        with open(errorHandler_path, 'a') as f:
            f.write(f'[{current_time}] Ignoring exception at BadArgument.\n')
            f.close()
        print(f'[{current_time}] Ignoring exception at {colors.red}BadArgument{colors.end}. See {colors.green}"{errorHandler_path}"{colors.end} for more info.')

### ON_MESSAGE ###
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if str(message.author.id) in cc:
    pass
  else:
    cc[str(message.author.id)] = 5000
  if str(message.author.id) in bagel:
    pass
  else:
    bagel[str(message.author.id)] = 0
  if str(message.author.id) in donut:
    pass
  else:
    donut[str(message.author.id)] = 0
  if str(message.author.id) in cake:
    pass
  else:
    cake[str(message.author.id)] = 0
  if str(message.author.id) in cookies:
    pass
  else:
    cookies[str(message.author.id)] = 0
  if str(message.author.id) in sandwich:
    pass
  else:
    sandwich[str(message.author.id)] = 0
  if str(message.author.id) in boba:
    pass
  else:
    boba[str(message.author.id)] = 0
  if str(message.author.id) in cappucino:
    pass
  else:
    cappucino[str(message.author.id)] = 0
  if str(message.author.id) in chocomilkshake:
    pass
  else:
    chocomilkshake[str(message.author.id)] = 0
  if str(message.author.id) in coffee:
    pass
  else:
    coffee[str(message.author.id)] = 0
  if str(message.author.id) in coldbrew:
    pass
  else:
    coldbrew[str(message.author.id)] = 0
  if str(message.author.id) in latte:
    pass
  else:
    latte[str(message.author.id)] = 0
  if str(message.author.id) in mocha:
    pass
  else:
    mocha[str(message.author.id)] = 0
  if str(message.author.id) in water:
    pass
  else:
    water[str(message.author.id)] = 0
  
  if str(message.guild.id) in config:
    pass
  else:
    config[str(message.guild.id)] = {"leveling": 1}
  save_data()

  if message.content.lower() == 'I came':
    await message.channel.send(f'Hi there, {message.author.mention}. <@&924868911973949442>, <@&924869506604613642>, <@&924873358095556641> your Café has a new customer!')

  if message.author.bot == False:
    with open('db/users.json', 'r') as f:
      users = json.load(f)
      await update_data(users, message.author)
      if config[str(message.guild.id)]['leveling'] == 1:
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
      else:
        pass
      with open('db/users.json', 'w') as f:
        json.dump(users, f)

  await client.process_commands(message)

### MAIN COMMANDS ###
@client.command(description='Works and gives you a random amount of CC')
@commands.cooldown(1, 300, commands.BucketType.user)
async def work(ctx):
  workcc = randint(34, 45)
  cc[str(ctx.message.author.id)] += workcc
  save_data()
  await ctx.send(f'You have made {workcc} CafeCurrency by working.')

@client.command(aliases=['bal', 'currency', 'bank'])
async def balance(ctx, user:User = None):
  show = None
  if user == None:
    show = ctx.message.author
  else:
    show = user
  embed = discord.Embed(title=f'{show.display_name}\'s CafeCurrency')
  embed.add_field(name='CafeCurrency', value=cc[str(show.id)])
  await ctx.reply(embed = embed)

@client.command(aliases=['inv'])
async def inventory(ctx, user:User = None):
  userID = ctx.message.author.id
  if user == None:
    pass
  else:
    userID = user.id
  embed = discord.Embed(title=f'{ctx.author.display_name}\'s Inventory', description=f'**Café Items**\nDonuts: {donut[str(userID)]}\nCake: {cake[str(userID)]}\nCookies: {cookies[str(userID)]}\nBagel: {bagel[str(userID)]}\nSandwich: {sandwich[str(userID)]}\n\n**Bar Items**\nCoffee: {coffee[str(userID)]}\nCappucino: {cappucino[str(userID)]}\nBoba: {boba[str(userID)]}\nLatte: {latte[str(userID)]}\nMocha: {mocha[str(userID)]}\nChoco Milkshake: {chocomilkshake[str(userID)]}\n Cold Brew Coffee: {coldbrew[str(userID)]}\nPlain Water: {water[str(userID)]}', color=theme_color)
  await ctx.send(embed=embed)

@client.command(desciption='Cook/bake some delicious food!', aliases=['cook', 'bake'])
@commands.cooldown(1, 180, commands.BucketType.user)
async def make(ctx):
  def check(msg):
    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
  await ctx.reply('What would you like to make? Type it in this channel.')
  msg = await client.wait_for("message", check=check)
  if msg.content in mainmenu:
    cookcc = 10
    cc[str(ctx.message.author.id)] += cookcc
    try:
      if msg.content.lower() == 'donut': donut[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'cake': cake[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'cookie': cookies[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'bagel': bagel[str(ctx.author.id)] += 1
    except:
      await ctx.send(':x: **An internal exception occured.** Please DM the developers with this error code: `internalexception@valueincrement#cook#make_cmd`')
    save_data()
    await ctx.send(f'{ctx.author.mention} just baked a {msg.content} and got {cookcc} CafeCurrency! Now go and serve that delicious meal! <:cookie:925292717813162024>')
  elif msg.content in barmenu:
    drinkcc = 5
    cc[str(ctx.message.author.id)] += drinkcc
    try:
      if msg.content.lower() == 'coffee': coffee[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'plain water': water[str(ctx.author.id)] += 1
      elif msg.content.lower() in ['cappucchino', 'cappucino']: cappucino[str(ctx.author.id)] += 1
      elif msg.content.lower() in ['cold brew coffee', 'coldbrew coffee', 'coldbrewcoffee', 'coldbrew', 'cold brew']: coldbrew[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'latte': latte[str(ctx.author.id)] += 1
      elif msg.content.lower() == 'mocha': mocha[str(ctx.author.id)] += 1
      elif msg.content.lower() in ['chocolate milkshake', 'chocolatemilkshake', 'chocomilkshake', 'choco milkshake']: chocomilkshake[str(ctx.author.id)] += 1
      elif msg.content.lower() in ['boba', 'boba tea', 'boba milk']: boba[str(ctx.author.id)] += 1
    except:
      await ctx.send(':x: **An internal exception occured.** Please DM the developers with this error code: `internalexception@valueincrement#drink#make_cmd`')
    save_data()
    await ctx.send(f'{ctx.author.mention} just made a {msg.content} and got {drinkcc} CafeCurrency! Now go and serve that drink! :latte: ')
  else:
    await ctx.reply(f'{msg.content} isn\'t a menu item. Please cook again by using `!cook`')

@client.command()
async def pay(ctx, user:User = None):
  if user == None:
    await ctx.reply(f'This isn\'t a valid user. Please pay again by using `!pay`')
    return
  elif user.id == ctx.author.id:
    await ctx.reply('You can\'t pay yourself! Pay again by using `!pay`')
    return
  else:
    pass
  def check(msg):
    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
  await ctx.send(f'How much would you like to pay?')
  msg = await client.wait_for("message", check=check)
  try:
    if int(msg.content) <= 0:
      await ctx.reply('You can\'t pay someone less than 1 CafeCurrency! Pay again with `!pay`')
      return
    else:
      pass
    cc[str(user.id)] += int(msg.content)
    cc[str(ctx.author.id)] -= int(msg.content)
    save_data()
    await ctx.reply(f'{ctx.author.mention} just gave {user.mention} {msg.content} CafeCurrency!')
  except:
    await msg.add_reaction('⚠')
    await ctx.reply('You can only give people CafeCurrency in non-numbers! Please pay again with `!pay`')

@client.command()
async def give(ctx, *, user:User = None):
  if user == None:
    await ctx.reply(f'This isn\'t a valid user. Please give the item again by using `!give`')
    return
  elif user.id == ctx.author.id:
    await ctx.reply('You can\'t give something to yourself! Give the item again by using `!give`')
    return
  else:
    pass
  def check(msg):
    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
  await ctx.reply(f'What would you want to give {user.display_name}? Type it here in this channel.')
  msg = await client.wait_for("message", check=check)
  if msg.content.lower() in mainmenu or barmenu:
    try:
      if msg.content.lower() == 'donut': 
        if donut[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          donut[str(ctx.author.id)] -= 1
          donut[str(user.id)] += 1
      elif msg.content.lower() == 'cake': 
        if cake[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          cake[str(ctx.author.id)] -= 1
          cake[str(user.id)] += 1
      elif msg.content.lower() == 'cookie': 
        if cookies[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          cookies[str(ctx.author.id)] -= 1
          cookies[str(user.id)] += 1
      elif msg.content.lower() == 'bagel': 
        if bagel[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          bagel[str(ctx.author.id)] -= 1
          bagel[str(user.id)] += 1
      elif msg.content.lower() == 'coffee': 
        if coffee[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          coffee[str(ctx.author.id)] -= 1
          coffee[str(user.id)] += 1
      elif msg.content.lower() == 'plain water': 
        if water[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          water[str(ctx.author.id)] -= 1
          water[str(user.id)] += 1
      elif msg.content.lower() in ['cappucchino', 'cappucino']: 
        if cappucino[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          cappucino[str(ctx.author.id)] -= 1
          cappucino[str(user.id)] += 1
      elif msg.content.lower() in ['cold brew coffee', 'coldbrew coffee', 'coldbrewcoffee', 'coldbrew', 'cold brew']: 
        if coldbrew[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          coldbrew[str(ctx.author.id)] -= 1
          coldbrew[str(user.id)] += 1
      elif msg.content.lower() == 'latte': 
        if latte[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          latte[str(ctx.author.id)] -= 1
          latte[str(user.id)] += 1
      elif msg.content.lower() == 'mocha': 
        if mocha[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          mocha[str(ctx.author.id)] -= 1
          mocha[str(user.id)] += 1
      elif msg.content.lower() in ['chocolate milkshake', 'chocolatemilkshake', 'chocomilkshake', 'choco milkshake']:
        if chocomilkshake[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          chocomilkshake[str(ctx.author.id)] -= 1
          chocomilkshake[str(user.id)] += 1
      elif msg.content.lower() in ['boba', 'boba tea', 'boba milk']: 
        if boba[str(ctx.author.id)] < 1:
          await ctx.reply('You don\'t have enough of those to give!')
          return
        else:
          boba[str(ctx.author.id)] -= 1
          boba[str(user.id)] += 1
      await ctx.reply(f'{ctx.author.mention} just gave {user.mention} a/an {msg.content}!')
    except:
      await ctx.send(':x: **An internal exception occured.** Please DM the developers with this error code: `internalexception@valueincrement#give_cmd`')
  else:
    await ctx.reply(f'{msg.content} isn\'t a valid item! Please give again by using `!give`')

@client.command()
async def ping(ctx):
  embed = discord.Embed(title='CaféBot Ping', description=f'Current Latency: {round(client.latency * 1000)}', color=theme_color)
  embed.set_footer(text='lol I think you have the wrong ping if you want to ping someone')
  await ctx.send(embed = embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(title='CaféBot Help', description='My prefix is `!`\n\n**Some very useful commands:**\n`!work`: `Works and gives you a random amount of CC`\n`!make`: `Cook some delicious food!`\n`!pay [User Ping]`: `Pay a cashier your CC!`\n`!give [User Ping]`: `Serve someone their food!`\n`!help`: `Generates this command`\n`!ping`: `Shows this bot\'s ping!`\n `!order`: `Orders food for you`\n `!daily`: `Claim your daily CC!`\n`!weekly`: `Claim your weekly CC!`\n`!leveltoggle`: `Enables or disables the leveling system for your server`', color=theme_color)
  embed.set_footer(text = 'More commands are coming soon')
  await ctx.send(embed = embed)

@client.command()
async def order(ctx):
  def check(msg):
    return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
  await ctx.reply('What would you like to order? Type it in this channel.')
  msg = await client.wait_for("message", check=check)
  if msg.content in mainmenu:
    await ctx.send(f'{ctx.author.mention} just ordered a {msg.content}!||<@&924873358095556641>|| ')
  elif msg.content in barmenu:
    await ctx.send(f'{ctx.author.mention} just ordered a {msg.content}!||<@&924873358095556641>|| ')
  else:
    await ctx.reply(f'{msg.content} isn\'t a menu item. Please order again by using `!order`')

@client.command()
async def endfight(ctx, user:User = None):
  if user == None:
    await ctx.reply(f'This isn\'t a valid user.')
    return
  elif user.id == ctx.author.id:
    await ctx.reply('ehhhhhhhhhhhhhhhhhhh')
    return
  else:
    await ctx.reply('HAI I AM SO CUTE uwu BAI SISTERS')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
  cc[str(ctx.message.author.id)] += 200
  save_data()
  embed = discord.Embed(title='Your Daily', description=f'You recieved `200` CC today!', color=theme_color)
  embed.set_footer(text = 'More commands are coming soon')
  await ctx.send(embed = embed)

@client.event
async def on_member_join(member):
  with open('db/users.json', 'r') as f:
    users = json.load(f)
  await update_data(users, member)
  with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)

async def update_data(users, user):
  if not f'{user.id}' in users:
    users[f'{user.id}'] = {}
    users[f'{user.id}']['experience'] = 0
    users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
  users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
  experience = users[str(user.id)]['experience']
  lvl_start = users[str(user.id)]['level']
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.channel.send(f'{user.mention} is now level {lvl_end}')
    users[str(user.id)]['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
  if member == None:
    e = discord.Embed(title=f'{ctx.author.display_name}\'s Level', color=theme_color)
    e.add_field(name='Level', value=int(users[str(ctx.author.id)]['level']), inline=True)
    e.add_field(name='XP', value=int(users[str(ctx.author.id)]['experience']), inline=True)
    await ctx.send(embed=e)
  else:
    e = discord.Embed(title=f'{member.id.display_name}\'s Level', color=theme_color)
    e.add_field(name='Level', value=int(users[str(member.id)]['level']), inline=True)
    e.add_field(name='XP', value=int(users[str(member.id)]['experience']), inline=True)
    await ctx.send(embed=e)

@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(ctx):
  cc[str(ctx.message.author.id)] += 1000
  save_data()
  embed = discord.Embed(title='Your Weekly', description=f'You recieved `1000` CC this week! Come back soon', color=theme_color)
  embed.set_footer(text = 'More commands are coming soon')
  await ctx.send(embed = embed)

@slash.slash(name='membercount', description='Shows the total number of members in the server.')
async def membercount(ctx:SlashContext):
  totalmembers = ctx.guild.member_count
  embed=discord.Embed(title=f"{ctx.guild.name} Member Count", color=theme_color)
  embed.add_field(name="Total Members", value=int(totalmembers), inline=False)
  embed.set_footer(text="Bots included")
  await ctx.send(embed=embed)

@client.command(aliases=['lvltoggle', 'levelingtoggle'])
async def leveltoggle(ctx):
  if config[str(ctx.guild.id)]['leveling'] == 0:
    config[str(ctx.guild.id)]['leveling'] = 1
    await ctx.reply('Leveling system enabled in this server.')
  elif config[str(ctx.guild.id)]['leveling'] == 1:
    config[str(ctx.guild.id)]['leveling'] = 0
    await ctx.reply('Leveling system disabled in this server.')
  else:
    await ctx.send(':x: An internal error occured. Try again later.')
  save_data()

@slash.slash(name='leveltoggle', description='Switches on or off the leveling system in this server')
async def _leveltoggle(ctx:SlashContext):
  if config[str(ctx.guild.id)]['leveling'] == 0:
    config[str(ctx.guild.id)]['leveling'] = 1
    await ctx.reply('Leveling system enabled in this server.')
  elif config[str(ctx.guild.id)]['leveling'] == 1:
    config[str(ctx.guild.id)]['leveling'] = 0
    await ctx.reply('Leveling system disabled in this server.')
  else:
    await ctx.send(':x: An internal error occured. Try again later.')
  save_data()

@slash.slash(name='ping', description='Shows the bot\'s latency.')
async def _ping(ctx:SlashContext):
  embed = discord.Embed(title='CaféBot Ping', description=f'Current Latency: {round(client.latency * 1000)}', color=theme_color)
  embed.set_footer(text='lol I think you have the wrong ping if you want to ping someone')
  await ctx.send(embed = embed)

@slash.slash(name='help', description='Do you need help?')
async def _help(ctx:SlashContext):
  embed = discord.Embed(title='CaféBot Help', description='My prefix is `!`\n\n**Some very useful commands:**\n`!work`: `Works and gives you a random amount of CC`\n`!make`: `Cook some delicious food!`\n`!pay [User Ping]`: `Pay a cashier your CC!`\n`!give [User Ping]`: `Serve someone their food!`\n`!help`: `Generates this command`\n`!ping`: `Shows this bot\'s ping!`\n `!order`: `Orders food for you`\n `!daily`: `Claim your daily CC!`\n`!weekly`: `Claim your weekly CC!`\n`!leveltoggle`: `Enables or disables the leveling system for your server`', color=theme_color)
  embed.set_footer(text = 'More commands are coming soon')
  await ctx.send(embed = embed)

keep_alive()

### BOT TOKEN ###
client.run('OTI1MTcyMjE4MjgyMDA4NTk2.YcpPxQ.KdIAekk-clTmDJBgTUGT9yQzKyY')