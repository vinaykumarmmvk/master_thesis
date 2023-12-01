<?php
// PHP program to implement
// iterative Binary Search

// An iterative binary search
// function
function binarySearch($arr, $l,
					$r, $x)
{
	while ($l <= $r)
	{
		$m = $l + ($r - $l) / 2;

		// Check if x is present at mid
		if ($arr[$m] == $x)
			return floor($m);

		// If x greater, ignore
		// left half
		if ($arr[$m] < $x)
			$l = $m + 1;

		// If x is smaller,
		// ignore right half
		else
			$r = $m - 1;
	}

	// If we reach here, then
	// element was not present
	return -1;
}

// Driver Code
$arr = array(2, 3, 4, 10, 40);
$n = count($arr);
$x = 10;
$result = binarySearch($arr, 0,
					$n - 1, $x);
if(($result == -1))
echo "Element is not present in array";
else
echo "Element is present at index ",
							$result;

// This code is contributed by anuj_67.
?>
