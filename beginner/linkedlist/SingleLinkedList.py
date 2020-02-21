class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :   ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes in the list = ", n)
    
    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, " not found in list")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for _ in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self, data, k):
        pass


if __name__ == "__main__":
    l = SingleLinkedList()
    l.create_list()
    
    while True:
        print("1. Display list")
        print("2. Count the number of nodes")
        print("3. Search for an element")
        print("4. Insert in empty list/Insert in beginning of the list")
        print("5. Insert a node at the end of the list.")
        print("6. Insert a node after a specified node")
        print("7. Insert a node before a specified node")
        print("8. Insert a node at a given position")
        print("9. Delete first node")
        print("10. Delete last node")
        print("11. Delete any node")
        print("12. Reverse the list")
        print("13. Bubble sort by exchanging data")
        print("14. Bubble sort by exchanging links")
        print("15. MergeSort")
        print("16. Insert Cycle")
        print("17. Detect Cycle")
        print("18. Remove Cycle")
        print("19. Quit")

        option = int(input("Enter your choice : "))

        if option == 1:
            l.display_list()
        elif option == 2:
            l.count_nodes()
        elif option == 3:
            data = int(input("Enter the element to be searched : "))
            l.search(data)

