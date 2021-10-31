import uvicorn as uvicorn
from fastapi import FastAPI
import app.controller.AppController as AppController 
 
 
def create_app():
    fast_app = FastAPI()
    fast_app.include_router(AppController.router)
    return fast_app
 
 
if __name__ == '__main__':
    app = create_app()
    uvicorn.run("main:create_app", reload=True)