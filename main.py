from NBprocessing import NBcategorical
from NBprocessing import NBcontinuous
from NBprocessing import NBplot
from NBprocessing import NBgeneral

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



if __name__ == '__main__':
    data = pd.read_csv('NBprocessing/dataset_cars.csv')
    print(data.columns)
    print(NBgeneral.missing_values(data))
