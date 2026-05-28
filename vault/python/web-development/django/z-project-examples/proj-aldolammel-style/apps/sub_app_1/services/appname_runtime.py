# from .. import consts
from ..models import SubappModelSettings


def stgs() -> SubappModelSettings | None:
    """Respecting Django runtime, it returns the SubappModelSettings singleton."""
    return SubappModelSettings.objects.first()


def is_something() -> bool:
    """Respecting Django runtime, it returns if xxxxxx is the xxxxxxxxxxxxxxxxxxxxx."""
    obj = stgs()
    return <some_bool_conditional>
