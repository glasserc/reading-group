This is a set of exercises meant to toughen up your ability to read and use urlpatterns. For more information, see https://docs.djangoproject.com/en/1.8/topics/http/urls/.

# Scenario

You recently started work at Games People Play, a small website with a passionate following of users. You're the only engineer; the last engineer for the company left after a month or so of getting up to speed with Django. The site basically follows normal patterns, but with some surprises.

The site is made up of three applications, each of which fills some part of the site's function. The views for these applications are just "stubs" -- they're incomplete, rough versions of what they might actually do. Models are completely absent.

# Exercise 1: reading patterns

Figure out where each of these requests goes to and why. If they don't
go to any view, write "404". Try to figure it out without running the
site. You can check your answers by running the site and loading the
URLs in your browser.

* http://localhost:8000/blog/
* http://localhost:8000/blog/1
* http://localhost:8000/voting/
* http://localhost:8000/voting/1
* http://localhost:8000/thoughts
* http://localhost:8000/play/1
* http://localhost:8000/logger/1
* http://localhost:8000/logger/4-new-version-today/
* http://localhost:8000/logger/1-how-to-play
* http://localhost:8000/logger/7-announcing-games-people-play-version-2

Figure out a URL that will take you to the "month" view in the blog
application.

# Exercise 2: fixing patterns

Your manager says that the "/thoughts/" part of the site isn't working
correctly. It's supposed to be an alias for "/logger/", but going to
http://localhost:8000/thoughts/1 doesn't seem to work. Why? How can we
fix it?

What other odd behaviors did you notice in exercise 1? What caused
them? How can we fix them?

# Exercise 3: changing patterns

The CEO of Games People Play comes to you with a request. He wants to
rebrand the polls as "GameChoices". He would like to change the site
so that going to http://localhost:8000/gamechoices/1 takes you to the
poll with ID 1. The old URLs for polls, http://localhost:8000/voting,
no longer needs to work.

# Exercise 4: adding patterns

There's no way to reach the ``games_for_me`` view in the Tic-tac-toe
application. Add a pattern that lets these be accessed.

Add another pattern for the ``games_for_player`` view.

Add a view for viewing blog posts of a particular year. What URL
should it have? Add the pattern to make that happen.

# Exercise 5: madness

Apparently the CEO's been talking to some SEO guru and he has some
requests for you.

* The CEO wants http://localhost:8000/gamechoices/1 to remain the
  preferred URL for polls, but wants to add the URL
  http://localhost:8000/voting which should show the polls index
  view. http://localhost:8000/voting/1 should *not* take you to a
  particular poll. Change your urls files to make this work.

* The CEO wants to change the site so that the URLs are no longer
  grouped. To go to tic-tac-toe game #1, you can go to
  http://localhost:8000/1, and to go to blog post #8, you can go to
  http://localhost:8000/8. Make the change or explain why it isn't
  possible.

# Notes

Hopefully it should be obvious by now that your URL patterns for your
site should be unambiguous -- a particular URL should only have one
interpretation. This can be challenging in the face of bizarre
requirements meant to improve your performance on search engines. When
working with URL patterns, you probably want each view to be covered
exactly once, no more and no less, with no overlap or gap.

Hopefully by now you're starting to get a feel for how URLs should be
structured on a site, with subsequent components of a URL representing
smaller and smaller sections of something.
