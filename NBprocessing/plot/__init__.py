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