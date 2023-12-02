class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        EMPTY = ""
        ordinals = {ch: i for i, ch in enumerate(chain((EMPTY,), order))}

        def is_lexico(s1: str, s2: str) -> bool:
            pairs = zip_longest(s1, s2, fillvalue=EMPTY)
            ch1, ch2 = next(dropwhile(lambda chs: eq(*chs), pairs), (EMPTY, "z"))
            return ordinals[ch1] < ordinals[ch2]
        
        return all(starmap(is_lexico, pairwise(words)))
        