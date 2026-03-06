Architecture Notes: Comparing Python and x86-64

I chose to analyze the sum_to_n function.

1. Code Length Comparison

In Python, the function is very short, only about 4-5 lines. 
However, in assembly, the loop body alone takes 5 instructions to do the same job. 
This shows that a single line of Python actually requires multiple low-level CPU steps to execute.

2. How the Loop Works

The Python for loop handles everything for us. 
In assembly, it’s much more manual. I had to use cmp to compare my counter with the limit and then use jg (jump if greater) to decide when to stop the loop. 

3. Register Roles in my Assembly Code
I used specific registers to keep track of the data: 

-Loop counter: I used `rbx` to act as `i` in my loop. 
-Accumulated result: I used `rax` to store the total sum as it grows.
-Target number:`rcx` was used to hold the value of `n`. 

4. Step-by-Step Execution
When I stepped through the code in the playground, I noticed it takes exactly 5 instructions (`add`, `inc`, `cmp`, `jg`, `jmp`) to complete just one single round of the loop. 