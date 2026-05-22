class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_to_index = {word: i for i, word in enumerate(words)}
        pairs = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]
                
                # Case 1: If left is a palindrome, look for reverse of right to prepend
                if left == left[::-1]:
                    reversed_right = right[::-1]
                    if reversed_right in word_to_index and word_to_index[reversed_right] != i:
                        pairs.append([word_to_index[reversed_right], i])
                
                # Case 2: If right is a palindrome, look for reverse of left to append.
                # Adding 'and right' ensures we don't duplicate work when right is empty.
                if right and right == right[::-1]:
                    reversed_left = left[::-1]
                    if reversed_left in word_to_index and word_to_index[reversed_left] != i:
                        pairs.append([i, word_to_index[reversed_left]])
                        
        return pairs
