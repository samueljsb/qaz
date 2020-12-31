# Python start-up file
# --------------------
# Ensure a PYTHONSTARTUP environment variable points to the location of this file.
# See https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP

# Always have pp available
from pprint import pprint as pp


# Import rich (https://rich.readthedocs.io/en/latest/introduction.html) to get prettier
# output in the REPL.
try:
    from rich import inspect as __inspect
    from rich import pretty as __pretty
except ImportError:
    # rich won't necessarily be installed in all environments
    inspect = pp
else:
    # Ensure printing is pretty by default.
    __pretty.install()

    def inspect(*args, **kwargs):
        # Custom rich.inspect wrapper to ensure methods are inspected by default.
        if "methods" not in kwargs:
            kwargs["methods"] = True
        __inspect(*args, **kwargs)


# Print the commands that have been imported as a memory jogger.
print(">>> from pprint import pprint as pp")
print(">>> from rich import inspect")

# Define aliases for true, false and null so JSON can be pasted straight in.
true = True
false = False
null = None
