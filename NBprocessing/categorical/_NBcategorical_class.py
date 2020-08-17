"""
Generic functions to manipulate categorical features in pandas data frame.

This library include the functions:
    1. remove_categories(database, column_name, categories_to_drop):
        Remove all indexes in the database that contain the categories from the categories_to_drop.
        Before removing the indexes will print a message to the user with the number of indexes that
        will be remove and the percent of the database that will be lost.
        the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
        If the user choose 'yes' the method will continue to drop the indexes and will
        plot the new database shape.

    2. fill_na_by_ratio(database, column_name):
        Fill all missing values in the given column by the ratio of the categories in the column.
        Because the ratio sum is not a perfect one - the extra missing values will
        be filled with the most common category in the column.

    3. combine_categories(database, column_name, category_name="other", threshold=0.01):
        Receives a threshold that is the minimum relative part of the category within the column.
        all categories that are less than this threshold will be combined under the same category
        under the name 'category_name'.
        the method will return a list with all the name of categories that were combined under 'category_name'
        with this list the user will be able to make the same action on the test set (assuming that the data
        was already splitted to train and test sets)

    4. categories_not_in_common(train, test, column_name):
        To avoid different shapes of train and test data sets after creating dummies, the user is able to
        check if one categories is missing in the data sets.
        It will check all categories name of the two data sets and returns the name of the categories not
        in common for every data set.
        The information from this method will be returned as list of tuples:
            [(exists only in the first data set),(exists only in the second data set)]
        will also print every list as a message to the user.

    5. category_ratio(database, columns_to_check=None, num_categories=5):
        Returns a data base with categories and their ratio of appearance in the column.
        The user can input a list of columns to check or the method will return all the columns categories ratio.
        The user can choose how many *top* categories will be returned.
        Categories with value under 5% or over 90% will be marked in red to raise a flag that the data
        is imbalanced.


Create by: Nir Barazida
Good luck!
"""

from NBprocessing.categorical._input_check_categorical import _InputCheckCategorical

from NBprocessing.categorical._general_functions_categorical import color_imbalanced
from NBprocessing.src import constance_object

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


class NBcategorical(object):
    """
    Generic functions to manipulate categorical features in pandas data frame.

    This library include the functions:
        1. remove_categories(database, column_name, categories_to_drop):
            Remove all indexes in the database that contain the categories from the categories_to_drop.
            Before removing the indexes will print a message to the user with the number of indexes that
            will be remove and the percent of the database that will be lost.
            the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
            If the user choose 'yes' the method will continue to drop the indexes and will
            plot the new database shape.

        2. fill_na_by_ratio(database, column_name):
            Fill all missing values in the given column by the ratio of the categories in the column.
            Because the ratio sum is not a perfect one - the extra missing values will
            be filled with the most common category in the column.

        3. combine_categories(database, column_name, category_name="other", threshold=0.01):
            Receives a threshold that is the minimum relative part of the category within the column.
            all categories that are less than this threshold will be combined under the same category
            under the name 'category_name'.
            the method will return a list with all the name of categories that were combined under 'category_name'
            with this list the user will be able to make the same action on the test set (assuming that the data
            was already splitted to train and test sets)

        4. categories_not_in_common(train, test, column_name):
            To avoid different shapes of train and test data sets after creating dummies, the user is able to
            check if one categories is missing in the data sets.
            It will check all categories name of the two data sets and returns the name of the categories not
            in common for every data set.
            The information from this method will be returned as list of tuples:
                [(exists only in the first data set),(exists only in the second data set)]
            will also print every list as a message to the user.

        5. category_ratio(database, columns_to_check=None, num_categories=5):
            Returns a data base with categories and their ratio of appearance in the column.
            The user can input a list of columns to check or the method will return all the columns categories ratio.
            The user can choose how many *top* categories will be returned.
            Categories with value over 90% will be marked in red to raise a flag that the data
            is imbalanced.

        6. def label_encoder_features(database, features_to_encode):
            Encode features in the giving database using LabelEncoder() from sklearn.
            Will preform encoding on all giving features and returns a dictionary with all the different
            encoders where the ket is the feature name and the value is the LabelEncoder instance fitted
            to that feature. Thus, the user is able to un-encode the feature when necessary.

    Create by: Nir Barazida
    Good luck!

    """

    @staticmethod
    @_InputCheckCategorical._remove_categories_checker
    def remove_categories(database, column_name, categories_to_drop):
        """
        General Information
        ----------
        Remove all indexes in the database that contain the categories from the categories_to_drop.
        Before removing the indexes will print a message to the user with the number of indexes that
        will be remove and the percent of the database that will be lost.
        the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
        If the user choose 'yes' the method will continue to drop the indexes and will
        plot the new database shape.

        Parameters
        ----------
        :param database: pandas Data Frame
        the database must contain the column that was sent to the method 'column_name'

        :param column_name: string
        The name of the column where the values ​​are and from which we will be parsing the categories.
        the column_name must be identical to the column name in the database.
        This column must be a categorical column.

        :param categories_to_drop: list or tuple of string int of float
        The name of the categories the user wish to drop.

        Returns
        -------
        None
        This method prints information to help the user decide rather to drop the categories or not.
        eventually returns None

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """

        remove_df = database[database[column_name].isin(categories_to_drop)]

        user_input = input(
            constance_object.USER_INPUT.format(len(remove_df), round(len(remove_df) * 100 / len(database), 2)))

        while user_input != 'y' and user_input != 'n':
            user_input = input(
                constance_object.USER_INPUT.format(len(remove_df), round(len(remove_df) * 100 / len(database), 2)))

        if user_input == 'y':
            for value in categories_to_drop:
                database.drop(database.loc[database[column_name] == value].index, inplace=True)
            print(constance_object.DATABASE_SHAPE.format(database.shape))

    @staticmethod
    @_InputCheckCategorical._fill_na_by_ratio_checker
    def fill_na_by_ratio(database, column_name):
        """
        General Information
        ----------
        Fill all missing values in the given column by the ratio of the categories in the column.
        Because the ratio sum is not a perfect one - the extra missing values will
        be filled with the most common category in the column.

        Parameters
        ----------
        :param database: pandas Data Frame
        the database must contain the column that was sent to the method 'column_name'

        :param column_name:  string
        The name of the column where method will fill the missing values in.
        This column must be a categorical column

        Returns
        -------
        None
        fill the missing values in the column inplace.

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """
        try:
            categories_names = list(database[column_name].value_counts(normalize=True, dropna=True).index)
            categories_ratio = list(database[column_name].value_counts(normalize=True, dropna=True).values)

            database[column_name] = database[column_name].fillna(
                pd.Series(np.random.choice(categories_names, p=categories_ratio, size=len(database))))

            # Fill the extra missing values
            database[column_name].fillna(database[column_name].value_counts().index[0], inplace=True)
        except NameError as e:
            print(e)

    @staticmethod
    @_InputCheckCategorical._combine_categories_checker
    def combine_categories(database, column_name, category_name="other", threshold=0.01):
        """
        General Information
        ----------
        Receives a threshold that is the minimum relative part of the category within the column.
        all categories that are less than this threshold will be combined under the same category
        under the name 'category_name'.
        the method will return a list with all the name of categories that were combined under 'category_name'
        with this list the user will be able to make the same action on the test set (assuming that the data
        was already splitted to train and test sets)

        Parameters
        ----------
        :param database: pandas Data Frame
        the database must contain the column that was sent to the method 'column_name'

        :param column_name: string
        The name of the column where method will fill the missing values in.
        This column must be a categorical column

        :param category_name: string
         The name of the new category of the combined categories

        :param threshold: float - 0 < threshold_percentage < 1
        Threshold that represent the ratio value the categories under it will be combined

        Returns
        -------
        the method will return a list with all the name of categories that were combined under 'category_name'
        with this list the user will be able to make the same action on the test set (assuming that the data
        was already splitted to train and test sets)

        for exemple: (LIST - the returned list from the function)
        X_test["column_name"].replace(LIST, category_name, inplace=True)

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2

        """

        values_to_combine = database[column_name].value_counts()[
            database[column_name].value_counts(normalize=True) < threshold].index
        database[column_name].replace(values_to_combine, category_name, inplace=True)
        return values_to_combine

    @staticmethod
    @_InputCheckCategorical._categories_not_in_common_checker
    def categories_not_in_common(train, test, column_name):
        """
        General Information
        ----------
        To avoid different shapes of train and test data sets after creating dummies, the user is able to
        check if one categories is missing in the data sets.
        It will check all categories name of the two data sets and returns the name of the categories not
        in common for every data set.
        The information from this method will be returned as list of tuples:
            [(exists only in the first data set),(exists only in the second data set)]
        will also print every list as a message to the user.

        Parameters
        ----------
        :param train: pandas Data Frame
        First data set to check columns names from

        :param test: pandas Data Frame
        Second data set to check columns names from

        :param column_name: string
        The name of the column to preform the check.
        This column must be a categorical column

        :return:
        The information from this method will be returned as list of tuples:
            [(exists only in the first data set),(exists only in the second data set)]

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """

        in_test = set(test[column_name]) - set(train[column_name])
        in_train = set(train[column_name]) - set(test[column_name])
        print(constance_object.FIRST.format(in_test))
        print(constance_object.SECOND.format(in_train))

    @staticmethod
    @_InputCheckCategorical._category_ratio_checker
    def category_ratio(database, columns_to_check=None, num_categories=5):
        """
        General Information
        ----------
        Returns a data base with categories and their ratio of appearance in the column.
        The user can input a list of columns to check or the method will return all the columns categories ratio.
        The user can choose how many *top* categories will be returned.
        Categories with value over 90% will be marked in red to raise a flag that the data
        is imbalanced.

        Parameters
        ----------
        :param database: pandas Data Frame
        First data set to check columns names from

        :param columns_to_check: list or tuple of strings/int/float
        The column name that the user wishes to check the categories ratio in.
        All column names must be in the database.


        :param num_categories: int
        The number of top categories that will be plotted.
        If the number is higher than the number of categories than will insert '0.00'

        :return:
        The information from this method will be returned as list of tuples:
            [(exists only in the first data set),(exists only in the second data set)]

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """

        category_ratio_df = pd.DataFrame()
        if not columns_to_check:
            columns_to_check = database.columns

        for column_name in columns_to_check:
            name = database[column_name].value_counts(normalize=True).index
            values = database[column_name].value_counts(normalize=True).values
            val_count_temp = [f"{category} : {round(frequent * 100, 2)}%" for category, frequent in zip(name, values)]
            if len(val_count_temp) < num_categories:
                val_count = ['0.00'] * num_categories
                val_count[:len(val_count_temp)] = val_count_temp
            else:
                val_count = val_count_temp[:num_categories]
            category_ratio_df[column_name] = val_count
        return category_ratio_df.transpose().style.applymap(color_imbalanced)

    # todo: debug
    # @staticmethod
    # @_InputCheckCategorical.label_encoder_features_checker
    # def label_encoder_features(database, features_to_encode):
    #     """
    #     General Information
    #     ----------
    #     Encode features in the giving database using LabelEncoder() from sklearn.
    #     Will preform encoding on all giving features and returns a dictionary with all the different
    #     encoders where the ket is the feature name and the value is the LabelEncoder instance fitted
    #     to that feature. Thus, the user is able to un-encode the feature when necessary.
    #
    #     Parameters
    #     ----------
    #     :param database: pandas Data Frame
    #     First data set to check columns names from
    #
    #     :param features_to_encode: list or tuple of strings/int/float
    #     The column names that the user wishes to encode.
    #     All column names must be in the database and categorical/
    #
    #     :return:
    #     returns a dictionary with all the different
    #     encoders where the ket is the feature name and the value is the LabelEncoder instance fitted
    #     to that feature. Thus, the user is able to un-encode the feature when necessary.
    #
    #     Raises
    #     ------
    #     ValueError : If input value not as mentioned above.
    #
    #     Exemples
    #     -------
    #     Will be added in version 0.2
    #     """
    #
    #     label_encoder_dict = {}
    #
    #     for feat in features_to_encode:
    #         le = LabelEncoder()
    #
    #         # fit the feature that we want to encode and tresform to numeric categories
    #         database[feat] = le.fit_transform(database[feat])
    #
    #         print(f"for deature {feat} the categories are:\n", database[feat].value_counts().index)#todo:changeToConst
    #
    #         label_encoder_dict[feat] = le
    #
    #     return label_encoder_dict
