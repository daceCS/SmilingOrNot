import numpy as np
import pandas as pd

# import all the images to train
import os

for dirname, _, filenames in os.walk('./images'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
