# I ended up having to write this function at work on Sunday to solve
# a problem I was facing. We have configurations for our website that
# are different if you are developing, if you are in production, or if
# you are in staging (where you test stuff before it goes to
# production). We also have a shared "global" configuration. We wanted
# to merge the global configuration with whatever coniguration made
# sense for a
#
# To write this, you'll need to know about the isinstance() function,
# plus get comfortable with recursion.

def recursive_merge(d1, d2):
    """Merges the contents of dictionaries d1 and d2.

    If a key is present in both d1 and d2, the value from d2 takes
    precedence, UNLESS the corresponding values are both dictionaries,
    in which case the value in the result will be the recursive_merge
    of those values.

    >>> recursive_merge({'a': {'sun': 1}}, {'b': {'moon': 2}})
    {'a': {'sun': 1}, 'b': {'moon': 2}}
    >>> recursive_merge({'a': {'sun': 1}}, {'a': {'moon': 2}})
    {'a': {'sun': 1, 'moon': 2}}
    >>> recursive_merge({'a': 1}, {'a': 2})
    {'a': 2}
    >>> recursive_merge({'a': {'sun': 1, 'moon': 1}}, {'a': {'sun': 2}})
    {'a': {'sun': 2, 'moon': 1}}
    """
    return {}
