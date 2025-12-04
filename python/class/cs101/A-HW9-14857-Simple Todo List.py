class PendingTaskIterator:
    def __init__(self, task_queue):
        self.pending = []
        self.index = 0
        # TODO: fill self.pending with the pending tasks in the correct order
        for task in list.__iter__(task_queue):
            if not task['done']:
                self.pending.append(task)
            
            
    def __next__(self):
        # TODO:
        if self.index >= len(self.pending):
            raise StopIteration
        task = self.pending[self.index]
        self.index += 1
        return task

class TaskQueue(list):
    def add_task(self, name):
        # TODO:
        # Append a new task dict to the list.
        task = {'name': name, 'done': False}
        self.append(task)
        

    def mark_done(self, name):
        # TODO:
        # Traverse the underlying list in insertion order
        for task in list.__iter__(self):
            if task['name'] == name and not task['done']:
                task['done'] = True
                break

    def __iter__(self):
        # TODO:
        # Return a PendingTaskIterator for this TaskQueue
        return PendingTaskIterator(self)


""" Do not change the code below """

q = int(input())
tq = TaskQueue()

for _ in range(q):
    op = input().split()

    if op[0] == "ADD":
        name = " ".join(op[1:])
        tq.add_task(name)

    elif op[0] == "DONE":
        name = " ".join(op[1:])
        tq.mark_done(name)

    elif op[0] == "LEN":
        print(len(tq))

    elif op[0] == "PRINTALL":
        print(tq)

    elif op[0] == "PENDING":
        k = int(op[1])
        it = iter(tq)
        for _ in range(k):
            print(next(it))
