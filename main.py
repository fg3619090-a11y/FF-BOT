import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ========== TU ID DEL CANAL ==========
CANAL_BIOS_ID = 1548464034632831036  # ID del canal
# =====================================

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
