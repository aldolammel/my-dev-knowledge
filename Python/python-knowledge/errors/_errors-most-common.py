
"""
    PYTHON: ERRORS, MOST COMMON OF THEM

    Or how to use 'try-catch' in Python:
        ./errors-exceptions.py

    For Django framework:
        /Python/Web-development/django/6-errors-and-validations/raise-error.txt

"""


# Generic - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
raise Exception("Unknown error!")



# IndexError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
list_ = ["apple", "banana"]  # 0, 1
item = list_[2]

raise IndexError("This index doesn't exist!")

idx = ...
array = [1, 2, 3]
if not array[idx]:
    raise IndexError("Index out of range")



# ValueError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")



# TypeError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# example 1:
text = "abc"
print(text + 5)
raise TypeError("Please, use just numbers (0-9)!")

# example 2:
name = 123
if not isinstance(name, str):
    raise TypeError("Name must be a string")



# KeyError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

data = {"name": "Aldo"}
if "age" not in data:
    raise KeyError("Key 'age' not found")



# FileNotFound - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Simplest:
import os
filename = "missing.txt"
if not os.path.exists(filename):
    raise FileNotFoundError(f"{filename} not found")

# Using try-exception: ./errors-exceptions.py
try:
    with open("missing.txt") as file:
        file.read()
except FileNotFoundError:
    print(f"{file} not found")



# ZeroDivisionError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def calculate_ratio(profit, investment):
    if investment == 0:
        raise ZeroDivisionError("Investment cannot be zero")
    return profit / investment



# NotImplementedError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class PaymentGateway:
    def charge(self, amount: float):
        raise NotImplementedError("Subclasses must implement 'charge' method")

class StripeGateway(PaymentGateway):
    def charge(self, amount: float):
        return f"Charging {amount} via Stripe"


# MemoryError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def process_large_dataset(records):
    if len(records) > 10_000_000:
        raise MemoryError("Dataset too large to process in memory")
    return sum(records)



# FloatingPointError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import math
def compute_log(value):
    if value <= 0:
        raise FloatingPointError("Log undefined for non-positive values")
    return math.log(value)



# PermissionError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import os
def delete_file(path):
    if not os.access(path, os.W_OK):
        raise PermissionError(f"No permission to delete: {path}")
    os.remove(path)



# IsADirectoryError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import os
def read_config(path):
    if os.path.isdir(path):
        raise IsADirectoryError(f"{path} is a directory, expected file")
    with open(path) as f:
        return f.read()



# NotADirectoryError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import os

def list_images(folder):
    if not os.path.isdir(folder):
        raise NotADirectoryError(f"{folder} is not a directory")
    return os.listdir(folder)



# TimeoutError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import time
def fetch_data(timeout_seconds):
    start = time.time()
    time.sleep(3)
    if time.time() - start > timeout_seconds:
        raise TimeoutError("Request exceeded timeout limit")
    return "data"



# ImportError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def load_numpy():
    try:
        import numpy
    except ImportError:
        raise ImportError("numpy is required for this operation")
    return numpy



# ModuleNotFoundError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import importlib
def load_plugin(plugin_name):
    try:
        return importlib.import_module(plugin_name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Plugin '{plugin_name}' not installed")



# NameError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def get_variable(var_name):
    if var_name not in globals():
        raise NameError(f"Variable '{var_name}' is not defined")
    return globals()[var_name]



# StopIteration - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
