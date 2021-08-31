from .. import loader, utils
import logging
import time

logger = logging.getLogger(__name__)

def register(cb):
	cb(TagallMod())


@loader.tds
class TagallMod(loader.Module):
	"""Tagall"""
	strings = {
		"name": "TagAll", "subscribe to": "helpmv"
	}

	async def client_ready(self, client, db):
		self.client = client
		
	def __init__(self):
		self.name = self.strings['name']
		
		
	
	@loader.sudo
	async def tagallcmd(self, message):
		args = utils.get_args(message)
		tag_ = 5
		notext = False
		if args:
			if args[0].isdigit():
				tag_ = int(args[0])
			if len(args) > 1:
				notext = True
				text = " ".join(args[1:])
				
		await message.delete()
		all = message.client.iter_participants(message.to_id)
		chunk = []
		async for user in all:
			if not user.deleted:
				name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
				name = name.replace("<","&lt;").replace(">","&gt;")
				name = name[:30]+"..." if len(name) > 33 else name
				tag = f'<a href="tg://user?id={user.id}">{name}</a>' if not notext else f'<a href="tg://user?id={user.id}">{text}</a>'
				chunk.append(tag)
			if len(chunk) == tag_:
				await message.client.send_message(message.to_id, "\n".join(chunk))
				chunk = []
		if len(chunk) != 0:
			await message.client.send_message(message.to_id, "\n".join(chunk))
			    if tag_ == 0:
                await event.delete()
                time.sleep(0.2)
                # await event.respond("анрег")
                return
            await event.reply(name)
            await event.delete()
        except Exception as e:
            # await event.client.send_message(event.chat_id, f'Ты тупой? Введи .tagall [количество юзеров(не больше 100), по дефолту 20]\n\n{e}')
            time.sleep(0.2)
            # await event.respond("анрег")