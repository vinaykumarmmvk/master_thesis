<script>
	// Javascript program for implementation of Bogo sort
	
	// To check if array is sorted or not
	function isSorted(a, n){
		for(var i = 1; i < arr.length; i++)
			if (a[i] < a[i-1])
				return false;
		return true;
	}
	
	//swap function
	function swap(arr, xp, yp){
		var temp = arr[xp];
		arr[xp] = arr[yp];
		arr[yp] = temp;
	}
	
	// To generate permutation of the array
	function shuffle(a, n){
		var i, j=n;
		for (i=0; i < n; i++){
			var ind = Math.floor(Math.random() * n);
			swap(a, j-i-1, ind);
		}
		return a;
	}
	
	// Sorts array a[0..n-1] using Bogo sort
	function bogosort(a, n){
		// if array is not sorted then shuffle
		// the array again
		while (!isSorted(a, n))
			a = shuffle(a, n);
		return a;
	}
	
	// prints the array
	function printArray(arr, size){
		var i;
		for (i=0; i < size; i++)
			document.write(arr[i]+ " ");
		document.write("\n");
	}
	
	// Driver code
	var arr = [3, 2, 5, 1, 0, 4];
	var n = arr.length;
	arr = bogosort(arr, n);
	document.write("Sorted array: \n");
	printArray(arr, n);
	
	// This code is contributed by Susobhan Akhuli
</script>
