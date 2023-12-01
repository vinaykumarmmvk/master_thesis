<script>

// Javascript Program to implement Gnome Sort

function gnomeSort(arr, n)
	{
		let index = 0;
	
		while (index < n) {
			if (index == 0)
				index++;
			if (arr[index] >= arr[index - 1])
				index++;
			else {
				let temp = 0;
				temp = arr[index];
				arr[index] = arr[index - 1];
				arr[index - 1] = temp;
				index--;
			}
		}
		return;
	}

// Driver Code
	
		let arr = [34, 2, 10, -9 ];
	
		gnomeSort(arr, arr.length);
	
		document.write("Sorted sequence after applying Gnome sort: ");
		document.write(arr.toString());
			
</script>
