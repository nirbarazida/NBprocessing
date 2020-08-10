from NBprocessing.categorical import _NBcategorical_class
from NBprocessing.continuous import _NBcontinuous_class
from NBprocessing.plot import _NBplot_class
from NBprocessing.general import _NBgeneral_class
import pandas as pd
if __name__ == '__main__':
    data = pd.read_csv('dataset_cars.csv')

    print(_NBgeneral_class.missing_values(data))

    filter_dict_up = {
        "selling_price": 3000000,
    }

    filter_dict_down = {
    }
