import copy
import math

def problem1(matrix):
    sums = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == 0:
                sums.append([])
            if i == 0:
                sums[i].append(matrix[i][j])
            else:
                if j == len(matrix) - 1:
                    sums[i].append(matrix[i][j] + matrix[i - 1][j - 1])
                elif j == 0:
                    sums[i].append(matrix[i][j] + matrix[i - 1][j + 1])
                else:
                    sums[i].append(matrix[i][j] + min(matrix[i - 1][j - 1], matrix[i - 1][j + 1]))
    return min(sums[len(sums) - 1])

print(problem1([[1,2,3], [4,5,6], [7,8,9]]))

def problem2(word):
    subWords = []
    count = 0
    for i in range(len(word)):
        subWords.append([])
        if i == 0:
            subWords[0].append(word[0])
            count += 1
        else:
            for subWord in subWords[i - 1]:
                newWord = subWord + word[i]
                subWords[i].append(newWord)
                if len(newWord) % 2 == 0:
                    if list(reversed(newWord[:len(newWord) // 2])) == list(newWord[len(newWord) // 2:]):
                        count += 1
                else:
                    if list(reversed(newWord[:len(newWord) // 2])) == list(word[len(newWord) // 2 + 1:]):
                        count += 1
            subWords[i].append(word[i])
            count += 1
    return count

print()
print(problem2("abc"))
print(problem2("aaa"))

def problem3(sequence):
    sequences = []
    count = 0
    for i in range(len(sequence)):
        sequences.append([])
        if i == 0:
            sequences[0].append(sequence[:1])
        else:
            for subSequence in sequences[i - 1]:
                newSequence = subSequence + [sequence[i]]
                if len(newSequence) < 3:
                    sequences[i].append(newSequence)
                else:
                    if newSequence[1] - newSequence[0] == newSequence[-1] - newSequence[-2]:
                        sequences[i].append(newSequence)
                        count += 1
            sequences[i].append([sequence[i]])
    return count

print()
print(problem3([1,2,3,4]))
print(problem3([1,3,5,7,9]))

def problem5(pairs):
    if len(pairs) == 0:
        return 0
    if len(pairs) == 1:
        return 1
    lengths = []
    for i in range(len(pairs)):
        lengths.append([])
        for j in range(len(pairs)):
            if pairs[i][1] < pairs[j][0]:
                lengths[i].append(1)
            else:
                lengths[i].append(0)
    top = -math.inf
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if lengths[i][j] > 0:
                lengths[i][j] += max(lengths[j])
                top = max([top, lengths[i][j]])
    return top + 1

print()
print(problem5([[0, 1], [2, 3], [4, 5]]))
print(problem5([[1, 2], [2, 3], [3, 4]]))

def problem8(n):
    matrix = []
    squares = []
    for i in range(1, int(n ** .5) + 1):
        squares.append(i ** 2)
        matrix.append([])
        for j in range(1, int(n ** .5) + 1):
            matrix[-1].append(squares[-1] + (j ** 2))
    count = 0
    while n != 0:
        if n in squares:
            return count + 1
        tmp = -math.inf
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == n:
                    return count + 2
                elif n - matrix[i][j] in squares:
                    return count + 3
                if matrix[i][j] < n:
                    tmp = max([tmp, matrix[i][j]])
        count += 2
        n -= tmp
    return count

print()
print(problem8(12))
print(problem8(13))