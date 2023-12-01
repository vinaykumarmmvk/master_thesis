// C# Program to implement
// Odd-Even / Brick Sort
using System;

class GFG
{
	public static void oddEvenSort(int []arr, int n)
	{
		// Initially array is unsorted
		bool isSorted = false;

		while (!isSorted)
		{
			isSorted = true;
			int temp =0;

			// Perform Bubble sort on
			// odd indexed element
			for (int i = 1; i <= n - 2; i = i + 2)
			{
				if (arr[i] > arr[i+1])
				{
					temp = arr[i];
					arr[i] = arr[i+1];
					arr[i+1] = temp;
					isSorted = false;
				}
			}

			// Perform Bubble sort on
			// even indexed element
			for (int i = 0; i <= n - 2; i = i + 2)
			{
				if (arr[i] > arr[i+1])
				{
					temp = arr[i];
					arr[i] = arr[i+1];
					arr[i+1] = temp;
					isSorted = false;
				}
			}
		}
		return;
	}
	
	// Driver code
	public static void Main ()
	{
		int []arr = {34, 2, 10, -9};
		int n = arr.Length;
		
		// Function calling
		oddEvenSort(arr, n);
		for (int i = 0; i < n; i++)
			Console.Write(arr[i] + " ");

		Console.WriteLine(" ");
	}
}

// This code is contributed by Sam007
