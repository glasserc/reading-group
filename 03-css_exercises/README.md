# CSS exercises

This project is essentially the template exercises, but with my
answers filled in already. Start off by loading the same fixtures you
did last time.

    $ python manage.py loaddata css_exercises/fixtures/sample_data.json
    Installed 11 object(s) from 1 fixture(s)

The purpose of this exercise is to:

1. Get you comfortable introducing CSS to your workflow.

2. Get comfortable manipulating basic CSS.

Future exercises will:

- Refine our layout, in particular share code across our templates.

- Deepen our understanding of CSS, in particular learn about HTML
structure and why it's important, as well as the CSS property
"display".

## Intro

The designers finally produced some images [^1] which got the
attention of upper management. They're about to undergo design reviews
with product which will probably produce at least fifteen different
versions of these designs, but in the meantime the CEO is extremely
eager for you to begin work on implementing even the (somewhat
half-baked) designs you have now. In this directory is a subdirectory
called "designs" [^2]. Your goal is to make the site look like the
designs.

The designers have so much to say, so they've added some notes in pink
text.

## Exercise 1

Add a "static" directory to the blog application. All the designs are
for views in the blog application, so that's where we'll put our
stylesheets. Create a ``blog`` directory containing a ``style.css``
stylesheet and link the list_posts template to it. Verify it works by
changing something outlandish (say, the color of all ``<p>``
elements).

Once you're sure it works, repeat this for the other views --
``show_post``, ``list_comments``, and ``show_comment``.

## Exercise 2

Fix up the "easy" parts of the design. Start with the foreground
colors, background colors, and spacing.

- You might need to add ``class`` attributes to certain elements so
  that you can target them more effectively.

- If you want to affect the entire page, you can write a selector that
  affects the ``body`` element.

## Exercise 3

Looks like the designers added a logo and masthead to the
page. Fortunately, they're both just text. Add some HTML to the
different templates to match. Be sure to style it so that it looks how
they want it.

## Exercise 4 (extra credit)

Try to get the lines and borders right.

- Some of you might know about the HTML ``<hr>`` element. Forget about
  it. All horizontal lines on the page are implemented using
  ``border`` properties.

- You might need to add, subtract, or change HTML elements. In
  particular, you might need the <div> element, which
  [has no meaning](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
  but can be used to group and style elements.

[^1]: Obviously my design skills are crap so I just took screenshots
    of what I hope the answer will look like.

[^2]: Normally designs are *not* included in code like this. I just
    did this for ease of distribution.
