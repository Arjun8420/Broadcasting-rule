# Broadcasting-rule
The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.

Broadcasting two arrays together follow these rules:
 
1. If the arrays don’t have the same rank then prepend the shape of the lower rank array with 1s until both shapes have the same length.
2. The two arrays are compatible in a dimension if they have the same size in the dimension or if one of the arrays has size 1 in that dimension.
3. The arrays can be broadcast together if they are compatible with all dimensions.
4. After broadcasting, each array behaves as if it had shape equal to the element-wise maximum of shapes of the two input arrays.
5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension.

  
