import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from challenge3 import process_file
import numpy as np


class TestChallenge3(unittest.TestCase):
    def test_process_file(self):
        test_data1 = {'tax_file_no': ["", "", ""],
                      'name': ["Makima", "Reeze", "Juam"],
                      'is_married': ['Y', 'N', 5],
                      'annual_salary': [20, 30, 50],
                      'employment_status': ['PE', 'PE', 'CA']
                      }
        cleaned_data = {'name': ["Makima", "Reeze", "Juam"],
                        'is_married': ["Y", "N", np.nan],
                        'annual_salary': [20, 30, 50],
                        'employment_status': ['PE', 'PE', 'CA']
                        }

        test_df = pd.DataFrame.from_dict(test_data1)
        cleaned_df = pd.DataFrame.from_dict(cleaned_data)
        processed_df = process_file(test_df)

        assert_frame_equal(cleaned_df, processed_df) # We compare 2 dataframes using pandas testing


if __name__ == '__main__':
    unittest.main()
