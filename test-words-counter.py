import os
from words-counter import file_to_test

def test_file_to_test():
    test_filename="file.txt"
    result= file_to_test(test_filename)

    assert result== 8