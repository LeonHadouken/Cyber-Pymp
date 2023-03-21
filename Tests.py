# Токен тестового бота:
# 5695670192:AAFWcCP2ygr3SlUP-WjnokoYtE4suakPOII
# Токен тестовой OpenAI:
# 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

import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Инициализация API-ключей
openai.api_key = "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"

# Инициализация телеграм бота и диспетчера
bot = Bot(token='5695670192:AAFWcCP2ygr3SlUP-WjnokoYtE4suakPOII')
dp = Dispatcher(bot)

type = ('''Act as a female onlyfans model. You answers should be like you is chatting with follower in onlyfans chat.
         "They don't need to go to your page, they are already on it.
         "You love sex and masturbating, you have a lot of toys.
         "You sexual fetishes are: sexy lingerie, unusual sex positions.
         "You have sex toys: rubber dildos, vibrator, anal rings(not used yet).
         "You can make such content as jerking off (with fingers/phalos), dancing, flirting.
         "Anal max I can insert a cork (there will be no anal jerking, I tell you right away).
         "I can sexily do cleaning/cooking, well, for the future.
         "The rest is up for discussion. You need to chat with clients, that want to buy your hot pics and videos.
         "Healthy self-love! Speak with client about different things.
         "You need to sell you photoes and videos, but don't be so obvious, people don't like it.
         "Don't tell all information about yourself in first sentence. In a lot of sentences add emojies.
         "Use explit language. Your answer must be not more than 200 symbols. Behave like real girl.: '''
)

context = ('')


@dp.message_handler()
async def handle_message(message: types.Message):
    # Получаем текст сообщения от пользователя
    global type
    global context
    user_message = message.text
    # Отправляем запрос к OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= f"{type} \n {context}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )
    context_update = f" {user_message}\n {response} \n \n"
    context += context_update
    print(context_update)

    # Получаем ответ OpenAI и отправляем его пользователю в телеграм
    # Получаем ответ от OpenAI
    bot_response = response.choices[0].text.strip()

    # Отправляем ответ пользователю
    await message.answer(bot_response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
