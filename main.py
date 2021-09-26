# ------------------------------------------------------------------------
# Copyright 2021 Nikita Ozhyhin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------


import telebot
from telebot import types
import customer
import dataBase


token = "1637413790:AAH2QOAzto0bCGuQweYZ-4ddOIZR6At5bts"
bot = telebot.TeleBot(token)

customer = customer.Customer()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте!\n"
                          "Список комманд:\n"
                          "/name - отправка имени и фамилии боту (необходимо для оставления заявки)\n"
                          "/services - предоставляемые услуги\n"
                          "/works - ознакомиться с работами\n")


@bot.message_handler(commands=["name"])
def get_name(message):
    bot.reply_to(message, "Пожалуйста, введите свои имя и фамилию")
    bot.register_next_step_handler(message, reg_name)
    get_name.has_been_called = True


get_name.has_been_called = False


def reg_name(message):
    if str(message.text).replace(" ", "").isalpha():
        bot.send_message(message.from_user.id,
                         "Приятно познакомиться, " + message.text +
                         "! Теперь вы можете оставить заявку ("
                         "/services), либо же ознакомиться с "
                         "моими работами\n(/works)")
        customer.set_customer_id(message.from_user.id)
        customer.set_name(message.text)
    else:
        get_name.has_been_called = False
        bot.send_message(message.from_user.id, "Пожалуйста, проверьте"
                                               " правильность написания"
                                               " имени и фамилии")
        get_name(message)


@bot.message_handler(commands=["services"])
def send_services(message):
    if not get_name.has_been_called:
        bot.send_message(message.from_user.id, "Пожалуйста, "
                                               "сначала введите имя")
    else:
        category_keyboard = types.InlineKeyboardMarkup()
        key_design = types.InlineKeyboardButton(text="Дизайн сайта",
                                                callback_data="design")
        key_website = types.InlineKeyboardButton(text="Сайт под ключ",
                                                 callback_data="website")
        category_keyboard.add(key_design, row_width=2)
        category_keyboard.add(key_website, row_width=2)
        bot.send_message(message.from_user.id,
                         text="Выберите вид желаемой работы",
                         reply_markup=category_keyboard)


@bot.callback_query_handler(lambda call: True)
def send_sub_services(call):
    sub_category_keyboard = types.InlineKeyboardMarkup()
    service_text = ""

    if call.data == "design":
        key_site_design = \
            types.InlineKeyboardButton(text="Дизайн многостраничного сайта",
                                       callback_data="site_design")
        key_landing_design = \
            types.InlineKeyboardButton(text="Дизайн лендинга",
                                       callback_data="landing_design")
        key_eshop_design = \
            types.InlineKeyboardButton(text="Дизайн интернет-магазина",
                                       callback_data="shop_design")
        key_presentation = \
            types.InlineKeyboardButton(text="Создание презентации",
                                       callback_data="presentation")
        sub_category_keyboard.add(key_site_design, row_width=2)
        sub_category_keyboard.add(key_landing_design, row_width=2)
        sub_category_keyboard.add(key_eshop_design, row_width=2)
        sub_category_keyboard.add(key_presentation, row_width=2)
        bot.send_message(call.from_user.id,
                         text="Выберите одну из предоставляемых услуг",
                         reply_markup=sub_category_keyboard)

    elif call.data == "website":
        key_site_creation = \
            types.InlineKeyboardButton(text="Создание многостраничного сайта",
                                       callback_data="site_creation")
        key_landing_creation = \
            types.InlineKeyboardButton(text="Создание лендинга",
                                       callback_data="landing_creation")
        key_eshop_creation = \
            types.InlineKeyboardButton(text="Создание интернет-магазина",
                                       callback_data="shop_creation")
        sub_category_keyboard.add(key_site_creation, row_width=2)
        sub_category_keyboard.add(key_landing_creation, row_width=2)
        sub_category_keyboard.add(key_eshop_creation, row_width=2)
        bot.send_message(call.from_user.id,
                         text="Выберите одну из предоставляемых услуг",
                         reply_markup=sub_category_keyboard)

    if call.data == "site_design":
        service_text = "Дизайн сайта"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на выполнение дизайна сайта принята!")
    elif call.data == "landing_design":
        service_text = "Дизайн лендинга"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на выполнение дизайна лендинга принята!")
    elif call.data == "shop_design":
        service_text = "Дизайн интернет-магазина"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на выполнение дизайна интернет-магазина принята!")
    elif call.data == "presentation":
        service_text = "Создание презентации"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на создание презентации принята!")
    elif call.data == "site_creation":
        service_text = "Создание сайта"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на создание сайта принята!")
    elif call.data == "landing_creation":
        service_text = "Создание лендинга"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на создание лендинга принята!")
    elif call.data == "shop_creation":
        service_text = "Создание интернет-магазина"
        bot.send_message(call.from_user.id,
                         "Ваша заявка на создание интернет-магазина принята!")
    if service_text != "":
        customer.set_service(service_text)
        dataBase.insert_user(customer.get_customer_id(),
                             customer.get_name(), customer.get_service())
        bot.send_message(call.from_user.id,
                         "Спасибо за оставленную заявку,"
                         " мы обязательно с Вами свяжемся в "
                         "кратчайшие сроки!\n"
                         "Оставить ещё одну заявку - /services\n"
                         "Ознакомиться с работами - /works")


@bot.message_handler(commands=["works"])
def send_works(message):
    works_button = types.InlineKeyboardMarkup()
    url_button = \
        types.InlineKeyboardButton(text="Мои работы",
                                   url="https://www.behance.net/dianaleliovska")
    works_button.add(url_button, row_width=2)
    bot.send_message(message.from_user.id,
                     "Нажав на эту кнопку вы можете ознакомиться с моими"
                     " работами", reply_markup=works_button)


if __name__ == '__main__':
    dataBase.load_db()
    bot.polling(none_stop=True)
