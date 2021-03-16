# Hash Tabble

class HashTable:
    def __init__(self, size):
        self.size = size
        self.lst = [-1 for _ in range(size)]
        
    def getHashKey(self, data):
        return hash(data)
    
    def getHashAddr(self, hashKey):
        return hashKey%self.size
    
    def saveData(self, key, data):
        hashKey = self.getHashKey(key)
        hashAddr = self.getHashAddr(hashKey)
        
        if self.lst[hashAddr] == -1:
            self.lst[hashAddr] = [[key, data]]
        else:
            for index in range(len(self.lst[hashAddr])):
                if self.lst[hashAddr][index][0] == key:
                    self.lst[hashAddr][index][1] = data
                    return
                    
            self.lst[hashAddr].append([key, data]) # 헷갈리지 말자
            
    def searchData(self, key):
        hashKey = self.getHashKey(key)
        hashAddr = self.getHashAddr(hashKey)
        print(hashAddr)
        print()
        for index in range(len(self.lst[hashAddr])):
            if self.lst[hashAddr][index][0] == key:
                return self.lst[hashAddr][index][1]
            
        return None
                    
                    
                    
        
hashTable = HashTable(10)
hashTable.saveData('BoxMinwoo1','천재다1')
hashTable.saveData('BoxMinwoo2','천재다2')
hashTable.saveData('BoxMinwoo3','천재다3')
hashTable.saveData('BoxMinwoo4','천재다4')
hashTable.saveData('BoxMinwoo5','천재다5')
hashTable.saveData('BoxMinwoo6','천재다6')
hashTable.saveData('BoxMinwoo7','천재다7')
hashTable.saveData('BoxMinwoo8','천재다8')
hashTable.saveData('BoxMinwoo9','천재다9')
hashTable.saveData('BoxMinwoo10','천재다11')
hashTable.saveData('BoxMinwoo11','천재다12')
hashTable.saveData('BoxMinwoo12','천재다13')
hashTable.saveData('BoxMinwoo13','천재다14')
hashTable.saveData('BoxMinwoo14','천재다15')
hashTable.saveData('BoxMinwoo15','천재다16')
hashTable.saveData('BoxMinwoo16','천재다17')

print(hashTable.searchData('BoxMinwoo12'))
        