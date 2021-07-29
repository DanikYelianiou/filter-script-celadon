import unittest
import filter


class TestFilter(unittest.TestCase):

    def test_first_text(self):
        self.assertEqual(filter.text_x(
            ['sad', 'mad', 'bad'],
            "I'm love sad because i'm bad"),
            "I'm love *** because i'm ***"
        )

    def test_second_text(self):
        self.assertEqual(filter.text_x(
            ['sad', 'mad', 'bad'],
            "sad, mad, bad"),
            "***, ***, ***"
        )

if __name__ == "__main__":
    unittest.main()
