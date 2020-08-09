"""
Generic functions to manipulate continuous features in pandas data frame.

This library include the functions:
    1. fill_na_timedate(database, column_name):
        Fill all the missing values in a time-date column with the mean time of the column.

    2. remove_outliers_by_boundaries(database, column_name, bot_qu, top_qu):
        Remove outliers values from column by top and bottom boundaries.
        Before removing the indexes will print a message to the user with the number of indexes that
        will be remove and the percent of the database that will be lost.
        the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
        If the user choose 'yes' the method will continue to drop the indexes and will
        plot the new database shape.

    3. get_num_outliers_by_value(database, filter_dict_up, filter_dict_down):
        Prints how many indexes are above the values in the 'filter_dict_up' dictionary and how many indexes are below
        The values in the 'filter_dict_down' dictionary.
        The dictionary keys are the column names while the values are the top/ bottom boundaries.
        Will not conduct the action on all columns - only on columns in keys.

    4. remove_outliers_by_value(database, filter_dict_up, filter_dict_down):
        remove all indexes that are above the values in the 'filter_dict_up' dictionary and indexes that are below
        The values in the 'filter_dict_down' dictionary.
        The dictionary keys are the column names while the values are the top/ bottom boundaries.
        Will not conduct the action on all columns - only on columns in keys.


Created by: Nir Barazida
Good luck!
"""