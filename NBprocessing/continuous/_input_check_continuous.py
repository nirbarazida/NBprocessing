"""
This file contain wraps function that will check the input of the continuous function.
will raise exceptions if the input is not valid.
This file is using the generic check input class 'CheckInput' that contains all the
input validation to all the functions

Created by: Nir Barazida
Good luck
"""


from functools import wraps
from NBprocessing.src._check_input import _CheckInput


def _fill_na_timedate_checker(func):
    """
    Wrapper function to validate the input for method 'fill_na_timedate'
    Will raise Exception if input incorrect or data type not date time.
    """

    @wraps(func)
    def wrapper_checker(database, column_name):
        _CheckInput._check_database_input(database)
        _CheckInput._check_column_name(column_name)
        _CheckInput._check_type_date_time(database,column_name)
        _CheckInput._check_column_in_database(column_name, database)
        return func(database, column_name)
    return wrapper_checker


def _remove_outliers_by_boundaries_checker(func):
    """
    Wrapper function to validate the input for method 'remove_outliers_by_boundaries'
    Will raise Exception if input incorrect or data type not date time.
    """

    @wraps(func)
    def wrapper_checker(database, column_name, bot_qu, top_qu):
        _CheckInput._check_database_input(database)
        _CheckInput._check_column_name(column_name)
        _CheckInput._check_column_in_database(column_name, database)
        _CheckInput._check_boundaries(top_qu)
        _CheckInput._check_boundaries(bot_qu)
        return func(database, column_name, bot_qu, top_qu)
    return wrapper_checker


def _remove_and_get_num_outliers_by_value_checker(func):
    """
    Wrapper function to validate the input for methods 'get_num_outliers_by_value' and 'remove_outliers_by_value'
    Will raise Exception if input incorrect or data type not date time.
    """

    @wraps(func)
    def wrapper_checker(database, filter_dict_up=None, filter_dict_down=None):
        _CheckInput._check_database_input(database)
        _CheckInput._check_dict(filter_dict_up)
        _CheckInput._check_dict(filter_dict_down)
        return func(database, filter_dict_up, filter_dict_down)
    return wrapper_checker