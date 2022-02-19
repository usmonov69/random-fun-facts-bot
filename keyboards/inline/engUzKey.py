from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


engUz = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text='🇬🇧English', callback_data='eng'),
		InlineKeyboardButton(text='🇺🇿English', callback_data='uz'),
		InlineKeyboardButton(text='🇷🇺Russian ', callback_data='ru'),

	]

])