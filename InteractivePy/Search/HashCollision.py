'''
Collision - In hash function if two or more items need to be in the same slot
Collision Resolution - When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table

One method for resolving collisions looks into the hash table and tries to find another open slot to hold the item that caused the collision.
A simple way to do this is to start at the original hash value position and then move in a sequential manner through the slots until we encounter
the first slot that is empty. Note that we may need to go back to the first slot (circularly) to cover the entire hash table.
This collision resolution process is referred to as open addressing in that it tries to find the next open slot or address in the hash table.
By systematically visiting each slot one at a time, we are performing an open addressing technique called linear probing.
'''

__author__="Ganesh"

