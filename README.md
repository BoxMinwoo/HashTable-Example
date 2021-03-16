## HashTable-Example
- HashTable을 최대한 쉽게 이해하기 위한 샘플 프로그램입니다
- Python3로 작성되었습니다.
***
![image](https://user-images.githubusercontent.com/72640840/111261128-4d33ee80-8665-11eb-8386-c3eec9dc2dcf.png)
- 해시는 다지고 섞어 만든 함박스테이크와 같습니다

![image](https://user-images.githubusercontent.com/72640840/111261209-6dfc4400-8665-11eb-84ef-d3b1f4d9be7f.png)
- 특정 데이터를 갈아버리고 Key를 만드는 과정이 있기 때문에 Hash라는 단어를 선택한 것으로 추정 됩니다
- 갈려버린 값(0x7a854n…)은 Hash Key 값으로 사용되며, 거의 유일한 값을 가지게 됩니다.

***
## HashTable이 필요한 이유
HashTable이 아닌 일반적인 테이블을 만들어 본다면
![image](https://user-images.githubusercontent.com/72640840/111261791-61c4b680-8666-11eb-91bb-49284f9f5aa7.png)
- Key 하나에 Data 하나가 매칭돼 있는 테이블입니다.
- "너이"를 찾기 위해서는 아래와 같은 과정이 필요합니다.

![image](https://user-images.githubusercontent.com/72640840/111261895-86b92980-8666-11eb-9e20-4c0f12eb3225.png)
- 앞에서부터 4번을 visit 해야 합니다


![image](https://user-images.githubusercontent.com/72640840/111261947-a4868e80-8666-11eb-9f26-f4559156177a.png)
- "무한2"를 찾기 위해서는 9조번의 연산을 수행 해야합니다

## 소스
```python
lst = list(0 for i in range(10)) # 배열 10개를 만듬
lst[0] = "one"
lst[1] = "two"
lst[2] = "three"
lst[3] = "four"
lst[4] = "five"
lst[5] = "six"
lst[6] = "seven"
lst[7] = "eight"
lst[8] = "nine"
lst[9] = "ten"

for i in range(len(lst)):
    if lst[i] == "eight":
        print("{0}번만에 찾았습니다.".format(i+1))
```
- 시간 복잡도는 O(n) 입니다.

## 해쉬테이블 적용
```python
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
                    
            self.lst[hashAddr].append([key, data])
            
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
hashTable.saveData('곽민우1','천재다1')
hashTable.saveData('곽민우2','천재다2')
hashTable.saveData('곽민우3','천재다3')
hashTable.saveData('곽민우4','천재다4')
hashTable.saveData('곽민우5','천재다5')
hashTable.saveData('곽민우6','천재다6')
hashTable.saveData('곽민우7','천재다7')
hashTable.saveData('곽민우8','천재다8')
hashTable.saveData('곽민우9','천재다9')
hashTable.saveData('곽민우10','천재다11')
hashTable.saveData('곽민우11','천재다12')
hashTable.saveData('곽민우12','천재다13')
hashTable.saveData('곽민우13','천재다14')
hashTable.saveData('곽민우14','천재다15')
hashTable.saveData('곽민우15','천재다16')
hashTable.saveData('곽민우16','천재다17')

print(hashTable.searchData('곽민우13'))
```

다음 시간에 계속
