from aiogram import Router, F, types
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message, ReplyKeyboardRemove


import random

router = Router()


Field = "MyData"
MyModel = "MyModel"

class Order(StatesGroup):
    get_exercise = State()
    getAnswer = State()
    ShowOrNotCorrectAnswer = State()


@router.message(StateFilter(None), Command(commands=["cancel"]))
@router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Order.get_exercise)
async def get_exercise(message: Message, state: FSMContext):

    user_data = await state.get_data()
    model = user_data[MyModel]
    #data = user_data[Field]

    t = list(model.data.keys())
    key = random.choice(t)

    text = model.text(key)

    await state.update_data(exercise=key)

    await message.answer(
        text=f"Решите задание:\n\n{text}",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(Order.getAnswer)



@router.message(Order.getAnswer)
async def get_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    model = user_data[MyModel]

    answer = message.text
    key = user_data["exercise"]

    if model.check_answer(key, answer):
        await message.answer(
            text="Все правильно!"
        )

        await state.set_state(Order.get_exercise)
        await get_exercise(message, state)

    else:

        kb = [
            [types.KeyboardButton(text="Да")],
            [types.KeyboardButton(text="Нет")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

        await message.answer(
            text="Неверно :(\nПоказать ответ?",
            reply_markup=keyboard,
        )

        await state.set_state(Order.ShowOrNotCorrectAnswer)


@router.message(Order.ShowOrNotCorrectAnswer, F.text.lower() == "да")
async def show_answer(message: Message, state: FSMContext):
     user_data = await state.get_data()

     model = user_data[MyModel]
     #data = user_data[Field]

     key = user_data["exercise"]
     correct_answer = model.get_correct_answer(key)



     await message.answer(
         text=f"Верный ответ:\n\n{correct_answer}",
     )

     await state.set_state(Order.get_exercise)
     await get_exercise(message, state)

@router.message(Order.ShowOrNotCorrectAnswer, F.text.lower() == "нет")
async def not_show_answer(message: Message, state: FSMContext):
    await state.set_state(Order.get_exercise)
    await get_exercise(message, state)

@router.message(Order.ShowOrNotCorrectAnswer)
async def incorrect_show_answer(message: Message, state: FSMContext):

    kb = [
        [types.KeyboardButton(text="Да")],
        [types.KeyboardButton(text="Нет")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(
        text="Нет такого варианта ответа. Выберите пожалуйста да/нет",
        reply_markup=keyboard
    )

    await state.set_state(Order.ShowOrNotCorrectAnswer)

