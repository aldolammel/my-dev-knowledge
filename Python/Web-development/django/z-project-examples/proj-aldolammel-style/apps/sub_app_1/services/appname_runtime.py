# from .. import consts
from ..models import SubappSettings


def stgs() -> SubappSettings | None:
    """Respecting Django runtime, it returns the SubappSettings singleton."""
    return SubappSettings.objects.first()


def is_something() -> bool:
    """Respecting Django runtime, it returns if xxxxxx is the xxxxxxxxxxxxxxxxxxxxx."""
    obj = stgs()
    return <some_bool_conditional>
