from typing import Optional

class Node():
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class SLinkedList():
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def prepend(self, value):
        """Method untuk insert data di awal linked list."""
        newNode = Node(value, next=self.head)

        if self.head is None: # jika linked list kosong
            self.head = newNode
            self.tail = newNode
        else:
            self.head = newNode

        self.size += 1

    def append(self, value):
        """Method untuk insert data di akhirt linked list."""
        newNode = Node(value, next=None)

        if self.tail is None: # jika linked list kosong
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def add_after(self, value, after):
        """Method untuk insert data setelah data tertentu dalam linked list."""
        currentNode = self.head
        newNode = Node(value)
        nextNode = None

        while currentNode is not None:
            if currentNode.data == after:
                nextNode = currentNode.next

                if nextNode is None: self.tail = newNode # dilakukan ketika insert setelah data terakhir

                currentNode.next = newNode
                newNode.next = nextNode
                self.size += 1
                return

            currentNode = currentNode.next

        return -1

    def add_before(self, value, before):
        """Method untuk insert data setelah data tertentu dalam linked list."""
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next
        newNode = Node(value)

        while currentNode is not None:
            if currentNode.data == before: # dilakukan ketika insert sebelum data pertama
                newNode.next = self.head
                self.head = newNode
                self.size += 1
                return
            elif nextNode is not None and nextNode.data == before:
                currentNode.next = newNode
                newNode.next = nextNode
                self.size += 1
                return

            currentNode = currentNode.next
            nextNode = currentNode.next

        return -1

    def display(self):
        """Method untuk memperlihatkan data pada linked list secara visual."""
        currentNode = self.head
        string_result = ""

        if currentNode == None:
            print("None")
        else:
            while currentNode is not None:
                string_result += f"[{currentNode.data}] -> "
                currentNode = currentNode.next

            print(string_result + "None")

    def traverse(self):
        """Method untuk menelusuri data pada linked list."""
        currentNode = self.head

        if currentNode == None:
            return None
        else:
            while currentNode is not None:
                yield currentNode.data
                currentNode = currentNode.next


    def contain(self, value):
        """Method untuk memeriksa apakah suatu data ada dalam linked list."""
        currentNode = self.head
        
        while currentNode is not None:
            if currentNode.data == value:
                return True

            currentNode = currentNode.next

        return False

    def getFirst(self):
        """Method untuk mendapatkan data pertama dalam linked list."""
        return None if self.head is None else self.head.data

    def getLast(self):
        """Method untuk mendapatkan data terakhir dalam linked list."""
        return None if self.tail is None else self.tail.data

    def popLeft(self):
        """Method untuk menghapus data pertama dalam linked list dan mengembalikannya."""
        firstNode = self.head

        if firstNode is None: # ketika linked list kosong
            return None
        elif firstNode.next is None: # ketika hanya ada satu data pada linked list
            self.head = None
            self.tail = None
            self.size -= 1
            return firstNode.data
        else:
            self.head = firstNode.next
            self.size -= 1
            return firstNode.data


    def pop(self):
        """Method untuk menghapus data terakhir dalam linked list dan mengembalikannya."""
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next

        if currentNode is None: # ketika linked list kosong
            return None
        elif currentNode.next is None: # ketika hanya ada satu data pada linked list
            self.head = None
            self.tail = None
            self.size -= 1
            return currentNode.data
        else:
            while currentNode is not None:
                if nextNode is not None and nextNode.next is None:
                    currentNode.next = None
                    self.tail = currentNode
                    self.size -= 1
                    return nextNode.data

                currentNode = currentNode.next
                nextNode = currentNode.next

    def remove(self, value):
        """Method untuk menghapus data dalam linked list berdasarkan nama datanya."""
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next

        if currentNode is None: # ketika linked list kosong
            return -1
        elif currentNode.next is None: # ketika hanya ada satu data pada linked list
            if currentNode.data == value:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                return -1
        else:
            while currentNode is not None:
                if currentNode.data == value:
                    self.head = currentNode.next
                    self.size -= 1
                    return
                elif nextNode is not None and nextNode.data == value:
                    currentNode.next = nextNode.next

                    if nextNode.next is None: self.tail = currentNode # jika yang dihapus data terakhir

                    self.size -= 1
                    return

                currentNode = currentNode.next
                nextNode = None if currentNode is None else currentNode.next

            return -1

    def empty(self):
        """Method ini akan mengembalikan True jika linked list kosong."""
        return True if self.head is None else False

class DLinkedList(SLinkedList):
    def prepend(self, value):
        """Method untuk insert data di awal linked list."""
        newNode = Node(value, next=self.head)

        if self.head is None: # jika linked list kosong
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            self.head = newNode

        self.size += 1

    def append(self, value):
        """Method untuk insert data di akhirt linked list."""
        newNode = Node(value, prev=self.tail)

        if self.tail is None: # jika linked list kosong
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def add_after(self, value, after):
        """Method untuk insert data setelah data tertentu dalam linked list."""
        currentNode = self.head
        newNode = Node(value)

        while currentNode is not None:
            if currentNode.data == after:
                newNode.next = currentNode.next
                newNode.prev = currentNode

                if currentNode.next is None: 
                    currentNode.next = newNode
                    self.tail = newNode # dilakukan ketika insert setelah data terakhir
                else:
                    currentNode.next.prev = newNode
                    currentNode.next = newNode

                self.size += 1
                return

            currentNode = currentNode.next

        return -1

    def add_before(self, value, before):
        """Method untuk insert data setelah data tertentu dalam linked list."""
        currentNode = self.head
        newNode = Node(value)

        while currentNode is not None:
            if currentNode.data == before:
                newNode.prev = currentNode.prev
                newNode.next = currentNode

                if currentNode.prev is None: 
                    currentNode.prev = newNode
                    self.head = newNode # dilakukan ketika insert sebelum data pertama
                else:
                    currentNode.prev.next = newNode
                    currentNode.prev = newNode

                self.size += 1
                return

            currentNode = currentNode.next

        return -1

    def popLeft(self):
        """Method untuk menghapus data pertama dalam linked list dan mengembalikannya."""
        firstNode = self.head

        if firstNode is None: # ketika linked list kosong
            return None
        elif firstNode.next is None: # ketika hanya ada satu data pada linked list
            self.head = None
            self.tail = None
            self.size -= 1
            return firstNode.data
        else:
            self.head = firstNode.next
            self.head.prev = None
            self.size -= 1
            return firstNode.data

    def pop(self):
        """Method untuk menghapus data terakhir dalam linked list dan mengembalikannya."""
        lastNode = self.tail

        if lastNode is None: # ketika linked list kosong
            return None
        elif lastNode.prev is None: # ketika hanya ada satu data pada linked list
            self.head = None
            self.tail = None
            self.size -= 1
            return lastNode.data
        else:
            self.tail = lastNode.prev
            self.tail.next = None
            self.size -= 1
            return lastNode.data

    def remove(self, value):
        """Method untuk menghapus data dalam linked list berdasarkan nama datanya."""
        currentNode = self.head

        if currentNode is None: # ketika linked list kosong
            return -1
        elif currentNode.next is None: # ketika hanya ada satu data pada linked list
            if currentNode.data == value:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                return -1
        else:
            while currentNode is not None:
                if currentNode.data == value:
                    if currentNode is self.head:
                        self.head = currentNode.next
                        self.head.prev = None
                        self.size -= 1
                        return
                    elif currentNode is self.tail:
                        self.tail = currentNode.prev
                        self.tail.next = None
                    else:
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev

                currentNode = currentNode.next

            return -1

    def traverse(self, reverse=False):
        """Method untuk menelusuri data pada linked list."""
        currentNode = self.head if not reverse else self.tail

        if currentNode == None:
            return None
        else:
            while currentNode is not None:
                yield currentNode.data
                currentNode = currentNode.next if not reverse else currentNode.prev

    def display(self, reverse=False):
        """Method untuk memperlihatkan data pada linked list secara visual."""
        currentNode = self.head if not reverse else self.tail
        string_result = "None ⇄ "

        if currentNode == None:
            print("None")
            return

        print("forward" if not reverse else "backward")
        while currentNode is not None:
            string_result += f"[{currentNode.data}] ⇄ "
            currentNode = currentNode.next if not reverse else currentNode.prev

        print(string_result + "None")
