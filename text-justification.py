# coding=utf-8
# @Time: 3/12/2019 1:33 PM
from typing import List


class Solution:
    def fullJustify0(self, words: List[str], maxWidth: int) -> List[str]:
        start = end = 0
        result, curr_words_length = [], 0
        for i, word in enumerate(words):
            if len(word) + curr_words_length + end - start > maxWidth:
                if end - start == 1:
                    result.append(words[start] + ' ' * (maxWidth - curr_words_length))
                else:
                    total_space = maxWidth - curr_words_length
                    space, extra = divmod(total_space, end - start - 1)
                    for j in range(extra):
                        words[start + j] += ' '
                    result.append((' ' * space).join(words[start:end]))
                curr_words_length = 0
                start = end = i
            end += 1
            curr_words_length += len(word)
        result.append(' '.join(words[start:end]) + ' ' * (maxWidth - curr_words_length - (end - start - 1)))
        return result

    def fullJustify1(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
            def lineJustify(line, curWidth, start):
                i = start
                while i < length and curWidth + len(words[i]) + 1 <= maxWidth:
                    curWidth += len(words[i]) + 1
                    i += 1
                end = i
                l = end - start

                if end == length:
                    """取到末尾，最后一行"""
                    for i in range(start, length):
                        line += ' ' + words[i]
                    line += ' ' * (maxWidth - len(line))

                else:
                    space = maxWidth - curWidth
                    pSpace = space // l if l > 0 else 0
                    leftPadding = space - pSpace * l

                    for i in range(start, end):
                        padSpace = 1 if leftPadding > 0 else 0
                        line += (' ' * (pSpace + padSpace + 1)) + words[i]
                        leftPadding -= 1

                    if i == start:
                        line += ' ' * (maxWidth - len(line))

                ans.append(line)
                return end

            ans = []
            length = len(words)
            k = 0

            while k < length:
                k = lineJustify(words[k], len(words[k]), k + 1)

            return ans


print(Solution().fullJustify1(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                               "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
