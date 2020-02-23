from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_results


# Method 4: Native sort (as done by pythons sorted method)
# Settings: duplicate/unique agnostic


def native_sort(
    random_list: list,
    known_solution_unique_random_list: list,
    debug: bool,
    help_text: str = "",
    create_csv: bool = False,
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
    method_name = "Native sort"
    step_count = 1
    start_time = datetime.now()
    ordered_list = sorted(random_list)
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
        create_csv=create_csv,
    )

    return ordered_list
