import unittest
import os

# I want to test whether the clean_text function is working correclty or not.
class TestMain(unittest.TestCase):
    def test_clean_text(self):
        from main.routes import clean_text
        text = "Hello, I am Rahul"
        expected = ['hello', 'rahul']
        result = clean_text(text)
        self.assertEqual(result , expected)
    
    def test_spam_or_not(self):
        from main.routes import spam_or_not
        text = "Hello, I am Rahul"
        expected = 'ham'
        result = spam_or_not(text)
        self.assertEqual(result , expected)
    
    def test_get_env(self):
        from main.routes import get_mode
        self.assertEqual(os.environ.get("MODE"),get_mode())

if __name__ == "__main__":
    unittest.main()

