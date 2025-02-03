# Yandex Music Bot
![image](https://github.com/user-attachments/assets/aefc9f26-5ed2-48b9-8fc6-181c0879b312)

## 📑 Описание
**Yandex Music Bot** — это Telegram-бот, который позволяет искать и прослушивать музыку из Yandex Music API прямо в Telegram. Бот поддерживает поиск по исполнителям, альбомам и трекам, а также предоставляет ссылки на прослушивание.

## 🧑‍🏭 Функционал
- 🎵 Получение информации о песне (название, исполнитель)
- 🔗 Скачивание треков

## 📥 Установка и запуск

### 1. 🤹 Клонирование репозитория
```bash
git clone https://github.com/faidychka/YandexMusicBot.git
cd YandexMusicBot
```

### 2. 🌀 Установка зависимостей
Убедитесь, что у вас установлен Python 3.8+.
```bash
pip install aiogram yandex-music
```

### 3. Получение API-ключей
Для работы бота потребуется:
- **Telegram Bot Token** (получить в @BotFather)
- **Yandex Music API Token** (получить через авторизацию в Yandex Music API)

### 4. 😋 Добавление токенов и ключей
Измените данные на свои
```env
bot = Bot(token='Bot API Token', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
yandex_client = Client('Yandex Music API Token').init()
```
чтобы получить Yandex Music API Token
Скачайте расширение [Yandex Music Token](https://chromewebstore.google.com/detail/yandex-music-token/)
или оставьте поле пустым '', чтоб протестировать 30 секундные треки

### 5. 👏 Запуск бота
```bash
python main.py
```

## 🧑‍🎤 Использование
- Отправьте ссылку на трек боту
- И слушайте на здоровье 🎶

## 🫖 Зависимости
- `aiogram` — для работы с Telegram API
- `yandex-music` — для работы с Yandex Music API

## 📇 Контакты
Если у вас есть вопросы или предложения, пишите в [Telegram](https://t.me/faidychka)!

