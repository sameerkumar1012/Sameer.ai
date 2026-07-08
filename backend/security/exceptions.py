
from fastapi import Request
from fastapi.responses import JSONResponse

from .validators import ValidationError
from .prompt_guard import PromptInjectionError
from .code_guard import UnsafeCodeRequest
from .budget import BudgetExceeded


async def validation_exception_handler(
    request: Request,
    exc: ValidationError,
):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )


async def prompt_exception_handler(
    request: Request,
    exc: PromptInjectionError,
):
    return JSONResponse(
        status_code=403,
        content={"detail": "This request cannot be processed."},
    )


async def code_exception_handler(
    request: Request,
    exc: UnsafeCodeRequest,
):
    return JSONResponse(
        status_code=403,
        content={"detail": "Unsafe request detected."},
    )


async def budget_exception_handler(
    request: Request,
    exc: BudgetExceeded,
):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Daily AI budget exceeded. Please try again tomorrow."
        },
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Something went wrong."
        },
    )