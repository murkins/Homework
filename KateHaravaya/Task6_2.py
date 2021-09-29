'''Task6_2. Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.'''

class LinkList:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def insertAfter(self, new):
        new.left = self
        new.right = self.right

        if new.left is not None:
            new.left.right = new

        if new.right is not None:
            new.right.left = new

    def removeNode(self):
        if self.left is not None:
            self.left.right = self.right

        if self.right is not None:
            self.right.left = self.left

def print_list(lst):
    values = []

    at = lst
    while at is not None:
        values.append(at.val)

        at = at.right

    stri = " ".join([str(val) for val in values])
    print(stri)

class HistoryDict:
    def __init__(self, d = dict()):
        self.d = d
        self.history_first = None

    def set_value(self, key, value):
        at_search = self.history_first

        found_node = None

        # searching for node with key equal to 'key' parameter
        while at_search is not None:
            if key == at_search.key:
                found_node = at_search
                break

            at_search = at_search.right

        # removing if node was found
        if found_node is not None:
            found_node.removeNode()
        else:
            found_node = LinkList(key)

        # adding found (or new) node into the beginning of the history
        found_node.right = self.history_first
        if self.history_first is not None:
            self.history_first.left = found_node

        # setting new node as first history
        self.history_first = found_node


    def get_history(self):
        res = []

        at = self.history_first
        counter = 0
        while (at is not None) and (counter < 10):

            res.append(at.key)

            counter += 1
            at = at.right

        return res


a = HistoryDict({"Dima": 25, "Kate": 24, "Vova": 13})
a.set_value("Vova", 12)
a.set_value("Kate", 23)
print(a.get_history())

