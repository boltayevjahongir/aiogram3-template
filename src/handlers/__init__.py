from aiogram import Router
from .start import router as start_router
from .callback import router as callback_router
from .user import router as user_router
from .echo import router as echo_router

def register_all_handlers() -> Router:
    """
    Barcha handlerlarni yagona routerda birlashtiradi.
    """
    main_router = Router()
    main_router.include_router(start_router)
    main_router.include_router(callback_router)
    main_router.include_router(user_router)


    main_router.include_router(echo_router)
    return main_router