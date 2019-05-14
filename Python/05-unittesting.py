import unittest


class Testlists(unittest.TestCase):
    def test_index_builtin_function(self):
        # Arrange
        self.test_list = [1, 2, 3]

        # Act
        actual = self.test_list.index(1)
        expected = 0

        # Assert
        self.assertEqual(expected, actual)

    def test_append_builtin_function(self):
        # Arrange
        self.fruit = ['banana', 'apple', 'orange', 'watermelon']
        self.new_fruit = 'pear'

        # Act
        self.fruit.append(self.new_fruit)
        actual = self.fruit
        expected = ['banana', 'apple', 'orange', 'watermelon', 'pear']

        # Assert
        self.assertEqual(expected, actual)

    def test_len_builtin_function(self):
        # Arrange
        self.animals = ['dog', 'cat', 'fish']

        # Act
        actual = len(self.animals)
        expected = 3

        # Assert
        self.assertEqual(expected, actual)
