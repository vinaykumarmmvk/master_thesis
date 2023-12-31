<?php
// PHP Program for counting sort

$RANGE = 255;

// The main function that sort 
// the given string arr[] in
// alphabetical order
function countSort($arr)
{
    global $RANGE;
    
    // The output character array 
    // that will have sorted arr
    $output = array(strlen($arr));
    $len = strlen($arr);
    
    // Create a count array to 
    // store count of individual 
    // characters and initialize
    // count array as 0
    $count = array_fill(0, $RANGE + 1, 0);

    // Store count of 
    // each character
    for($i = 0; $i < $len; ++$i)
        ++$count[ord($arr[$i])];

    // Change count[i] so that 
    // count[i] now contains 
    // actual position of this
    // character in output array
    for ($i = 1; $i <= $RANGE; ++$i)
        $count[$i] += $count[$i - 1];

    // Build the output
    // character array
    // To make it stable we are operating 
    // in reverse order.
    for ($i = $len-1; $i >= 0 ; $i--)
    {
        $output[$count[ord($arr[$i])] - 1] = $arr[$i];
        --$count[ord($arr[$i])];
    }

    // Copy the output array to 
    // arr, so that arr now 
    // contains sorted characters
    for ($i = 0; $i < $len; ++$i)
        $arr[$i] = $output[$i];
return $arr;
}

// Driver Code
$arr = "geeksforgeeks"; //"applepp";

$arr = countSort($arr);

echo "Sorted character array is " . $arr;

// This code is contributed by mits
?>