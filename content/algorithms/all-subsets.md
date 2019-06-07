Title: Interview Question - Powerset
Date: 2018-01-01
Category: Algorithms
Tags: algorithms, coding, interview, set

Powerset (sometimes written as power set) means all the subsets of a given set. Find powerset of a given set is a common interview problem.

### Problem

Given a set of distinct numbers, $nums$, return all possible subsets(the powerset).

For example:

```
Input: nums = {1,2,3}
Output: 
{
    {},
    {1},
    {2},
    {3},
    {1,2},
    {1,3},
    {2,3},
    {1,2,3},
}
```

### Recursion

```java
public static <T> Set<Set<T>> powerSet(Set<T> originalSet) {
    Set<Set<T>> sets = new HashSet<Set<T>>();
    if (originalSet.isEmpty()) {
        sets.add(new HashSet<T>());
        return sets;
    }
    List<T> list = new ArrayList<T>(originalSet);
    T head = list.get(0);
    Set<T> rest = new HashSet<T>(list.subList(1, list.size())); 
    for (Set<T> set : powerSet(rest)) {
        Set<T> newSet = new HashSet<T>();
        newSet.add(head);
        newSet.addAll(set);
        sets.add(newSet);
        sets.add(set);
    }       
    return sets;
}  
```

### Bmi manipulation

```java
public static <T> Set<Set<T>> powerSetBit(Set<T> originalSet) {
	List<T> list = new ArrayList<T>(originalSet);
	int size = list.size();
	Set<Set<T>> results = new HashSet<>();
	for (int i=0; i < Math.pow(2, size); i++) {
		Set<T> set = new HashSet<>();
		for (int count=0; count < size; count++) {
			int bit = i >> count & 1;
			if (bit == 1) {
				set.add(list.get(count));
			}
		}
		results.add(set);
	}
	return results;
}
```
