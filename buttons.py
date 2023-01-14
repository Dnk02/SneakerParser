from aiogram import types

buttons_street_beat = ["👟Puma", "👟Adidas", "👟New-balance", "👟Reebok", "⏪К выбору магазина"]
markup_brands = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_brands.row(buttons_street_beat[0], buttons_street_beat[1]).row(buttons_street_beat[2],
                                                                      buttons_street_beat[3]).row(
    buttons_street_beat[4])

buttons_sneaker_head = ["👟👟Puma", "👟👟Adidas", "👟👟New-balance", "⏪К выбору магазина"]
markup_brands2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_brands2.row(buttons_sneaker_head[0], buttons_sneaker_head[1], buttons_sneaker_head[2]).row(
    buttons_sneaker_head[3])

markup_street_beat_choose = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2 = ["Показать⏩", "Вернуться к выбору⏪"]
markup_street_beat_choose.row(buttons2[0]).row(buttons2[1])

markup_sneaker_head_choose = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2 = ["Показать⏭", "Вернуться к выбору⏮"]
markup_sneaker_head_choose.row(buttons2[0]).row(buttons2[1])

buttons3 = ["Street-beat", "Sneaker-head"]
markup_stores = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_stores.row(*buttons3)
