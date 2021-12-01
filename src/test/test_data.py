import unittest
import sys
  
# append the path of the
# parent directory
import os
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))

from src.data import Dataset
import pandas as pd
from pandas._testing import assert_frame_equal

def test_dataset():
    ''' Creating dataset for unit test
    return df'''
    data = { 'Area Code':[303,970,409,850,850,562],
    'Date':['10/1/2012 0:00',None,'10/1/2012 0:00','10/1/2012 0:00','10/1/2012 0:00','10/1/2012 0:00'],
    'Inventory' : [503,405,None,871,871,650],
    'Margin' : [71.00,71.15,64.50,56.00,56.00,110.90],
    'Market Size' : ['Major Market','Major Market','Major Market','Major Market','Major Market','Major Market'],
    'Market' : ['Central','Central','South','East','East','West']}

    df = pd.DataFrame(data)
    return df

file_name = 'test_dataset' 
df = test_dataset()       
class Test_get_name(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        self.assertEqual(file_name, self.output.get_name())

class Test_get_n_rows(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        self.assertEqual(6, self.output.get_n_rows())

class Test_get_n_cols(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        self.assertEqual(6, self.output.get_n_cols())

class Test_get_cols_list(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        col_list = ['Area Code','Date','Inventory','Margin','Market Size','Market']
        self.assertEqual(col_list, self.output.get_cols_list())

class Test_get_cols_dtype(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        cols_dtype_dict = {'Area Code':"int64",
        'Date':"object",
        'Inventory':"float64",
        'Margin':"float64",
        'Market Size':"object",
        'Market':"object"}

        output_dict =  self.output.get_cols_dtype()
        for col in output_dict:
            output_dict[col] = str(output_dict[col])

        self.assertEqual(cols_dtype_dict,output_dict)

class Test_get_n_duplicates(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        answer = 1
        self.assertEqual(answer, self.output.get_n_duplicates())

class Test_get_n_missing(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check if return expected output
        answer = 2 
        self.assertEqual(answer, self.output.get_n_missing())

class Test_get_head(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        n = 1
        answer = test_dataset().head(n)
        output = self.output.get_head(n)

        # check if output is similar in a specific cell
        self.assertEqual(answer.iloc[0,1], output.iloc[0,1])
        # check if output has expected length
        self.assertEqual(n,output.shape[0])
        # check if output and answers are two identical dataframes
        self.assertIsNone(assert_frame_equal(answer, output))

class Test_get_tail(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        n = 2
        answer = test_dataset().tail(n)
        self.assertEqual(answer.iloc[0,1], self.output.get_tail(n).iloc[0,1])
        # check if output has expected length
        self.assertEqual(n,self.output.get_tail(n).shape[0])
         # check if output and answers are two identical dataframes
        self.assertIsNone(assert_frame_equal(answer, self.output.get_tail(n)))

class Test_get_sample(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        n = 5
        answer = test_dataset().sample(n)
        # check if output has expected length
        self.assertEqual(n,self.output.get_sample(n).shape[0])

class Test_get_numeric_columns(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        answer = ['Area Code','Inventory','Margin']
        self.assertEqual(answer, self.output.get_numeric_columns())

class Test_get_text_columns(unittest.TestCase):
    def setUp(self):        
        self.output = Dataset(name = file_name , df = df)

    def test_function(self):
        # check data class update
        answer = ['Date','Market Size','Market']
        self.assertEqual(answer, self.output.get_text_columns())

if __name__ == '__main__':
    unittest.main()