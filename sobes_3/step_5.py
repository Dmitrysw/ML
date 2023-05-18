
def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # find the length of linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # make the list circular
    tail.next = head

    # find new head and tail position
    new_tail = head
    for _ in range(length - k % length - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # break the circular list
    new_tail.next = None

    return new_head
