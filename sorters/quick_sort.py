import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_results


# Method 5: Quick sort https://en.wikipedia.org/wiki/Quicksort
# Settings: duplicate/unique agnostic


def find_pivot(random_list: list) -> dict:
    """

    :param random_list:
    :return:

    Doctest

    >>> find_pivot([7,3,5,12,18,9,2])
    {'step_count': 2, 'pivot': 7, 'pivot_index': 0}

    >>> find_pivot([7,3,5,18,9,2])
    {'step_count': 2, 'pivot': 7, 'pivot_index': 0}

    >>> find_pivot([2,3,18,7,9,5])
    {'step_count': 3, 'pivot': 7, 'pivot_index': 3}

    >>> find_pivot([14,8,15,15,18,14])
    {'step_count': 9, 'pivot': 15, 'pivot_index': 2}
    """

    indexes = {
        "begin": 0,
        "middle": int(len(random_list) / 2),
        "pre_middle": int(len(random_list) / 2) - 1,
        "end": len(random_list) - 1,
    }

    vals_to_chose_from = {
        "begin": random_list[indexes["begin"]],
        "middle": random_list[indexes["middle"]],
        "end": random_list[indexes["end"]],
    }
    if not len(random_list) % 2:
        vals_to_chose_from["pre_middle"] = random_list[indexes["pre_middle"]]

    temp = {
        "step_count": 1,
        "pivot": None,
        "pivot_index": None
    }

    step_count = 1
    for pivot_index_key, pivot in vals_to_chose_from.items():
        step_count += 1
        if pivot != min(list(vals_to_chose_from.values())) and pivot != max(list(vals_to_chose_from.values())):
            temp = {
                "step_count": step_count,
                "pivot": pivot,
                "pivot_index": indexes[pivot_index_key]
            }
            return temp

    if None in list(temp.values()):
        max_val = max(list(vals_to_chose_from.values()))
        for i in list(vals_to_chose_from.keys()):
            step_count += 1
            if vals_to_chose_from[i] == max_val:
                max_val_index = indexes[i]
        return {
            "step_count": step_count,
            "pivot": max_val,
            "pivot_index": max_val_index
        }


def sort_wrt_pivot(random_list: list, pivot: int, debug: bool = False) -> dict:
    """

    :param random_list:
    :param pivot:
    :return:

    Doctest

    >>> sort_wrt_pivot([7,3,5,12,18,9,2], 8)
    {'step_count': 23, 'less_random_list': [[7, 3, 5, 2], [8], [18, 9, 12]]}

    >>> sort_wrt_pivot([12,18,9,2,7,3,5], 8)
    {'step_count': 39, 'less_random_list': [[5, 3, 7, 2], [8], [9, 18, 12]]}

    >>> sort_wrt_pivot([4,4,2], 4)
    {'step_count': 9, 'less_random_list': [[2], [4], [4, 4]]}
    """
    step_count = 0
    cache_random_list = copy.deepcopy(random_list)

    while True:

        for val_ind, val in enumerate(cache_random_list):
            step_count += 1
            if val >= pivot:
                item_from_left = val
                item_from_left_ind = val_ind
                break

        for val_ind, val in enumerate(cache_random_list):
            step_count += 1
            if val <= pivot:
                item_from_right = val
                item_from_right_ind = val_ind

        if debug:
            print("item_from_left", item_from_left)
            print("item_from_left_ind", item_from_left_ind)
            print("item_from_right", item_from_right)
            print("item_from_right_ind", item_from_right_ind)

        if item_from_right_ind <= item_from_left_ind or item_from_right == item_from_left:
            return {
                "step_count": step_count,
                "less_random_list": [
                    cache_random_list[:item_from_left_ind],
                    [pivot],
                    cache_random_list[item_from_left_ind:]
                ],
            }

        else:
            cache_random_list[item_from_right_ind] = item_from_left
            cache_random_list[item_from_left_ind] = item_from_right


def recursive_sorter(list_of_random_lists: list, step_count: int = 0, debug: bool = False) -> dict:
    """

    :param list_of_random_lists:
    :param step_count:
    :return:

    Doctest

    >>> recursive_sorter([[7,3,5,12,18,9,2]])
    {'ordered_list_of_lists': [[2], [3], [5], [7], [9], [12], [18]], 'step_count': 41}
    """

    new_list_of_random_lists = []
    sorting_action_carried_out = False

    if debug and not step_count:
        print("Beginning of Quick sort.")
        print("Random list: ", list_of_random_lists)
    elif debug and step_count:
        print("\tRandom list: ", list_of_random_lists)

    for random_list in list_of_random_lists:

        if len(random_list) < 3:
            try:
                if random_list[0] > random_list[1]:
                    random_list.reverse()
            except IndexError:
                pass
            new_list_of_random_lists.append(random_list)
        else:
            sorting_action_carried_out = True
            pivot_data = find_pivot(random_list)
            step_count += pivot_data["step_count"]
            pivot = pivot_data["pivot"]
            pivot_index = pivot_data["pivot_index"]

            if debug:
                print("\t\t pivot", pivot)

            new_random_list = copy.deepcopy(random_list)
            del new_random_list[pivot_index]

            partition_data = sort_wrt_pivot(new_random_list, pivot, debug)
            step_count += partition_data["step_count"]
            new_list_of_random_lists.extend(partition_data["less_random_list"])

    current_result = {
        "ordered_list_of_lists": new_list_of_random_lists,
        "step_count": step_count
    }

    if sorting_action_carried_out:
        if debug:
            print("\tnew_list_of_random_lists", new_list_of_random_lists)
        return recursive_sorter(new_list_of_random_lists, step_count, debug)
    else:
        return current_result


def quick_sort(
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

    >>> quick_sort([5,4,3,2,1],[1,2,3,4,5], debug=False)
    [1, 2, 3, 4, 5]

    >>> quick_sort([3,3,2,1,2,3], [1,2,2,3,3,3], debug=False)
    [1, 2, 2, 3, 3, 3]

    """
    method_name = "Quick sort"
    step_count = 0
    start_time = datetime.now()
    ordered_list = []

    ordered_list_dict = recursive_sorter([random_list], debug=debug)
    step_count = ordered_list_dict["step_count"]
    ordered_list_of_lists = ordered_list_dict["ordered_list_of_lists"]
    for i in ordered_list_of_lists:
        ordered_list.extend(i)

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
