# bot/states/order_states.py

from aiogram.fsm.state import StatesGroup, State

class SomeOrderStates(StatesGroup):
    viewing = State()

