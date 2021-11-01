"""
main.py lança a aplicação inicando o servidor
"""
import uvicorn
from fastapi import FastAPI
from src.controller import app_controller as AppController


def create_app():
    """ cria aplicação FastApi """
    fast_app = FastAPI()
    fast_app.include_router(AppController.router)
    return fast_app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run("main:create_app", reload=True)
