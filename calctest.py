from telebot import types
import telebot, time, math, re
import logging



class КулькуляторMod(loader.Module):
	"""Кукулирует вырожения"""
	strings = {'name': 'Кулькулятор'}
	
	async def calhelpccmd(self, message):
             """Мной пользоваться очень просто. Вы мне отправляете выражение, а я вам возвращаю его результат.
***Операторы***:
    + - сложение;
    - - вычитание;
    \* - умножение;
    / - деление;
    \*\* - возведение в степнь.
    
***Функции***:
    cos(x) - косинус x;
    sin(x) - синус x;
    tg(x) - тангенс x;
    fact(x) - факториал x;
    sqrt(x) - квадратный корень х;
    sqr(x) - х в квадрате.
***Логарифмы***:
    log2(x) - логарифм х по основанию 2;
    lg(х) - десятичный логарифм х;
    ln(x) - натуральный логарифм x;
    log(b, х) - логарифм х по основанию b;
***Системы счисления***:
    0bx - перевести двоичное число х в десятичное;
    0ox - перевести восьмиричное число х в десятичное;
    0xx - перевести шестнадцатиричное число х в десятичное;"""

пи = п = p = pi = 3.141592653589793238462643 # число Пи asd 

# Ниже все понятно...
async def factcmd(self, message):
    return math.factorial(self, message)
    text = utils.get_args_raw(message)

async def coscmd(self, message):
    return math.cos(self, message)
    text = utils.get_args_raw(message)

async def sincmd(self, message):
    return math.sin(self, message)
    text = utils.get_args_raw(message)

async def tgcmd(self, message):
    return math.tan(self, message)
    text = utils.get_args_raw(message)
    
async def tancmd(self, message):
    return math.tan(self, message)
    text = utils.get_args_raw(message)
    
async def lncmd(self, message):
    return math.log(self, message)
    text = utils.get_args_raw(message)

async def logcmd(base, float_):
    return math.log(float_, base)
    text = utils.get_args_raw(message)
async def lgcmd(float_):
    return math.log10(float_)
    text = utils.get_args_raw(message)

async def log2cmd(float_):
    return math.log2(float_)
    text = utils.get_args_raw(message)

async def expcmd(float_):
    return math.exp(float_)
    text = utils.get_args_raw(message)

# Обработчик сообщений-команд


# Обработчик всех сообщений
