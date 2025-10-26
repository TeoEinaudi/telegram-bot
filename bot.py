from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Токен бота, который ты получил у BotFather
import os
BOT_TOKEN = os.getenv("8264390202:AAFu29-XTv3unSwenhNnjov1Vd3O5-Kn_1g")

# 🔗 Имя канала (пример: @my_channel)
CHANNEL_USERNAME = "@zhizn_z"

# Функция, которая выполняется при команде /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Проверяем, подписан ли пользователь на канал
    try:
        chat_member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    except Exception as e:
        await update.message.reply_text(f"Ошибка проверки подписки: {e}")
        return

    if chat_member.status in ["member", "administrator", "creator"]:
        await update.message.reply_text(
            "✅ Спасибо! Вы подписаны на канал. Вот ваше сообщение:"
        )
        await update.message.reply_text("👉 Ваш бонус: https://example.com")
    else:
        await update.message.reply_text(
            f"❌ Чтобы получить сообщение, подпишитесь на канал {CHANNEL_USERNAME} и нажмите /start снова."
        )

# Основной блок запуска бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")

    app.run_polling()
