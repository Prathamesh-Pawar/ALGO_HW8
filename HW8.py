import re
import string
import math
import statistics
from collections import Counter



with open('alice.rtf', 'r') as file:
    alice = file.read()

class Node:    
    def __init__(self,value, next=None, key=None):
        self.value = value 
        self.next = next    
        self.key = key
        
class hash_node:
    def __init__(self,key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
       
class Linked_list:
    
    def __init__(self, head=None):
        self.head = head
        
    def display(self):
        node = self.head
        
        while node.next!=None:
            print(node.value)
            node = node.next
            
    def insert(self,key, value,Maxhash):
        
        node = self.head
    

        map_key  = get_hash_key(key , Maxhash)
        print(key,map_key)
        
        
        while(map_key>0):
            node = node.next
            map_key-=1
            
        
        node1 = node.key
        if node1.head==None:
            node1.head = hash_node(key,value)
        else:
            x = hash_node(key,value)
            x.next = node1.head 
            node1.head = x

            
    def delete(self, key_to_be_removed, Maxhash):
        
        node = self.head
        
        map_key  = get_hash_key(key , Maxhash)
        while(map_key>0):
            node = node.next
            map_key-=1
        
        node1 = node.key
        
        while node1.next!=None:
            if node1.next.key == key_to_be_removed:
                node1.next = node1.next.next
                break
            
            node = node.next

               
                
    def increase(self, key_to_increase, increment):
        
        node = self.head
        
        while node.next!=None:
            
            if node.key == key_to_increase:
                node.value +=increment
                break
                
            node = node.next
    
    
    def find_key(self, key_to_find):
        
        node = self.head
        
        while node!=None:
            
            node1 = node.key.head
            
            while node1!= None:
                
                if node1.key == key_to_find:
                    return node1
                node1 = node1.next
            node = node.next
                
    def list_all_keys(self):
        
        keys_dict={}
        node = self.head
        
        while node.next!=None:
            node1 = node.key.head
            
            while node1.next != None:
                
                keys_dict[node1.key] = node1.value
                
                print(node1.key,node1.value)
                
                node1 = node1.next
            node = node.next
        return keys_dict
    
    def get_collisions(self):
        x=[]
        node = self.head

        while node != None:
            c=0
            node1 = node.key.head
            while node1!=None:
                c+=1
                node1 = node1.next
            node = node.next
            x.append(c)
        
        return x
        

def clean_text(s):

        s = s.lower()
        s = re.sub(r'[\n\t]',' ',s)
        s = re.sub(r'[^A-Za-z ]', ' ',s)
        s = s.split()
        s = [i.strip() for i in s if i.strip()]
        
        return s
      
def get_ascii_addition(s): 
    x=0
    for n,i in enumerate(s):
        x+=(ord(i))^2+(3*n)^2-(int(n/35))^2
        
    return x
         
def get_hash_key(s, Maxhash):
    s = get_ascii_addition(s)
    s= math.floor(Maxhash*((s*0.6180339887)%1))
    return s
    
def create_hash_map(Maxhash):
    temp = None
    for i in reversed(list(range(Maxhash))):
        temp = Node(i,temp,Linked_list())

    hash_map = Linked_list(temp)
        
    return hash_map

    
def main():  
    Maxhash = 30
    x = clean_text(alice)
    x_dict = dict(Counter(x))
    hash_map = create_hash_map(Maxhash)

    for k, v in x_dict.items():
        hash_map.insert(k,v,Maxhash)

    print(statistics.variance(hash_map.get_collisions()))




if __name__=="__main__":
    main()