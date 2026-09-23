from pydantic import BaseModel
from typing import Literal


class CustomerSupportResponse(BaseModel):

    category: Literal[
        "payment",
        "shipping",
        "technical",
        "account",
        "other",
    ]


    priority: Literal[
        "low",
        "medium",
        "high",
    ]


    sentiment: Literal[
        "positive",
        "neutral",
        "negative",
    ]


    summary: str

    needs_human: bool

    department: Literal[
    "billing",
    "logistics",
    "technical_support",
    "account_support",
]