class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target: 
            return 0  # If the source is the same as the target, no travel is needed.
    
        # Map each stop to the list of buses (indices in the routes array) that go through it.
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)
        
        # Perform BFS from the source stop
        queue = deque([(source, 0)])  # Each element is a tuple (current_stop, num_buses_taken)
        visited_stops = {source}
        visited_buses = set()
        
        while queue:
            current_stop, num_buses_taken = queue.popleft()
            
            # Check all buses that go through the current stop
            for bus in stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue  # Skip if this bus has already been used
                visited_buses.add(bus)
                
                # Check all stops that this bus goes to
                for next_stop in routes[bus]:
                    if next_stop in visited_stops:
                        continue  # Skip if we've already visited this stop
                    
                    if next_stop == target:
                        return num_buses_taken + 1  # Found the target, return the number of buses taken
                    
                    visited_stops.add(next_stop)
                    queue.append((next_stop, num_buses_taken + 1))
        
        # If we exit the while loop, it means the target cannot be reached
        return -1