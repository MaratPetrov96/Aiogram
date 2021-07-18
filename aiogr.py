from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3

objs=('Квартира','Комната','Дом','Дача','Участок','Коммерция')

def phone(teleph):
    if teleph.startswith(('8' or '7' or '+7' or '+8')):
        return len(teleph) in range(10,13)

bot = Bot(token='')
dp = Dispatcher(bot)

#меню выбора района
rayon=types.InlineKeyboardMarkup(row_width=2)
rayon.add(types.InlineKeyboardButton('Полтава',callback_data='Poltava'),
          types.InlineKeyboardButton('Полтавский район',callback_data='Poltavski'))

#инлайн меню
item=types.InlineKeyboardMarkup(row_width=2)
for i in objs:
    item.add(types.KeyboardButton(i))
    #item.add(types.InlineKeyboardButton(i,callback_data='object'))

#Меню продажи
menu=types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(types.InlineKeyboardButton('Вернуться',callback_data='SellBack'),
         types.KeyboardButton('Далее'),
         types.KeyboardButton('Перезвоните мне'))

#настройки
#кол-во комнат
room_num=types.InlineKeyboardMarkup
for i in range(3):
    room_num.add(types.KeyboardButton(f'{i+1}'))
room_num.add(types.KeyboardButton('4+'))

price1=types.InlineKeyboardMarkup(row_width=2)
price1.add(types.InlineKeyboardButton('до 25',callback_data='price'),
          types.InlineKeyboardButton('26-40',callback_data='price'),
          types.InlineKeyboardButton('41-60',callback_data='price'),
          types.InlineKeyboardButton('61-80',callback_data='price'),
          types.InlineKeyboardButton('81-100',callback_data='price'),
          types.InlineKeyboardButton('100+',callback_data='price'))

price2=types.InlineKeyboardMarkup(row_width=2)
price2.add(types.InlineKeyboardButton('до 5',callback_data='price'),
           types.InlineKeyboardButton('5-10',callback_data='price'),
           types.InlineKeyboardButton('11+',callback_data='price'))

price3=price1
price4=price1
price5=price2

squareChosen=types.InlineKeyboardMarkup(row_width=2)
squareChosen.add(types.KeyboardButton('до 30'),
          types.KeyboardButton('31-40'),
          types.KeyboardButton('41-50'),
          types.KeyboardButton('51-60'),
          types.KeyboardButton('61-70'),
          types.KeyboardButton('71+'))

sq1=types.InlineKeyboardMarkup(row_width=2)
sq1.add(types.InlineKeyboardButton('до 30',callback_data='Square'),
        types.InlineKeyboardButton('31-60',callback_data='Square'),
        types.InlineKeyboardButton('61+',callback_data='Square'))

sq2=types.InlineKeyboardMarkup(row_width=2)
sq2.add(types.InlineKeyboardButton('до 10',callback_data='Square'),
        types.InlineKeyboardButton('11-20',callback_data='Square'),
        types.InlineKeyboardButton('21+',callback_data='Square'))

sq3=types.InlineKeyboardMarkup(row_width=2)
sq3.add(types.InlineKeyboardButton('до 30',callback_data='Square'),
          types.InlineKeyboardButton('31-40',callback_data='Square'),
          types.InlineKeyboardButton('41-50',callback_data='Square'),
          types.InlineKeyboardButton('51-60',callback_data='Square'),
          types.InlineKeyboardButton('61-70',callback_data='Square'),
          types.InlineKeyboardButton('71+',callback_data='Square'))

sq4=sq3

sq5=sq2

comm=types.InlineKeyboardMarkup(row_width=2)
for i in 'Офис','Гараж','Магазин','Свобод','Производство':
    comm.add(types.InlineKeyboardButton(i,callback_data='comm'))

sell=types.InlineKeyboardMarkup(row_width=2)
sell.add(types.KeyboardButton('Продать быстро'),
         types.KeyboardButton('Продать дорого'))

#'Меню договоров
dogovor=types.ReplyKeyboardMarkup(resize_keyboard=True)
dogovor.add(types.KeyboardButton('О компании'),
            types.KeyboardButton('Пакетная система оплаты'),
            types.KeyboardButton('Договор сотрудничества'),
            types.InlineKeyboardButton('Вернуться',callback_data='DogovorBack'))

#Меню настроек
sets=types.ReplyKeyboardMarkup(resize_keyboard=True)
sets.add(types.KeyboardButton('Параметры рассылки'),
types.KeyboardButton('Перезвоните мне'),
types.KeyboardButton('Главное меню'))

#главное меню
main=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Поиск'),
types.KeyboardButton('Настройки'),
types.KeyboardButton('Связь с оператором'),
types.KeyboardButton('Условия сотрудничества'))

main=types.ReplyKeyboardMarkup(True,True)
for i in 'Поиск','Настройки','Связь с оператором','Условия сотрудничества':
    main.row(i)
#main=types.ReplyKeyboardMarkup(reply_keyboard=[[types.KeyboardButton('Поиск')]])
#main=types.InlineKeyboardMarkup(row_width=2)

cancel=types.InlineKeyboardMarkup(row_width=2)
cancel.add(types.KeyboardButton('Отменить'))

#меню поиск
search=types.ReplyKeyboardMarkup(resize_keyboard=True)
search.add(types.KeyboardButton('Вернуться'),
           types.KeyboardButton('Подобрать'),
           types.KeyboardButton('Сохранить настройки'))

params=types.ReplyKeyboardMarkup(resize_keyboard=True)
search.add(types.KeyboardButton('Задать параметры'),
           types.KeyboardButton('По сохранённым параметрам'),
           types.KeyboardButton('Главное меню'))

chosen=types.InlineKeyboardMarkup(row_width=2)
chosen.add(types.KeyboardButton('Вариант 1'),
           types.KeyboardButton('Вариант 2'),
           types.KeyboardButton('Вариант 3'),
           types.KeyboardButton('Редактировать'))

@dp.message_handler(commands=["start"])
async def start_(message):
    start=types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy=types.KeyboardButton('Купить')
    sell=types.KeyboardButton('Продать')
    start.add(buy,sell)
    await message.reply("Стартовое меню", reply_markup=start)
@dp.message_handler(content_types=['text'])
async def main(message):
    global obj,action,place
    if message.text=='Купить':
        action='Buy'
        await bot.send_message(message.from_user.id,'Я помогу вам найти актуальные квартиры, дома, помещения и участки',reply_markup=main)
        #await bot.send_message
        #await types.Message.edit_reply_markup(main)
        #await bot.edit_message_text(chat_id=message.from_user.id,message_id=message.message_id,text='На рынок',
                                  #reply_markup=main)
    elif message.text=='Продать':
        action='Sell'
        await bot.send_message(message.from_user.id,'Выберите район',reply_markup=rayon)
    elif message.text in ('Полтавский район','Полтава'):
        place=message.text
        if action=='Sell':
            await bot.send_message(message.from_user.id,'Выберите объект',reply_markup=item)
        else:
            await bot.send_message(message.from_user.id,'Количество комнат',reply_markup=room_num)
    elif message.text=='Далее':
        if obj in ('Квартира','Дом','Дача'):
            await bot.send_message(message.from_user.id,'Количество комнат',reply_markup=room_num)
        elif obj=='Коммерция':
            await bot.send_message(message.from_user.id,'Выберите',reply_markup=comm)
        else:
            ind=objs.index(obj)
            await bot.send_message(message.from_user.id,'Площадь',reply_markup=eval(f'sq{ind}'))
    elif message.text=='Перезвоните мне':
        await bot.send_message(message.from_user.id,'Вы хотите отправить номер телефона? (слитно)',reply_markup=phone)
    elif message.text=='Связь с оператором':
        await bot.send_message(message.from_user.id,'Ожидайте подключения оператора',reply=cancel)
    elif message.text=='Отменить':
        await bot.send_message(message.from_user.id,'Главное меню',reply_markup=main)
    elif message.text in '1234+':
        ind=objs.index(obj)
        await bot.send_message(message.from_user.id,'Площадь',reply_markup=eval(f'sq{ind}'))
    elif phone(message.text):
        await bot.send_message(message.from_user.id,'Спасибо, свяжемся в удобное для вас время')
    elif message.text in objs:
        obj=message.text
        if action=='Sell':
            await bot.send_message(message.from_user.id,'Выберите действие',reply_markup=menu)
        else:
            if obj in ('Квартира','Дом','Дача'):
                await bot.send_message(message.from_user.id,'Количество комнат',reply_markup=room_num)
            elif obj=='Коммерция':
                await bot.send_message(message.from_user.id,'Выберите',reply_markup=comm)
            else:
                ind=objs.index(obj)
                await bot.send_message(message.from_user.id,'Площадь',reply_markup=eval(f'sq{ind}'))
    elif message.text=='Условия сотрудничества':
        await bot.send_message(message.from_user.id,'''Здесь найдёте все необходимые документы о компании
                         , договоры и условия сотрудничества с нами''',reply_markup=dogovor)

@dp.callback_query_handler(posts_cb.filter(action=["jsonbox"]))
async def callback_inline(call):
    global obj,action,place
    if call.message:
        if call.data=='SellBack':
            await bot.send_message(message.chat.id,'Выберите объект',reply_markup=item)
        elif call.data in ('Poltava','Poltavski'):
            place=message.text
            if action=='Sell':
                await bot.send_message(message.from_user.id,'Выберите объект',reply_markup=item)
            else:
                await bot.send_message(message.from_user.id,'Количество комнат',reply_markup=room_num)
        elif call.data=='PhoneBack':
            await bot.send_message(message.chat.id,'Выберите действие',reply_markup=menu)
        elif call.data=='DogovorBack':
            bot.send_message(message.chat.id,'Главное меню',reply_markup=main)
        elif call.data=='Square':
            ind=objs.index(obj)
            bot.send_message(message.chat.id,'Площадь',reply_markup=eval(f'price{ind}'))
executor.start_polling(dp)
