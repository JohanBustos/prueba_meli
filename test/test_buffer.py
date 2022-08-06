from src.buffer import Buffer

def test_valid_insert_lifo():
    first_buffer = Buffer('Lifo')
    first_buffer.insert(4)
    first_buffer.insert(3)
    first_buffer.insert(2)
    now_buffer = first_buffer.get_queue()
    assert now_buffer == [2,3,4]

def test_valid_insert_fifo():
    first_buffer = Buffer('fifo')
    first_buffer.insert(4)
    first_buffer.insert(3)
    first_buffer.insert(2)
    now_buffer = first_buffer.get_queue()
    assert now_buffer == [4,3,2]

def test_valid_remove():
    first_buffer = Buffer('fifo')
    first_buffer.insert(4)
    first_buffer.insert(3)
    first_buffer.insert(2)
    first_buffer.extract()
    first_buffer.extract()
    first_buffer.extract()
    first_buffer.extract()
    now_buffer = first_buffer.get_queue()
    assert now_buffer == []