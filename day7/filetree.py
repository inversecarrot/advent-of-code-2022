from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
from typing import List, Optional

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
    def __init__(self, commands: TextIOWrapper):
        self.root = DirectoryNode(NodeType.DIR, '/', None, [])
        next_command = commands.readline()
        cur = None
        while next_command != '\n':
            tokens = next_command.strip('\n').split(' ')
            print(tokens)
            if tokens[0] == '$':
                if tokens[1] == 'ls':
                    files = []
                    next_command = commands.readline()
                    while not next_command.startswith('$') and not next_command == '\n':
                        files.append(next_command)
                        next_command = commands.readline()
                    print(files)
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
        print(cur)