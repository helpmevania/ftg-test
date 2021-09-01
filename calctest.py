from .. import loader, utils, telebot, datetime, time, math, re
from telebot import types
class КалякуляторMod(loader.Module):
	"""Калякулятор вырожения"""
	strings = {'name': 'Кукулятор'}
	
	async def calccmd(self, message):
		""".calc <выражение или реплай на то, что нужно посчитать>
			Кстати:
			** - возвести в степень
			/ - деление
			% - деление по модулю"""
		question = utils.get_args_raw(message)
		reply = await message.get_reply_message()
        def fact(float_):
         return math.factorial(float_)

def cos(float_):
    return math.cos(float_)

def sin(float_):
    return math.sin(float_)

def tg(float_):
    return math.tan(float_)
    
def tan(float_):
    return math.tan(float_)


def ln(float_):
    return math.log(float_)

def log(base, float_):
    return math.log(float_, base)

def lg(float_):
    return math.log10(float_)

def log2(float_):
    return math.log2(float_)

def exp(float_):
    return math.exp(float_)
		if not question:
			if not reply:
				await utils.answer(message, "<b>2+2=5</b>")
				return
			else:
				question = reply.raw_text
		try:
			answer = eval(question)
			answer = f"<b>{question}=</b><code>{answer}</code>"
		except Exception as e:
			answer =  f"<b>{question}=</b><code>{e}</code>"
		await utils.answer(message, answer)
	