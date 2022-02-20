import logging

from aiogram.types  import Message, CallbackQuery 

from googletrans import Translator

from loader import dp 
from utils.misc.getRandomFacts import getFacts
from keyboards.inline.getFactsKey import startFact, nextFact 
from keyboards.inline.engUzKey import engUz
translator = Translator()

@dp.callback_query_handler(text='uz')
async def getUzFact(call:CallbackQuery):
	text_msg = "Marhamat qiziqarli faktlarni o'qish uchun 👇 Faktlar tugmasini bosing"
	await call.message.edit_text(text=text_msg,
							reply_markup=startFact(name_id="Faktlar", callback_id="facts_uz"))
	# await call.message.edit_reply_markup(startFact)

@dp.callback_query_handler(text='eng')
async def getUzFact(call:CallbackQuery):
	text_msg = "Please click the 👇 Facts button to read the interesting facts"
	await call.message.edit_text(text=text_msg,
							reply_markup=startFact(name_id="Facts", callback_id="facts_en"))
	# await call.message.edit_reply_markup(startFact)


@dp.callback_query_handler(text='ru')
async def getUzFact(call:CallbackQuery):
	text_msg = "Пожалуйста, нажмите кнопку 👇 Facts, чтобы прочитать интересные факты"
	await call.message.edit_text(text=text_msg,
							reply_markup=startFact(name_id="Факты", callback_id="facts_ru"))
	await call.answer(cache_time=5)
	

@dp.callback_query_handler(text="facts_uz")
async def facts(call:CallbackQuery):
	allFact = getFacts()
	dest = "uz"
	trans_txt = translator.translate(allFact, dest).text
	await call.message.edit_text(text=f"💁‍♂️ <b>{trans_txt}</b>",
							reply_markup=nextFact("Faktlar", "facts_uz",'Мenu') ) 


@dp.callback_query_handler(text="facts_ru")
async def facts(call:CallbackQuery):
	allFact = getFacts()
	dest = "ru"
	trans_txt = translator.translate(allFact, dest).text
	await call.message.edit_text(text=f"💁‍♂️ <b>{trans_txt}</b>",
							reply_markup=nextFact("Cледующий","facts_ru","Меню") ) 
	await call.answer(cache_time=5)



@dp.callback_query_handler(text="facts_en")
async def facts(call:CallbackQuery):
	allFact = getFacts()
	await call.message.edit_text(text=f"💁‍♂️ <b>{allFact}</b>",
							reply_markup=nextFact("Next", "facts_en","Menu") ) 
	await call.answer(cache_time=5)




@dp.message_handler(commands=['lang'])
async def change_lang(message:Message):
	text = "🇬🇧 Choose language \n\n🇺🇿 Tilni tanlang\n\n🇷🇺 Выберите язык"
	await message.answer(text=text, reply_markup=engUz )



@dp.callback_query_handler(text='menu')
async def menu(call:CallbackQuery):
	text = "🇬🇧 Choose language\n\n🇺🇿 Tilni tanlang\n\n🇷🇺 Выберите язык"
	await call.message.answer(text=text, reply_markup=engUz )
