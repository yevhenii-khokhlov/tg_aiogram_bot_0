from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import dp, bot
from keyboards.inline.choice_buttons import choice_inline_buttons
from keyboards.inline.callback_datas import edit_callback


@dp.message_handler(Command("inline_buttons_1"))
async def show_inline_buttons_1(message: types.Message):
    await message.answer(text="Edit @Sberleadbot info.\n\n"
                              "Name: Бот для Заданий на Курсе Udemy\n"
                              "Description: ?\n"
                              "About: ?\n"
                              "Botpic: ? no botpic\n"
                              "Commands: no commands yet",
                         reply_markup=choice_inline_buttons
                         )


@dp.callback_query_handler(edit_callback.filter(new_value='SomeValue'))
async def edit_values(call: CallbackQuery):
    await bot.answer_callback_query(callback_query_id=call.id)
