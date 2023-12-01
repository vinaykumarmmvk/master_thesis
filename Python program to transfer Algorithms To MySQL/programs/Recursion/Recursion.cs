// A C# program to demonstrate
// working of recursion
using System;

class GFG {

	// function to demonstrate
	// working of recursion
	static void printFun(int test)
	{
		if (test < 1)
			return;
		else {
			Console.Write(test + " ");

			// statement 2
			printFun(test - 1);

			Console.Write(test + " ");
			return;
		}
	}

	// Driver Code
	public static void Main(String[] args)
	{
		int test = 3;
		printFun(test);
	}
}

// This code is contributed by Anshul Aggarwal.
