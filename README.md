# TrainingTasks

***CountingSort***:

Comparison Sorting
Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).
Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
Example

All of the values are in the range , so create an array of zeros, . The results of each iteration follow:
i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]
The frequency array is . These values can be used to create the sorted array as well: .
Note
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.
Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.
Function Description
Complete the countingSort function in the editor below.
countingSort has the following parameter(s):
arr[n]: an array of integers
Returns
int[100]: a frequency array
Input Format
The first line contains an integer , the number of items in .
Each of the next  lines contains an integer  where .
Constraints



***Diagonal Difference***:

Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
Function description
Complete the  function in the editor below.
diagonalDifference takes the following parameter:
int arr[n][m]: an array of integers
Return
int: the absolute diagonal difference
Input Format
The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .
Constraints

Output Format
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.


***LonelyInteger***:

Given an array of integers, where all elements but one occur twice, find the unique element.
Example

The unique element is .
Function Description
Complete the lonelyinteger function in the editor below.
lonelyinteger has the following parameter(s):
int a[n]: an array of integers
Returns
int: the element that occurs only once
Input Format
The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .
Constraints

It is guaranteed that  is an odd number and that there is one unique element.
, where .



***TimeConversion***:

Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Example

Return '12:01:00'.

Return '00:01:00'.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
string s: a time in  hour format
Returns
string: the time in  hour format
Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).
Constraints
All input times are valid
Sample Input
07:05:45PM
Sample Output


***MiniMaxSum***:

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Example

The minimum sum is  and the maximum sum is . The function prints
16 24
Function Description
Complete the miniMaxSum function in the editor below.
miniMaxSum has the following parameter(s):
arr: an array of  integers
Print
Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
Input Format
A single line of five space-separated integers.
Constraints

Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
Sample Input
1 2 3 4 5
Sample Output
10 14
Explanation
The numbers are , , , , and . Calculate the following sums using four of the five integers:
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.
Need help to get started? Try the Solve Me First problem



***PlusMinus***:

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
0.400000
0.400000
0.200000
Function Description
Complete the plusMinus function in the editor below.
plusMinus has the following parameter(s):
int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
Input Format
The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .
Constraints


Output Format
Print the following  lines, each to  decimals:
proportion of positive values
proportion of negative values
proportion of zeros
Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output
0.500000
0.333333
0.166667
Explanation
There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive:  , negative:  and zeros:


***Tower Breakers ***

Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:
Initially there are  towers.
Each tower is of height .
The players move in alternating turns.
In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
If the current player is unable to make a move, they lose the game.
Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .
Example.   

There are  towers, each  units tall. Player  has a choice of two moves: 
- remove  pieces from a tower to leave  as  
- remove  pieces to leave 
Let Player  remove . Now the towers are  and  units tall.
Player  matches the move. Now the towers are both  units tall.
Now Player  has only one move.
Player  removes  pieces leaving . Towers are  and  units tall. 
Player  matches again. Towers are both  unit tall.
Player  has no move and loses. Return .
Function Description
Complete the towerBreakers function in the editor below.
towerBreakers has the following paramter(s):
int n: the number of towers
int m: the height of each tower
Returns
int: the winner of the game
Input Format
The first line contains a single integer , the number of test cases. 
Each of the next  lines describes a test case in the form of  space-separated integers,  and .
Constraints


Sample Input
STDIN   Function
-----   --------
2       t = 2
2 2     n = 2, m = 2
1 4     n = 1, m = 4
Sample Output
2
1
Explanation
We'll refer to player  as  and player  as 
In the first test case,  chooses one of the two towers and reduces it to . Then  reduces the remaining tower to a height of . As both towers now have height ,  cannot make a move so  is the winner.
In the second test case, there is only one tower of height .  can reduce it to a height of either  or .  chooses  as both players always choose optimally. Because  has no possible move,  wins.



***Caesar Cypher***

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example 
 

The alphabet is rotated by , matching the mapping above. The encrypted string is .
Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
Function Description
Complete the caesarCipher function in the editor below.
caesarCipher has the following parameter(s):
string s: cleartext
int k: the alphabet rotation factor
Returns
string: the encrypted string
Input Format
The first line contains the integer, , the length of the unencrypted string. 
The second line contains the unencrypted string, . 
The third line contains , the number of letters to rotate the alphabet by.
Constraints
 
 
 is a valid ASCII string without any spaces.
Sample Input
11
middle-Outz
2
Sample Output
okffng-Qwvb
Explanation
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b



*** Grid Challenge***

Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
Example 

The grid is illustrated below.
a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.
Function Description
Complete the gridChallenge function in the editor below.
gridChallenge has the following parameter(s):
string grid[n]: an array of strings
Returns
string: either YES or NO
Input Format
The first line contains , the number of testcases.
Each of the next  sets of lines are described as follows: 
- The first line contains , the number of rows and columns in the grid. 
- The next  lines contains a string of length 
Constraints
 
 
Each string consists of lowercase letters in the range ascii[a-z]
Output Format
For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.
Sample Input
STDIN   Function
-----   --------
1       t = 1
5       n = 5
ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
fghij
olmkn
trpqs
xywuv
Sample Output
YES
Explanation
The x grid in the  test case can be reordered to
abcde
fghij
klmno
pqrst
uvwxy
This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.


***Recursive Digit Sum***

We define super digit of an integer  using the following rules:
Given an integer, we need to find the super digit of the integer.
If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:
	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
Example 
 

The number  is created by concatenating the string   times so the initial .
    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of  sum to . The digits of  sum to .   is only one digit, so it is the super digit.
Function Description
Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.
superDigit has the following parameter(s):
string n: a string representation of an integer
int k: the times to concatenate  to make 
Returns
int: the super digit of  repeated  times
Input Format
The first line contains two space separated integers,  and .
Constraints


*** NEW Year Chaos ***


It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
Example

If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.

Person  had to bribe  people to get to the current position. Print Too chaotic.
Function Description
Complete the function minimumBribes in the editor below.
minimumBribes has the following parameter(s):
int q[n]: the positions of the people after all bribes
Returns
No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than people.
Input Format
The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows: 
- The first line contains an integer , the number of people in the queue 
- The second line has  space-separated integers describing the final state of the queue.
Constraints


Subtasks
For  score 
For  score 
Sample Input
STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]
Sample Output
3
Too chaotic
Explanation
Test Case 1
The initial state:
pic1(1).png
After person  moves one position ahead by bribing person :
pic2.png
Now person  moves another position ahead by bribing person :
pic3.png
And person  moves one position ahead by bribing person :
pic5.png
So the final state is  after three bribing operations.
Test Case 2
No person can bribe more than two people, yet it appears person has done so. It is not possible to achieve the input state.


*** Merge two sorted linked lists***

a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.
Example 
 refers to  
 refers to 
The new list is 
Function Description
Complete the mergeLists function in the editor below.
mergeLists has the following parameters:
SinglyLinkedListNode pointer headA: a reference to the head of a list
SinglyLinkedListNode pointer headB: a reference to the head of a list
Returns
SinglyLinkedListNode pointer: a reference to the head of the merged list
Input Format
The first line contains an integer , the number of test cases.
The format for each test case is as follows:
The first line contains an integer , the length of the first linked list. 
The next  lines contain an integer each, the elements of the linked list. 
The next line contains an integer , the length of the second linked list. 
The next  lines contain an integer each, the elements of the second linked list.
Constraints


, where  is the  element of the list.
Sample Input
1
3
1
2
3
2
3
4
Sample Output
1 2 3 3 4 
Explanation
The first linked list is: 
The second linked list is: 
Hence, the merged linked list is: 


***Queue using two stacks***


A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
A basic queue has the following operations:
Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following types:
1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format
The first line contains a single integer, , denoting the number of queries. 
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.
Constraints



It is guaranteed that a valid answer always exists for each query of type .
Output Format
For each query of type , print the value of the element at the front of the queue on a new line.
Sample Input
STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element
Sample Output
14
14
Explanation
Perform the following sequence of actions:
Enqueue ; .
Dequeue the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Enqueue ; .
Dequeue the value at the head of the queue, ; .
Dequeue the value at the head of the queue, ; 