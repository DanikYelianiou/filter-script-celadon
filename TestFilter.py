import unittest
import filter


class TestFilter(unittest.TestCase):

    def test_first_text(self): # 1
        self.assertEqual(filter.text_x(
            ['sad', 'mad', 'bad'],
            "I'm love sad because i'm bad"),
            "I'm love *** because i'm ***"
        )

    def test_second_text(self): # 2
        self.assertEqual(filter.text_x(
            ['sad', 'mad', 'bad'],
            "sad, mad, bad"),
            "***, ***, ***"
        )

    def test_second_text(self): # 3
        self.assertEqual(filter.text_x(
            ['sad,', 'mad,', 'bad,'],
            "sad, mad, bad,"),
            "**** **** ****"
        )

    def test_second_text(self): # 4
        self.assertEqual(filter.text_x(
            ['saded', 'mad', 'bad'],
            "saded and, death"),
            "***** and, death"
        )

    def test_second_text(self): # 5
        self.assertEqual(filter.text_x(
            ['sad', 'mad', 'bad!'],
            "sad. and mad. want bad!."),
            "***. and ***. want ****."
        )

if __name__ == "__main__":
    unittest.main()
