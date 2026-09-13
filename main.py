import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

CANAL_BIOS_ID = 1548464034632831036  # Tu canal

# LISTA DE BIOS FF - AGREGA LAS TUYAS
BIOS_FF = [
    "❤️‍🔥 ᴇʟ ᴅɪᴀʙʟᴏ ʀᴇɢʀᴇꜱᴏ ❤️‍🔥",
    "⚡ ᴄᴀʙᴇᴢᴀ ᴏ ɴᴀᴅᴀ ⚡",
    "💀 ꜱᴏʟᴏ ᴅɪᴏꜱ ᴍᴇ ᴊᴜᴢɢᴀ 💀",
    "🔥 ᴍᴠᴘ ᴏ ɴᴀᴅᴀ 🔥"
]

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    mandar_bios.start()  # Empieza a mandar bios solo
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos slash")
    except Exception as e:
        print(e)

@tasks.loop(hours=1)  # Cada 1 hora manda bio
async def mandar_bios():
    canal = bot.get_channel(CANAL_BIOS_ID)
    if canal:
        bio = random.choice(BIOS_FF)
        await canal.send(f"**DARK BIO FF**\n```{bio}```")

@bot.tree.command(name="setup", description="Configura el bot DARK BIO FF")
async def setup(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot configurado! Mandaré bios cada 1 hora")

@bot.tree.command(name="bio", description="Manda una bio al instante")
async def bio(interaction: discord.Interaction):
    bio = random.choice(BIOS_FF)
    await interaction.response.send_message(f"**DARK BIO FF**\n```{bio}```")

bot.run(os.environ['TOKEN'])
