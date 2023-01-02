import time
'''
Stress test. Reading a list of english words and placing them in the hash table. 
Then reading another list and looking through the hash table for matches.
'''
counter = 0
timer_start = time.time()
array = []

print("Running time for initializing the hash table: ", time.time() - timer_start)

with open('PA\words_alpha.txt') as file:
    for line in file:
        array.append(line.strip())

print("Running time for adding the words to the list: ", time.time() - timer_start)

with open('PA\kaikkisanat.txt') as file:
    for line in file:
        if line in array:
            counter += 1

print("Running time for searching matching words: ", time.time() - timer_start)

print("Number of matches: ", counter)

