<script>

// JavaScript program to demonstrate working of
// recursion

function printFun(test)
	{
		if (test < 1)
			return;
		else {
			document.write(test + " ");
			printFun(test - 1); // statement 2
			document.write(test + " ");
			return;
		}
	}

// Driver code
	let test = 3;
	printFun(test);

</script>
