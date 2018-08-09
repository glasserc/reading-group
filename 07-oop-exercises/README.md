1. Define a Person class. A person is made up of a name and an
age. Implement a birthday() operation that prints a cheerful message
for the person and updates their age.

2. Actually, that's a pretty silly way to do ages. Define a second
Person class. Objects of this class should store their name and a
birthday. A birthday is a Python
[datetime](https://docs.python.org/2/library/datetime.html). Define an
age(t) method that figures out how old the user was at the given
time. This is better because you don't need to ever worry about
updating the object, or of updating it too many times, so that's one
less thing to forget about.

2b. Make the time be an optional parameter. If it isn't given, you
should get whatever the current time is and use that.

3. Define a LinkedList class. It should be made up of Nodes. Each node
should point to the next node (or None, if it's the last link). Your
linked list class should support at least these operations:

- get_at(n)  # which is the same as lst[n] in a regular list
- append(x)
- insert(i, x), or insert(x) (in which case i = 0).

4. Let's say we were designing a zoo video game. What are some of the
classes you might define for it? What operations would they support?
What about the animals? How would their class hierarchies look?

5. Look up the Python sort() function at
https://docs.python.org/2/tutorial/datastructures.html and
https://docs.python.org/2/library/stdtypes.html#typesseq-mutable. Here
are a bunch of calls to the sort function. Which are the same? Which
arguments are understood as which parameters?

- l.sort()
- l.sort(foo)
- l.sort(key=foo)
- l.sort(None, None, True)
- l.sort(foo, None, False)
- l.sort(reversed=True)
- l.sort(reversed=False)

Write a my_sort function that lets a user sort a list and then
capitalizes every element of the list.
