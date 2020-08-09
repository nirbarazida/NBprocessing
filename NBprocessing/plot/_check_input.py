import pandas as pd
from pandas.api.types import is_datetime64_any_dtype as is_datetime


class _CheckInput(object):

    @staticmethod
    def _check_database_input(database):
        if type(database) != pd.core.frame.DataFrame:
            raise ValueError("Database input is not valid - Please enter pandas dataframe")

    @staticmethod
    def _check_column_name(column_name):
        if type(column_name) != str and type(column_name) != int and type(column_name) != float:
            raise ValueError("column_name input is not valid - Please enter a string")

    @staticmethod
    def _check_categories_to_drop(categories_to_drop):
        if type(categories_to_drop) != list and type(categories_to_drop) != tuple:
            raise ValueError("categories_to_drop must be a list or a tuple - please enter as list / tuple")

    @staticmethod
    def _check_column_in_database(column_name, database):
        if column_name not in database.columns:
            raise NameError("column_name not in database - please enter column that exists in database")

    @staticmethod
    def _check_threshold(threshold):
        if (type(threshold) != float and type(threshold) != int) or threshold > 1 or threshold < 0:
            raise ValueError("threshold input is not valid - Please enter a float in range 0-1")

    @staticmethod
    def _check_type_date_time(database, column_name):
        if not is_datetime(database[column_name]):
            raise ValueError(f"The column {column_name} is not date-time type.")  # todo: MUST check this!!!

    @staticmethod
    def _check_boundaries(boundary):
        if (type(boundary) != float and type(boundary) != int) or boundary > 1 or boundary < 0:
            raise ValueError("boundary input is not valid - Please enter a float in range 0-1")

    @staticmethod
    def _check_dict(dictionary):
        if type(dictionary) != dict and dictionary is not None:
            raise ValueError("filter dictionary input is not valid - Please enter a dictionary")

    @staticmethod
    def _check_num_categories(num_categories):
        if type(num_categories) != int or num_categories < 0:
            raise ValueError("num_categories input is not valid - Please enter a int higher than 1")
