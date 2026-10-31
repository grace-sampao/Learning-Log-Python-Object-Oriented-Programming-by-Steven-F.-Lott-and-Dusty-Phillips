# Variations of the `import` statement syntax used to access parts of a module:
# 1. Import the module as a whole
import random

def dice1() -> tuple[int, int]:
    return (
        random.randint(1, 6), random.randint(1, 6)
    )


# 2. Import just the one class we need using the `from...import` syntax
from random import randint

def dice2() -> tuple[int, int]:
    return (
        randint(1, 6), randint(1, 6)
    )


# 3. Rename the object during import
from random import randint as rng

def dice3() -> tuple[int, int]:
    return (
        rng(1, 6), rng(1, 6)
    )


# 4. Import multiple items in one statetment
from random import seed, Random


# 5. Import all classes and functions from a module (DON'T DO THIS!!!)
from random import *
