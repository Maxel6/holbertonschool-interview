#!/usr/bin/python3
def canUnlockAll(boxes):
    opened = set()
    keys = [0]
    
    while keys:
        key = keys.pop()
        
        if key not in opened:
            opened.add(key)
            keys.extend(boxes[key])
    
    return len(opened) == len(boxes)
