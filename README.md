# DSA_PracticalAssignment
Data Structures and Algorithms course practical assignment. Implementing an open hashing algorithm.


Creating a hash table that uses open hashing in Python. Each slot of the hash table contains a linked structure where the data (keys) are stored. The hash system must include search, insert, and delete operations. The hash table must be able to store both integer (int) and string (str) values. That means that also all the operations/methods (search, insert, and delete) need to work with both data types. The size of the hash table is fixed. That means that after initializing the size of the table must stay the same.

The hashing algorithm and the table is then stress tested and evaluated. The algorithm is also compared to linear array operations.

1.1 Structure of the hash table

The implemented hash table uses linear probing to resolve the collision problem. The hash function calculates the hash table slot by changing the input string to an integer representing a Unicode character. Every slot of the table contains a linked list which prevents collisions from happening by appending new values to the end of the linked list. After the hash table is initialized, the size of the table stays the same for the whole duration of the execution. 

1.2 Hash function

The hashing function I uses the python function ‘ord()’ to converts each character in the input string to an integer representing the respective Unicode character. The values are added together and raised to the fourth power. Then we divide the value by the size of the hash table, and use the remainder as the index for the value.
The reason why we do this is so we can distribute the values across the table roughly evenly. If we didn’t do this, if a lot of similar values are inputted to the table, most of them will be placed at the beginning slots which results in very long linked lists. This affects the performance of the program massively.

1.3 Methods
The hashing table has the following methods:
- insert
- search
- delete
- print
- hash

The insert method is responsible for inserting data to the has table. The hash function is responsible for hashing the data before it is inserted in to the table in the insert function. The hash function converts fed data into an integer value and raises it to the power of 4. Then the value is divided by the size of the table, and the remainder is used as an index value to store the data in. 
The deletion function is rather self explanatory; The function gets the data that requires deletion as a parameter, and finds and deletes it from the table. After the data is deleted from the linked list, a temporary variable is used to point the previous node to the next node.
The search function loops through the list and looks for the data needs to be searched for. The wanted data is given as a parameter. The function returns True if it found the data, and False if it didn’t.
The print function traverses through the entire table and prints out each index which holds data, and their respective linked list.

2.1 Running time analysis of the hash table 
    • The running time for adding a new value to the hash table is Θ(1), because both the hash table data structure and the linked list have a running time of Θ(1) in the average case of insertion.
    • The running time for finding a new value in the has table is Θ(N), because searching through the linked list take Θ(N) time.
    • The running time for removing a value from the hash table is Θ(1), because both the hash table data structure and the linked list have a running time of Θ(1) in the average case of deletion.
   

3. The Pressure Test

  Table 1. Results of the pressure test.
  
  ![image](https://user-images.githubusercontent.com/47125778/210257260-48cd5c96-99f2-42ac-b348-0826c2dd9e68.png)

3.1 Comparison of the data structures

Adding the words from the file to the list was significantly faster than adding them to the hash table.  This is because the hashing function takes some time calculate the indexes where to store the data.
The search function was the complete opposite. Searching for the common words between the lists took roughly 3.5 seconds with the has table and a staggering 220 seconds when adding the words to a list instead of the hash table. This is because the location of the wanted value is generated based on the value. If we give the value again, the same hash is calculated as the one when inserting the value in the first place. This gives the location of the data almost immediately. When we’re adding the words to a list instead of the hash table, we have to search through the entire list to find the data we’re looking for.

3.2 Further improvements

The program gets significantly faster when we use a bigger size table. In the stress test, increasing the table size to 100,000 yielded much faster times for all of the operations. Increasing the size beyond that however, significantly slows down every operation. The reason this is happening, is because when we increase the size of the table, data gets distributed more evenly throughout the hash table, which in turn means less lengthy linked lists, which equals to less time searching through the lists.
