import pandas as pd
from pandas.api.types import is_datetime64_any_dtype as is_datetime

from NBprocessing.src import constance_object

class _CheckInput(object):

    @staticmethod
    def _check_database_input(database):
        if type(database) != pd.core.frame.DataFrame:
            raise ValueError(constance_object.CHECK_DATABASE_INPUT)

    @staticmethod
    def _check_column_name(column_name):
        if type(column_name) != str and type(column_name) != int and type(column_name) != float:
            raise ValueError(constance_object.CHECK_COLUMN_NAME)

    @staticmethod
    def _check_column_in_database(column_name, database):
        if column_name not in database.columns:
            raise NameError(constance_object.CHECK_COLUMN_IN_DATABASE)

    @staticmethod
    def _check_list_tuple_None(user_input):
        if type(user_input) != list and type(user_input) != tuple and user_input is not None:
            raise ValueError(constance_object.CHECK_LIST_TUPLE_NONE)

    @staticmethod
    def _check_threshold(threshold):
        if (type(threshold) != float and type(threshold) != int) or threshold > 1 or threshold < 0:
            raise ValueError(constance_object.CHECK_THRESHOLD)

    @staticmethod
    def _check_type_date_time(database, column_name):
        if not is_datetime(database[column_name]):
            raise ValueError(constance_object.CHECK_TYPE_DATE_TIME.format(column_name))  # todo: MUST check this!!!

    @staticmethod
    def _check_boundaries(boundary):
        if (type(boundary) != float and type(boundary) != int) or boundary > 1 or boundary < 0:
            raise ValueError(constance_object.CHECK_BOUNDARIES)

    @staticmethod
    def _check_dict(dictionary):
        if type(dictionary) != dict and dictionary is not None:
            raise ValueError(constance_object.CHECK_DICT)

    @staticmethod
    def _check_num_categories(num_categories):
        if type(num_categories) != int or num_categories < 0:
            raise ValueError(constance_object.CHECK_NUM_CATEGORIES)

    @staticmethod
    def _check_title(title):
        if type(title) != str and type(title) != int and type(title) != float and title != None:
            raise ValueError(constance_object.CHECK_TITLE)

