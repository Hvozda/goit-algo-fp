# === Клас вузла (елемента списку) ===
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# === Клас однозв’язного списку ===
class LinkedList:
    def __init__(self):
        self.head = None

# Додаємо елемент у кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
                self.head = new_node
        return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Вивід спис
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
        current = current.next
print()

# === 1. Реверсування списку ===
def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    self.head = prev

# === 2. Сортування вставками ===
def insertion_sort(self):
    sorted_head = None
    current = self.head

    while current:
        next_node = current.next
# вставка вузла у відсортований список
    if sorted_head is None or current.data < sorted_head.data:
        current.next = sorted_head
        sorted_head = current
    else:
        sorted_current = sorted_head
    while sorted_current.next and sorted_current.next.data < current.data:
        sorted_current = sorted_current.next
    current.next = sorted_current.next
    sorted_current.next = current
    current = next_node

    self.head = sorted_head


# === 3. Об’єднання двох відсортованих списків ===
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    a = l1.head
    b = l2.head

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
            tail = tail.next

            tail.next = a if a else b

            merged_list = LinkedList()
            merged_list.head = dummy.next
    return merged_list


# === Демонстрація роботи ===
if __name__ == "__main__":
# Створюємо список
    llist = LinkedList()
for val in [4, 2, 1, 3]:
    llist.insert_at_end(val)

print("Оригінальний список:")
llist.print_list()

# Сортування
llist.insertion_sort()
print("\nВідсортований список:")
llist.print_list()

# Реверс
llist.reverse()
print("\nРеверсований список:")
llist.print_list()

# Об’єднання двох списків
list1 = LinkedList()
list2 = LinkedList()
for val in [1, 3, 5]:
    list1.insert_at_end(val)
for val in [2, 4, 6]:
    list2.insert_at_end(val)

merged = merge_sorted_lists(list1, list2)
print("\nОб’єднаний відсортований список:")
merged.print_list()
