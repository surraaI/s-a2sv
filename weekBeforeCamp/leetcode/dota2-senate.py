class Solution:
        def predictPartyVictory(self, senate: str) -> str:
            r_positions = deque([i for i, s in enumerate(senate) if s == 'R'])
            d_positions = deque([i for i, s in enumerate(senate) if s == 'D'])
            next_position = len(senate)
            while r_positions and d_positions:
                if r_positions[0] < d_positions[0]:
                    r_positions.append(next_position)
                else:
                    d_positions.append(next_position)
                r_positions.popleft()
                d_positions.popleft()
                next_position += 1
            return 'Radiant' if r_positions else 'Dire'