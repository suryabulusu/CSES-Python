# CSES_Python
Solutions to some CSES questions in Python

CSES Problem Set : https://cses.fi/problemset

CSES Username : `stbv`

CSES Book : https://cses.fi/book/book.pdf [Excellent Material! :pray:]


1. I've written this code with a pedagogical perspective - learn algorithms. The code isn't meant to be fast or short. Most solutions above are accepted. 
2. Why **Python**? It's easy to translate ideas into code with Python. However it comes with a lot of caveats; *avoid* using Python if your target is competitive programming. 
3.  **Please consider trying a few more times before referring to this code.**
4.  More solutions will be added soon... 

### Some Insights
1. Python is terribly slow! You might get TLE despite using the right algorithm. CSES Hacking section has some great Pythonic solutions for these problems. However, you need to solve the question to access the Hacking Section. I typically try out the same algorithm in C++ and then check the Python solutions in Hacking section.
2. Use `PyPy3` for compilation
3. DFS with more than `10^4` node-depth fails in Python :sweat: `set_recursion_limit` saves you sometimes, but prefer using stack-based DFS code. I learned a lot of clean tricks to get Python algorithms run fast from [PyRival](https://github.com/cheran-senthil/PyRival). 
4. Do not sort tuples! (in Suffix Array algorithm, for example). It's very slow. Convert tuple `(a, b)` to `c = (a * m + b)` or similar variant, and retrieve using `c//m `, `c % m`. 
5. Always check the Hacking section - even after getting the solution right. There's a lot to learn from others' approaches. (Thanks, `zdu863` - [link](https://stackoverflow.com/questions/63329220/i-tried-solving-traffic-lights-problem-in-the-cses-problem-set-my-approach-seem/65035468#65035468)). 
6. Try out Python libraries like `heapq`, `bisect`, `re` etc. They'd probably throw a TLE, but it's good to know quick ways to solve problems. 
7. Sometimes, you end up getting all answers right except one => TLE. It could be an extra `len()` somwwhere, or a simple `max()`, leading to TLE. At times, it becomes very irritating to optimize Python code further. If your target is just to learn the algorithm and you are satisfied with the code written despite TLE - move on. No point in banging your head over an extra `len()` or an extra destructuring. (Yes, a simple destructure was the *sole* reason for TLE). 
8

