from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Q # 1 is:")

# await Test.first()
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(massage: types.Message, state: FSMContext):
    answer = massage.text

    await massage.answer("Answer 1.")

    # await Test.Q1.set()
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(massage: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = massage.text

    await massage.answer("Test is done.")
    await massage.answer(f"A1 = {answer1}")
    await massage.answer(f"A2 = {answer2}")

    await state.finish()
    # await state.reset_state()
    # await state.reset_state(with_data=False) #сохраняет данніе
