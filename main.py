import discord
from discord.ext import commands
from discord import app_commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ========== AQUI PEGAS TUS ID ==========
CANAL_BIOS_ID = 123456789012345678  # ID del canal donde manda bios
ROL_ID = 123456789012345678         # ID del rol @ que va a mencionar
# =======================================

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos slash")
    except Exception as e:
        print(e)

@bot.tree.command(name="setup", description="Configura el bot DARK BIO FF")
async def setup(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot configurado correctamente! Ya estoy 24/7")

bot.run(os.environ['TOKEN'])
