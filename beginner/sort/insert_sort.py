def my_insert_sort(l):
    for i in range(1, len(l)):
        tmp = l[i]
        for j in range(i-1, -1, -1):
            if tmp < l[j]:
                l[j+1] = l[j]
            else:
                l[j+1] = tmp
                break
        else:
            l[0] = tmp

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    my_insert_sort(org_list)
