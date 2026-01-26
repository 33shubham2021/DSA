"""
This contains demo of using python sorting library
sorted(iterable, key=None, reverse=False)
iterable - can be any sequence like list, tuple, string,
key (optinal) = a function to customize the sort order, default is None
Returns a new sorted list containing all elements from the iterable according to the given criteria.


zip() - used to combine two or more iterables (like lists, tuples, strings, 
        dictionaries, etc.) into a single iterator of tuples. 
        Each tuple contains elements that share the same index across the input iterables.

"""

if __name__ == "__main__":
    a = [4, 1, 3, 2]
    b = sorted(a)
    print(b)

    # sort as per the length, then alphabetically
    a = ["apple", "banana", "cherry", "date"]
    res = sorted(a, key=len)
    print(res)

    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    #print(list(zip(a,b)))

    c = ['Shubham', "Ravi", "Veena"]
    print(list(zip(a, b, c)))