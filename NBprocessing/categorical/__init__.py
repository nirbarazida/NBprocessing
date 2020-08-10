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

