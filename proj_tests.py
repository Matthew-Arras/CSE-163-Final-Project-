import data_prep 
import math
import pandas as pd


def parse(file_name):
    """
    Reads the CSV with the given file_name and returns it as a list of
    dictionaries. The list will have a dictionary for each row, and each
    dictionary will have a key for each column.
    """
    df = pd.read_csv(file_name)
    return df.to_dict('records')


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=0.001)
        else:
            return expected == received
    except Exception as e:
        print(f'EXCEPTION: Raised when checking check_approx_equals {e}')
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    assert check_approx_equals(expected, received), \
        f'Failed: Expected {expected}, but received {received}'



def test_rstats(r_stats18, r_stats19):

    # Row count check
    assert_equals(30, len(r_stats18['Team']))
    assert_equals(30, len(r_stats19['Team']))

    # Column count check

    assert_equals(24, len(r_stats19.columns))
    assert_equals(24, len(r_stats19.columns))


def main():
    r_stats18 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    r_stats19 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')


    test_rstats(r_stats18, r_stats19)



if __name__ == '__main__':
    main()