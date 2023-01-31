# This is a set of "code reading" exercises in Ruby. It's meant to
# strengthen your ability to read code as well as write it. Most
# curriculums are missing as much practice on the reading side of the
# equation, emphasizing only writing it, which leads to unfortunate
# consequences. This is an attempt to remedy that.
#
# Below you will find some code samples that are not representative of
# code you should write. Perhaps they were written by a team of
# outsourced Russian engineers. Perhaps they were generated by an
# algorithm. For whatever reason, they are completely missing
# documentation, descriptions, comments, useful variable names, or
# even common sense. Your mission, if you choose to accept it, is to
# answer the questions after each exercise. These questions may ask
# you to predict the behavior of the code given certain inputs. Try to
# solve these without running the code itself. Other questions may ask
# how to modify it to achieve certain objectives. If you can do this,
# you will be capable of reading anyone's code, including your
# own. Cheers!

def exercise_1(a)
  x = []
  b = a - a
  while a > b
    x.push(x.length)
    a + 5
    a = a - 5
    puts a + 3
    x.push(a)
  end
  x.join("!")
end

# Exercise 1.1. What is printed by exercise_1(9) ?

# Exercise 1.2. What is returned by exercise_1(9) ?

# Exercise 1.3. What is returned by exercise_1(0) ?

# Exercise 1.4. What simplifications can you make to this code without
# changing its behavior? (I can think of at least two.)

def exercise_2(z, zz, zzz)
  a = []
  if z.even?
    a = ['a', 'b']
  end
  r = a.length + 1          # Line 5
  while r < 14
    r = r * 2
    if r > zz
      y = 'c'
    elsif r > zzz
      y = 'd'               # Line 11
    else
      y = e
    end
    a.push(y)
  end
  puts r
  a
end

# Exercise 2.1. What happens if we execute exercise_2(4, 2, 0)? (Is
# anything printed? Does an error occur? If not, what is returned?)

# Exercise 2.2. What happens if we execute exercise_2(4, 8, 2)?

# Exercise 2.3. What happens if we execute exercise_2(4, 8, 8)?

# Exercise 2.4. What happens if we execute exercise_2(3, 8, -1)?

# Exercise 2.5. If we change the line "r = a.length + 1" to just "r =
# a.length", what happens if we execute exercise_2(3, 8, -1)?

# Exercise 2.6. Is it possible to provide arguments to exercise_2 that
# will cause it to return an empty array? If so, what arguments can
# you provide? If not, why not?

# Exercise 2.7. Let's say we only want our array `a` to add elements
# until we put the first "d" in it (and then stop). What commands can
# we insert after line 11 to make that happen?