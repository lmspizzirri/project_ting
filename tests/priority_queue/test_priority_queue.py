from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 11})
    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 2})
    assert queue.dequeue() == {"qtd_linhas": 5}
    assert queue.search(1) == {"qtd_linhas": 11}
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(100)
