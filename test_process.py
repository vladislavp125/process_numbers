from main import process_numbers


def test_process_num():
    assert process_numbers([2, 3, 4, 5, 6, 7, -1, -300]) == 56
