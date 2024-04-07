from __future__ import annotations
import time
from heapq import heapify, heappush, heappop
import math
from io import StringIO


class NotFound(Exception):
    def __init__(self, *args: object, msg: str) -> None:
        super().__init__(*args, msg)
        self.msg = msg


class Expired(Exception):
    def __init__(self, *args: object, msg: str) -> None:
        super().__init__(*args, msg)
        self.msg = msg


class CacheNode:
    def __init__(self, key: int, value: int, created_at: int, expire_at: int) -> None:
        self.key = key
        self.value = value
        self.created_at = created_at
        self.expire_at = expire_at

    # this method if used by heapq to order the objects by specific attributes
    def __lt__(self, other: CacheNode) -> bool:
        # overload the less than operator for comparison
        # self is the new node about to get inserted
        # other is the older, already present one
        return self.created_at < other.created_at

    def check_expiry(self) -> bool:
        if int(time.time()) > self.expire_at:
            return True
        else:
            return False


class LRUCache:
    def __init__(self, capacity: int):
        self.myheap = []
        # cache should contain only self.capacity nodes
        self.capacity = capacity

    def get(self, key: int) -> int | Exception:
        # to store the found node
        foundNode = CacheNode(-1, -1, 0, 0)
        is_expired = False

        node: CacheNode
        for i, node in enumerate(self.myheap):
            if node.key == key:
                # if node is found, directly delete
                self.myheap.pop(i)
                foundNode = node
                if node.check_expiry():
                    is_expired = True

        # check if key is invalid
        if foundNode.key == -1:
            raise NotFound(msg="invalid key, not found!!")

        # key is found and if its not expired, then we need to update its created_at and pushback to heap
        # since its not least recently accessed anymore
        if not is_expired:
            foundNode.created_at = int(time.time())
            # add back
            self.myheap.append(foundNode)

            # call heapify to maintain the variance
            heapify(self.myheap)
            return foundNode.value
        else:
            # node has been dropped, call heapify to maintain the variance
            self.capacity += 1
            heapify(self.myheap)
            raise Expired(msg="key has been expired!!")

    def put(self, key: int, value: int, expire_at: int) -> None:
        # check the current capacity, if its 0, then pop the topmost(least recently accessed node) and push the new one
        when_expire = int(time.time() + expire_at)
        cache_node = CacheNode(
            key=key, value=value, created_at=int(time.time()), expire_at=when_expire
        )
        if self.capacity == 0:
            print("making room for the new node")
            heappop(self.myheap)
            heappush(self.myheap, cache_node)
        else:
            heappush(self.myheap, cache_node)
            self.capacity -= 1

    # shamelessly copied from here: https://github.com/chaupmcs/some_python_functions/blob/master/printTreeHeapq.py
    def show_tree(self, total_width=60, fill=" "):
        output = StringIO()
        last_row = -1

        for i, node in enumerate(self.myheap):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write("\n")
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(
                str("key:" + str(node.key) + " " + "value:" + str(node.value)).center(
                    col_width, fill
                )
            )
            last_row = row

        print(output.getvalue())
        print("-" * total_width)


if __name__ == "__main__":
    lru = LRUCache(capacity=3)

    # expiry is in secs
    lru.put(5, 500, 3)
    time.sleep(1)
    lru.put(2, 200, 300)
    time.sleep(1)
    lru.put(1, 100, 40)

    lru.show_tree()

    # check for expiry
    time.sleep(4)

    try:
        print("value got:", lru.get(5))
    except NotFound as nf:
        print(nf.msg)
    except Expired as exp:
        print(exp.msg)

    # capacity should be increased since expired node was popped.
    lru.put(3, 300, 10)

    lru.show_tree()


"""
while self.myheap:
    top_most: CacheNode = heappop(self.myheap)
    print(top_most.key, top_most.value)

    if top_most.key == key:
        # key found
        not_found = False

        # check for expiry
        if not top_most.check_expiry():
            # update the created_at and then pushback
            top_most.created_at = time.time()
            heappush(self.myheap, top_most)
            return top_most.value
        else:
            raise Expired("key has been expired!!")
    else:
        # add that key back
        heappush(self.myheap, top_most)

    time.sleep(3)

if not_found:
    raise NotFound("invalid key, key not found")
"""
