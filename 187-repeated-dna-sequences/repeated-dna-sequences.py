class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_length = 10
        if len(s) < sequence_length:
            return []

        seen_sequences = {}
        repeated_sequences = set()

        for i in range(len(s) - sequence_length + 1):
            substring = s[i:i + sequence_length]
            if substring in seen_sequences:
                repeated_sequences.add(substring)
            else:
                seen_sequences[substring] = 1

        return list(repeated_sequences)

            