"""
Generic functions to plot pandas data frame.

This library include the functions:
    1.plot_missing_value_heatmap(database):
        plots a heat-map with all columns filled with green color.
        The missing values indexes will be shown by a line in a gray color in their position.

    2.plot_corr_heat_map(database):
        plot a correlation heat map between the columns - positive and negative.
        will include correlation score rounded to .2%f.
        The color of the box will include how strong is the correlation between the columns.
        The color bar will be plot next to the heat map.

    3. count_plot(database, column_list=None):
        plot a count plot for all columns in the column_list.
        if a column list wasn't given will plot all non-numeric columns in the given database.

    4. distribution_plot(database, column_list=None):
        plot a distribution plot for all columns in the column_list.
        if a column list wasn't given will plot all numeric columns in the given database.
        Please note that in this case the method will also plot categorical columns that are numeric.


Create by: Nir Barazida
Good luck!

"""


from ._input_check_plot import _plot_missing_value_and_corr_heatmap_checker, _count_and_distribution_plot_checker

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


@_plot_missing_value_and_corr_heatmap_checker
def plot_missing_value_heatmap(database):
    """
    plots a heat-map with all columns filled with green color.
    The missing values indexes will be shown by a line in a gray color in their position.

    Parameters
    ----------
    :param database: pandas Data Frame
    data set to fill missing values in.

    Returns
    -------
    None
    Plots a heat-map

    Raises
    ------
    ValueError : If input value not as mentioned above.

    Exemples
    -------
    Will be added in version 0.2

    """

    sns.set(font_scale=1.2)
    plt.subplots(figsize=(12, 5))

    ax = sns.heatmap(database.isnull(), yticklabels=False, cbar=False, cmap='Accent')
    for i in range(database.isnull().shape[1] + 1):
        ax.axvline(i, color='white', lw=2)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, horizontalalignment='right')
    plt.title('Nulls Heatmap')
    plt.show()

@_plot_missing_value_and_corr_heatmap_checker
def plot_corr_heat_map(database):
    """
    plot a correlation heat map between the columns - positive and negative.
    will include correlation score rounded to .2%f.
    The color of the box will include how strong is the correlation between the columns.
    The color bar will be plot next to the heat map.


    Parameters
    ----------
    :param database: pandas Data Frame
    data set to fill missing values in.

    Returns
    -------
    None
    plot a correlation heat map between the columns - positive and negative.
    will include correlation score rounded to ".2f".
    The color of the box will include how strong is the correlation between the columns.
    The color bar will be plot next to the heat map.

    Raises
    ------
    ValueError : If input value not as mentioned above.

    Exemples
    -------
    Will be added in version 0.2
    """

    sns.set(font_scale=1)
    plt.subplots(figsize=(20, 6))

    mask = np.tril(np.ones_like(database.corr(), dtype=np.bool))
    ax = sns.heatmap(database.corr(), annot=True, fmt=".2f", mask=mask, square=True,
                     linecolor='white', linewidths=1)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, horizontalalignment='right')
    plt.title('Features correlation plot by heat map', size=15)


@_count_and_distribution_plot_checker
def count_plot(database, column_list=None):
    """
    plot a count plot for all columns in the column_list.
    if a column list wasn't given will plot all non-numeric columns in the given database.

    Parameters
    ----------
    :param database: pandas Data Frame
    data set to fill missing values in.

    :param column_list: list or tuple
    a column list from the database that the user wish to plot.
    if a column list is not given - the method will plot all non-numeric columns in the given database.
    all columns must be categorical columns.

    Returns
    -------
    None
    plot a count plot

    Raises
    ------
    ValueError : If input value not as mentioned above.

    Exemples
    -------
    Will be added in version 0.2

    """

    if not column_list:
        column_list = [col for col in database if col not in list(database._get_numeric_data().columns)]

    sns.set(font_scale=1)
    for col in column_list:
        sns.set_style("whitegrid")
        plt.subplots(figsize=(8, 4))
        g = sns.countplot(database[col], palette="Set2")
        g.set_title(label=col + " distribution", fontsize=20)

        plt.tight_layout()
        plt.show()

@_count_and_distribution_plot_checker
def distribution_plot(database, column_list=None):
    """
    plot a distribution plot for all columns in the column_list.
    if a column list wasn't given will plot all numeric columns in the given database.
    Please note that in this case the method will also plot categorical columns that are numeric.

    Parameters
    ----------
    :param database: pandas Data Frame
    data set to fill missing values in.

    :param column_list: list or tuple
    a column list from the database that the user wish to plot.
    if a column list wasn't given will plot all numeric columns in the given database.
    Please note that in this case the method will also plot categorical columns that are numeric.

    Returns
    -------
    None
    plot a count plot

    Raises
    ------
    ValueError : If input value not as mentioned above.

    Exemples
    -------
    Will be added in version 0.2
    """

    if not column_list:
        column_list = list(database._get_numeric_data().columns)

    print("continuous features distribution")

    sns.set(font_scale=1.4)
    for col in column_list:
        sns.set_style("whitegrid")
        plt.subplots(figsize=(9, 6))
        g = sns.distplot(database[col], kde=False, color='blue')
        g.set_title(label=col + " distribution", fontsize=20)

        plt.tight_layout()
        plt.show()



