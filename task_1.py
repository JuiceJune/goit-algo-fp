class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(x) for x in self.to_list())

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # старий head стає останнім вузлом після реверсування
        while current:
            next_node = current.next   # запам'ятали "далі", бо зараз перепишемо current.next | ->2 | ->3 | ->4 | ->5 | None |
            current.next = prev        # розвертаємо посилання: тепер вузол дивиться назад | None | ->1 | ->2 | ->3 | ->4 |
            prev = current             # prev просувається на поточний вузол | ->1 | ->2 | ->3 | ->4 | ->5 |
            current = next_node        # current просувається на запам'ятаний "далі" | ->2 | ->3 | ->4 | ->5 | None |
        self.head = prev 

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return # порожній список або один елемент — сортувати нема що

        sorted_head = None # голова нового, вже відсортованого списку
        current = self.head # вузол, який зараз "виймаємо" зі старого списку

        while current:
            next_node = current.next # запам'ятали, звідки продовжити обхід старого списку
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

        # оновлюємо tail — доходимо до кінця нового відсортованого списку
        current = self.head
        while current.next:
            current = current.next
        self.tail = current

    @staticmethod
    def _sorted_insert(sorted_head, new_node):
        # new_node стає першим, якщо список порожній або новий елемент найменший
        if sorted_head is None or new_node.data <= sorted_head.data:
            new_node.next = sorted_head
            return new_node

        # інакше шукаємо вузол, після якого треба вставити new_node
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head


def merge_sorted_lists(list1: LinkedList, list2: LinkedList):
    """Приймає два вже відсортовані LinkedList, повертає новий відсортований LinkedList."""
    merged = LinkedList()

    # dummy — фіктивний вузол-заглушка, щоб не обробляти окремо випадок "перший вузол результату"
    dummy = Node(None)
    tail = dummy  # tail завжди вказує на останній вже приєднаний вузол результату

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current2.data < current1.data:
            smaller = current2
            current2 = current2.next
        else:
            smaller = current1
            current1 = current1.next

        tail.next = smaller
        tail = smaller

    if current1:
        tail.next = current1

    if current2:
        tail.next = current2

    merged.head = dummy.next

    # оновлюємо tail — доходимо до кінця злитого списку
    current = merged.head
    while current and current.next:
        current = current.next
    merged.tail = current

    return merged


if __name__ == "__main__":
    ll = LinkedList()
    for x in [1, 2, 3, 4, 5]: # [2, 1, 3, 4, 5], [3, 2, 1, 4, 5], [4, 3, 2, 1, 5], [5, 4, 3, 2, 1]
        ll.append(x)
    print("Початковий список:", ll)

    ll.reverse()
    print("Після реверсування:", ll)

    ll2 = LinkedList()
    for x in [9, 8, 7, 6, 5]:
        ll2.append(x)
    print("\nДо сортування:", ll2)
    ll2.insertion_sort()
    print("Після сортування:", ll2)

    ll3 = LinkedList()
    for x in [1, 2, 3, 4]:
        ll3.append(x)
    print("\nДва відсортовані списки для злиття:")
    print("list1:", ll3)
    print("list2:", ll2)

    mergedList = merge_sorted_lists(ll3, ll2)
    print("Після злиття:", mergedList)
