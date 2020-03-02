import csv
import logging
import uuid
from pathlib import Path


def print_sort_progress(lowest_number: int, step_count: int, debug: bool):
    if debug:
        logging.info(f"Lowest number in this round = {lowest_number}. Step_count = {step_count}")


def print_sort_results(
    method_name: str,
    time_taken_to_sort: float,
    step_count: int,
    sort_state: bool,
    matches_known_solution: bool = None,
    help_text: str = "",
    create_csv: bool = False,
):
    result_f_string = f"{method_name} {help_text} took {time_taken_to_sort} seconds to order in {step_count} steps. Check: Sort status = {sort_state}."

    if matches_known_solution is not None:
        logging.info(
            f"{result_f_string} Accurate (against known solution: {matches_known_solution})"
        )
    else:
        logging.info(result_f_string)

    if create_csv:

        temp = {
            "run_id": uuid.uuid4(),
            "method_name": method_name,
            "time_taken": time_taken_to_sort,
            "step_count": step_count,
            "sort_state": sort_state,
        }

        if Path().joinpath("perf.csv").exists():

            with open("perf.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(list(temp.values()))

        else:

            with open("perf.csv", "w") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(list(temp.keys()))
                csv_writer.writerow(list(temp.values()))
