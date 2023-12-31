<?php
// PHP implementation of Radix Sort


// A function to do counting sort of arr[]
// according to the digit represented by exp.
function countSort(&$arr, $n, $exp)
{
	$output = array_fill(0, $n, 0); // output array
	$count = array_fill(0, 10, 0);

	// Store count of occurrences in count[]
	for ($i = 0; $i < $n; $i++)
		$count[ ($arr[$i] / $exp) % 10 ]++;

	// Change count[i] so that count[i]
	// now contains actual position of
	// this digit in output[]
	for ($i = 1; $i < 10; $i++)
		$count[$i] += $count[$i - 1];

	// Build the output array
	for ($i = $n - 1; $i >= 0; $i--)
	{
		$output[$count[ ($arr[$i] /
						$exp) % 10 ] - 1] = $arr[$i];
		$count[ ($arr[$i] / $exp) % 10 ]--;
	}

	// Copy the output array to arr[], so
	// that arr[] now contains sorted numbers
	// according to current digit
	for ($i = 0; $i < $n; $i++)
		$arr[$i] = $output[$i];
}

// The main function to that sorts arr[]
// of size n using Radix Sort
function radixsort(&$arr, $n)
{
	
	// Find the maximum number to know
	// number of digits
	$m = max($arr);

	// Do counting sort for every digit. Note
	// that instead of passing digit number,
	// exp is passed. exp is 10^i where i is
	// current digit number
	for ($exp = 1; $m / $exp > 0; $exp *= 10)
		countSort($arr, $n, $exp);
}

// A utility function to print an array
function PrintArray(&$arr,$n)
{
	for ($i = 0; $i < $n; $i++)
		echo $arr[$i] . " ";
}

// Driver Code
$arr = array(170, 45, 75, 90, 802, 24, 2, 66);
$n = count($arr);

// Function Call
radixsort($arr, $n);
PrintArray($arr, $n);

// This code is contributed by rathbhupendra
?>
