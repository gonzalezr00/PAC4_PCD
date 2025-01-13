# pylint: skip-file
import unittest
import os


# Import the functions to test
from ex1_module import ex1
from ex2_module import ex2
from ex3_module import ex3
from ex4_module import ex4
from ex5_module import ex5


# Create a class to test the functions
class PublicTests1(unittest.TestCase):

    def test_ex1(self):
        # Test the ex1 function
        orbea_df = ex1()
        self.assertEqual(orbea_df.shape, (3975, 4))
        self.assertNotEqual(orbea_df.shape, (100, 4))
        self.assertEqual(list(orbea_df.columns), ['dorsal', 'biker', 'club', 'time'])
        self.assertEqual(len(orbea_df['biker'].unique()), 3865)


    def test_ex2(self):
        # Test the ex2 function
        orbea_df = ex1()
        orbea_df = ex2(orbea_df)
        self.assertNotEqual(orbea_df.shape, (3975, 4))
        self.assertEqual(orbea_df.shape, (3887, 4))
        self.assertNotEqual(len(orbea_df['biker'].unique()), 3865)
        self.assertEqual(len(orbea_df['biker'].unique()), 3780)


    def test_ex3(self):
        # Test the ex3 function
        orbea_df = ex1()
        orbea_df = ex2(orbea_df)
        orbea_df = ex3(orbea_df)
        self.assertEqual(len(orbea_df['biker'].unique()), 3780)
        self.assertTrue(os.path.exists("./img/rides_histogram.png"))
        self.assertTrue(os.path.exists("./img/rides_histogram.html"))
        self.assertTrue(orbea_df['time_groupped'].str.split(':', expand=True)[1].astype(int).isin([0, 20, 40]).all())


    
    def test_ex4(self):
        # Test the ex4 function
        orbea_df = ex1()
        orbea_df = ex2(orbea_df)
        orbea_df = ex3(orbea_df)
        orbea_df = ex4(orbea_df)
        two_char_strings = [' TT',  'S.C ', 'CLUB ', 'AGRUPACIO CICLISTA ']
        for string in two_char_strings:
            self.assertFalse(orbea_df['club'].str.contains(string).any())

    def test_ex5(self):
        # Test the ex5 function
        orbea_df = ex1()
        orbea_df = ex2(orbea_df)
        orbea_df = ex3(orbea_df)
        orbea_df = ex4(orbea_df)
        orbea_df = ex5(orbea_df)
        self.assertEqual(len(orbea_df[orbea_df['club'] == 'UCSC']), 19)
        self.assertEqual(len(orbea_df[orbea_df['club'] == 'UNIÓ CICLISTA SANT CUGAT']), 2)
        self.assertEqual(orbea_df[orbea_df['club'] == 'UCSC']['time'].min(), '04:48:42')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PublicTests1)
    unittest.TextTestRunner(verbosity=2).run(suite)
