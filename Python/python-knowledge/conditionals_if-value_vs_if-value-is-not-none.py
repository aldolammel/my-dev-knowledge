

if VAR:                   # cond: if VAR is True. (not necessarily demands bool type!)
    pass


if VAR is not None:       # cond: if VAR is not None (var could be str, int, bool, list, dict, etc)
    pass

"""
COMPARISON:

VAR ---------------- if VAR: -------------- if VAR is not None:
"hello" . . . . . . . pass . . . . . . . . . . pass
"" . . . . . . . . . FAIL . . . . . . . . . . . pass
0 . . . . . . . . . . FAIL . . . . . . . . . . pass
[] . . . . . . . . . FAIL . . . . . . . . . . . pass
False . . . . . . . . FAIL . . . . . . . . . . pass
None . . . . . . . . . FAIL . . . . . . . . . . FAIL

"""

