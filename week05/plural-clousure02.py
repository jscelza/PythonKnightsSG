"""Fun with plurals."""


import re


def build_match_and_apply_functions(pattern, search, replace):
    """Function to handle all matches and replace via variables."""
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )

rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]


def plural(noun):
    """Function to handle pluralization entry point."""
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)
