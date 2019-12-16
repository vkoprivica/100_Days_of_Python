from regex import (extract_course_times)

def test_extract_course_times():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected




if __name__ == "__main__":
    test_extract_course_times()