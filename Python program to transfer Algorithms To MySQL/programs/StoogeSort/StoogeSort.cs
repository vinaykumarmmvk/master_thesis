// C# program to implement stooge sort
using System;

class GFG {
	
	// Function to implement stooge sort
	static void stoogesort(int[] arr,
							int l, int h)
	{
		if (l >= h)
			return;

		// If first element is smaller
		// than last, swap them
		if (arr[l] > arr[h]) {
			int t = arr[l];
			arr[l] = arr[h];
			arr[h] = t;
		}

		// If there are more than 2
		// elements in the array
		if (h - l + 1 > 2) {
			int t = (h - l + 1) / 3;

			// Recursively sort first
			// 2/3 elements
			stoogesort(arr, l, h - t);

			// Recursively sort last
			// 2/3 elements
			stoogesort(arr, l + t, h);

			// Recursively sort first
			// 2/3 elements again to
			// confirm
			stoogesort(arr, l, h - t);
		}
	}

	// Driver Code
	public static void Main()
	{
		int[] arr = { 2, 4, 5, 3, 1 };
		int n = arr.Length;

		// Calling Stooge Sort function
		// to sort the array
		stoogesort(arr, 0, n - 1);

		// Display the sorted array
		for (int i = 0; i < n; i++)
			Console.Write(arr[i] + " ");
	}
}

// This code is contributed by Sam007.
