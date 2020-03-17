from util import Queue
f = open('words.txt', 'r')
words = f.read().lower().split("\n")
f.close()

# Step 2: Build the Graph
# Create an equality functions


def words_are_neighbors(w1, w2):
    ''' Return boolean whether or not words are one letter apart '''
    list_word = list(w1)
    for i in range(len(list_word)):
        for letter in 'abcdefghijklmnopqrstuvwyz':
            temp_word = list_word.copy()
            temp_word[i] = letter
            if "".join(temp_word) == w2:
                return True
    return False


def words_are_neighbors2(word1, word2):
    for i in range(len(word1)):
        list_word1 = list(word1)
        list_word2 = list(word2)
        list_word1.pop(i)
        list_word2.pop(i)
        if list_word1 == list_word2:
            return True
    return False

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
