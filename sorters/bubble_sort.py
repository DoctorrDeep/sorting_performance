import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_progress, print_sort_results


# Method 2: Bubble sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Bubble_sort
# Settings: duplicate/unique agnostic (I think)


def bubble_sort(random_list: list, known_solution_unique_random_list: list, debug: bool, help_text: str = ""):
    method_name = "Bubble sort"
    step_count = 0
    start_time = datetime.now()

    ordered_list = copy.deepcopy(random_list)

    while check_order(ordered_list)["random_bool"]:
        step_count += 1
        cache_random_list = copy.deepcopy(ordered_list)
        for num_index, num in enumerate(cache_random_list[:-1]):
            step_count += 1
            if num > ordered_list[num_index + 1]:
                step_count += 1
                ordered_list[num_index] = copy.deepcopy(ordered_list[num_index + 1])
                ordered_list[num_index + 1] = num
                print_sort_progress(ordered_list[num_index + 1], step_count, debug=debug)
                break

    time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
    sort_state = check_order(ordered_list)["random_bool"] is False
    matches_known_solution = (ordered_list == known_solution_unique_random_list)
    print_sort_results(method_name=method_name,
                       time_taken_to_sort=time_taken_to_sort,
                       step_count=step_count,
                       sort_state=sort_state,
                       matches_known_solution=matches_known_solution,
                       help_text=help_text
                       )
