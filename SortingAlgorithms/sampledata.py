#sampledata.py
from random import sample

def create_sample(size):
    dataset = sample(range(1, size+1), size)
    return dataset