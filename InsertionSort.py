def insertion_sort(array):
    for i in range(1,len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
         array[j+1] = array[j]
         j = j - 1
        array[j+1] = value
unsorted_array = [14,13,9,-8,3,23,5,-17]
insertion_sort(unsorted_array)
print("The array is sorted by ascending order:\n",unsorted_array)
