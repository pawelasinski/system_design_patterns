"""Bloom filter

A `Bloom filter` is a probabilistic data structure that efficiently checks
whether an element is possibly in a set or definitely not in the set.
It is particularly useful for fast membership queries with minimal memory usage.

How it works:
* A `Bloom filter` consists of a bit array and multiple hash functions.
* When an item is added, it is passed through the hash functions,
    setting specific bits in the array.
* To check if an item is in the set, the same hash functions verify
    whether the corresponding bits are set.
* If all bits are set, the item might be present; otherwise, it is definitely not in the set.

Key Properties:
* Fast & Memory Efficient (uses much less memory compared to traditional sets).
* False Positives Possible (the filter may mistakenly indicate presence,
    but never false negatives).
* No Deletion (once an element is added, it cannot be removed directly
    (without additional structures)).
* Ideal for Large Datasets (used in applications where space and speed are critical).

Where it's used?
* Database caching (prevents unnecessary lookups in large databases).
* Spam filtering (detects known spam messages efficiently).
* Web crawling (ensures URLs are not revisited).
* Blockchain & networking (ptimizes transaction verification).

"""

import hashlib
import bitarray


class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        return [
                   int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size,
                   int(hashlib.sha1(item.encode()).hexdigest(), 16) % self.size,
                   int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size,
               ][: self.hash_count]

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def might_contain(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))


if __name__ == "__main__":
    bloom_filter = BloomFilter(size=50, hash_count=3)

    bloom_filter.add("1984")
    bloom_filter.add("Brave New World")
    bloom_filter.add("Fahrenheit 451")

    print(bloom_filter.might_contain("1984"))  # True (probably)
    print(bloom_filter.might_contain("Dune"))  # False (definitely not)
