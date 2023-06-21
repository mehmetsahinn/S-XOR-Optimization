In accordance with the format given in the assignment file of the matrices to the sample.txt file by the user.
(how many matrices will be given in the first row, the size of the given matrix is ​​specified before the matrix, the data of the matrices
with one space between each.) is loaded into the file. Desired number and size of matrix
may contain. The algorithm is dynamically designed to suit this. Characters from the file
spaces are taken into a list as separate elements by reference. Each matrix from the list
It is made into a dictionary structure with a key and its elements as its own value. later
Xor circuits are created from the value values ​​and the created circuits are calculated as the value of each matrix.
It becomes a dictionary structure. Afterwards, the values ​​read through this structure are "y0,y1 ..." inside the circuits.
Values ​​such as "x0,x1..." are collected in a multidimensional array by making assignments. These added equations are entered into multiple
It is collected in a dynamic array to look at each matrix according to the matrix variables. This is obtained
how many times the pairs pass in the circuits by selecting all the pairs from the equations (y0,y1 ...)
being looked after. Then, among the selected pairs, let it be "x1-x3", the left element will remain constant.
Is there any other binary that starts with the element on the right? Elements of the algorithm like "x3-x14" or "x3-x7"
finds it and after finding it continues the same process with x7 or x14. Elements like "x1,x3,x7" obtained
It tries to obtain that circuit by throwing it into an array, looking at the contents of such arrays as "y0= x1,x3,x6,x7,x9,x10".
After the tracking process is finished, whether the elements in "x1,x3 and x7" have other values, such as "x1-x14".
 trying to get "y0" by looking at it. This ongoing algorithm looks at all the binaries and the Path example for each "y"
taking it out. These instances are thrown into a certain array and processed again. All obtained in this process
If paths such as 6 paths for "y0" and 4 paths for "y1" are removed from the equations, the algorithm will continue until "y15".
It looks at the number of similar pairs between them before creating the general circuit by choosing 1 path from an equation y.
Among these selected y equations, MINIMUM XOR gate, that is, paths with the most similar elements
and prints the GENERAL CIRCUIT EQUATIONS to an array like "x3 = x3^x7". If the last circuit occurred there
Typing "x9 = x9^x13 y11" indicates that the equation has been formed. This way for example 64 XOR when we look straight
GENERAL CIRCUIT to use 45 XOR gates, thanks to the S-XOR optimization algorithm.
An obtained optimization is provided and presented to the user by printing it to the result.txt file.

First, we take our circuit, which we print to result.txt, and process it and throw it into arrays in binary groups.
Then we can use our previous equations such as y0,y1 ...
we call our array of "equations" holding The multidimensional array here contains the equations of all 3 matrices.
From here, values ​​such as y0,y1 of each matrix are taken one by one and S-XOR optimization is performed.
We check the correctness of the circuit we created. Here the code stops the moment each instance sees "y1" and
trying to construct "y1" by looking at previous data. This algorithm
in this way, it checks the values ​​on the circuit made with S-XOR for each y value of the matrix.
While doing this, in each verification two equations, "Circuit Y" and "Matrix Y"
We present it to the user to show that they are the same. If all Y value is found ie "checkCount=16"
If "Matrix 1 OK !" S-XOR Optimization by giving feedback
We prove the correctness of the circuit created with Although all entered matrices are validated
 ("finCheck = number of all matrices") gives the user that all matrices have been verified and the code is successful
We give feedback.

