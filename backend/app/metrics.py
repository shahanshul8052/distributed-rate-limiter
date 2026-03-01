from typing import Dict

class MetricsTracker:
    def __init__(self):
        # tracks total requests, blocked requests, and per-user request counts
        self.total_requests = 0
        self.blocked_requests = 0
        # per_user dictionary to track request counts for each API key
        self.per_user: Dict[str, int] = {}
    
    def record_request(self, api_key: str):
        self.total_requests += 1

        if api_key not in self.per_user:
            self.per_user[api_key] = 0
        
        self.per_user[api_key] += 1
    
    def record_blocked(self):
        self.blocked_requests += 1
    
    def get_metrics(self):
        return {
            "total_requests": self.total_requests,
            "blocked_requests": self.blocked_requests,
            "per_user": self.per_user
        }