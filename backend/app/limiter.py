import time
from typing import Dict

class FixedWindowRateLimiter:
    # init with limit and window size in seconds
    def __init__(self, limit:int, window_size: int):
        self.limit = limit
        self.window_size = window_size
        # storage format: {user_id: {window_start_time: count}}
        self.storage: Dict[str, Dict[str, float]] = {}
    
    # check if request is allowed for given api_key
    def is_allowed(self, api_key: str) -> bool:
        current_time = time.time()

        # if api_key not in storage, initialize it
        if api_key not in self.storage:
            self.storage[api_key] = {
                "count": 1,
                "window_start": current_time
            }
            return True
        # get user data
        user_data = self.storage[api_key]

        # check if current window has expired - then reset
        if current_time - user_data["window_start"] > self.window_size:
            self.storage[api_key] = {
                "count": 1,
                "window_start": current_time
            }
            return True
        
        # if within window, check count
        if user_data["count"] < self.limit:
            user_data["count"] += 1
            return True
        
        return False

# this maintains a dictionary in memory to track counts for each key
# checks if the current time is within the window, if not it resets the count and window start time
# if within the window, it checks if the count is less than the limit, if so
# it increments the count and allows the request, otherwise it denies the request
