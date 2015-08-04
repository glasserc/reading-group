# CSS exercises pt. 2

This project is essentially the CSS exercises, but with my
answers filled in already. Start off by loading the same fixtures you
did last time.

    $ python manage.py loaddata css_exercises/fixtures/sample_data.json
    Installed 11 object(s) from 1 fixture(s)

The purpose of this exercise is to:

1. Clean up some of the awful things we did in the last exercises,
   specifically abstracting away repetition using template
   inheritance.

2. Practice use of CSS "inline"/"block" as well as "position" and
   "float".

## Intro

The UX designer looked at the designs from last session and declared
them an utter failure of usability. "Users have almost no options for
navigation. At the very least, this site needs a sidebar menu."

At the same time, the designers from last week decided to take a
three-week vacation at the same time. (They aren't vacationing
together, they just had unfortunate timing.) In the meantime, the CEO
added a few flourishes to the site.

Most of these changes are minor, but they're site-wide, so let's start
by unifying our templates.

## Exercise 1

Let's fix up the template problems we created last time around. Create
a "base" template called "base.html". For now, put it in the blog
templates directory. Move the important "framework" parts of the site
-- the masthead and the links to the stylesheet -- into the base
template. Change the view templates to extend this base template. Make
sure it works by changing the masthead on the base. It should take
effect everywhere.

## Exercise 2

Let's add some navigation elements.

- The logo should probably link to the main blog view. If there were
  other parts of the site, it would probably be better to make the
  logo go to the "home" part of the site, but we don't, so whatever.

- Add a sidebar to the left side of all pages. This should have links
  to any commonly used pages. So far we only have: all posts, and all
  comments.

A sidebar, in case you aren't familiar with the term, is simply a
section of a web page off to the side of the main content. Usually it
contains useful links. Gmail's list of tags on the left is a
sidebar. I've included a screenshot of the sidebar from
http://thedailywtf.com/ for reference.

We don't have designs for the sidebar because all the designers are on
vacation. Try to make it look like how you think they would have
wanted. If they don't like it when they get back, well, that's their
fault for going on vacation.

## Exercise 3

The CEO wants to add a few elements to the site.

- He found an image of a gutter, courtesy of
  http://www.guttersupply.com/. He'd like this to appear floating in
  the lower right corner of all pages, sort of like the Jenkins logo
  (see http://i1-mac.softpedia-static.com/screenshots/Jenkins_4.jpg).

- He also wants each blog post to have a little clock in the upper
  right corner, sort of like how Slashdot does (except without the
  different icons to indicate the different categories of story).  He
  found a picture of a clock at
  https://openclipart.org/detail/119143/modern-clock. I've taken the
  liberty of converting that into a PNG for you.

The picture of the gutter and of the clock are available in
``design/assets/``.

## Exercise 4

Add a link to the sidebar called "Latest Post". This should link to
the latest blog post. However, most views won't have the latest blog
post already fetched when they render a template, so instead, create a
new view accessed at ``/latest_post``. This view should load the
latest post, and then use a *redirect* to send the browser to that
page.

## Exercise 5

There are at least two ways to implement the "clock" part of Exercise
3: using ``position:``, and using ``float:``. Implement both. What
differences do you notice about how to implement them, and how do they
behave differently?
