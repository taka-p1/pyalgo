def binary_search(l, target):
    """
    1. Compare center number and target.
       If target is larger, need not to search the first half of the list.
    2. Compare center number of the list and target again.
    3. Repeat this loop until center number epuals to target or the length of the list is zero.
    """
    head_idx = 0
    tail_idx = len(l)-1
    while head_idx < tail_idx:
        mid_idx = (head_idx+tail_idx)//2
        if target == l[mid_idx]:
            print(mid_idx)
            break
        elif target < l[mid_idx]:
            tail_idx = mid_idx-1
        else:
            head_idx = mid_idx+1
    else:
        print("no data")


if __name__ == '__main__':
    binary_search(sorted([3, 4, 5, 1, 12, 54, 512, 43, 42, 676, 34, 978]), 42)
    binary_search(sorted([3, 4, 5, 1, 12, 54, 512, 43, 42, 676, 34, 978]), 1)
    binary_search(sorted([3, 4, 5, 1, 12, 54, 512, 43, 42, 676, 34, 978]), 100)
