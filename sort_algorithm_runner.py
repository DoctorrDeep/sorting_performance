from app_scripts.create_check_random_number_list import generate_list
from sorters.bubble_sort import bubble_sort as bu_s
from sorters.selection_sort_1 import selection_sort as ss1
from sorters.selection_sort_2 import selection_sort as ss2

debug = False
count = None
# count = 500

if debug:
    unique_random_list = generate_list(count=5, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(count=5, uniqued_list=False)
else:
    unique_random_list = generate_list(count=count, uniqued_list=True)
    duplicate_allowed_random_list = generate_list(count=count, uniqued_list=False)

known_solution_unique_random_list = ss1(unique_random_list, debug=debug, help_text="for unique numbers")
known_solution_duplicate_allowed_random_list = ss2(duplicate_allowed_random_list, debug=debug,
                                                   help_text="for non-unique numbers")

bu_s(unique_random_list, known_solution_unique_random_list, debug=debug, help_text="for unique numbers")
bu_s(duplicate_allowed_random_list, known_solution_duplicate_allowed_random_list, debug=debug,
     help_text="for non-unique numbers")

# TODO: Merge Sort (as done in youtube linked video in Readme) https://en.wikipedia.org/wiki/Merge_sort
# TODO: Quick Sort https://en.wikipedia.org/wiki/Quicksort
# TODO: Heap Sort https://en.wikipedia.org/wiki/Heapsort
# TODO: Bucket Sort (this is the  method that I used to sort cards when I need to sort under distraction. Takes longer because more steps required.) https://en.wikipedia.org/wiki/Bucket_sort
