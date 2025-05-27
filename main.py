import discord
from discord.ext import commands 
import requests
import pyttsx3
from Examen import obtener_pregunta_aleatoria

Puntos = 0
intents = discord.Intents.default()
intents.message_content = True

engine = pyttsx3.init()

intents = discord.Intents.default() 
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)


def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t&lang=es"
    response = requests.get(base_url)
    if response.status_code == 200: 
        return response.text.strip()
    else:   
        return "No se pudo obtener la información del clima. Por favor, inténtalo más tarde."
 

@bot.command()
async def meme(ctx):
    await ctx.send(f'En en link que ven podran ver y desarrollar memes de gran calidad http://127.0.0.1:5000!')
    speak(f'En en link que ven podran ver y desarrollar memes de gran calidad http://127.0.0.1:5000!')



@bot.command()
async def ayuda(ctx):
    """Muestra una lista de comandos disponibles y su descripción."""
    embed = discord.Embed(
        title="Comandos Disponibles",
        description="Estos son los comandos que puedes utilizar:",
        color=0x1ABC9C
    )
    embed.add_field(name="$hola", value="Saluda al bot.", inline=False)
    embed.add_field(name="$clima", value="Obtiene información del estado del clima actual en una ciudad", inline=False)
    embed.add_field(name="$ayuda", value="Muestra este mensaje de ayuda.", inline=False)
    embed.add_field(name="$masinfo", value="Muestra enlaces para obtener mas información.", inline=False)
    embed.add_field(name="$inundaciones", value="Muestra información sobre inundaciones relacionadas al cambio climático.", inline=False)
    embed.add_field(name="$tornados", value="Muestra información sobre tornados extremos.", inline=False)
    embed.add_field(name="$sequias", value="Muestra información sobre sequías prolongadas.", inline=False)
    embed.add_field(name="$catastrofes", value="Muestra información sobre catástrofes climáticas.", inline=False)
    embed.add_field(name="$trivia", value="Inicia un sencillo juego de trivia sobre cambio climático.", inline=False)
    await ctx.send(embed=embed)


def GET_weather(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C\n\nTemperatura: %t\nViento: %w\nHumedad: %h\nAmanecer: %S\nAtardecer: %s&lang=es"
    response = requests.get(base_url) 
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "No se pudo obtener la información del clima. Por favor, inténtalo más tarde."  # Retornar el mensaje de error    


@bot.command()
async def Examen(ctx): 
    global Puntos
    """Inicia un Examen sobre el cambio climático."""
    pregunta_actual = obtener_pregunta_aleatoria()
    
    embed = discord.Embed(
        title="Trivia sobre Cambio Climático",
        description=pregunta_actual['pregunta'],
        color=0x2ECC71
    )
    
    opciones = "\n".join(pregunta_actual['opciones'])
    embed.add_field(name="Opciones", value=opciones, inline=False)
    embed.set_footer(text="Responde con A, B, C o D")
    
    await ctx.send(embed=embed)
    speak(f"{pregunta_actual['pregunta']}\n{opciones}")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in ["A", "B", "C", "D"]
    
    try:
        msg = await bot.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        embed_timeout = discord.Embed(
            title="¡Tiempo agotado!",
            description=f"La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}",
            color=0xE74C3C
        )
        await ctx.send(embed=embed_timeout)
        speak(f"Tiempo agotado. La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}")
        return
    
    if msg.content.upper() == pregunta_actual['respuesta']:
        embed_correct = discord.Embed(
            title="¡Correcto!",
            description=pregunta_actual['explicacion'],
            color=0x2ECC71
            
        )
        await ctx.send(embed=embed_correct)
        speak(f"Correcto. {pregunta_actual['explicacion']}")
        Puntos += 1
    else:
        embed_incorrect = discord.Embed(
            title="Incorrecto",
            description=f"La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}",
            color=0xE74C3C
        )
        await ctx.send(embed=embed_incorrect)
        speak(f"Incorrecto. La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}")



def speak(text):
    engine.say(text)
    engine.runAndWait()


@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')


@bot.command()
async def weather(ctx, *, city):
    weather_info = get_weather(city) 
    await ctx.send(f"Clima en {city}: {weather_info}")
    speak(weather_info)


bot.run("")