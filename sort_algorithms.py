import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import generate_list, check_order

debug = False
# count = None
count = 500

if debug:
    unique_random_list = generate_list(count=5, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(count=5, uniqued_list=False)
else:
    unique_random_list = generate_list(count=count, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(count=count, uniqued_list=False)

known_solution_unique_random_list = []
known_solution_duplicate_allowed_random_list = []


def print_sort_progress(lowest_number: int, step_count: int):
    if debug:
        print(f"Lowest number in this round = {lowest_number}. Step_count = {step_count}")


def print_sort_results(method_name: str, time_taken_to_sort: float, step_count: int, sort_state: bool,
                       matches_known_solution: bool = None):
    result_f_string = f"Sort {method_name} took {time_taken_to_sort} seconds to order in {step_count} steps. Check: Sort status = {sort_state}."

    if matches_known_solution is not None:
        print(f"{result_f_string} Accurate (against known solution: {matches_known_solution})")
    else:
        print(result_f_string)


# Method 1: Selection sort. The method that is easiest. I used it to sort the cards.
# Settings: only unique numbers

method_name = "Selection sort 1.0"
random_list = copy.deepcopy(unique_random_list)
step_count = 0
start_time = datetime.now()

ordered_list = []

cache_random_list = copy.deepcopy(random_list)

while len(ordered_list) != len(random_list):
    step_count += 1
    lowest_number = cache_random_list[0]
    for i in cache_random_list:
        step_count += 1
        if i < lowest_number:
            step_count += 1
            lowest_number = i
    print_sort_progress(lowest_number, step_count)

    ordered_list.append(lowest_number)
    cache_random_list.remove(lowest_number)

time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
sort_state = check_order(ordered_list)["random_bool"] is False
known_solution_unique_random_list = copy.deepcopy(ordered_list)
print_sort_results(method_name, time_taken_to_sort, step_count, sort_state)

# Method 1.1: Selection sort.
# Settings: duplicate numbers allowed

method_name = "Selection sort 1.1"
random_list = copy.deepcopy(duplicate_allowed_random_list)
step_count = 0
start_time = datetime.now()

ordered_list = []

cache_random_list = copy.deepcopy(random_list)

while len(ordered_list) != len(random_list):
    step_count += 1
    lowest_number = cache_random_list[0]
    for i in cache_random_list:
        step_count += 1
        if i < lowest_number:
            step_count += 1
            lowest_number = i
    # print_sort_progress(lowest_number, step_count)

    lowest_number_list = []
    for i in cache_random_list:
        step_count += 1
        if i == lowest_number:
            step_count += 1
            lowest_number_list.append(i)

    ordered_list.extend(lowest_number_list)

    for i in lowest_number_list:
        step_count += 1
        cache_random_list.remove(i)

time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
sort_state = check_order(ordered_list)["random_bool"] is False
known_solution_duplicate_allowed_random_list = copy.deepcopy(ordered_list)
print_sort_results(method_name, time_taken_to_sort, step_count, sort_state)

# Method 2: Bubble sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Bubble_sort
# Settings: duplicate/unique agnostic (I think)

method_name = "Bubble sort"
random_list = copy.deepcopy(unique_random_list)
step_count = 0
start_time = datetime.now()

ordered_list = copy.deepcopy(random_list)

cache_random_list = copy.deepcopy(random_list)
found_pairs_to_swap = True

while check_order(ordered_list)["random_bool"]:
    step_count += 1
    cache_random_list = copy.deepcopy(ordered_list)
    for num_index, num in enumerate(cache_random_list[:-1]):
        step_count += 1
        if num > ordered_list[num_index + 1]:
            step_count += 1
            ordered_list[num_index] = copy.deepcopy(ordered_list[num_index + 1])
            ordered_list[num_index + 1] = num
            print_sort_progress(ordered_list[num_index + 1], step_count)
            break

time_taken_to_sort = round((datetime.now() - start_time).total_seconds(), 4)
sort_state = check_order(ordered_list)["random_bool"] is False
matches_known_solution = (ordered_list == known_solution_unique_random_list)
print_sort_results(method_name, time_taken_to_sort, step_count, sort_state, matches_known_solution)

# TODO: Merge Sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Merge_sort
# TODO: Quick Sort https://en.wikipedia.org/wiki/Quicksort
# TODO: Heap Sort https://en.wikipedia.org/wiki/Heapsort
