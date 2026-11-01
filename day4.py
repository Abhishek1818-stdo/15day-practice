#TASK A
import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} complete"

async def main():
    first = await fetch("profile", 1)
    second = await fetch("alerts", 1)
    third = await fetch("feed", 1)
    print(first, second, third)
    results = await asyncio.gather(
        fetch("profile", 1),
        fetch("alerts", 1),
        fetch("feed", 1),
    )
    print(results)

asyncio.run(main())

#“When I run the three coroutines one after another, each one waits for the previous one to finish. Since each takes about one second the total time is around three seconds.
#With asyncio.gather(), the three independent tasks can wait at the same time, so the total is around one second. This is useful when an API needs to fetch data from multiple independent services. It can save waiting time, but it doesn’t automatically make CPU-heavy work faster.

#TaskB

import asyncio
from fastapi import FastAPI

app = FastAPI()
@app.get("/status")
async def get(status):
    await asyncio.sleep(1)
    return{"status":"ready"}

#I made this endpoint asynchronous using async def. The await asyncio.sleep(1) is just a way to show waiting without stopping the whole app. While this endpoint is waiting, FastAPI can work on other requests too,I should avoid blocking calls like time.sleep() inside an async route because they can hold up other requests



#task c
from time import perf_counter
from fastapi import Request

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start = perf_counter()

    response = await call_next(request)

    elapsed = perf_counter() - start
    response.headers["X-Process-Time"] = f"{elapsed:.6f}"

    return response
#I added middleware to check how long each request takes. It starts a timer when a request comes in, lets the endpoint do its work, and then adds the time taken to the response. This helps me spot requests that are taking too long


#task D
from fastapi import Depends, HTTPException

def get_current_user():
    return{"id":7,"role":"admin"}

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403,detail="Forbidden")
    return user

@app.get("/admin")
def admin_details(user=Depends(require_admin)):
    return{"user_id":user["id"]}

#I used Depends() so I don’t have to repeat the same thing in every endpoint. One helper gets the user’s details, and the other checks if they’re an admin


#TASK E


#I put the user routes and product routes in separate files to keep my code organized. APIRouter helps me group related endpoints, and include_router() connects them to the main app
#i have arranged them in app.py4 folder


#TASK F

#lifespan

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting")
    app.state.ready = True

    yield

    app.state.ready = False
    print("App is shutting down")

app = FastAPI(lifespan=lifespan)


#background

from fastapi import BackgroundTasks

def write_log(message: str):
    print(message)

@app.post("/orders")
def create_order(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Order created")
    return {"message": "Order accepted"}


#I used lifespan to handle things when the app starts and stops. I also added a small task that runs after the response, like printing a log message. That’s handy for simple tasks, but for important work that must not be missed, I’d use a proper background worker because the task could be lost if the app shuts down

