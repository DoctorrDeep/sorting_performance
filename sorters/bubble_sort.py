import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_results


# Method 2: Bubble sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Bubble_sort
# Settings: duplicate/unique agnostic


def bubble_sort(
        random_list: list,
        known_solution_unique_random_list: list,
        debug: bool,
        help_text: str = "",
):
    """

    :param random_list:
    :param known_solution_unique_random_list:
    :param debug:
    :param help_text:
    :return:

    Doctest

    >>> bubble_sort([5,4,3,2,1],[1,2,3,4,5], debug=False)
    [1, 2, 3, 4, 5]

    >>> bubble_sort([3,3,2,1,2,3], [1,2,2,3,3,3], debug=False)
    [1, 2, 2, 3, 3, 3]

    """
    method_name = "Bubble sort"
    step_count = 0
    start_time = datetime.now()

    cache_random_list = copy.deepcopy(random_list)
    ordered_list = []
    count_cache_list = len(cache_random_list)

    while count_cache_list > 1:
        for num_index in range(count_cache_list - 1):
            current_num = cache_random_list[num_index]
            next_num = cache_random_list[num_index + 1]

            if current_num > next_num:
                cache_random_list[num_index] = next_num
                cache_random_list[num_index + 1] = current_num
                step_count += 1
            else:
                cache_random_list[num_index] = current_num
                cache_random_list[num_index + 1] = next_num
                step_count += 1

        ordered_list.insert(0, cache_random_list[-1])
        cache_random_list = copy.deepcopy(cache_random_list[:-1])
        count_cache_list = len(cache_random_list)

        if debug:
            print("\t\t\tgrowing ordered_list", ordered_list)

    ordered_list = cache_random_list + ordered_list
    if debug:
        print("\t\t\t\tordered_list", ordered_list)

    time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
    sort_state = check_order(ordered_list)["random_bool"] is False
    matches_known_solution = ordered_list == known_solution_unique_random_list
    print_sort_results(
        method_name=method_name,
        time_taken_to_sort=time_taken_to_sort,
        step_count=step_count,
        sort_state=sort_state,
        matches_known_solution=matches_known_solution,
        help_text=help_text,
    )

    return ordered_list
