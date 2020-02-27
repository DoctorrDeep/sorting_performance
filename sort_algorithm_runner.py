import logging

from app_scripts.create_check_random_number_list import generate_list
from sorters.bubble_sort import bubble_sort as bu_s
from sorters.merge_sort import merge_sort as ms
from sorters.native_sort import native_sort as ns
from sorters.quick_sort import quick_sort as qs
from sorters.selection_sort_1 import selection_sort as ss1
from sorters.selection_sort_2 import selection_sort as ss2

debug = False
count = None
# count = 500

logging.basicConfig(
    # filename=f"{my_dir}/sort_runner.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

if debug:
    unique_random_list = generate_list(max_number=20, count=6, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(
        max_number=20, count=6, uniqued_list=False
    )
else:
    unique_random_list = generate_list(count=count, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(count=count, uniqued_list=False)

known_solution_unique_random_list = ss1(
    unique_random_list, debug=debug, help_text="for unique numbers"
)
known_solution_duplicate_allowed_random_list = ss2(
    duplicate_allowed_random_list, debug=debug, help_text="for non-unique numbers"
)

bu_s(
    unique_random_list,
    known_solution_unique_random_list,
    debug=debug,
    help_text="for unique numbers",
)

bu_s(
    duplicate_allowed_random_list,
    known_solution_duplicate_allowed_random_list,
    debug=debug,
    help_text="for non-unique numbers",
)

ms(
    unique_random_list,
    known_solution_unique_random_list,
    debug=debug,
    help_text="for unique numbers",
)

ms(
    duplicate_allowed_random_list,
    known_solution_duplicate_allowed_random_list,
    debug=debug,
    help_text="for non-unique numbers",
)

ns(
    unique_random_list,
    known_solution_unique_random_list,
    debug=debug,
    help_text="for unique numbers",
)

ns(
    duplicate_allowed_random_list,
    known_solution_duplicate_allowed_random_list,
    debug=debug,
    help_text="for non-unique numbers",
)

qs(
    unique_random_list,
    known_solution_unique_random_list,
    debug=debug,
    help_text="for unique numbers",
)

qs(
    duplicate_allowed_random_list,
    known_solution_duplicate_allowed_random_list,
    debug=debug,
    help_text="for non-unique numbers",
)


def create_graph():

    for i in range(100):
        unique_random_list = generate_list(count=count, uniqued_list=True)
        known_solution_unique_random_list = ss1(
            unique_random_list, debug=debug, help_text="for unique numbers", create_csv=True
        )
        bu_s(
            unique_random_list,
            known_solution_unique_random_list,
            debug=debug,
            help_text="for unique numbers",
            create_csv=True,
        )
        ms(
            unique_random_list,
            known_solution_unique_random_list,
            debug=debug,
            help_text="for unique numbers",
            create_csv=True,
        )
        ns(
            unique_random_list,
            known_solution_unique_random_list,
            debug=debug,
            help_text="for unique numbers",
            create_csv=True,
        )
        qs(
            unique_random_list,
            known_solution_unique_random_list,
            debug=debug,
            help_text="for unique numbers",
            create_csv=True,
        )

create_graph()

## Experimental
# import pandas as pd
# import matplotlib.pyplot as plt
# all_data_df = pd.read_csv("perf.csv")
# perf_df = all_data_df.loc[:, ["method_name", "time_taken"]]
# steps_df = all_data_df.loc[:, ["method_name", "step_count"]]
#
# fig, (ax1, ax2) = plt.subplots(1, 2)
#
# perf_mer = perf_df[perf_df["method_name"] == "Merge sort"].loc[:,"time_taken"].to_numpy()
# perf_quk = perf_df[perf_df["method_name"] == "Quick sort"].loc[:,"time_taken"].to_numpy()
# perf_bub = perf_df[perf_df["method_name"] == "Bubble sort"].loc[:,"time_taken"].to_numpy()
# perf_nat = perf_df[perf_df["method_name"] == "Native sort"].loc[:,"time_taken"].to_numpy()
# perf_sel = perf_df[perf_df["method_name"] == "Selection sort 1.0"].loc[:,"time_taken"].to_numpy()
# ax1.set_title("Box plot of performance (lower is better)")
# ax1.set_xlabel("sorters")
# ax1.set_ylabel("time in seconds")
# ax1.boxplot((perf_mer, perf_bub, perf_nat, perf_sel, perf_quk))
# ax1.legend(["perf_mer", "perf_bub", "perf_nat", "perf_sel", "perf_quk"])
#
# steps_mer = steps_df[steps_df["method_name"] == "Merge sort"].loc[:,"step_count"].to_numpy()
# steps_quk = steps_df[steps_df["method_name"] == "Quick sort"].loc[:,"step_count"].to_numpy()
# steps_bub = steps_df[steps_df["method_name"] == "Bubble sort"].loc[:,"step_count"].to_numpy()
# steps_nat = steps_df[steps_df["method_name"] == "Native sort"].loc[:,"step_count"].to_numpy()
# steps_sel = steps_df[steps_df["method_name"] == "Selection sort 1.0"].loc[:,"step_count"].to_numpy()
# ax2.set_title("Box plot of steps (lower is better)")
# ax2.set_xlabel("sorters")
# ax2.set_ylabel("count")
# ax2.boxplot((steps_mer, steps_bub, steps_nat, steps_sel, steps_quk))
# ax2.legend(["steps_mer", "steps_bub", "steps_nat", "steps_sel", "steps_quk"])
#
# fig.show()




# TODO: Heap Sort https://en.wikipedia.org/wiki/Heapsort
# TODO: Bucket Sort (this is the  method that I used to sort cards when I need to sort under distraction. Takes longer because more steps required.) https://en.wikipedia.org/wiki/Bucket_sort
