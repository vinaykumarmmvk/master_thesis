<?php

// Php program for implementation of Heap Sort

// To heapify a subtree rooted with node i which is
// an index in arr[]. n is size of heap
function heapify(&$arr, $N, $i)
{
    $largest = $i; // Initialize largest as root
    $l = 2*$i + 1; // left = 2*i + 1
    $r = 2*$i + 2; // right = 2*i + 2

    // If left child is larger than root
    if ($l < $N && $arr[$l] > $arr[$largest])
        $largest = $l;

    // If right child is larger than largest so far
    if ($r < $N && $arr[$r] > $arr[$largest])
        $largest = $r;

    // If largest is not root
    if ($largest != $i)
    {
        $swap = $arr[$i];
        $arr[$i] = $arr[$largest];
        $arr[$largest] = $swap;

        // Recursively heapify the affected sub-tree
        heapify($arr, $N, $largest);
    }
}

// main function to do heap sort
function heapSort(&$arr, $N)
{
    // Build heap (rearrange array)
    for ($i = $N / 2 - 1; $i >= 0; $i--)
        heapify($arr, $N, $i);

    // One by one extract an element from heap
    for ($i = $N-1; $i > 0; $i--)
    {
        // Move current root to end
        $temp = $arr[0];
            $arr[0] = $arr[$i];
            $arr[$i] = $temp;

        // call max heapify on the reduced heap
        heapify($arr, $i, 0);
    }
}

/* A utility function to print array of size n */
function printArray(&$arr, $N)
{
    for ($i = 0; $i < $N; ++$i)
        echo ($arr[$i]." ") ; 
        
} 

    // Driver's program
    $arr = array(12, 11, 13, 5, 6, 7);
    $N = sizeof($arr)/sizeof($arr[0]);
    
    // Function call
    heapSort($arr, $N);

    echo 'Sorted array is ' . "\n";
    
    printArray($arr , $N);

// This code is contributed by Shivi_Aggarwal
?>