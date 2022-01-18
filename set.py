class Set():
    def __init__(self, elements = []):
        self.elements = elements
    
    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)

    def delete(self, item):
        if item in self.elements:
            self.elements.remove(item)

    def pr(self):
        print(self.elements)

    def union(self, li = []):
        ans = self.elements
        for item in li:
            if item not in ans:
                ans.append(item)
        return ans

    def intersection(self, li = []):
        ans = []
        for item in li:
            if item in self.elements:
                ans.append(item)
        return ans
        

    def symmetric_difference(self, li = []):
        a = self.union(li)
        print(a)
        b = self.intersection(li)
        print(b)
        ans = a
        for item in b:
            ans.remove(item)
        return ans

    def copy(self):
        return self.elements.copy()
