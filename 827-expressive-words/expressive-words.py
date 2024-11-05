class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def group(word):
            return [(char, len(list(grp))) for char, grp in groupby(word)]
        
        s_groups = group(s)
        stretchy_count = 0

        for word in words:
            word_groups = group(word)

            if len(s_groups) != len(word_groups):
                continue 
            
            stretchy = True
            for (sc, sl), (wc, wl) in zip(s_groups, word_groups):
                if sc != wc or (sl < 3 and sl != wl) or (sl >= 3 and wl > sl):
                    stretchy = False
                    break

            if stretchy:
                stretchy_count += 1

        return stretchy_count