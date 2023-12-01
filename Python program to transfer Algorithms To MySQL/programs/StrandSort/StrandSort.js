// Javascript program to implement Strand Sort

// A recursive function to implement Strand sort.
// ip is input list of items (unsorted).
// op is output list of items (sorted)
function strandSort(ip)
{
	// Create a sorted sublist with
	// first item of input list as
	// first item of the sublist
	var sublist=[];
	sublist.push(ip[0]);
	ip.shift();
	
	
	// Traverse remaining items of ip list
	var len=ip.length-1;//last index of input list
	var len2=sublist.length-1;//last index of sublist
	
	var it =0;
	while(it<=len){

		// If current item of input list
		// is greater than last added item
		// to sublist, move current item
		// to sublist as sorted order is
		// maintained.
		if (ip[it] >sublist[len2]) {
			sublist.push(ip[it]);
			len2++;
			
			// splice(index,1) on list removes an
			// item and moves "it" to
			// next of removed item.
			
			ip.splice(it,1);
		
		}

		// Otherwise ignore current element
		else{
			it++;
		}
	}

// Merge current sublist into output
while(sublist.length>0 && op.length>0){
		if(sublist[0]>=op[0]){opp.push(op.shift());}
		else{opp.push(sublist.shift());}
	}
	if(sublist.length==0){
		opp=[...opp,...op];
	}
	if(op.length==0){
		opp=[...opp,...sublist];
	}
	op=[...opp];
	opp.length=0;
	
	// Recur for remaining items in input and current items in op.
	//Added base case
	if(ip.length>0){
	strandSort(ip);
	}
}

// Driver code

	var ip=[10, 5, 30, 40, 2, 4, 9];

	// To store sorted output list
	var op=[];
	//list helping in merge operation
	var opp=[];
	// Sorting the list
	strandSort(ip);
	
	// Printing the sorted list
		console.log(op);
