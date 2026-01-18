# QUICK-SORT
def quickSort(arr,low,high):
    if (low < high):
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)


def partition(arr , low , high):
    i = low-1  
    pivot = high
    for j in range(low,high):
        if (arr[j] < arr[pivot]):
            i += 1
            swap(arr,i,j)
    swap(arr,i+1,pivot)
    return i+1

def swap(arr , i , j):
    arr[i],arr[j] = arr[j], arr[i] # check why and how this works in python 



if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr , 0 , n-1)

    for val in arr:
        print(val , end=" ")

