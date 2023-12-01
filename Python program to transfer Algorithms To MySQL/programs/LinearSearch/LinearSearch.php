<?php
// PHP code for linearly search x in arr[].

function search($arr, $n, $x)
{
	for($i = 0; $i < $n; $i++) {
		if($arr[$i] == $x)
			return $i;
	}
	return -1;
}

// Driver Code
$arr = array(2, 3, 4, 10, 40);
$x = 10;

// Function call
$result = search($arr, sizeof($arr), $x);
if($result == -1)
	echo "Element is not present in array";
else
	echo "Element is present at index " ,
								$result;

// This code is contributed
// by jit_t
?>
