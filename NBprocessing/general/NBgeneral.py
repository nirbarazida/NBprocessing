"""
Generic functions to manipulate features in pandas data frame.

This library include the functions:
    1. missing_values(database):
        prints a data frame with all columns that have missing values.
        for every column will print the number of missing values and the present of it out of total index in the column

Created by: Nir Barazida
Good luck!
"""



import pandas as pd
from ._input_check_general import _missing_values_checker


@_missing_values_checker
def missing_values(database):
    """
    General Information
    ----------
    prints a data frame with all columns that have missing values.
    for every column will print the number of missing values and the present of it out of total index in the column

    Parameters
    ----------
    :param database: pandas Data Frame
    data set to fill missing values in.

    Returns
    -------
    None.
    prints a data frame with all columns that have missing values.

    Raises
    ------
    ValueError : If input value not as mentioned above.

    Exemples
    -------
    Will be added in version 0.2
    """

    columns_missing_values = (database.count() / len(database)) < 1
    missing_values = database.loc[:, columns_missing_values].isnull().sum().sort_values(ascending=False)
    missing_value_df = pd.concat([missing_values, 100 * round(missing_values / len(database), 3)],
                                 axis=1, keys=["#Missing_values", "%Missing_values"])
    return missing_value_df

