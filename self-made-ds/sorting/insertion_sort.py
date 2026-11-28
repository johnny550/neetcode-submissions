# Python implementation of Insertion Sort
# Best case runtime: O(n)
# Worst case runtime: O(n²)
def insertionSort(arr):
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them 
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr

if __name__=="__main__":
    print(insertionSort(arr=[9,4,6,7,100,1]))