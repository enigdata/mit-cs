### Bogo sort 
# O(?) it is unbounded if really unlucky
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

### Bubble sort 
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True 
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                swap = False 
                temp = L[i]
                L[i] = L[i-1]
                L[i-1] = temp 

# inner for loop is for doing the comparisons; outer while loop is for doing multiple passes until no more swaps
# O(n**2)           

#### Selection Sort 
#Keep the left portion of the list sorted 
#O(n**2)

def selection_sort(L):
    i = 0 
    while i != len(L):
        for j in range(i, len(L)):
            if L[j] < L[i]:
                #swap 
                L[i], L[j] = L[j], L[i]
        i += 1 

####### Merge Sort

### the merging sublist step
def merge(left, right):
    result = []
    i, j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 

    #when right sublist is empty
    while (i < len(left)):
        result.append(left[i])
        i += 1 
    while j < len(right):
        result.append(right[j])
        j += 1

    #when left sublist is empty

def merge_sort(L):
    if len(L) < 2:
        return L[:]

    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

#dividing list in half with each recursive call: O(log(n)) where n is len(L)
#at each recursion level time complexity is O(n) where n is len(L)
#overall complexity if O(n*log(n))

