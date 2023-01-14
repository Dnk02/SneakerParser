from aiogram import Dispatcher, Bot, types, executor
from environs import Env

from Parser import street_beat_puma, street_beat_adidas, street_beat_reebok, street_beat_new_balance, \
    next_street_beat
from buttons import markup_stores, markup_brands, markup_brands2, markup_street_beat_choose, markup_sneaker_head_choose
from sneaker_head import sneaker_head_puma, sneaker_head_adidas, sneaker_head_new_balance, next_sneaker_head

env = Env()
env.read_env()

bot = Bot(token=env.str("token"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(mess: types.Message):
    await mess.answer("Выберите магазин", reply_markup=markup_stores)


@dp.message_handler(text="Street-beat")
async def street_beat(mess: types.Message):
    await mess.answer("Выберите бренд", reply_markup=markup_brands)


@dp.message_handler(text="Sneaker-head")
async def street_beat(mess: types.Message):
    await mess.answer("Выберите бренд", reply_markup=markup_brands2)


@dp.message_handler(text="⏪К выбору магазина")
async def street_beat(mess: types.Message):
    await mess.answer("Выберите магазин", reply_markup=markup_stores)


@dp.message_handler(text="Вернуться к выбору⏪")
async def street_beat_back(mess: types.Message):
    await mess.answer("Что искать", reply_markup=markup_brands)


@dp.message_handler(text="Вернуться к выбору⏮")
async def sneaker_head_back(mess: types.Message):
    await mess.answer("Что искать", reply_markup=markup_brands2)


@dp.message_handler(text="👟Puma")
async def streetbeat_puma(mess: types.Message):
    try:
        positions = street_beat_puma()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_street_beat_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟Adidas")
async def streetbeat_adidas(mess: types.Message):
    try:
        positions = street_beat_adidas()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_street_beat_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟Reebok")
async def streetbeat_reebok(mess: types.Message):
    try:
        positions = street_beat_reebok()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_street_beat_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟New-balance")
async def streetbeat_new_balance(mess: types.Message):
    try:
        positions = street_beat_new_balance()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_street_beat_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟👟Puma")
async def sneakerhead_puma(mess: types.Message):
    try:
        positions = sneaker_head_puma()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_sneaker_head_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟👟Adidas")
async def sneakerhead_puma(mess: types.Message):
    try:
        positions = sneaker_head_adidas()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_sneaker_head_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="👟👟New-balance")
async def sneakerhead_puma(mess: types.Message):
    try:
        positions = sneaker_head_new_balance()
        await mess.answer(f"Найдено {positions} позиций", reply_markup=markup_sneaker_head_choose)
    except:
        await mess.answer("Ошибка 403, повтори позже")



@dp.message_handler(text="Показать⏩")
async def next(mess: types.Message):
    try:
        sneakers = next_street_beat()
        for position in sneakers:
            result = f""
            for item in position:
                result += f"{item}\n"
            await mess.answer(result)
    except IndexError:
        await mess.answer("Просмотрены все позиции")


@dp.message_handler(text="Показать⏭")
async def next(mess: types.Message):
    try:
        sneakers = next_sneaker_head()
        for position in sneakers:
            result = f""
            for item in position:
                result += f"{item}\n"
            await mess.answer(result)
    except IndexError:
        await mess.answer("Просмотрены все позиции")


if __name__ == "__main__":
    executor.start_polling(dp)
