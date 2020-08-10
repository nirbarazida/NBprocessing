from NBprocessing import NBcategorical
import unittest
import pandas as pd


class TestCategorical(unittest.TestCase):

    # will REPLACE the methods (setUp tearDown) if will want to set up the test variable only once and not for etch test
    # relevant when working with big DB / long process to acquire the self.variables

    # @classmethod
    # def setUpClass(cls):
    #     print('setupClass\n')
    #     self.database = pd.read_csv('listings.csv')[FEATURE_LIST + TARGET_LIST]
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('teardownClass')

    # create a class variable that is now a class test variable.
    # this way can use the same variable and change it if necessary at one place
    def setUp(self):
        print('setUp')
        self.database = pd.read_csv('dataset_cars.csv')

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_remove_categories(self):
        print('remove_categories\n')
        column_name = 'fuel'
        categories_to_drop = ['CNG', 'LPG', 'Electric']

        with self.assertRaises(ValueError):
            NBcategorical.remove_categories(['nir'], column_name, categories_to_drop)
            NBcategorical.remove_categories(['nir'], ['fuel'], categories_to_drop)
            NBcategorical.remove_categories(['nir'], column_name, ['nir'])

        with self.assertRaises(NameError):
            NBcategorical.remove_categories(self.database, 'nir', categories_to_drop)

    def test_fill_na_by_ratio(self):
        print('fill_na_by_ratio\n')

        with self.assertRaises(NameError):
            NBcategorical.fill_na_by_ratio(self.database, 'nir')
        with self.assertRaises(ValueError):
            NBcategorical.fill_na_by_ratio(['nir'], 'fuel')

    def test_combine_categories(self):
        print('combine_categories\n')

        column_name = 'fuel'
        category_name = 'other'
        threshold = 0.01

        with self.assertRaises(NameError):
            NBcategorical.combine_categories(self.database, 'nir')

        with self.assertRaises(ValueError):
            NBcategorical.combine_categories(['nir'], column_name)
            NBcategorical.combine_categories(self.database, column_name, category_name, 1.1)
            NBcategorical.combine_categories(self.database, column_name, category_name, -0.001)
            NBcategorical.combine_categories(self.database, column_name, [category_name], threshold)

        NBcategorical.combine_categories(self.database, column_name, category_name, 0.2)
        len(self.database[column_name].value_counts())
        self.assertEqual(len(self.database[column_name].value_counts()), 3)

    # def categories_not_in_common(train, test, column_name)
    def test_categories_not_in_common(self):
        print('categories_not_in_common - to complete\n')


if __name__ == '__main__':
    unittest.main()
