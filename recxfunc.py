import asyncio
import time
from random import seed
from random import random

seed(time.time())

def fire_and_forget(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return wrapped


@fire_and_forget
def choose_lib(libraries, books):
