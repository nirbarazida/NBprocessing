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
from NBprocessing.general._input_check_general import _InputCheckGeneral
from sklearn.model_selection import train_test_split
from NBprocessing.src import constance_object

class NBgeneral(object):
    """
    Generic functions to manipulate features in pandas data frame.

    This library include the functions:
        1. missing_values(database):
            prints a data frame with all columns that have missing values.
            for every column will print the number of missing values and the present of it out of total index in the column

        2. split_and_check(database, column_name, test_size=0.3):
            Gets a database and target column, split and return:
                2 different data sets splitted by the ratio defined in 'test_size' variable
                etch data set will be split to main data and target column
                total 4 variables
            Will also print the shape of every data set.

    Created by: Nir Barazida
    Good luck!
    """

    @staticmethod
    @_InputCheckGeneral._missing_values_checker
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
        """

        columns_missing_values = (database.count() / len(database)) < 1
        missing_values = database.loc[:, columns_missing_values].isnull().sum().sort_values(ascending=False)
        missing_value_df = pd.concat([missing_values, 100 * round(missing_values / len(database), 3)],
                                     axis=1, keys=["#Missing_values", "%Missing_values"])
        return missing_value_df

    @staticmethod
    @_InputCheckGeneral._split_and_check_checker
    def split_and_check(database, column_name, test_size=0.3):
        """
        General Information
        ----------
        Gets a database and target column, split and return:
            2 different data sets splitted by the ratio defined in 'test_size' variable
            etch data set will be split to main data and target column
            total 4 variables
        Will also print the shape of every data set.

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to fill missing values in.

        :param column_name: string
        the name of the target column

        :param test_size: float range 0<x<1
        the ratio that the data set will be split by


        Returns
        -------
        X_train, X_test, y_train, y_test
        print the shape of every data set.

        Raises
        ------
        ValueError : If input value not as mentioned above.
        """

        X = database.drop(column_name, axis=1)
        y = database[column_name]
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                            test_size=test_size, random_state=42)
        print(constance_object.SPLIT_AND_CHECK.format(X_train.shape,y_train.shape,
                                                      X_test.shape,y_test.shape))
        return X_train, X_test, y_train, y_test


