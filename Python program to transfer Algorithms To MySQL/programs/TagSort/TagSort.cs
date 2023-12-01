using System;

public class Person
{
	private int id;
	private float salary;
	private Object someBigObject = new Object();

	public Person(int id, float salary)
	{
		this.id = id;
		this.salary = salary;
	}

	public float GetSalary()
	{
		return salary;
	}

	public override string ToString()
	{
		return "Person{" +
			"id=" + id +
			", salary=" + salary +
			", someBigObject=" + someBigObject +
			'}';
	}
}

public class MainClass
{
	public static void Main(string[] args)
	{
		// Creating objects and their original
		// order (in tag array)
		int n = 5;
		Person[] persons = new Person[n];
		persons[0] = new Person(0, 233.5f);
		persons[1] = new Person(1, 23f);
		persons[2] = new Person(2, 13.98f);
		persons[3] = new Person(3, 143.2f);
		persons[4] = new Person(4, 3f);
		int[] tag = new int[n];
		for (int i = 0; i < n; i++)
			tag[i] = i;

		// Every Person object is tagged to
		// an element in the tag array.
		Console.WriteLine("Given Person and Tag ");
		for (int i = 0; i < n; i++)
			Console.WriteLine(persons[i] +
							" : Tag: " + tag[i]);

		// Modifying tag array so that we can access
		// persons in sorted order.
		TagSort(persons, tag);

		Console.WriteLine("New Tag Array after " +
						"getting sorted as per Person[] ");
		for (int i=0; i<n; i++)
			Console.WriteLine(tag[i]);

		// Accessing persons in sorted (by salary)
		// way using modified tag array.
		for (int i = 0; i < n; i++)
			Console.WriteLine(persons[tag[i]]);
	}

	// Modifying tag array so that we can access
	// persons in sorted order of salary.
	public static void TagSort(Person[] persons, int[] tag)
	{
		int n = persons.Length;
		for (int i=0; i<n; i++)
		{
			for (int j=i+1; j<n; j++)
			{
				if (persons[tag[i]].GetSalary() >
						persons[tag[j]].GetSalary())
				{
					// Note we are not sorting the
					// actual Persons array, but only
					// the tag array
					int temp = tag[i];
					tag[i] = tag[j];
					tag[j] = temp;
				}
			}
		}
	}
}
