from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        # Step 2: Sort destinations in reverse order.
        # This allows us to use pop() to get the lexicographically smallest destination in O(1) time.
        for src in graph:
            graph[src].sort(reverse=True)
            
        itinerary = []
        
        # Step 3: Implement Hierholzer's algorithm via DFS
        def dfs(airport):
            # While there are valid outgoing flights from this airport
            while graph[airport]:
                next_destination = graph[airport].pop()
                dfs(next_destination)
            # Once we hit a dead end, append the airport to the itinerary
            itinerary.append(airport)
            
        # Start the traversal from JFK
        dfs("JFK")
        
        # Step 4: The itinerary is built backwards, so reverse it for the final result
        return itinerary[::-1]
