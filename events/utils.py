from django.conf import settings
from dhooks import Webhook, Embed
import datetime

hook = Webhook(settings.DISCORD_WEBHOOK)

def send_embed(request):
    embed = Embed(
        title=request.POST['title'],
        timestamp='now',
        color='5347285'
    )
    print(request.POST['time'])
    formatted_date = datetime.datetime.strptime(request.POST['time'], '%Y-%m-%d %H:%M').strftime('%A %-d %B %-I%p')
    print(formatted_date)
    embed.add_field(name="Location", value=request.POST['location'], inline=False)
    embed.add_field(name="Date and Time", value=formatted_date, inline=False)
    embed.add_field(name="Extra Information", value=request.POST['info'], inline=False)
    embed.set_footer(text="UWA Ethical Hacking Club 2019",
                     icon_url='https://images-ext-1.discordapp.net/external/3wjZZaOG21Ithgy7gMEZXsOAS07cVlwNw3741mVDSP8/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/594903351414620161/9086c3dea5e5779b4bf73b969e7f809c.png')
    hook.send(embed=embed)
    hook.send("@everyone")