import copy
from datetime import datetime

from app_scripts.create_check_random_number_list import check_order
from app_scripts.print_scripts import print_sort_results


# Method 3: Merge sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Merge_sort
# Settings: duplicate/unique agnostic (I think)


def get_combined_chunk(chunk_a: list, chunk_b: list) -> dict:
    chunk_ordered_list = []
    step_count = 0

    while chunk_a and chunk_b:

        if chunk_a[0] > chunk_b[0]:
            chunk_ordered_list.append(chunk_b[0])
            chunk_b = chunk_b[1:]
            step_count += 1
        else:
            chunk_ordered_list.append(chunk_a[0])
            chunk_a = chunk_a[1:]
            step_count += 1

    chunk_ordered_list.extend(chunk_a)
    chunk_ordered_list.extend(chunk_b)

    return {
        "chunk_ordered_list": chunk_ordered_list,
        "step_count": step_count,
    }


def merge_sort(
    random_list: list,
    known_solution_unique_random_list: list,
    debug: bool,
    help_text: str = "",
):
    method_name = "Merge sort"
    step_count = 0
    start_time = datetime.now()
    ordered_list = copy.deepcopy(random_list)
    chunk_size = 1

    random_count = len(random_list)

    while chunk_size <= random_count:
        cache_random_list = copy.deepcopy(ordered_list)
        ordered_list = []

        chunk_indexes = [i for i in range(0, random_count, chunk_size)] + [random_count]
        step_count += len(chunk_indexes)
        chunk_pos = list(zip(chunk_indexes[:-1], chunk_indexes[1:]))
        chunks = [cache_random_list[i[0] : i[1]] for i in chunk_pos]
        step_count += len(chunks)

        for chunk_index, a_chunk in enumerate(chunks[:-1]):
            if chunk_index % 2 == 0:
                temp = get_combined_chunk(a_chunk, chunks[chunk_index + 1])
                ordered_list.extend(temp["chunk_ordered_list"])
                step_count += temp["step_count"]

        leftover_random_numbers = cache_random_list[
            len(ordered_list) : len(cache_random_list)
        ]
        ordered_list.extend(leftover_random_numbers)

        chunk_size = chunk_size * 2

        if debug:
            print("current_chunk_size =", chunk_size)
            print("\tcache_random_list", cache_random_list)
            print("\tchunk_indexes", chunk_indexes)
            print("\tchunk_pos", chunk_pos)
            print("\tchunks", chunks)
            print("\t\t`ordered_list`, next `cache_random_list`", ordered_list)

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
