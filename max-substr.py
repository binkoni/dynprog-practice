import numpy as np
def max_substr(s):
  n = len(s)
  tot = np.zeros(shape=(n, n))
  max_len = 0
  for i in range(n):
    tot[i][i] = int(s[i]) # calculate length 1
  for l in range(2, n + 1):
    for i in range(0, n - l + 1):
      j = i + l - 1
      k = l // 2
      #print('n: %d, i: %d j: %d k: %d' % (n, i, j, k))
      tot[i][j] = tot[i][j - k] + tot[j - k + 1][j]
      if l % 2 == 0 and tot[i][j - k] == tot[j - k + 1][j] and l > max_len:
        max_len = l
  return max_len

print('142124: %d' % max_substr('142124'))
print('9430723: %d' % max_substr('9430723'))
