class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
    
        # Step 2: Set to track people who know the secret
        secret_holders = {0, firstPerson}
        
        # Step 3: Iterate through meetings and propagate the secret
        i = 0
        while i < len(meetings):
            # Collect all meetings happening at the same time
            time = meetings[i][2]
            batch = []
            
            while i < len(meetings) and meetings[i][2] == time:
                batch.append((meetings[i][0], meetings[i][1]))
                i += 1
                
            # Graph for this batch
            graph = defaultdict(list)
            for x, y in batch:
                graph[x].append(y)
                graph[y].append(x)
            
            # BFS to propagate the secret within the batch
            visited = set()
            for x, y in batch:
                if x in secret_holders or y in secret_holders:
                    queue = deque([x] if x in secret_holders else [y])
                    while queue:
                        person = queue.popleft()
                        if person not in visited:
                            visited.add(person)
                            secret_holders.add(person)
                            for neighbor in graph[person]:
                                if neighbor not in visited:
                                    queue.append(neighbor)
        
        # Return the list of all people who know the secret
        return list(secret_holders)


