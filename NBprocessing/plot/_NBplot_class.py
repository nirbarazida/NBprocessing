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

from NBprocessing.plot._input_check_plot import _check_plot_input
from NBprocessing.src import constance_object

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import iplot


class NBplot(object):
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

        5. world_map_plot(database, locations_column, feature, title=None, color_bar_title=None):
            plot a world map with the distribution of a feature based on the different countries.
            every country wull be colored by the value of the feature.
            A color bar will be shown  next to the plot


    Create by: Nir Barazida
    Good luck!

    """

    @staticmethod
    @_check_plot_input._plot_missing_value_and_corr_heatmap_checker
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
        plt.title(constance_object.NULL_HEAT_MAP_TITLE)
        plt.show()

    @staticmethod
    @_check_plot_input._plot_missing_value_and_corr_heatmap_checker
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
        plt.title(constance_object.FEATURE_CORR, size=15)

    @staticmethod
    @_check_plot_input._count_and_distribution_plot_checker
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

    @staticmethod
    @_check_plot_input._count_and_distribution_plot_checker
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

        sns.set(font_scale=1.4)
        for col in column_list:
            sns.set_style("whitegrid")
            plt.subplots(figsize=(9, 6))
            g = sns.distplot(database[col], kde=False, color='blue')
            g.set_title(label=col + " distribution", fontsize=20)

            plt.tight_layout()
            plt.show()

    @staticmethod
    @_check_plot_input._world_map_plot_checker
    def world_map_plot(database, locations_column, feature, title=None, color_bar_title=None):
        """
        plot a world map with the distribution of a feature based on the different countries.
        every country wull be colored by the value of the feature.
        A color bar will be shown  next to the plot

        Parameters
        ----------
        :param database: pandas Data Frame
        data set to fill missing values in.

        :param locations_column: string
        The column name that contains the name of the countries

        :param feature: string
        The column name that it's values will be shown on the world map.

        :param title: string
        Plot title

        :param color_bar_title: string
        Color bar title

        Returns
        -------
        None
        World map plot

        Raises
        ------
        ValueError : If input value not as mentioned above.

        Exemples
        -------
        Will be added in version 0.2
        """

        data = dict(type='choropleth',
                    locations=database[locations_column],  # series / list with country names that we have data about
                    z=database[feature],  # information to plot
                    locationmode='country names',  # what will be shown when pointing on the map

                    colorscale=[[0, "rgb(5, 10, 172)"], [0.2, "rgb(40, 60, 190)"], [0.4, "rgb(70, 100, 245)"],
                                [0.6, "rgb(90, 120, 245)"], [0.8, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
                    # changing color of the country by total scale, blueish coler

                    autocolorscale=False,  # use auto color scale - if True do'nt need 8colorscale*
                    reversescale=False,  # revers scale with color scale and heat map
                    colorbar={'title': color_bar_title},  # Colorbar title
                    marker=dict(line=dict(color='rgb(180,180,180)', width=1))  # border lines
                    )

        layout = dict(title=title,  # Map title
                      geo=dict(scope='world',
                               # scope ("world" | "usa" | "europe" | "asia" | "africa" | "north america" | "south america" )
                               showframe=True,  # display with frame
                               showcoastlines=True,  # display with coast lines borders
                               )
                      )

        # Assign the variables to the go.Figure method
        iplot(go.Figure(data=[data], layout=layout))
