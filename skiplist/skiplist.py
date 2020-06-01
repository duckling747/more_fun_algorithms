#!/usr/bin/env python3

import random

class Skiplist:

    class Node:
        def __init__(self, key, level, value):
            self.value = value
            self.key = key
            self.forward = [None] * (level + 1)
            

    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self.Node(-1, max_level, -1)
        self.level = 0
    
    def search(self, search_key):
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i].key < search_key:
                x = x.forward[i]
        x = x.forward[1]
        if x.key == search_key:
            return x.value
        else:
            return False


    def insert(self, search_key, new_value):
        update = [None] * (self.max_level+1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].key < search_key:
                x = x.forward[i]
            update[i] = x
        x = x.forward[0]
        if x != None and x.key == search_key:
            x.value = new_value
        else:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            x = self.Node(search_key, new_level, new_value)
            for i in range(new_level + 1):
                x.forward[i] = update[i].forward[i]
                update[i].forward[i] = x
                
                
    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
        
        
    def print_me(self):
        print("Skip list:")
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end = " ")
            node = head.forward[lvl]
            while node != None:
                print("{} -> {}".format(node.key, node.value), end = " ")
                node = node.forward[lvl]
            print()
        
        
lista = Skiplist(3, 0.5)
lista.insert(3, 1)
lista.insert(6, 2)
lista.insert(7, 3)
lista.insert(9, 4)
lista.insert(12, 5)
lista.insert(19, 6)
lista.insert(17, 7)
lista.insert(26, 8)
lista.insert(21, 9)
lista.insert(25, 10)
lista.print_me()






