from collections import Counter
def countElements(arr):
    
    counts = Counter(arr)
    
    true_count = 0
    
    for num in arr:
        if num+1 in counts:
            true_count += 1
    
    return true_count