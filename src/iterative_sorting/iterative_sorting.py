# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

   for i in range(len(arr)):

       min_num = i

       for x in range(i+1, len(arr)):
           if arr[min_num] > arr[x]:
               min_num = x
                    
       s = arr[i]
       arr[i] = arr[min_num]
       arr[min_num] = s

   return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # range to compare. (first round: n, second: n-1)
    for i in range(len(arr)-1,0,-1):
        for x in range(i):
            # compare element with right
            if arr[x] > arr[x+1]:
                #swap
                s = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = s


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
