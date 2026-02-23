class History:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self._entries = []

    def add_entry(self, entry: str):
        if len(self._entries) >= self.max_size:
            self._entries.pop(0)
        self._entries.append(entry)

    def get_entries(self):
        return list(self._entries)

    def clear(self):
        self._entries = []