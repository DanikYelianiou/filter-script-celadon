import unittest
import filter


class TestFilter(unittest.TestCase):

    def test_first_text(self): # 1
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "I'm love sad because i'm bad"),
            "I'm love *** because i'm ***"
        )

    def test_second_text(self): # 2
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "sad, mad, bad"),
            "***, ***, ***"
        )

    def test_second_text(self): # 3
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "sad, mad, bad,"),
            "**** **** ****"
        )

    def test_second_text(self): # 4
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "saded and, death"),
            "***** and, death"
        )

    def test_second_text(self): # 5
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "sad. and mad. want bad!."),
            "***. and ***. want ****."
        )

    def test_second_text(self): # 6
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "Hello Bad"),
            "Hello ***"
        )

    def test_second_text(self): # 7
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "Hello, Bad"),
            "Hello, ***"
        )

    def test_second_text(self): # 8
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "Hello Bad!"),
            "Hello ***!"
        )

    def test_second_text(self): # 9
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "Hello Bad?"),
            "Hello ***?"
        )

    def test_second_text(self): # 10 
        self.assertEqual(filter.text_x(
            filter.BAD_WORDS,
            "HELLO BAD"),
            "HELLO ***"
        )

if __name__ == "__main__":
    unittest.main()
