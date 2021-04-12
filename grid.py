"""
имплеметација просторног хеша
"""

import math
import itertools

class Grid:
    # иницијализација инстанце класе Grid
    def __init__(self, width, height, cellsize):
        self.width = width
        self.height = height
        self.cellsize = cellsize

        self.cells = [[Node(-1) for _ in range(math.ceil(height / cellsize))] for _ in range(math.ceil(width / cellsize))]
        self.xcells = len(self.cells)
        self.ycells = len(self.cells[0])
        self.nodes = {}  # сет инстанца класе Node

    # фунција која даје координате поља у хешу у којој се налази честица на датој позицији
    def coords_to_index(self, coords):
        return int(coords[0] // self.cellsize), int(coords[1] // self.cellsize)

    # враћа суседе честице са задатим координатама
    def neighbours(self, coords):
        location = self.coords_to_index(coords)
        for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
            node = self.cells[location[0] + dx][location[1] + dy].next
            while node is not None:
                yield node.id
                node = node.next

    # хендловање преласка честица између поља просторног хеша
    def move(self, id, new_coords):
        node = self.nodes.get(id)
        if node is None:
            node = Node(id)
            self.nodes[id] = node

        location = self.coords_to_index(new_coords)
        node.attach(self.cells[location[0]][location[1]])


class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

    def attach(self, start):
        if self.prev is not None:
            self.prev.next = self.next
            self.prev = None
        if self.next is not None:
            self.next.prev = self.prev
            self.next = None

        self.next = start.next
        if self.next:
            self.next.prev = self

        self.prev = start
        start.next = self
        pass

