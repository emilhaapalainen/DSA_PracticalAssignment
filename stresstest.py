import hash_1
import time

'''
Hash table stress test. Reading a list of english words and placing them in the hash table. 
Then reading through a list of finnish words and looking through the hash table for matches.
'''

counter = 0
timer_start = time.time()

HT = hash_1.HashTable(10000) #Initializing the hash table. 10000 is the size of the table, however 100,000 seems to be the optimal size.
print("Running time for initializing the hash table: ", time.time() - timer_start)

with open('PA\words_alpha.txt') as file:
    for line in file:
        HT.insert(line.strip())

print("Running time for adding the words to the hash table: ", time.time() - timer_start)

with open('PA\kaikkisanat.txt') as file:
    for line in file:
        if HT.search(line.strip()) == True:
            counter += 1

print("Running time for searching matching words: ", time.time() - timer_start)

print("Number of matches: ", counter)
print()
