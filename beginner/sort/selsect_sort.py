org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]

def my_select_sort(int_list):
    """"""
    sorted_list = []
    org_len = len(int_list)
    for _ in range(org_len):
        tmp_min = find_min(int_list)
        int_list.remove(tmp_min)
        sorted_list.append(tmp_min)
            
    print(sorted_list)

def find_min(l):
    min_num = l[0]
    for num in l:
        if min_num > num:
            min_num = num
    return min_num

# 選択ソート
def select_sort(arr):
  for i in range(0, len(arr)-1): #配列の要素数-1回繰り返す
    select_min(arr, i)
    
def select_min(arr, i):
  #最小要素の位置の特定
  min = i
  for j in range(i + 1, len(arr)):
    if arr[min] > arr[j]:
      min = j
  #最小要素と先頭要素を交換
  arr[i], arr[min] = arr[min], arr[i]

if __name__ == '__main__':
    select_sort(org_list)
