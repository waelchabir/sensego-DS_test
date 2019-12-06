Problem 1 : Warm up


There are zombies in Seattle. Liv and Ravi are trying to track them down to find out who is
creating new zombies in an effort to prevent an apocalypse. Other than the patient-zero
zombies, new people only become zombies after being scratched by an existing zombie.
Zombiism is transitive. This means that if zombie 0 knows zombie 1 and zombie 1 knows
zombie 2, then zombie 0 is connected to zombie 2 by way of knowing zombie 1. A zombie
cluster is a group of zombies who are directly or indirectly linked through the other zombies
they know, such as the one who scratched them or supplies who them with brains.
The diagram showing connectedness will be made up of a matrix of values 0 or 1. The value
matrix[i, j] indicates if the zombie i knows the zombie j. For example, in a world of 3 zombies the
complete matrix of zombie connectedness could be:
110
110
001
Zombies 0 and 1 know each other. Zombie 2 does not know anyone.
Question:
Your task is to determine the number of connected groups of zombies, or clusters, in a given matrix
square matrix of size n.
1) Write a function zombieCluster that compute this number without using any other library than the
standard ones. Typically you method should take as input a list of lists representing the matrix and
should output an integer.
We provide some examples in the file problem1_test.txt where you will find matrices and the
corresponding results your function should return. In addition if you are coding in python we
provide the script problem1_test.py that allows you to test your function by writing in it and then
running the script.
Constraints:
You may consider these constraints to prevent the function testing to use too much memory and
take too much time.
• 1 ≤ n ≤ 300
Examples :
Sample Input 0
1100
1110
0110
0001
Sample Output 0
2
In the diagram above, the squares highlighting a known connection between two different zombies
are highlighted in green. Because each zombie is already aware that they are personally a zombie,
those are highlighted in grey.
Explanation 0
We have 4 zombies numbered . There are 2 pairs of zombies who directly know each another: (0, 1)
and (1, 2). Because of zombiism's transitive property, the set of zombies {0, 1, 2} is considered to
be a single zombie cluster. The remaining zombie - 3 -, doesn't know any other zombies and is
considered to be his own, separate zombie cluster {3}. This gives us a total of 2 zombie clusters.
Sample Input 1
5
10000
01000
00100
00010
00001
Sample Output 1
5
Explanation 1
No zombie knows who any other zombie is, so they each form their own zombie cluster: {0}, {1},
{2}, {3}, and {4}. This means we have 5 zombie clusters, so we print 5 on a new line.
Question (bonus):
2) In mathematical terms what does zombieCluster do ? Do you already know one or more libraries
that can do that in the language you used ? Find a library that does that, and use it to write a test
function to show that you get the same results using your function and the one from the library.
