

class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """

    def __init__(self, policy):
        policy = policy.upper()
        if policy not in ['FIFO', 'LIFO']:
            raise ValueError()
        self._policy = policy
        self._queue = []

    def __str__(self):
        message = "<Buffer> {} - <Policy> {}.".format(self._queue, self._policy)
        return message

    def get_queue(self):
        return self._queue

    def insert(self, item):
        """method for insert buffer value that depends policy

        Args:
            item (any): [value to save in buffer]
        """
        if(self._policy == 'FIFO'):
            self._queue.append(item)
        elif(self._policy == 'LIFO'):
            self._queue.insert(0,item)
    
    def extract(self):
        """method for extract buffer value  that depends policy

        Returns:
            [list]: [Buffer next extract element]
        """
        if(self._queue):
            self._queue.pop(0)    
        return self.get_queue()


