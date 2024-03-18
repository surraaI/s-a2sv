class Solution:
  def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    forbidden = set(forbidden)
    res, i, max_len = 0, 0, max(len(w) for w in forbidden)

    for j in range(len(word)):
      is_found = 0
      for k in range(1, max_len + 1):
        if j + 1 - k < i:
          break

        sub_word = word[j + 1 - k:j + 1]
        if sub_word in forbidden:
          is_found = len(sub_word)
          break

      if is_found:
        i = j + 2 - is_found
      else:
        res = max(res, j + 1 - i)

    return res