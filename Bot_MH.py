import telebot
from telebot import types
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

bot = telebot.TeleBot('')

# меню для выбора
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вход по телефону")
item2 = types.KeyboardButton("Вход по почте")
markup.add(item1, item2)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Начать обучение")
markup1.add(item1)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Пройти")
item2 = types.KeyboardButton("Пропустить")
markup2.add(item1, item2)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Дальше")
markup3.add(item1)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Перейти к тесту")
markup5.add(item1)

markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Завершить тест")
markup6.add(item1)

markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выбрать курс из списка")
item2 = types.KeyboardButton("Подобрать курс")
markup7.add(item1, item2)

markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выбрать курс из списка")
item2 = types.KeyboardButton("Подобрать курс")
item3 = types.KeyboardButton("Продолжить курс...")
item4 = types.KeyboardButton("Достижения")
markup8.add(item1, item2, item3, item4)

markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Завершить")
markup10.add(item1)

markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Начать курс")
item2 = types.KeyboardButton("Выбрать курс из списка")
markup9.add(item1, item2)

name = mail = ''
fwd = 0
message_id = chat_id = 0
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard

    bot.send_message(message.chat.id,
                     "Вас приветствует бот по кибербезопасности!\n".format(
                         message.from_user, bot.get_me()), reply_markup=markup,
                     parse_mode='html')


@bot.message_handler(commands=['menu'])
def welcome(message):
    # keyboard
    bot.send_message(message.chat.id,
                     "Выберите опцию".format(
                         message.from_user, bot.get_me()), reply_markup=markup8,
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        global name, mail, fwd, message_id, chat_id
        if message.text == 'Вход по телефону':
            bot.send_message(message.chat.id, "Код подтверждения выслан 89134226712",
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'Достижения':
            bot.send_photo(message.chat.id, open('achievments.jpg', 'rb'),
                           reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'Вход по почте':
            bot.send_message(message.chat.id, "Код подтверждения выслан example@mail.com",
                             reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'Завершить тест':
            bot.send_message(message.chat.id, "Тест пройден! Ваш результат - 86%, достижения обновлены:",
                             reply_markup=types.ReplyKeyboardRemove())
            bot.send_photo(message.chat.id, open('achievments.jpg', 'rb'),
                             reply_markup=markup7)
        elif message.text == '123':
            bot.send_message(message.chat.id, 'Добрый день, Виктор!'
                                              '\nХотите пройти курс "Пароли и конфиденциальности"?'
                                              '\nДля выхода в меню используйте /menu', reply_markup=markup2)
        elif message.text == 'Завершить':
            bot.send_message(message.chat.id, 'Вам подобран курс "Кибергигиена"', reply_markup=markup9)
        elif message_id and message.text == '123456':
            bot.send_message(message.chat.id, '_Неверно_ 💔', parse_mode="Markdown", reply_markup=markup6)
            bot.forward_message(chat_id, chat_id, message_id + 1)
        if message.text == 'Пройти':
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("✅ Правильно", callback_data='good_ex')
            item2 = types.InlineKeyboardButton("❌ Неправильно", callback_data='bad_ex')

            markup4.add(item1, item2)
            bot.send_message(message.chat.id, "Начем с азов...", reply_markup=markup3)
            bot.send_message(message.chat.id, "62% россиян используют одну и ту же комбинацию символов для входа в "
                                              "личный и рабочий электронные ящики, а также при регистрации в социальных сетях.",
                             reply_markup=markup4)
        elif message.text == 'Начать курс':
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item2 = types.InlineKeyboardButton("Подробнее...", callback_data='bad_ex')

            markup4.add(item2)
            bot.send_message(message.chat.id, "Немного терминов...", reply_markup=markup3)
            bot.send_message(message.chat.id, "Спам — сообщения рекламного характера."
                                              "\nТроян — разновидность вредоносной программы, проникающая в компьютер под видом легитимного программного обеспечения."
                                              "\nФлуд — это сообщения в интернет-форумах и чатах, не несущие никакой полезной информации."
                                              "\nЧервь — разновидность вредоносной программы, самостоятельно распространяющейся через локальные и глобальные (Интернет) компьютерные сети.",
                             reply_markup=markup4)
        elif message.text == 'Дальше' and fwd == 2:
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("✅ Правильно", callback_data='good_pwd')
            item2 = types.InlineKeyboardButton("❌ Неправильно", callback_data='bad_pwd')

            markup4.add(item1, item2)
            bot.send_photo(message.chat.id, open('frauds.jpg', 'rb'), caption="Кибергигиена важна для всех", reply_markup=markup4)
            message_id = message.id

        elif message.text == 'Дальше' and not fwd:
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("✅ Правильно", callback_data='good_pwd')
            item2 = types.InlineKeyboardButton("❌ Неправильно", callback_data='bad_pwd')

            markup4.add(item1, item2)
            bot.send_photo(message.chat.id, open('passwords.jpg', 'rb'), caption="А знали ли вы?", reply_markup=markup4)
            message_id = message.id

            fwd += 1
        elif message.text == 'Дальше' and fwd == 1:
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("✅ Правильно", callback_data='good_vid')
            item2 = types.InlineKeyboardButton("❌ Неправильно", callback_data='bad_vid')

            markup4.add(item1, item2)
            bot.send_message(message.chat.id, 'И наконец', reply_markup=markup5)
            bot.send_video(message.chat.id, open('video.mp4', 'rb'),
                             reply_markup=markup4)

            fwd += 1
        if message.text == 'Перейти к тесту':

            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Внутри", callback_data='right1')
            item2 = types.InlineKeyboardButton("Извне", callback_data='wrong')

            markup4.add(item1, item2)
            bot.send_message(message.chat.id, 'Вопрос №1', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Люди внутри или извне представляют большую угрозу '
                                              'кибербезопасности вашей компании?', reply_markup=markup4)
            chat_id = message.chat.id

        if message.text == 'Подобрать курс':

            markup4 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("У меня несколько паролей", callback_data='right4')
            item2 = types.InlineKeyboardButton("У меня один пароль", callback_data='wrong')

            markup4.add(item1, item2)
            bot.send_message(message.chat.id, 'Вопрос №1', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Вы заводите новую учетную запись на каком-либо сайте. '
                                              'Как будете выбирать пароль?', reply_markup=markup4)
            chat_id = message.chat.id

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good_pwd':
                bot.send_message(call.message.chat.id, "_Ставить пароль: O@UqG?%E*u_", parse_mode="Markdown")
            elif call.data == 'bad_pwd':
                bot.send_message(call.message.chat.id, '_Пользоваться таким паролем: 123456_', parse_mode="Markdown")
            elif call.data == 'bad_ex':
                bot.send_message(call.message.chat.id, '_Использовать одинаковые пароли для разных ящиков_', parse_mode="Markdown")
            elif call.data == 'good_ex':
                bot.send_message(call.message.chat.id, '_Создавать оригинальный пароль для каждого ящика_', parse_mode="Markdown")
            elif call.data == 'right1':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item2 = types.InlineKeyboardButton("Это возможно", callback_data='right2')
                item1 = types.InlineKeyboardButton("Это невозможно", callback_data='wrong')

                markup4.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Вопрос №2', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'Роман – крупный предприниматель. Опасаясь взлома, '
                                                       'он защитил свою почту двухфакторной авторизацией через SMS. '
                                                       'Но его все равно взломали.', reply_markup=markup4)
            elif call.data == 'right2':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("1.", callback_data='wrong')
                item2 = types.InlineKeyboardButton("2.", callback_data='wrong')
                item3 = types.InlineKeyboardButton("3.", callback_data='wrong')
                item4 = types.InlineKeyboardButton("4.", callback_data='right3')

                markup4.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id, 'Вопрос №3', reply_markup=types.ReplyKeyboardRemove())
                bot.send_photo(call.message.chat.id, open('choicejpg.jpg', 'rb'), caption='Где лучше хранить пароль?'
                                                                                          '(выберите номер изображения)',
                               reply_markup=markup4)
            elif call.data == 'right3':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                bot.send_message(call.message.chat.id, 'Вопрос №4', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'Введите пример надежного пароля', reply_markup=types.ReplyKeyboardRemove())
            elif call.data == 'right4':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item2 = types.InlineKeyboardButton("Специальную", callback_data='right5')
                item1 = types.InlineKeyboardButton("Личную", callback_data='wrong')
                item3 = types.InlineKeyboardButton("Рабочую", callback_data='wrong')

                markup4.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Вопрос №2', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'Чтобы временно зарегистрироваться на новом сервисе '
                                                       '(например, чтобы заказать разовую доставку)'
                                                       ', вам необходимо указать свой e-mail. Какую почту вы укажете?', reply_markup=markup4)
            elif call.data == 'right5':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Да", callback_data='wrong')
                item2 = types.InlineKeyboardButton("Нет", callback_data='right6')

                markup4.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Вопрос №3', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'В ресторане вы решили расплатиться за '
                                                       'ужин банковской картой. Отдадите ли вы для оплаты карту официанту?', reply_markup=markup4)
            elif call.data == 'right6':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Читаю все сообщения", callback_data='right7')
                item2 = types.InlineKeyboardButton("Нажимаю «Далее-Далее»", callback_data='wrong')

                markup4.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Вопрос №4', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'Как вы обычно устанавливаете новые приложения на компьютер?', reply_markup=markup4)
            elif call.data == 'right7':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("1.", callback_data='wrong')
                item2 = types.InlineKeyboardButton("2.", callback_data='wrong')
                item3 = types.InlineKeyboardButton("3.", callback_data='wrong')
                item4 = types.InlineKeyboardButton("4.", callback_data='right8')
                markup4.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id, 'Вопрос №5', reply_markup=types.ReplyKeyboardRemove())
                bot.send_photo(call.message.chat.id, open('question.jpg', 'rb'), caption='Какой из вариантов'
                                                                                         ' не является фишинг сайтом?', reply_markup=markup4)
            elif call.data == 'right8':
                bot.send_message(call.message.chat.id, '_Верно!_ 💚', parse_mode="Markdown", reply_markup=markup10)
            elif call.data == 'wrong':
                bot.send_message(call.message.chat.id, '_Неверно_ 💔', parse_mode="Markdown")
                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Читаю все сообщения", callback_data='right7')
                item2 = types.InlineKeyboardButton("Нажимаю «Далее-Далее»", callback_data='wrong')

                markup4.add(item1, item2)
                bot.send_message(call.message.chat.id, 'Вопрос №4', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(call.message.chat.id, 'Как вы обычно устанавливаете новые приложения на компьютер?',
                                 reply_markup=markup4)

    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)