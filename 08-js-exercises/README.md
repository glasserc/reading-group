# Pimp My Transcript

So, it's senior year and you're about to apply to grad school. Only problem is, you were kind of a terrible student. You learned an awful lot about Ultimate Frisbee and hotwiring cars, but academically you were a complete flop. Well, not a complete flop, because you did OK in computer science. And a good thing, too!

Start by running the migrations and loading the fixtures (`python manage.py loaddata js_exercises/fixtures/sample_data.json`). Run the site. Take a look at your transcript. Not awesome, right?

Fortunately, there's a security hole in the server. There's a file called `uploaded.js` that you can use to inject JavaScript code to "modify" the transcript. To complete this assignment, you'll craft an `uploaded.js` that makes you look much more academically inclined.

It looks like the noobs who put together this system for the administration used jQuery even to add a few classes here and there, so you'll have that available to you as well.

# Exercises

1.  Those red boxes which signify failure are really quite unsightly. Turn them into green "passing" boxes instead. This shouldn't be too hard, but it won't really fool a serious examination.

2.  Oops! Seems like someone in the administration noticed that all the boxes are green on all the transcripts. Better add some code to check that the transcript is for you before it does anything.

3.  You took a couple years off in the middle of your degree program. Grad schools hate that. It's not really lying to say that your graduation date WOULD HAVE been 2012-06 if you had taken all your classes, is it? And passed them?

    1. You better update those other semester dates too, come to think of it.

4.  It's not your fault that you did so badly in Chem 101. You were distracted by how attractive all the other students were. You learned a lot here too. Out of fairness, bump your grade to a B-.

5.  But now your averages and especially your GPA aren't accurate. You're going to be changing lots of stuff here, so we may as well just write code that recalculates your averages.

    1. First, write code that will recalculate each semester's average. Remember, A = 4, B = 3, C = 2, D = 1, F = 0, and divide by the number of credits.

    2. Then, write code that will recalculate your total GPA.

6. Second semester, you took it kinda easy. In hindsight, it would be great if you took another course.

7. You'd really like to appeal to those CS grad programs, so add something that will find all your CSCI courses and bump them a full letter grade.

8. Your math grades would have been acceptable except the courses you were taking were sort of basic. Update them to some more rigorous classes, like MATH314 Numerical Prestidigitation, MATH410 Spontaneous Mathogenesis, MATH602 Statistical Malfeasance, etc.

9. Hey, you worked really hard in those linguistic courses. At least 4 credit-hours worth. It's probably an accident that they had an adjunct lecturer teaching them. Try to correct their mistake.
