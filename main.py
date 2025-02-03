import re
import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import FSInputFile
from yandex_music import Client

bot = Bot(token='Bot API Token', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

yandex_client = Client('Yandex Music API Token').init()

DOWNLOAD_DIR = 'downloaded_tracks' # куда пойдут скаченные треки для повторной отправки
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def extract_ids(url):
    match = re.search(r'album/(\d+)/track/(\d+)', url)
    if match:
        album_id, track_id = match.groups()
        return album_id, track_id
    else:
        return None, None

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("👋 Привет! Отправь мне ссылку на трек Яндекс.Музыки, и я скачаю его для тебя.")

@dp.message()
async def handle_message(message: types.Message):
    url = message.text.strip()
    bot_info = await bot.get_me()
    album_id, track_id = extract_ids(url)

    if album_id and track_id:
        edited_message = await message.answer("<i>🎶 Скачиваю трек...</i>")

        try:
            track = yandex_client.tracks([track_id])[0]
            names = ', '.join(name.name for name in track.artists)
            track_title = f"{names} - {track.title}"
            file_name = f"{track_title}.mp3"
            file_path = os.path.join(DOWNLOAD_DIR, file_name)

            if os.path.exists(file_path): pass
            else: track.download(file_path)

            audio = FSInputFile(file_path, filename=file_name)
            await message.answer_audio(audio, title=track.title, performer=names, caption=f"<b>📱 Скачано через @{bot_info.username}</b>")

        except Exception as e:
            await message.answer(f"😔 К сожалению, не удалось скачать трек. Попробуйте позже..")
            print(e)
    else:
        await message.reply_photo("https://imgur.com/a/sNWe7NC", # Ссылка на пример
                                  "⁉️ Пожалуйста, отправьте корректную ссылку на трек Яндекс.Музыки")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
