class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.size = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def parent_dirs(self, dir: str):
        # construct the parent directories
        node = self.root
        if dir not in node.children:
            new_node = TrieNode()
            node.children[dir] = new_node

    def display(
        self,
    ):
        for k, v in self.root.children.items():
            print(k, v.size, v.children)

    def parse_dirs(self, parent_dir: str, child_dir: str, file_size: int):
        # construct the directory structure
        # check if its a file or a child dir
        # if file, add it to size else construct a child node

        node = self.root

        parent_node = node.children[parent_dir]
        if isinstance(child_dir, str) and not file_size:
            if child_dir not in parent_node.children:
                child_node = TrieNode()
                parent_node.children[child_dir] = child_node
        elif isinstance(file_size, int):
            parent_node.size += file_size
            for k, v in parent_node.children.items():
                if k == child_dir:
                    v.size += file_size
        else:
            pass
