"""Fun with plurals."""


import re


def match_sxz(noun):
    """Searching for sxz in end of word."""
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    """Applying sub for sxz in end of word."""
    return re.sub('$', 'es', noun)


def match_h(noun):
    """Searching for soft h in end of word."""
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    """Applying sub for soft h in end of word."""
    return re.sub('$', 'es', noun)


def match_y(noun):
    """Searching for y  in end of word."""
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    """Applying sub for y in end of word."""
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    """Searching default in end of word."""
    return True


def apply_default(noun):
    """Applying default to end of word."""
    return noun + 's'


rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default))


def plural(noun):
    """Function to handle all plural case."""
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
