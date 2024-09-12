from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
from typing import Dict, List, Optional

class NodeType(Enum):
    DIR = 0
    FILE = 1

@dataclass
class Node:
    type: NodeType
    name: str
    parent: Optional[Node]

@dataclass
class DirectoryNode(Node):
    children: List[Node]

@dataclass
class FileNode(Node):
    size: int


class FileTree:
    root: Node
    dir_sizes: Dict[str, int]
    def __init__(self, commands: TextIOWrapper):
        self.root = DirectoryNode(NodeType.DIR, '/', None, [])
        self.dir_sizes = {}
        next_command = commands.readline()
        cur = None
        while next_command:
            tokens = next_command.strip('\n').split(' ')
            if tokens[0] == '$':
                if tokens[1] == 'ls':
                    files = []
                    next_command = commands.readline()
                    while not next_command.startswith('$') and next_command:
                        files.append(next_command)
                        next_command = commands.readline()
                    nodes = []
                    for file in files:
                        file_tokens = file.strip('\n').split(' ')
                        if (file_tokens[0] == 'dir'):
                            nodes.append(DirectoryNode(NodeType.DIR, file_tokens[1], cur, []))
                        else:
                            nodes.append(FileNode(NodeType.FILE, file_tokens[1], cur, file_tokens[0]))
                    cur.children = nodes
                elif tokens[1] == 'cd':
                    if tokens[2] == '/':
                        cur = self.root
                        next_command = commands.readline()
                    elif tokens[2] == '..':
                        cur = cur.parent
                        next_command = commands.readline()
                    else:
                        # directory name
                        next_node = next((node for node in cur.children if node.name == tokens[2]))
                        cur = next_node
                        next_command = commands.readline()
        self._compute_directory_sizes(self.root)


    def get_sum_of_large_directories(self):
        return self._get_sum_of_large_directories(self.root)[1]

    def _get_sum_of_large_directories(self, cur: Node):
        if cur.type == NodeType.FILE:
            return (int(cur.size), 0)
        else:
            child_sizes = [self._get_sum_of_large_directories(node) for node in cur.children]
            size = 0
            sum = 0
            for (child_size, child_sum) in child_sizes:
                size += child_size
                sum += child_sum
            if size <= 100000:
                sum += size
            return (size, sum)


    def print_tree(self):
        self._print_node(self.root, 0)

    def _print_node(self, node: Node, depth: int):
        node_string = ''
        for _ in range(0, depth):
            node_string += '    '
        node_string += f'- {node.name} ({node.type}'
        if node.type == NodeType.FILE:
            node_string += f', size={node.size})'
            print(node_string)
        else:
            print(node_string + ')')
            for child in node.children:
                self._print_node(child, depth + 1)

    def get_smallest_big_directory(self, total_space: int, free_space: int):
        current_space = total_space - self.dir_sizes[self.root.name]
        min_size = free_space - current_space
        smallest_dir = self.dir_sizes[self.root.name]
        for val in self.dir_sizes.values():
            if val >= min_size and val < smallest_dir:
                smallest_dir = val
        return smallest_dir
    
    def _compute_directory_sizes(self, node: Node) -> int:
        if node.type == NodeType.FILE:
            return int(node.size)
        else:
            size = 0
            for child in node.children:
                size += self._compute_directory_sizes(child)
            self.dir_sizes[node.name] = size
            return size


        
        