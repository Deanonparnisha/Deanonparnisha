#Creator by @DeanonParnisha

from asyncio import sleep
import random
from telethon import functions
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from .. import loader, utils

def register(cb):
    cb(GosuMod())

class GosuMod(loader.Module):
    """ты еблан да?"""
    strings = {'name': 'Госу от Деда'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def gosucmd(self, event):
        chat = '@Gosu_DeanonParnisha_bot'
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users= 1068175354 ))
                await event.client.send_message(chat, '/start')
                response = await response
            except YouBlockedUserError:
                await event.edit('<code>Разблокируй @Gosu_DeanonParnisha_bot</code>')
                return
            await event.edit(response.text)
