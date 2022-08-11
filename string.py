def longestSubstring(X, Y, m, n):
    maxLength = 0
    storeindex = m

    length_of_substring = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):


            if X[i - 1] == Y[j - 1]:
                length_of_substring[i][j] = length_of_substring[i - 1][j - 1] + 1

                if length_of_substring[i][j] > maxLength:
                    maxLength = length_of_substring[i][j]
                    storeindex = i

    return X[storeindex - maxLength: storeindex]


if __name__ == '__main__':
    str1 = 'practice'
    str2 = 'preactive'

    m = len(str1)
    n = len(str2)

    print('The longest substring i: ', longestSubstring(str1, str2, m, n))
