<script>
	// Javascript program to implement stooge sort
	
	// Function to implement stooge sort
	function stoogesort(arr, l, h)
	{
		if (l >= h)
			return;
	
		// If first element is smaller
		// than last, swap them
		if (arr[l] > arr[h]) {
			let t = arr[l];
			arr[l] = arr[h];
			arr[h] = t;
		}
	
		// If there are more than 2
		// elements in the array
		if (h - l + 1 > 2) {
			let t = parseInt((h - l + 1) / 3, 10);
	
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
	
	let arr = [ 2, 4, 5, 3, 1 ];
	let n = arr.length;

	// Calling Stooge Sort function
	// to sort the array
	stoogesort(arr, 0, n - 1);

	// Display the sorted array
	for (let i = 0; i < n; i++)
	document.write(arr[i] + " ");
	
</script>
