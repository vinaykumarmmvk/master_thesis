<?php
// PHP program to illustrate
// recursive approach to ternary search

// Function to perform Ternary Search
function ternarySearch($l, $r, $key, $ar)
{
	if ($r >= $l)
	{

		// Find the mid1 and mid2
		$mid1 = (int)($l + ($r - $l) / 3);
		$mid2 = (int)($r - ($r - $l) / 3);

		// Check if key is present at any mid
		if ($ar[$mid1] == $key)
		{
			return $mid1;
		}
		if ($ar[$mid2] == $key)
		{
			return $mid2;
		}

		// Since key is not present at mid,
		// check in which region it is present
		// then repeat the Search operation
		// in that region
		if ($key < $ar[$mid1])
		{

			// The key lies in between l and mid1
			return ternarySearch($l, $mid1 - 1,
									$key, $ar);
		}
		else if ($key > $ar[$mid2])
		{

			// The key lies in between mid2 and r
			return ternarySearch($mid2 + 1, $r,	
								$key, $ar);
		}
		else
		{

			// The key lies in between mid1 and mid2
			return ternarySearch($mid1 + 1, $mid2 - 1,
											$key, $ar);
		}
	}

	// Key not found
	return -1;
}

// Driver code

// Get the array
// Sort the array if not sorted
$ar = array( 1, 2, 3, 4, 5,
			6, 7, 8, 9, 10 );

// Starting index
$l = 0;

// end element index
$r = 9;

// Checking for 5

// Key to be searched in the array
$key = 5;

// Search the key using ternarySearch
$p = ternarySearch($l, $r, $key, $ar);

// Print the result
echo "Index of ", $key,
	" is ", (int)$p, "\n";

// Checking for 50

// Key to be searched in the array
$key = 50;

// Search the key using ternarySearch
$p = ternarySearch($l, $r, $key, $ar);

// Print the result
echo "Index of ", $key,
	" is ", (int)$p, "\n";

// This code is contributed by Arnab Kundu
?>
