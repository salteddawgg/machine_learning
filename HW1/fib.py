#Implement the function texttt{fibonacci(n)} in the code listing
#\ref{fib}.

#A Python 3 program to print out the first $n \geq 0$ Fibonacci numbers.}]
#def fibonacci(n):
    # implement me

#for t in fibonacci(50):
 #   print(t)

#Run your program for $n=50$. What are the last five numbers
#printed? Put your code in a file called \texttt{fibonacci.py}.



def fibonacci(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for t in fibonacci(50):
    print(t)