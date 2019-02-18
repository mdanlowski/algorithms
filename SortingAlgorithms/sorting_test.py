from merge_sort import *
from selection_sort import *
from bubble_sort import *
import sys

from timeit import default_timer as dt
from sampledata import create_sample

start = dt()
data = create_sample(int(sys.argv[1]))
print("Sample ready:", dt() - start, '\n -----------------')

# merge
mergesdata = list(data)
start = dt()
done = merge_sort(mergesdata)
print("Merge sort time on dataset of size:", len(data), "is:", dt() - start)

# bubble
bubblesdata = list(data)
start = dt()
done = bubble_sort(bubblesdata)
print("Bubble sort time on dataset of size:", len(data), "is:", dt() - start)

# select
selectsdata = list(data)
start = dt()
done = selection_sort(selectsdata)
print("Selection sort time on dataset of size:", len(data), "is:", dt() - start)