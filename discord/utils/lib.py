import discord

COLOR_INFO = 5347285
COLOR_SUCCESS = 2664261
COLOR_DANGER = 14431557
COLOR_WARNING = 16761095


def checkBotLoop(message, client):
    if message.author == client.user:
        return