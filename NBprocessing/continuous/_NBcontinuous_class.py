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

from NBprocessing.continuous._input_check_continuous import _fill_na_timedate_checker, \
    _remove_outliers_by_boundaries_checker, _remove_and_get_num_outliers_by_value_checker
from NBprocessing.src import constance_object


class NBcontinuous(object):

    @staticmethod
    @_fill_na_timedate_checker
    def fill_na_timedate(database, column_name):
        """
        General Information
        ----------
        Fill all the missing values in a time-date column with the mean time of the column.

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to fill missing values in.

        :param column_name: string
        The name of the column to preform the check.
        This column must be a time-date column

        Returns
        -------
        None.
        preform the action on the database inplace

        Raises
        ------
        ValueError : If input value not as mentioned above.
        ValueError : If the column type is not date-time

        Exemples
        -------
        Will be added in version 0.2
        """

        start_date = database[column_name].max()
        end_date = database[column_name].min()
        missing_date_value = start_date + (end_date - start_date) / 2

        database[column_name].fillna(missing_date_value, inplace=True)

    @staticmethod
    @_remove_outliers_by_boundaries_checker
    def remove_outliers_by_boundaries(database, column_name, bot_qu, top_qu):
        """
        Remove outliers values from column by top and bottom boundaries.

        The theory behind it:
        the number of outliers  will follow a binomial distribution with parameter p, which can generally be
        well-approximated by the Poisson distribution with λ = pn. Thus if one takes a normal distribution with
        cutoff 3 standard deviations from the mean, p is approximately 0.3%, and thus for 1000 trials one can
        approximate the number of samples whose deviation exceeds 3 sigmas by a Poisson distribution with λ = 3.
        3 times of standard deviation as my main data and out of this range would be the outlier.

        Thus, in a normal distribution the top and bottom boundaries should contain 99.7% of the data.
        However, not all data has Normal distribution thus the user is able to change the top and bottom boundaries

        Before removing the indexes will print a message to the user with the number of indexes that
        will be remove and the percent of the database that will be lost.
        the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
        If the user choose 'yes' the method will continue to drop the indexes and will
        plot the new database shape.

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to remove outliers from.

        :param column_name: string
        The name of the column to preform the check.
        the data type must be numeric

        :param bot_qu: float, 0 < bot_qu < 1
         bottom boundary to remove outliers from - percent in fraction

        :param top_qu: float, 0 < top_qu < 1
         upper boundary to remove outliers from - percent in fraction

        Returns
        -------
        None
        preform the action on the database inplace

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """
        try:
            removed_outliers = database[column_name].between(database[column_name].quantile(bot_qu),
                                                             database[column_name].quantile(top_qu))

            drop_row = input(constance_object.DROP_ROW.format(removed_outliers.value_counts()[0],
                                                              round(removed_outliers.value_counts()[0] * 100 / len(
                                                                  database), 2)))

            while drop_row != 'y' and drop_row != 'n':
                drop_row = input(constance_object.DROP_ROW.format(removed_outliers.value_counts()[0], round(
                    removed_outliers.value_counts()[0] * 100 / len(database), 2)))

            if drop_row == 'y':
                index_names = database[~removed_outliers].index
                database.drop(index_names, inplace=True)

        except TypeError:
            print(constance_object.TYPE_ERROR)

    @staticmethod
    @_remove_and_get_num_outliers_by_value_checker
    def get_num_outliers_by_value(database, filter_dict_up=None, filter_dict_down=None):
        """
        Prints how many indexes are above the values in the 'filter_dict_up' dictionary and how many indexes are below
        The values in the 'filter_dict_down' dictionary.
        The dictionary keys are the column names while the values are the top/ bottom boundaries.
        Will not conduct the action on all columns - only on columns in keys.

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to fill missing values in.

        :param filter_dict_up: dictionary - {column name : top boundary}
        dictionary with features as keys and values to filter from then and above as values.
        the column value type must be numeric.

        :param filter_dict_down: dictionary - {column name : bottom boundary}
        dictionary with features as keys and values to filter from then and down as values.
        the column value type must be numeric.

        Returns
        -------
        None
        print the number of indexes that will be lost using the top and bottom boundaries

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """
        try:
            sum_row = 0
            if filter_dict_up:
                print(constance_object.OUTLIERS_ABOVE)
                for col, outlier_value in filter_dict_up.items():
                    print(constance_object.SUM_OUTLIERS_ABOVE.format(col,(database[col] > outlier_value).sum()))
                    sum_row += (database[col] > outlier_value).sum()

            if filter_dict_down:
                print(constance_object.OUTLIERS_UNDER)
                for col, outlier_value in filter_dict_down.items():
                    print(constance_object.SUM_OUTLIERS_UNDER.format(col,(database[col] < outlier_value).sum()))
                    sum_row += (database[col] < outlier_value).sum()
            print(constance_object.SUM_OUTLIERS_TOT.format(sum_row,round((sum_row * 100) / len(database), 2)))

        except KeyError:
            print(constance_object.KEY_ERROR)
        except TypeError:
            print(constance_object.TYPE_ERROR)

    @staticmethod
    @_remove_and_get_num_outliers_by_value_checker
    def remove_outliers_by_value(database, filter_dict_up=None, filter_dict_down=None):
        """
        remove all indexes that are above the values in the 'filter_dict_up' dictionary and indexes that are below
        The values in the 'filter_dict_down' dictionary.
        The dictionary keys are the column names while the values are the top/ bottom boundaries.
        Will not conduct the action on all columns - only on columns in keys.

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to fill missing values in.

        :param filter_dict_up: dictionary - {column name : top boundary}
        dictionary with features as keys and values to filter from then and above as values.
        the column value type must be numeric.

        :param filter_dict_down: dictionary - {column name : bottom boundary}
        dictionary with features as keys and values to filter from then and down as values.
        the column value type must be numeric.

        Returns
        -------
        None
        remove indexes by top and bottom boundaries in the database inplace
        print the data shape before after conduction the action, and the percent of the data that was lost

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2

        """

        try:
            print(constance_object.SHAPE_BEFORE.format(database.shape))
            before = database.shape[0]

            # delete outliers that crates head tail
            if filter_dict_up:
                for col, outlier_value in filter_dict_up.items():
                    database.drop(database.loc[database[col] > outlier_value].index, inplace=True)

            # delete outliers that crates back tail
            if filter_dict_down:
                for col, outlier_value in filter_dict_down.items():
                    database.drop(database.loc[database[col] < outlier_value].index, inplace=True)

            print(constance_object.SHAPE_AFTER.format(database.shape))
            after = database.shape[0]
            print(constance_object.DATA_LOST.format(before - after,round((before - after) * 100 / before, 2)))

        except KeyError:
            print(constance_object.KEY_ERROR)
        except TypeError:
            print(constance_object.TYPE_ERROR)
