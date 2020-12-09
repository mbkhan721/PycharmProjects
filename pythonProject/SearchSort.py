""" One way to measure the time cost of an algorithm is to use computer’s
clock to obtain actual run time

Benchmarking or profiling

Can use time() in time module
Returns number of seconds that have elapsed between current time on the computer’s
clock and January 1, 1970
 """


def ourMin(lyst):
    # Returns the position of the minimum item.
    minpos = 0
    current = 1
    while current < len(lyst):
        if lyst[current] < lyst[minpos]:
            minpos = current
        current += 1
    return minpos


x = [1, 2, 3, 4, 5, 6]
print(x)


left = 0
right = len(x) - 1

val = 6

while left <= right:
    middle = (left+right)//2
    print(left, ", ", right, ", ", middle, ", ", x[left], ", ", x[right], ", ", x[middle])

    if val == x[middle]:
        print("found it")
        break
    elif val <= x[middle]:
        print("smaller")
        right = middle-1
    else:
        print("bigger")
        left = middle+1