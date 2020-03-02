import random


def generate_list(
    min_number: int = 1, max_number: int = 1000000, count: int = 1000, uniqued_list: bool = True,
) -> list:
    """
    This function will create a list of random numbers.
    It accepts min number in list, max number in list and count of numbers in list.
    Note; if `count` is None then it defaults to 1000

    :param min_number: mininum value of single number in list of random numbers
    :param max_number: maximum value of single number in list of random numbers
    :param count: number of random numbers expected
    :param uniqued_list: boolean of whether or not the returned random list is allowed to have duplicate values or not
    :return: list of size `count` of random numbers in random order
    """

    if count is None:
        count = 1000

    random_numbers_list = []

    while not len(random_numbers_list) >= count:

        temp = random.randint(min_number, max_number)

        if uniqued_list:
            if temp in random_numbers_list:
                continue

        random_numbers_list.append(temp)

    if not check_order(random_numbers_list)["random_bool"]:
        # If the generated list is somehow ordered then run the generator
        # until randomness found. Useful in test scenarios.
        generate_list(min_number, max_number, count, uniqued_list)

    return random_numbers_list


def check_order(list_of_numbers: list) -> dict:
    """
    Take a list of numbers and returns whether the list
    was ordered in ascending manner or not

    :param list_of_numbers:
    :return: dictionary with 1 key `random_bool`.
        - Value True means the list is random.
        - Value False means the list is ordered in an ascending manner.

    Doctest

    >>> check_order([1,2,3])
    {'random_bool': False}

    >>> check_order([2,2,3])
    {'random_bool': False}

    >>> check_order([3,2,3])
    {'random_bool': True}

    """

    state_of_randomness = {"random_bool": False}

    for index, num in enumerate(list_of_numbers[:-1]):
        if num > list_of_numbers[index + 1]:
            state_of_randomness["random_bool"] = True

    return state_of_randomness
