"""
    Define the api and tie api routers
"""

from fastapi import FastAPI
from  routers import users, orders
import uvicorn

app = FastAPI()

app.include_router(users.router)
app.include_router(orders.router)

if __name__ == "__main__":
    """ Main Function """
    uvicorn.run(app, host='localhost', port=8000)


