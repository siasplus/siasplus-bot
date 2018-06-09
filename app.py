# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests

bot = telebot.TeleBot("587880587:AAGX-EODQaZ-RHnjqK-vVZm5dkUb_n2aky8")

# Кнопки

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('💬 Начать 💬')
    bot.send_message(message.from_user.id, '👋 Приветствую {0}! Я чат-бот, который ознакомит тебя с миром Криптовалют.\n\n'
                                           'В Чем моя уникальность ?\n\n'
                                           '- Ознакомлю с Криптовалютой\n'
                                           '- Покажу с чего начать\n'
                                           '- Предоставлю список популярных сервисов\n\n'
                                           'Для начала нашего с тобой общения, нажми кнопку "Начать"'
                                           .format(message.from_user.first_name), reply_markup=user_markup)
    #bot.send_message(message.chat.id,wallet)
    #arh=wallet.archive_address('1P69cjBUWXT3qvGJCcLmqjXVqqCtWzKorQ')
    #print(str(stats))


@bot.message_handler(commands=['help'])
def handle_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать в Тех.Поддержку", url="https://telegram.me/siashelp")
    keyboard.add(url_button)
    bot.send_message(message.chat.id,
                     "Если все вышеперечисленное вам не помогло, обращайтесь в тех.поддержку", reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def handle_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('🅱 Биткоин', '🅰 Альткоины')
    user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
    user_markup.row('📈 Курсы 📈', '📊 Биржи 📊')
    user_markup.row('🔖 Новости 🔖','💎 НАЧАТЬ ЗАРАБАТЫВАТЬ')
    user_markup.row('☎ Контакты ☎')
    bot.send_message(message.from_user.id, "Вы вернулись в начальное меню.", reply_markup=user_markup)


@bot.message_handler(commands=['mvideo'])
def handle_mvideo(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('🎥 Видео инструкция')
    user_markup.row('🎥 Открытие Ilgamos в Украине')
    user_markup.row('🎥 Всё о биткоине')
    user_markup.row('🎥 Цельные советы')
    user_markup.row('🔙 Вернуться')
    bot.send_message(message.from_user.id, "Выберите видео информацию, которая вас интересует.",reply_markup=user_markup)

def get_btc(): #Показує реальний курс бітка
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url).json()
    price = r['ticker']['last']
    return str(price) + ' USD'

def get_ltc():  # Показує реальний курс лайта
   url = 'https://yobit.net/api/2/ltc_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'

def get_eth():  # Показує реальний курс езера
   url = 'https://yobit.net/api/2/eth_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'

def get_dash():  # Показує реальний курс деша
   url = 'https://yobit.net/api/2/dash_usd/ticker'
   r = requests.get(url).json()
   price = r['ticker']['last']
   return str(price) + ' USD'


        ##################################1
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text=='💬 Начать 💬':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🅱 Биткоин', '🅰 Альткоины')
        user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
        user_markup.row('📈 Курсы 📈', '📊 Биржи 📊')
        user_markup.row('🔖 Новости 🔖', '💎 НАЧАТЬ ЗАРАБАТЫВАТЬ')
        user_markup.row('☎ Контакты ☎')
        bot.send_message(message.from_user.id, 'О биткоине ', reply_markup=user_markup)
    elif message.text == '🅱 Биткоин': #1
            user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            user_markup.row('Особенности')
            user_markup.row('Принцип роботы')
            user_markup.row('Международный Форум')
            user_markup.row('🔙 Вернуться "Главное меню"')
            bot.send_message(message.from_user.id, 'Bitcoin – первая в мире криптовалюта, которая занимает лидирующую позицию на рынке.'
                                                   'Главной целью Bitcoin было создание системы полностью необратимых сделок, когда '
                                                   'электронный платёж между двумя сторонами происходит без третьей стороны-гаранта и'
                                                   'ни одна из сторон, в том числе какой-либо внешний администратор не могла бы повлиять '
                                                   'на проведение транзакции.\n\n'
                                                   'Кроме того, Bitcoin значительно доступнее других криптовалют — больше обменов, '
                                                   'больше продавцов и поддержка всеми крипто-биржами мира. Также в развитие Bitcoin'
                                                   'предприниматели вкладывают больше финансов. '
                                                   'Чтобы обеспечить успешное функционирование и защитить систему от '
                                                   'взломов  используются криптографические методы. Для прозрачности каждой сделки'
                                                   'информация о транзакциях не шифруется и всегда доступна.\n\n'
                                                   'Прогресс пошел настолько далеко , что теперь  Биткойн можно  использовать для обмена '
                                                   'на товары, услуги, и рассчитываться в магазинах вместо наличных денег.\n\n'
                                                   , reply_markup=user_markup)
    elif message.text=='Особенности': #1.1
        bot.send_message(message.chat.id, "✅ Bitcoin  можно  использовать без предоставления конфиденциальных данных. \n\n"
                                          "✅ Пересылать в любом количестве, на любой адрес, в любую страну. Без запретов и "
                                          "лимитов.\n\n"
                                          "✅ Использовать в качестве оплаты для онлайн и оффлайн покупок. Список организаций, "
                                          "принимающих биткоин, постоянно растет.\n\n"
                                          "✅ Использовать в путешествиях, снижая потери на комиссиях и кросскурсах.\n\n"
                                          "✅ Использовать в качестве инвестиций или способа сохранения капитала.\n\n"
                                          "❌ У злоумышленников не получится напечатать Bitcoin  - количество монет заранее известно, 21 000 "
                                          "000 - и они появляются в сети строго по заранее известному алгоритму;\n\n"
                                          "❌ Не выйдет уничтожить  Bitcoin  - все компьютеры, находящиеся в сети, заменяют единый центр, "
                                          "а  целостность цепочки блоков от разного вида атак защищена этой большой компьютерной "
                                          "сетью;\n\n"
                                          "❌ Как бы вы не старались у вас не получиться изменить исходный код без согласия большей части "
                                          "сообщества - как условия появления количества монет, так любые другие правила;\n\n"
                                          "❌ Невозможно заблокировать или арестовать -  Bitcoin контролирует только тот, кто имеет прямой "
                                          "доступ к кошельку. Чтобы арестовать кошелек Bitcoin, нужно сначала арестовать его хозяина.\n\n"
                                          "❌ Также никак не получиться подделать или потратить дважды - в системе используются "
                                          "специальные криптографические ключи, которые подтверждаются цепочкой блоков – главной "
                                          "учетной книгой системы.\n\n")
    elif message.text=='Принцип роботы': #1.2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Официальный сайт", url="https://bitcoin.org")
        url_button1 = types.InlineKeyboardButton(text="Видео №1", url="https://youtu.be/IdWgvOxjYi8")
        url_button2 = types.InlineKeyboardButton(text="Видео №2", url="https://youtu.be/RuZ80TPUF_A")
        keyboard.add(url_button)
        keyboard.add(url_button1,url_button2)
        bot.send_message(message.chat.id,"В этом разделе я помогу разобраться с принципами роботы Bitcoin.\n"
                                          "Ниже предоставляю ссылку на оффициальный сайт Bitcoin и подборку из видео:\n\n - Кратко о Bitcoin #1\n - Тех. часть Bitcoin #2",reply_markup=keyboard)
    elif message.text=='Международный Форум': #1.3
        bot.send_message(message.chat.id, "Вам не придется больше искать ответы на свои вопросы у ненадежных источников, "
                                          "обратите внимание на  русский раздел крупнейшего криптовлаютного форума. \n\n"
                                          "Это поистине гигантская копилка коллективных знаний с 2010 года. Где вы можете найти "
                                          "ответы на все ваши вопросы.\n"
                                          "https://bitcointalk.org/index.php?board=10.0 \n\n")
    elif message.text=='🔙 Вернуться "Главное меню"': #1.6
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🅱 Биткоин', '🅰 Альткоины')
        user_markup.row('🎥 Видео 🎥', '💰 Кошельки 💰')
        user_markup.row('📈 Курсы 📈', '📊 Биржи 📊')
        user_markup.row('🔖 Новости 🔖', '💎 НАЧАТЬ ЗАРАБАТЫВАТЬ')
        user_markup.row('☎ Контакты ☎')
        bot.send_message(message.from_user.id, "Вы вернулись в начальное меню.", reply_markup=user_markup)
    elif message.text=='🅰 Альткоины': #2
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('❓ Сколько я мог заработать')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Альткоины -  называют все остальные криптовалюты, которые надеются либо "
                                               "заменить биткоин, либо улучшить по меньшей мере хотя бы один из его параметров. \n"
                                               "В мире их больше 1300 и они стремительно увеличивают свое \n"
                                               "количество.  https://coinmarketcap.com/currencies/views/all/ \n"
                                               "Чем нам интересны Альткоины ? На них можно заработать огромные проценты, как на начале "
                                               "с bitcoin. \n\n", reply_markup=user_markup)
    elif message.text=='❓ Сколько я мог заработать':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, 'Вам интересно во сколько превратилась бы ваша 1000 дол, если бы вы приобрели в свое '
                                          'время популярные сейчас Криптовалюты? (фото). Еще не поздно, Присоединяйтесь к миру '
                                          'Криптовалют и позвольте сделать Себе большую прибыль.\n\n' , reply_markup=user_markup)
    elif message.text=='🎥 Видео 🎥': #2
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('🎥 Краткие Видео')
        user_markup.row('🎥 Большие Видео')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Ближайшее время ждите подборку интерестного видео со всего мира. Мы роботаем над этим 😊", reply_markup=user_markup)
    elif message.text=='🎥 Краткие Видео':
        bot.send_message(message.chat.id, 'Идёт робота над материалом!')
    elif message.text=='🎥 Большие Видео':
        bot.send_message(message.chat.id,'Идёт робота над материалом!')
    elif message.text=='💰 Кошельки 💰': #6
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('💰 Список холодных')
        user_markup.row('💰 Список горячих')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id,  'Все кошельки делятся на «горячие» и «холодные».  «Горячие» кошельки это те к '
                                               'которым есть постоянный  онлайн доступ , а «Холодные» кошельки можно устанавливать себе на устройство или'
                                               'извлекать (например устанавливать на флешки ). \n\n'
                                                'На волне пристального внимания к криптовалютам создаются десятки новых '
                                               'проектов, включая криптокошельки. Хотя скептики указывают на недолговечность '
                                               'многих начинаний, ведь существуют лишь централизованные кошельки, а '
                                               '«централизованный» — слово, не совсем подходящее для блокчейна.\n',reply_markup=user_markup)
    elif message.text=='💰 Список холодных':
        bot.send_message(message.chat.id, 'Представим вашему вниманию небольшой перечень «холодных» кошельков\n\n'
                                            'Electrum Portable version\n'
                                            'Отличный небольшой Bitcoin-кошелек. Electrum поддерживает детерминированные кошельки . '
                                            'Xapo\n'
                                            'Xapo предоставляет своим пользователям довольно удобный кошелек для повседневных операций, а также Хранилище (Vault, холодный биткоин кошелек), предназначенное для долгосрочного безопасного хранения криптовалюты биткоин. Существуют мобильные версии данного кошелька для Android, а также для iOS.'
                                            'Кроме этого, каждый из пользователей имеет возможность заказать дебетовую карту Xapo для покупок в онлайн-магазинах или снятия наличности в банкоматах по всему миру.\n\n'
                                            'Trezor\n'
                                            'Аппаратный кошелек Trezor рекомендуется тем, кто беспокоится о безопасности собственных средств, хранящихся в биткоинах или поддерживаемых альткойнах. Причем, кошелек является именно дополнительной защитой, реализуемой встроенным микроконтроллером Cortex M3. Для обеспечения защиты используются официальные реализации BIP39 (для работы с ключевыми словами), а также BIP32 и BIP44. Однако, кошелек не хранит в себе весь набор транзакций, используя для этого внешнее хранилище, с которым и организована работа. По этой причине, данный кошелек можно назвать только условно аппаратным. Тем не менее, в своем сегменте Trezor достаточно популярен и эту популярность ему обеспечивает именно реализация обратной связи с пользователем, что является «изюминкой» данного устройства.\n\n'
                                            'GreenAddress\n'
                                            'Среди основных преимуществ мультивалютного кошелька GreenAddress следует выделить следующие:\n'
                                            '• повышенная степень безопасности за счет системы генерации двух ключей;\n'
                                            '• разбивка кошелька на группы по биткоин-адресам;\n'
                                            '• отправка транзакций через SMS-сообщения или аккаунты соцсетей;\n'
                                            '• наличие мобильного приложения для комфортного пользования кошельком.\n\n'
                                            'KeepKey\n'
                                            'Данный кошелек был разработан так, чтобы работать с любым кошельком Bitcoin, установленным на вашем компьютере. Однако, KeepKey будет брать на себя роль хранилища закрытых ключей, а также обрабатывать все транзакции, подписанные с открытым ключом. Основные преимущества, которые предлагают аппаратные кошельки, заключаются в безопасности хранения средств и совершения сделок. Закрытый ключ пользователя хранится на самом устройстве KeepKey, и никогда не покидает его. Кроме того, каждый кошелек защищен PIN кодом, что делает кошелек бесполезным, если было сделано слишком много неправильных попыток ввода.\n')
    elif message.text=='💰 Список горячих':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="BlockChain", url="https://blockchain.info/ru/wallet/#/")
        url_button1 = types.InlineKeyboardButton(text="Holy Transaction", url="https://holytransaction.com")
        url_button2 = types.InlineKeyboardButton(text="Coins Bank", url="https://coinsbank.com")
        url_button3 = types.InlineKeyboardButton(text="Bit AC", url="http://www.bitac.net")
        url_button4 = types.InlineKeyboardButton(text="Bit GO", url="https://www.bitgo.com")
        url_button5 = types.InlineKeyboardButton(text="Coinomi", url="https://coinomi.com")
        url_button6 = types.InlineKeyboardButton(text="Mycelium", url="https://www.mycelium.com")
        url_button7 = types.InlineKeyboardButton(text="Airbitz", url="https://airbitz.co")
        url_button8 = types.InlineKeyboardButton(text="Copay", url="https://copay.io")
        keyboard.add(url_button)
        keyboard.add(url_button1)
        keyboard.add(url_button2)
        keyboard.add(url_button3)
        keyboard.add(url_button4)
        keyboard.add(url_button5)
        keyboard.add(url_button6)
        keyboard.add(url_button7)
        keyboard.add(url_button8)
        bot.send_message(message.chat.id, 'Представим вашему вниманию небольшой перечень «горячих» кошельков.\n\n',reply_markup=keyboard)
    elif message.text=='📈 Курсы 📈': #7
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('Web-сервисы')
        user_markup.row('Мобильные сервисы')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, 'Цена на все Криптовалюты абсолютно разная и не стабильная. Поэтому, вам постоянно нужно '
                                               'быть в курсе всех событий на рынке, так как на разнице в курсе можно заработать \n'
                                               'Сумасшедшие деньги.\n\n'
                                               'Курсы самых известных валют: \n'
                                               'BTC - {0}\n'
                                               'LTC - {1}\n'
                                               'ETH - {2}\n'
                                               'DASH - {3}\n'.format(get_btc(),get_ltc(),get_eth(),get_dash()), reply_markup=user_markup)
    elif message.text== 'Web-сервисы':
        bot.send_message(message.chat.id, 'Обратите внимание на список самых популярные 🖥 Веб-сервисов 🖥, которые позволят вам всегда '
                                          'быть в курсе дела, быть в ТРЕНДЕ! \n\n')
        bot.send_message(message.chat.id,'https://coinmarketcap.com/ - Мониторинг всех Бирж\n\n')
        bot.send_message(message.chat.id,'https://poloniex.com/exchange#btc_bts - Биржа\n\n')
        bot.send_message(message.chat.id,'https://bittrex.com/Home/Markets - Биржа\n\n')
    elif message.text =='Мобильные сервисы': #9
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="IOS -Blockfolio", url="https://appsto.re/ua/n2ptbb.i")
        url_button1 = types.InlineKeyboardButton(text="IOS -Bitcoin Ticker", url="https://appsto.re/ru/dZvpA.i")
        url_button2 = types.InlineKeyboardButton(text="IOS -Polo", url="https://appsto.re/ua/D93Jjb.i")
        url_button3 = types.InlineKeyboardButton(text="IOS -Polofolio", url="https://appsto.re/ua/vd2lkb.i")
        url_button11 = types.InlineKeyboardButton(text="Android -Blockfolio", url="https://play.google.com/store/apps/details?id=com.blockfolio.blockfolio")
        url_button12 = types.InlineKeyboardButton(text="Android -Bitcoin Ticker", url="https://play.google.com/store/apps/details?id=st.brothas.mtgoxwidget")
        url_button13 = types.InlineKeyboardButton(text="Android -Polo", url="https://play.google.com/store/apps/details?id=jonathan.veg.poloniextracker")
        keyboard.add(url_button, url_button11)
        keyboard.add(url_button2,url_button13)
        keyboard.add(url_button1,url_button12)
        keyboard.add(url_button3)
        bot.send_message(message.chat.id, 'В этом разделе вам предоставлены 📲 мобильные 📲 приложения бирж для IOS & Android.',reply_markup=keyboard)
    elif message.text =='📊 Биржи 📊': #9
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('Большие международные')
        user_markup.row('🇺🇦 Украина','🇷🇺 Россия')
        user_markup.row('🇵🇼 Казахстан')
        user_markup.row('💎 НАЧАТЬ ЗАРАБАТЫВАТЬ')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "В мире есть множество Крипто-бирж но как в любой индустрии есть лидеры, с "
                                               "большими оборотами и клиентскими базами. Все биржи «условно» делятся на "
                                               "Большие, средние и малые. \n"
                                               "Перед новичком стоит выбор какую же биржу мне использовать для торгов ? Конечно "
                                               "нужно выбирать самые большие, надежные и стабильные биржи, от этого зависит "
                                               "скорость обработки ваших ордеров на покупку или продажу, сохранность и "
                                               "безопасность ваших монет.\n\n", reply_markup=user_markup)
    elif message.text == 'Большие международные':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard = types.InlineKeyboardMarkup()
        url_button2 = types.InlineKeyboardButton(text="Poloniex", url="https://poloniex.com")
        url_button3 = types.InlineKeyboardButton(text="Bittrex", url="https://bittrex.com")
        url_button4 = types.InlineKeyboardButton(text="Bitfinex", url="https://www.bitfinex.com")
        url_button5 = types.InlineKeyboardButton(text="Livecoin", url="https://www.livecoin.net/ru/site/login")
        url_button6 = types.InlineKeyboardButton(text="Kraken", url="https://www.kraken.com")
        keyboard.add(url_button2,url_button3)
        keyboard.add(url_button4,url_button5)
        keyboard.add(url_button6)
        bot.send_message(message.from_user.id, '📊 Список ТОП-5 криптобирж 📊', reply_markup=keyboard)
    elif message.text=='🇺🇦 Украина':
        bot.send_message(message.chat.id, '📊 Биржи 📊 такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на 🇺🇦 Гривну . \n\n'
                                          '1.	https://btc-trade.com.ua/\n'
                                          '2.	https://exmo.com \n'
                                          '3.	Список обменников работающих PrivatBant - BTC \n'
                                          'https://www.bestchange.ru/privat24-uah-to-bitcoin.html \n\n')
    elif message.text=='🇷🇺 Россия':
        bot.send_message(message.chat.id, '📊 Биржи 📊 такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на 🇷🇺 Рубль. \n\n'
                                          '1.	http://YoBit.Net\n'
                                          '2.	http://EXMO.com \n'
                                          '3.	Список обменников работающих СберБанк - BTC \n'
                                          'https://www.bestchange.ru/sberbank-to-bitcoin.html \n\n')
    elif message.text=='🇵🇼 Казахстан':
        bot.send_message(message.chat.id, '📊 Биржи 📊 такого формата рекомендуем использовать только для Ввода или Вывода \n'
                                          'Криптовалюты на 🇷🇺 Рубль 🇵🇼 Тенге. \n\n'
                                          '1.	https://1wm.kz\n'
                                          '2.	https://pmcash.kz/  \n'
                                          '3.	Список обменников работающих СберБанк - BTC\n'
                                          'https://www.bestchange.ru/sberbank-to-bitcoin.html \n\n')
    elif message.text =='💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎': #10
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('📚 Посмотреть отзывы 📚')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Мы удивим вас если Вы профессионал и обучим - если Новичек.\n\n"
                                               "Мы собрали для вас поток информации  из 16 проверенных источников. Наша "
                                               "команда постаралась объединить информацию со всего мира, от Запада до "
                                               "Востока. Также мы напрямую общаемся с Крупными игроками на биржах, "
                                               "Собственниками фондов и самых больших Майнинговых ферм. И теперь готовы "
                                               "делится этой информацией с Вами.\n\n"
                                               "Наш Чат-Бот\n\n"
                                               "- Пошагово научит торговли на Биржах\n"
                                               "- С формирует Ваш долгосрочный инвестиционный портфель\n"
                                               "- Предоставит сигналы краткосрочных сделок\n"
                                               "- Будет курировать ваши действия\n\n"
                                               "Будем делать Вам деньги или ознакомимся с Нашими отзывами ? \n\n", reply_markup=user_markup)
    elif message.text =='Сколько я могу зароботать?':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Вы заметили какими темпами развивается индустрия криптовалют и сколько "
                                               "людей заработали миллионы $ ? Как показывает практика результат с нашей "
                                               "помощью - Минимум 1000% за Год и Максимума не существует.\n\n"
                                               "      *Давайте предположим что средний результат будет\n 3000%/ год, при  вашей"
                                               "максимальной Активности.\n\n"
                                               "      Инвестиция -   1000$\n"
                                               "      Через год  - 30 000$\n", reply_markup=user_markup)
    elif message.text== '🔙 Вернуться':
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_markup.row('📄 Начать роботу 📄')
        user_markup.row('📚 Посмотреть отзывы 📚')
        user_markup.row('Сколько я могу зароботать?')
        user_markup.row('🔙 Вернуться "Главное меню"')
        bot.send_message(message.from_user.id, "Вы вернулись в меню '💎 НАЧАТЬ ЗАРАБАТЫВАТЬ 💎' ", reply_markup=user_markup)
    elif message.text=='📚 Посмотреть отзывы 📚': #10.2
        bot.send_message(message.chat.id, "Предоставляем краткую подборку наших отзывов")
    elif message.text=='📄 Начать роботу 📄': #10.3
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти к платному боту", url="https://telegram.me/siastrade_bot")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Для активации Всех параметров Вам нужно проплатить   месячную подписку на нашем платном боте для "
                                               "использования нашего Полного функционала.\n Сколько вы готовы заплатить за "
                                               "информацию Которая поможет вам сделать от 1000% до 10 000% за Год ?\n Не "
                                               "упустите ваш реальный Шанс сделать Миллионером. \n\n"
                                               "Для перехода на нашего бота нажмите ссылку внизу\n\n\n", reply_markup=keyboard)
    elif message.text=='🔖 Новости 🔖':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Канал SIAS Plus в Telegram", url="https://telegram.me/siasplus")
        url_button1= types.InlineKeyboardButton(text="Сайт SIAS Plus", url="https://sias.plus")
        keyboard.add(url_button)
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,"Следите за новостями на нашем канале Telegram и на нашем сайте.", reply_markup=keyboard)
    elif message.text =='☎ Контакты ☎': #11
        bot.send_message(message.chat.id, 'Тех.обслуживание')
    elif message.text =='💎 НАЧАТЬ ЗАРАБАТЫВАТЬ':
        bot.send_message(message.chat.id,'Последовательность ваших действий:\n\n'
                                         '1. Регистрация Биткоин кошелька 🔒\n'
                                            '2. Пополнение кошелька через биржи или обменники 📲\n'
                                            '3. Выбор биржи где желаете торговать 📊\n'
                                            '4. Регистрация на бирже 🖥\n'
                                            '5. Пополнение баланса Биржи 💰\n'
                                            '6. Правельный выбор Монет и верная стратегия Торгов 📈\n'
                                            '7. Следить за сервисом SIAS Plus 👀\n'
                                            '8. Вывод Прибыли 💸\n')
    else:
        bot.send_message(message.chat.id,"{0}, вы заблокированы в системе!".format(message.from_user.first_name))




    print(bot.get_me())

    def log(message, answer):
        print("\n ---------------------")
        from datetime import datetime
        print(datetime.now())
        print("Сообщение от {0} {1}. (id={2}) \n Текст- {3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))

bot.polling(none_stop=True,interval=0)
