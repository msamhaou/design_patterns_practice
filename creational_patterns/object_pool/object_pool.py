"""
When to Use:
    -Expensive Object Creation: When creating objects is resource-intensive (e.g., database connections, thread pools).
    -High Frequency of Object Use: When objects are used and discarded frequently.
    -Limited Resources: When system resources are limited and need careful management.
    -Immutable or Resettable Objects: When objects can be easily reset or returned to a default state for reuse.
"""
from abc import  ABC, abstractmethod
from queue import Queue
import threading
import time

class databaseConnection():
    def __init__(self, id):
        self.id = id
        self.connected = False
    
    def connect(self):
        time.sleep(0.1)
        self.connected = True
        print(f'Connection {self.id} established')
    
    def disconnect(self):
        self.connected = False
        print(f'Connection {self.id} closed')
    
    def execute(self, snippet):
        if not self.connected:
            raise ErrorValue('You are not connected')
        print(f'Executing {snippet} by {self.id}')


class ConnectionPool():
    def __init__(self, size:int):
        self.size = size
        self.pool = Queue(maxsize=size)

        for i in range(size):
            conn = databaseConnection(i)
            conn.connect()
            self.pool.put(conn)
        self.lock = threading.Lock()
    
    def acquire(self, timeout=None):
        try:
            conn = self.pool.get(block=True, timeout=timeout)
            print(f'Connection {conn.id} acquired')
            return conn
        except Exception as e:
            print("Failed to aquire connection")
            return None
        
    def release(self, conn):
        if conn:
            self.pool.put(conn)
            print(f"Released connection {conn.id}")

    def close_all(self):
        while not self.pool.empty():
            conn = self.pool.get()
            conn.disconnect()

def worker(pool, query):
    conn = pool.acquire(timeout=2)
    if conn:
        try :
            conn.execute(query)
        finally:
            pool.release(conn)

if __name__ == '__main__':
    pool = ConnectionPool(10)
    threads = []
    queries = ["SELECT * FROM game_obj", "TRUNCATE table1"]
    for q in queries:
        t = threading.Thread(target=worker, args=(pool, q))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    pool.close_all()