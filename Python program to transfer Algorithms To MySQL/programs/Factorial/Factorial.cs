// C# code to implement factorial
using System;
class GFG {

// Factorial function
static int f(int n)
{
	// Stop condition
	if (n == 0 || n == 1)
	return 1;

	// Recursive condition
	else
	return n * f(n - 1);
}

// Driver code
static void Main()
{
	int n = 5;
	Console.WriteLine("factorial of " + n + " is: " + f(n));
}
}

// This code is contributed by divyeshrabadiya07.
