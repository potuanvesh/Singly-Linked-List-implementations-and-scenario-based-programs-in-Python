class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        nn = Node(data)

        if self.head is None:
            self.head = nn
            return

        nn.next = self.head
        self.head = nn

    def insert_end(self, data):
        nn = Node(data)

        if self.head is None:
            self.head = nn
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = nn

    def insert_at_any_pos(self, pos, data):
        if pos <= 0:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        nn = Node(data)
        nn.next = temp.next
        temp.next = nn

    def delete_begin(self):
        if self.head is None:
            print("Playlist is empty")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Playlist is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        prev = None

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

    def delete_any_pos(self, pos):
        if pos <= 0:
            print("Invalid position")
            return

        if self.head is None:
            print("Playlist is empty")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        prev = None
        i = 1

        while i < pos and temp is not None:
            prev = temp
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        prev.next = temp.next

    def search(self, song):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == song:
                print("Song found at position:", pos)
                return

            temp = temp.next
            pos += 1

        print("Song not found")

    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        return c

    def display(self):
        if self.head is None:
            print("Playlist is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" → ")
            temp = temp.next

        print("None")

    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev


ll = SinglyLinkedList()

while True:

    print("\n===== MUSIC PLAYLIST MANAGER =====")
    print("1. Add song at beginning")
    print("2. Add song at end")
    print("3. Insert song at specified position")
    print("4. Remove first song")
    print("5. Remove last song")
    print("6. Remove song at specified position")
    print("7. Search for a song")
    print("8. Display total number of songs")
    print("9. Display complete playlist")
    print("10. Reverse playlist")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            song = input("Enter song name: ")
            ll.insert_begin(song)

        case 2:
            song = input("Enter song name: ")
            ll.insert_end(song)

        case 3:
            pos = int(input("Enter position: "))
            song = input("Enter song name: ")
            ll.insert_at_any_pos(pos, song)

        case 4:
            ll.delete_begin()

        case 5:
            ll.delete_end()

        case 6:
            pos = int(input("Enter position: "))
            ll.delete_any_pos(pos)

        case 7:
            song = input("Enter song name to search: ")
            ll.search(song)

        case 8:
            print("Total number of songs:", ll.count())

        case 9:
            ll.display()

        case 10:
            ll.reverse()
            print("Playlist reversed successfully")

        case 11:
            print("Application terminated")
            break

        case _:
            print("Invalid choice")