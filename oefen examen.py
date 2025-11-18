class Node:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

    def __str__(self):
        return f"Task: {self.task_name}, Duration: {self.duration}, Priority: {self.priority}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_task(self, task_name, duration, priority):
        newNode = Node(task_name, duration, priority)
        if self.size == 0:
            self.head = newNode
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def remove_task(self, task_name):
        if self.size == 0:
            return f"No tasks in list"

        previous = self.head
        while previous.next.task_name != task_name:
            previous = previous.next

        temp = previous.next
        previous.next = temp.next
        self.size -= 1
        return temp

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next

    def find_task(self, task_name):
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return current
            else:
                current = current.next
        return "Task not found"

    def calculate_total_durations(self):
        totaal = 0
        current = self.head
        while current is not None:
            totaal += current.duration
            current = current.next
        return totaal

    def read_tasks_from_csv(self,file):
        inpoet = open(file, 'r')
        taken = inpoet.readlines()
        for taak in taken[1:]:
            taak = taak.strip('\n')
            opdracht = taak.split(',')
            self.add_task(opdracht[0], int(opdracht[1]), int(opdracht[2]))

    def reorder_tasks_by_priority(self):
        current = self.head
        inpoet = None
        while current is not None:
            inpoet = self.sorted_insert_by_priority(inpoet, current)
            current = current.next
        gesorteerd = LinkedList()
        while inpoet is not None:
            gesorteerd.add_task(inpoet.task_name, inpoet.duration, inpoet.priority)
            inpoet = inpoet.next
        return gesorteerd

    def sorted_insert_by_priority(self, head, node):
        newNode = Node(node.task_name, node.duration, node.priority)
        if head is None:
            head = newNode
            return head
        if newNode.priority < head.priority:
            newNode.next = head
            head = newNode
            return head

        previous = head
        while previous.next is not None and newNode.priority > previous.next.priority:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
        else:
            current = previous.next
            previous.next = newNode
            newNode.next = current
        return head

    def reorder_tasks_by_priority_duration(self):
        inpoet = None
        current = self.head
        while current is not None:
            inpoet = self.sorted_insert_by_priority_duration(inpoet, current)
            current = current.next
        resultaat = LinkedList()
        while inpoet is not None:
            resultaat.add_task(inpoet.task_name, inpoet.duration, inpoet.priority)
            inpoet = inpoet.next
        return resultaat

    def sorted_insert_by_priority_duration(self, head, node):
        newNode = Node(node.task_name, node.duration, node.priority)

        if head is None:
            head = newNode
            return head
        if newNode.priority < head.priority:
            newNode.next = head
            head = newNode
            return head
        if newNode.priority == head.priority:
            if newNode.duration < head.duration:
                newNode.next = head
                head = newNode
                return head

        previous = head
        while previous.next is not None and newNode.priority > previous.next.priority:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
            return head

        while previous.next is not None and previous.next.priority == newNode.priority and newNode.duration > previous.next.duration:
            previous = previous.next

        if previous.next is None:
            previous.next = newNode
        else:
            temp = previous.next
            previous.next = newNode
            newNode.next = temp
        return head