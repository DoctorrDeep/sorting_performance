import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_progress, print_sort_results


# Method 1: Selection sort. The method that is easiest. I used it to sort the cards. this was the quickest for me.
# Settings: only unique numbers


def selection_sort(random_list: list, debug: bool, help_text: str = "") -> list:
    method_name = "Selection sort 1.0"
    step_count = 0
    start_time = datetime.now()

    ordered_list = []

    cache_random_list = copy.deepcopy(random_list)

    while len(ordered_list) != len(random_list):
        lowest_number = cache_random_list[0]
        for i in cache_random_list:
            if i < lowest_number:
                step_count += 1
                lowest_number = i
            else:
                step_count += 1
        print_sort_progress(lowest_number, step_count, debug=debug)

        ordered_list.append(lowest_number)
        cache_random_list.remove(lowest_number)

    time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
    sort_state = check_order(ordered_list)["random_bool"] is False
    known_solution_unique_random_list = copy.deepcopy(ordered_list)
    print_sort_results(
        method_name=method_name,
        time_taken_to_sort=time_taken_to_sort,
        step_count=step_count,
        sort_state=sort_state,
        help_text=help_text,
    )

    return known_solution_unique_random_list
