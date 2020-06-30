# O(N)
import unittest


def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            # come across the critical
            compressed.append(string[i - 1] + str(counter))
            # need str() not like cpp
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)
    # not permit the a1b1c1, f
    # sort() also support key=lambda v: v[2]
    # key=str.lower
    ''' sorted(student_tuples, key=itemgetter(1,2))
from operator import itemgetter, attrgetter

'''


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
