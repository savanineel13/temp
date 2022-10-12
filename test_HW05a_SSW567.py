from unittest import mock
from HW05a_SSW567 import github_api_commit


@mock.patch('Desktop.HW05a_SSW567.github_api_commit')
class TestHW05a(unittest.TestCase):
    
    def test_check(self):
        assertTrue(github_api_commit())
        

        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    
