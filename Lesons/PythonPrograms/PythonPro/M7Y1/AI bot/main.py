import discord
from discord.ext import commands
from setting import TOKEN
from check import get_class

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            photo_name = attachment.filename
            await attachment.save(f'images/{photo_name}')
            msg = await ctx.send('Please wait...')
            Give_acsses, Score= get_class(model_path='cl_model/keras_model.h5', labels_path='cl_model/labels.txt', image_path=f'images/{photo_name}')
            await msg.delete()
            if Give_acsses == 'Give access' and Score >=90:
                await ctx.send(f'You get acsses')
                user = ctx.author
                role = discord.utils.get(user.guild.roles, name="Give_acsses")
                await user.add_roles(role)
                
            else:
                await ctx.send(f'acsses denied')
                print(f"{Give_acsses} {Score}")
                
    else:
        await ctx.send("NO Attachments Detected!")




bot.run(TOKEN)