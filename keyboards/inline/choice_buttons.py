from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import edit_callback


keyboard = [
    [
        InlineKeyboardButton(
            text='Edit Name',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
        InlineKeyboardButton(
            text='Edit Description',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
    ],
    [
        InlineKeyboardButton(
            text='Edit About',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
        InlineKeyboardButton(
            text='Edit Botpic',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
    ],
    [
        InlineKeyboardButton(
            text='Edit Commands',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
        InlineKeyboardButton(
            text='<<Back to Bot',
            callback_data=edit_callback.new(new_value='SomeValue')
        ),
    ],
]

choice_inline_buttons = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=keyboard
)
