def linear_search(l, target):
    for i, num in enumerate(l):
        if num == target:
            print(i)
            break
    else:
        print("No number")


if __name__ == '__main__':
    linear_search([3, 4, 5, 1], 4)
    linear_search([3, 4, 5, 1], 9)
