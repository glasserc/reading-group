No particular scaffolding on this one. You can re-use whatever you did for exercise #4.

1. Write by hand the HTML code corresponding to this form, which might
be used for comments on blog posts.

    Name:   ___________
    Email:  ___________
    Comment:
    ____________________
    ____________________
    ____________________

This seems like a tedious/stupid exercise, since Django lets you do it
from a Python class, but it's helpful to know how the HTML you want is
supposed to look in case things go wrong. Remember to use the web
development tools to inspect the HTML elements if they seem like
they're coming out horribly.

2. Add a view that can handle form submissions and does something
interesting with it. "Interesting" is loosely defined here and just means something that proves you got the request and could process it. Experiment with what happens if you enter invalid data -- missing email, for example.

Try this exercise with both GET and with POST. How does your view change? How do your URLs change?

3. Despite what I said about the Django forms framework not being modern, it's still useful, so let's get some practice with it. Solve exercises #1 and #2 again, but using the Django forms library to generate the form and process it. Use POST this time. Verify that it still works by doing the same "interesting" thing. How does it handle invalid form submissions?

The form pattern from the tutorial follows a pattern called https://en.wikipedia.org/wiki/Post/Redirect/Get.

4. If you still have time, take a look at https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/. See if you can use this feature to implement an upload form for dollhouse elements, including letting the user upload images.
