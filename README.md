# NBprocessing 

Pre-processing database using pre-written functions

**Written by**: Nir Barazida


How many times have you received raw database and conduct the same action to pre-process it?
 - Check for missing values and fill them if necessary.
 - Combine low appearance categories under one umbrella category. 
 - Plot your data distribution and check for outliers.
 - Drop outliers by different methods.
 
 If you said yes to all of the above you have reached to right place!
 
The main purpose of the '**NBprocessing**' package is to make our Data Scientist life **easier**, or better yet - more efficient.
The '**NBprocessing**' package stores must of the generics functions that we all use on a daily basic, such remove outliers, fill missing values etc.


##install and usage

Run from your command line prompt:
 
`pip install NBprocessing`
 
 It will also install all the dependent packages such pandas, numpy, seaborn etc.

## General
###package libraries
- Categorical - contains functions that are relevant to categorical features:

    - `remove_categories(database, column_name, categories_to_drop)`
    - `fill_na_by_ratio(database, column_name)`
    - `combine_categories(database, column_name, category_name="other", threshold=0.01)`
    - `categories_not_in_common(train, test, column_name)`
    - `category_ratio(database, columns_to_check=None, num_categories=5)` 
    
- Continuous - contains functions that are relevant to continuous features:

    - `remove_outliers_by_boundaries(database, column_name, bot_qu, top_qu)` 
    - `fill_na_timedate(database, column_name)`
    - `get_num_outliers_by_value(database, filter_dict_up, filter_dict_down)`
    - `remove_outliers_by_value(database, filter_dict_up, filter_dict_down)`
    
- General - contains general functions:

    - `missing_values(database)`
    
- Plot - contains plots functions:

    - `plot_missing_value_heatmap(database)`
    - `plot_corr_heat_map(database)`
    - `count_plot(database, column_list=None)`
    - `distribution_plot(database, column_list=None)`


### import
- `from NBprocessing.categorical import NBcategorical`
- `from NBprocessing.continuous import NBcontinuous`
- `from NBprocessing.plot import NBplot`
- `from NBprocessing.general import NBgeneral`


## Usage

all Usage of the package functions are reviewed very specifically in this [jupyter Notebook() 

### Usage Example

- Categorical:
    - Fill missing values in a categorical feature by the ratio of the categories:\
    `fill_na_by_ratio(database, column_name)`
    
        Fill all missing values in the given column by the ratio of the categories in the column.\
        Because the ratio sum is not a perfect one - the extra missing values will be filled with the most common category in the column.
        
       - First, we would like to sum all missing values in every categorical feature.\
            **pic categorical 1** 
       
       - Second, Lets explore the ratio of evey category in the feature 'fuel' with and without missing values\
            **pic categorical 1** 
       
       - Last, we would like to fill the missing values and to keep the ratio of the features without them.\
       To do so we will use the `fill_na_by_ratio` function.\
             **pic categorical 3**
             
       As we can see from the above, all the missing values were filled and we manged to keep the ratio of the categories.
      
    - Combine low appearance categories under one category\
     `combine_categories(database, column_name, category_name="other", threshold=0.01)`
     
        Receives a threshold that is the minimum relative part of the category within the column.\
        All categories that are less than this threshold will be combined under the same category
        under the name 'category_name'.\
        The method will return a list with all the name of categories that were combined under 'category_name'.\
        With this list the user will be able to make the same action on the test set (assuming that the data
        was already splitted to train and test sets)

       - First, we will check the ratio of appearance per etch category in the feature.\
            **pic categorical 4**
            
       - Second, we would like to combine all the low appearance categories under one category and save the redacted features to a list.\
            **pic categorical 5**
            
       - Last, we will make the same changes on our test data-set using the list that we've created:\
            **pic categorical 6**
                
- Continuous:
    - Remove outliers by top and bottom percentage of data boundaries 
     `remove_outliers_by_boundaries(database, column_name, bot_qu, top_qu)`
    
    The theory behind it:\
        _the number of outliers  will follow a binomial distribution with parameter p, which can generally be
        well-approximated by the Poisson distribution with λ = pn. Thus if one takes a normal distribution with
        cutoff 3 standard deviations from the mean, p is approximately 0.3%, and thus for 1000 trials one can
        approximate the number of samples whose deviation exceeds 3 sigmas by a Poisson distribution with λ = 3.
        3 times of standard deviation as my main data and out of this range would be the outlier._
        
     ![Image of Yaktocat](https://i.stack.imgur.com/AxYue.png)

    Thus, in a normal distribution the top and bottom boundaries should contain 99.7% of the data.
    However, not all data has Normal distribution thus the user is able to change the top and bottom boundaries

    Before removing the indexes will print a message to the user with the number of indexes that
    will be remove and the percent of the database that will be lost.
    the user will input 'y'(yes) to pressed and 'n'(no) to cancel the action.
    If the user choose 'yes' the method will continue to drop the indexes and will
    plot the new database shape.
    
    Let's see a live example:
        **Continuous 1**
        
- Plot:
    - Plot heat map of missing values
     `plot_missing_value_heatmap(database)`
     
        Plots a heat-map with all columns filled with green color.\
        The missing values indexes will be shown by a line in a gray color in their position.
        
        **plot_1**
        
# Contact
- linkedin - [NirBarazida()

Please let me know if you have any questions.

Good luck,
Nir Barazida