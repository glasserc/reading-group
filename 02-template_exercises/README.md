# View/template exercises

This project comes with some simple models and some sample data you
can use to build some simple views and templates.

    $ python manage.py loaddata template_exercises/fixtures/sample_data.json
    Installed 11 object(s) from 1 fixture(s)

If you start this site up and go to http://localhost:8000, you should
see a rendered template. I put this "default" template in the site's
"templates" directory rather than in any app, because it belongs to
the site rather than to a specific app. Don't do this for your
solutions![^1] This "welcome" view might be helpful as a refresher if
you forgot how HTML works.

These exercises are organized by view, but each view has many
features. You may find it easier to implement features from different
views in some other order.

## Exercise 1

Create an "index" view for the blog.

- It should be accessible at ``/blog``.
- It should load all the blog posts and show a list of them.[^2] In other
  words, you should see something like this:

    1. On Feb. 1, 2015, midnight by Ethan: This is the first blog post.
    2. On Feb. 8, 2015, midnight by Ethan: This is another blog post.
    3. On Feb. 12, 2015, midnight by Rita: This is a guest post!
    4. On Feb. 17, 2015, 9:01 a.m. by Ethan: This is our most recent post.

- The blog posts should be newest first, not oldest first.
- Each blog post should show the number of comments it has. In other
  words, you should see something like this:

    1. On Feb. 17, 2015, 9:01 a.m. by Ethan: This is our most recent post. (0 comments)
    2. On Feb. 12, 2015, midnight by Rita: This is a guest post! (4 comments)
    3. On Feb. 8, 2015, midnight by Ethan: This is another blog post. (2 comments)
    4. On Feb. 1, 2015, midnight by Ethan: This is the first blog post. (1 comment)

- You should probably limit this view to only 5 or 10 blog posts to
  avoid overwhelming the user/user's browser.
- Turn the date into a link. Clicking the link should take you to a
  single blog post.

## Exercise 2

Create a "post" view for the blog.

- It should be accessible at ``/blog/<post_id>``.
- It should show the blog post as well as all comments on that blog
  post. In other words, you should see something like this:

    On Feb. 8, 2015, midnight by Ethan
    This is another blog post.

    Comment on Feb. 09, 2015, 12:12 p.m. by Rick:
    Wow, this is great!

    Comment on Feb. 09, 2015, 12:19 p.m. by Ethan:
    Thanks Rick!

- Comments should be ordered oldest first. (Are they already?)
- If the person posting the comment has the same name as the person
  posting the blog post, add a tag saying so. Something like this:

    Comment on Feb. 09, 2015, 12:19 p.m. by Ethan (original author):
    Thanks Rick!

## Exercise 3

Create an "all comments" view for the blog.

- It should be accessible at ``/blog/comments``.
- It should show all the comments made on all blog posts. In other
  words, you should see something like this:

    Comment posted on Feb. 09, 2015, 12:12 p.m. by Rick:
    Wow, this is great!

    Comment posted on Feb. 09, 2015, 12:19 p.m. by Ethan:
    Thanks Rick!

    Comment posted on Feb. 13, 2015, 12:41 p.m. by Ethan:
    Great work Rita!

etc.

- Comments should be ordered newest first.
- You should probably only limit it to the last 10 comments to avoid
overwhelming the user.
- Each comment should contain a link to the blog post it was made
  on. You should be able to click on the text of the blog post to go
  to that blog post. Something like this:

    Comment posted on Feb. 13, 2015, 12:41 p.m. by Ethan:
    Great work Rita!
    Posted on "This is a guest post!" by Rita

    Comment posted on Feb. 09, 2015, 12:19 p.m. by Ethan:
    Thanks Rick!
    Posted on "This is another blog post" by Ethan

    Comment posted on Feb. 09, 2015, 12:12 p.m. by Rick:
    Wow, this is great!
    Posted on "This is another blog post" by Ethan

## Exercise 4

Create a "comment" view for the blog.

- It should be accessible at ``/blog/comments/<comment_id>``.
- It should show the text of just one comment as well as the text of
the blog post itself. Something like this:

    On Feb. 8, 2015, midnight by Ethan
    This is another blog post.

    Comment on Feb. 09, 2015, 12:19 p.m. by Ethan:
    Thanks Rick!

- Add a link to the bottom that says "See the whole
  conversation". Clicking this link should take you to the blog post
  itself.

## Notes

[^1]:
    In order to get the "welcome" template to work, I changed the "DIRS"
    option in the "TEMPLATES" section of the project's settings.py file.

[^2]:
    I'm not crazy about this date format, but it's the default, so
    let's just leave it for now.
