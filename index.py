from src.buffer import Buffer

def run():
    first_buffer = Buffer('fifo')
    print(first_buffer)
    first_buffer.insert(4)
    first_buffer.insert(3)
    first_buffer.insert(2)
    first_buffer.extract()
    second_buffer = Buffer('lifo')
    print("Firts Buffer is {} , next last extraction".format(first_buffer.get_queue()))
    print(second_buffer)
    second_buffer.insert(4)
    second_buffer.insert(3)
    second_buffer.insert(2)
    second_buffer.extract()
    second_buffer.extract()
    print("Second Buffer is {} , next last extraction".format(second_buffer.get_queue()))

if __name__ == "__main__":
    run()