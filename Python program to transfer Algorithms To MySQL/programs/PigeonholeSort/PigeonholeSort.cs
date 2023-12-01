// C# program to implement
// Pigeonhole Sort
using System;

class GFG
{
public static void pigeonhole_sort(int []arr,
								int n)
{
	int min = arr[0];
	int max = arr[0];
	int range, i, j, index;

	for(int a = 0; a < n; a++)
	{
		if(arr[a] > max)
			max = arr[a];
		if(arr[a] < min)
			min = arr[a];
	}

	range = max - min + 1;
	int[] phole = new int[range];
	
	for(i = 0; i < n; i++)
	phole[i] = 0;

	for(i = 0; i < n; i++)
		phole[arr[i] - min]++;

	
	index = 0;

	for(j = 0; j < range; j++)
		while(phole[j] --> 0)
			arr[index++] = j + min;

}

// Driver Code
static void Main()
{
	int[] arr = {8, 3, 2, 7,
				4, 6, 8};

	Console.Write("Sorted order is : ");

	pigeonhole_sort(arr,arr.Length);
	
	for(int i = 0 ; i < arr.Length ; i++)
		Console.Write(arr[i] + " ");
}
}

// This code is contributed
// by Sam007
