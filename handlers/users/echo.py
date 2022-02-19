from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
	text = f"⚠️ Mendan foydalanish uchun siz faqat korsatilgn tugmalarni  bosishingiz mumkin "
	text += f"iltimos menga <i>photo, sticker, emoji, text...</i> yuborlang! <i>etiboringiz uchun raxmat</i>\n\n"
	text += f"<i>Tilni tanlash uchun: </i>/lang"
	await message.reply(text)


