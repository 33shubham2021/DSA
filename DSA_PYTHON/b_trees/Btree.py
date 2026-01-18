class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                      # Minimum degree (defines range of keys)
                                        # Max keys = 2t-1 , Max Children = 2t
                                        # Min keys(non root) = t-1 , Min Children = t
                                        
        self.leaf = leaf                # Is leaf node
        self.keys = []                  # Keys stored in increasing order
        self.children = []              # Child pointers, len = len(keys) + 1


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    # -------- SEARCH --------
    def search(self, k, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == k:
            return node, i

        if node.leaf:
            return None

        return self.search(k, node.children[i])

    # -------- INSERT --------
    def insert(self, k):
        root = self.root

        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    # -------- SPLIT --------
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, leaf=y.leaf)

        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)

        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    # -------- DISPLAY --------
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Level", level, ":", node.keys)
        level += 1

        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level)
