def print_sort_progress(lowest_number: int, step_count: int, debug: bool):
    if debug:
        print(f"Lowest number in this round = {lowest_number}. Step_count = {step_count}")


def print_sort_results(method_name: str, time_taken_to_sort: float, step_count: int, sort_state: bool,
                       matches_known_solution: bool = None, help_text: str = ""):
    result_f_string = f"Sort {method_name} {help_text} took {time_taken_to_sort} seconds to order in {step_count} steps. Check: Sort status = {sort_state}."

    if matches_known_solution is not None:
        print(f"{result_f_string} Accurate (against known solution: {matches_known_solution})")
    else:
        print(result_f_string)
