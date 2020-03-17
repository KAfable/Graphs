from util import Queue
f = open('words.txt', 'r')
words = f.read().lower().split("\n")
# Step 2: Build the Graph

# Step 3: Traverse the Graph


def word_ladder(self, begin_word, end_word):
    '''
    Return a list of words containing the least amount of changes from begin_word to end_word.
    '''

    q = Queue()
    q.enqueue([begin_word])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        word = path[-1]
        if word == end_word:
            return path
        if word not in visited:
            for neighbor in get_neighbors():
                q.enqueue([*path, neighbor])
