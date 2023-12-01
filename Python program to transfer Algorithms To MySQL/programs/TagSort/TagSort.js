// Javascript Program to illustrate Tag Sort. This code
// uses Bubble Sort to modify tag array according
// to salaries. We can use other optimized sorting
// techniques also.
class Person
{
	constructor(id,salary)
	{
		this.id = id;
		this.salary = salary;
	}

	getSalary()
	{
		return this.salary;
	}

	// @Override
	toString()
	{
		return "Person{"+"id=" + this.id +", salary=" + this.salary +'}';
	}
}


		// Creating objects and their original
		// order (in tag array)
		
		
		var n=5;
		var persons0 = new Person(0, 233.5);
		var persons1 = new Person(1, 23.0);
		var persons2 = new Person(2, 13.98);
		var persons3 = new Person(3, 143.2);
		var persons4 = new Person(4, 3.0);
		var persons=[persons0,persons1,persons2,persons3,persons4];


		var tag =[];
		for (var i = 0; i<n; i++){
			tag[i] = i;
		}
		// Every Person object is tagged to
		// an element in the tag array.
		
		console.log("Given Person and Tag");
		for (var i = 0; i<n; i++){
			console.log(persons[i] +" : Tag: "+ tag[i]);
		}
		// Modifying tag array so that we can access
		// persons in sorted order.
		tagSort(persons, tag);

		console.log("New Tag Array after"+
						"getting sorted as per Person[]");
		for (var i=0; i<n; i++)
			console.log(tag[i]);

		// Accessing persons in sorted (by salary)
		// way using modified tag array.
		for (var i = 0; i<n; i++)
			console.log(persons[tag[i]]);
	

	// Modifying tag array so that we can access
	// persons in sorted order of salary.
	function tagSort(persons,tag)
	{
		var n = persons.length;
		for (var i=0; i<n; i++)
		{
			for (var j=i+1; j<n; j++)
			{
				if (persons[tag[i]].getSalary() > persons[tag[j]].getSalary())
				{
					// Note we are not sorting the
					// actual Persons array, but only
					// the tag array
					var temp = tag[i];
					tag[i] = tag[j];
					tag[j] = temp;
				}
			}
		}
	}
