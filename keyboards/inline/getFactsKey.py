from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def startFact(name_id, callback_id):
	startFacts = InlineKeyboardMarkup(inline_keyboard=[
		[
			InlineKeyboardButton(text=f"📜 {name_id}", callback_data=f'{callback_id}'),
			# InlineKeyboardButton(text="📜 Faktlar", callback_data='facts_uz'),
			# InlineKeyboardButton(text="📜 Facts ", callback_data='facts_en')

		]

		])
	return startFacts
def nextFact(next_id,callback_id, menu_id):	
	nextFacts = InlineKeyboardMarkup(inline_keyboard=[
		[
			InlineKeyboardButton(text=f"{menu_id} ⏺", callback_data="menu"),
			InlineKeyboardButton(text=f"{next_id} ➡️", callback_data=f'{callback_id}')
		]

		])
	return nextFacts

