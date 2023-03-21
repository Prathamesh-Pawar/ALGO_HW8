import random

class Node:
    def __init__(self, key, level):
        self.key = key 
        self.forward = [None]*(level+1)
        
class SkipList:
    def __init__(self, max_level, probability):
        self.max_level = max_level
        self.probability = probability
        self.header = self.create_node(self.max_level, -1)
        self.level = 0
     
    def create_node(self, level, key):
        node = Node(key, level)
        return node
     
    def random_level(self):
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level
 
    def insert(self, key):
        update = [None]*(self.max_level+1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current == None or current.key != key:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level+1, new_level+1):
                    update[i] = self.header
                self.level = new_level
            node = self.create_node(new_level, key)
            for i in range(new_level+1):
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node
                
    def delete(self, search_key):
  
    
        update = [None]*(self.max_level+1)
        node = self.header
  
    
        for i in range(self.level, -1, -1):
            while(node.forward[i] and node.forward[i].key < search_key):
                node = node.forward[i]
            update[i] = node
  
   
        node = node.forward[0]
  
   
        if node != None and node.key == search_key:
  
        
            for i in range(self.level+1):
  
                if update[i].forward[i] != node:
                    break
                update[i].forward[i] = node.forward[i]
  
            while(self.level>0 and self.header.forward[self.level] == None):
                self.level -= 1
  
    def lookup(self, key): 
        node = self.header
  
        for i in range(self.level, -1, -1):
            while(node.forward[i] and\
                  node.forward[i].key < key):
                node = node.forward[i]
  
        node = node.forward[0]

        if node and node.key == key:
            print("The Skiplist has the value ", key)

 
    def display_list(self):
        print("Skip List")
        head = self.header
        for level in range(self.level+1):
            print("Level {}: ".format(level), end=" ")
            node = head.forward[level]
            while node != None:
                print(node.key, end=" ")
                node = node.forward[level]
            print("")



def main():
    skip_list = SkipList(3, 0.5)
    
    skip_list.display_list()


if __name__=="__main__":
    main()