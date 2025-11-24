from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        layer = [beginWord]
        found = False

        while layer and not found:
            next_layer = defaultdict(list)
            for word in layer:
                for i in range(len(word)):
                    prefix, suffix = word[:i], word[i+1:]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = prefix + ch + suffix
                        if new_word in wordSet:
                            if word not in next_layer[new_word]:
                                next_layer[new_word].append(word)
                            if new_word == endWord:
                                found = True

            visited = set(next_layer.keys())
            wordSet -= visited
            layer = list(next_layer.keys())

            for child, pars in next_layer.items():
                for p in pars:
                    if p not in parents[child]:
                        parents[child].append(p)

        if not found:
            return []

        results = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                results.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()

        backtrack(endWord)
        return results
