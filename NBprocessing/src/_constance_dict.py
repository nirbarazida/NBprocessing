data={}

data['CHECK_INPUT'] = {
    'CHECK_DATABASE_INPUT': "Database input is not valid - Please enter pandas dataframe",
    'CHECK_COLUMN_NAME': "Column name input is not valid - Please enter a string",
    'CHECK_COLUMN_IN_DATABASE': "Column name not in database - please enter column that exists in database",
    'CHECK_LIST_TUPLE_NONE': "Categories to drop must be a list or a tuple or None for all",
    'CHECK_THRESHOLD': "threshold input is not valid - Please enter a float in range 0-1",
    'CHECK_TYPE_DATE_TIME': r"The column {} is not date-time type.",
    'CHECK_BOUNDARIES': "boundary input is not valid - Please enter a float in range 0-1",
    'CHECK_DICT': "filter dictionary input is not valid - Please enter a dictionary",
    'CHECK_NUM_CATEGORIES': "num_categories input is not valid - Please enter a int higher than 1",
    'CHECK_TITLE': "Title input is not valid"
}
data["CATEGORICAL"] = {

    'GENERAL_FUNCTIONS_CATEGORICAL': {"RED": "red", "BLACK": "black", "OUTPUT": "color: {}"},

    "NBCATEGORICAL_CLASS": {
        "REMOVE_CATEGORIES": {"USER_INPUT": 'Using remove_categories will result in deletion of {}\n'
                                            'Which is {} % of the database.\nDo you wish to continue? [y/n]',
                              "DATABASE_SHAPE": "the new database shape is{}"
                              },

        "CATEGORIES_NOT_IN_COMMON": {"FIRST": "values existing only in the first data-set {}",
                                     "SECOND": "values existing only in the second data-set {}"
                                     }
        }
}

data["CONTINUOUS"] = {
    "NBCONTINUOUS_CLASS": {"REMOVE_OUTLIERS_BY_BOUNDARIES": {"DROP_ROW": "Do you wish to drop {} rows"
                                                                         " ({}% of the database)? [y/n]",
                                                             "TYPE_ERROR": "Error - the column value type must be numeric"
                                                             },
                           "GET_NUM_OUTLIERS_BY_VALUE": {"OUTLIERS_ABOVE": "\nOutliers above:",
                                                         "SUM_OUTLIERS_ABOVE": "{}: {}",
                                                         "OUTLIERS_UNDER": "\nOutliers under:",
                                                         "SUM_OUTLIERS_UNDER": "{}: {}",
                                                         "SUM_OUTLIERS_TOT": "\nBy removing all {} rows we will lose"
                                                                             " {} % of the data",
                                                         "KEY_ERROR": "Error one or more of the column names is not in "
                                                                      "the data base. "
                                                         },
                           "REMOVE_OUTLIERS_BY_VALUE": {"SHAPE_BEFORE": "\nShape before removing outliers: {}",
                                                        "SHAPE_AFTER": "\nshape after removing outliers: {}",
                                                        "DATA_LOST": "\nDroped {} rows that are {} % of the database"
                                                        },
                           }
}
data["PLOT"] = {
               "NBPLOT_CLASS": {"NULL_HEAT_MAP_TITLE": "Nulls Heatmap",
                                "FEATURE_CORR": "Features correlation plot by heat map"
                                }

               }
data["GENERAL"] = {
                    "SPLIT_AND_CHECK": "X_train shape: {}, y_train shape:"
                                       " {}, X_test shape: {}"
                                       ", y_test shape: {}"
                  }