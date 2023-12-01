<script>
// JavaScript code to implement factorial

// Factorial function
function f(n)
{
// Stop condition
if(n == 0 || n == 1)
	return 1;
	
// Recursive condition
else
	return n*f(n-1);
}

// Initialize variable n.
let n = 5;
document.write("factorial of "+ n +" is: " + f(n));

// This code is contributed by probinsah.
</script>
