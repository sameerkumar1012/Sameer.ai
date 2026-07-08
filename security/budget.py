DAILY_BUDGET = 3.00


class BudgetExceeded(Exception):
    pass


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Temporary placeholder.

    Replace with actual Nova Lite pricing later.
    """

    return (
        input_tokens * 0.0000001
        + output_tokens * 0.0000003
    )


def check_budget(today_cost: float):

    if today_cost >= DAILY_BUDGET:
        raise BudgetExceeded(
            "Daily AI budget exceeded."
        )