class Queue():
    def __init__(self, max: int) -> None:
        self._queue = []
        self._max = max

    def enqueue(self, value):
        if self.size() == self._max:
            return -1
        else:
            self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def ldequeue(self):
        return self._queue.pop()

    def remove(self, value):
        self._queue.remove(value)

    def size(self):
        return len(self._queue)

    def empty(self):
        return self.size() == 0

    def full(self):
        return self.size() == self._max

    def getFirst(self):
        return self._queue[0]

    def getLast(self):
        return self._queue[-1]
