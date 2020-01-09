def my_bubble_sort(l):
    for i in range(0, len(l)-1):
        for j in range(len(l)-1, i, -1):
            print("j: {}".format(j))
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]


if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    my_bubble_sort(org_list)
    print(org_list)
