class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        # Sort events by timestamp; OFFLINE before MESSAGE at same timestamp
        def sort_key(e):
            t = int(e[1])
            kind = 0 if e[0] == "OFFLINE" else 1
            return (t, kind)
        
        events.sort(key=sort_key)
        
        # offline_until[u] = time until which user u is offline (exclusive).
        # User u is offline at time t if t < offline_until[u].
        offline_until = [0] * numberOfUsers
        
        mentions = [0] * numberOfUsers
        
        for kind, ts, arg in events:
            t = int(ts)
            
            if kind == "OFFLINE":
                user_id = int(arg)
                # User goes offline at time t for 60 units: [t, t+60)
                offline_until[user_id] = t + 60
            
            else:  # MESSAGE
                tokens = arg.split()
                
                for token in tokens:
                    if token == "ALL":
                        # All users, regardless of online/offline
                        for u in range(numberOfUsers):
                            mentions[u] = (mentions[u] + 1) % MOD
                    
                    elif token == "HERE":
                        # Only users currently online
                        for u in range(numberOfUsers):
                            # online if current time >= offline_until[u]
                            if t >= offline_until[u]:
                                mentions[u] = (mentions[u] + 1) % MOD
                    
                    else:
                        # id<number> form
                        # e.g., "id3" -> 3
                        if token.startswith("id"):
                            uid = int(token[2:])
                            # id mentions count even if user is offline
                            mentions[uid] = (mentions[uid] + 1) % MOD
        
        return mentions
