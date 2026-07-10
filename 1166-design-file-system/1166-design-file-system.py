class FileSystem:

    def __init__(self):
        self.paths = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.paths:
            return False
        
        last_slash_index = path.rfind("/")
        parent = path[:last_slash_index]

        if parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Solution: hashmap