from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Create your states here.
class TaxiState(StatesGroup):
    """
    Taksi buyurtma holati uchun StateGroup.
    """
    Location = State()
    Destination = State()
    Number_People = State()
    Summa = State()
    Tel_Nomer = State()
    UnFinished = State()
    Finish = State()
    Edit_Location = State()
    Edit_Destination = State()
    Edit_Number_People = State()
    Edit_Summa = State()
    Edit_Tel_Nomer = State()
    Cancel = State()