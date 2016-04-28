'''
Given a sorted array of interger, write a function to find the index
of first element which is larger than or equal to another given interger

'''

def find_index(r, n):
    '''
    r[i-1] < n =< r[i]
    reutn i
    '''

    start = 0
    end = len(r) -1

    while start <= end:
        mid = (start + end)/2
        if n > r[mid]:
             start = mid + 1
        elif r[mid -1] < n <= r[mid]:
             return mid
        elif  n <= r[mid-1]:
             end = mid - 1

    return -1


if __name__ == "__main__":

    r = [1, 3, 4, 7, 8, 9]
    n = 5
    assert find_index(r, n) == 3

    r = [1, 3, 4, 5, 7, 8, 9]
    n = 5
    assert find_index(r, n) == 3

    r = [1, 3, 4, 5, 5, 7, 8, 9]
    n = 5
    assert find_index(r, n) == 3

    r = [1, 3, 5, 7, 8, 9]
    n = 10
    assert find_index(r, n) == -1

    r = [1, 3, 5, 7, 8, 9]
    n = -1
    assert find_index(r, n) == -1