import os
from words-counter import file_to_test

def test_file_to_test():
    test_filename="file.txt"
    file_to_test(test_filename)

   assert file_to_test("file.txt") == 8