import random
import numpy as np
import torch
from loguru import logger

def set_random_seed(seed, device):

  if seed != -1:
    
