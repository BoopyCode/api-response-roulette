#!/usr/bin/env python3
"""
API Response Roulette - Because third-party APIs are like a box of chocolates,
you never know what you're gonna get. Except it's more like Russian roulette.
"""

import random
import json
from typing import Dict, Any, Optional

# The casino of broken dreams
ERROR_TYPES = [
    "success_but_with_error_field",
    "error_but_with_200_status",
    "nested_error_ception",
    "plain_text_in_json_endpoint",
    "xml_response_on_json_api",
    "rate_limit_without_headers",
    "deprecated_field_without_warning",
    "cors_headers_on_internal_api",
    "timestamp_in_13_different_formats",
    "null_instead_of_empty_array"
]

# Because who needs documentation anyway?
UNDOCUMENTED_STATUS_CODES = [418, 451, 499, 520, 521, 522, 523, 524, 525, 526]


def spin_the_roulette() -> Dict[str, Any]:
    """
    Pull the trigger and see what you get.
    Warning: May cause existential dread in developers.
    """
    
    # The house always wins
    if random.random() < 0.3:  # 30% chance of "success"
        return {
            "status": "success",
            "data": {
                "id": random.randint(1, 1000),
                "name": "Sample Data",
                "timestamp": "2023-12-25T25:61:61Z",  # Because time is relative
                "extra_field": random.choice([None, "", [], {}, 0])
            },
            "message": random.choice(["", None, "Operation completed successfully"])
        }
    
    # Welcome to the error dimension
    error_type = random.choice(ERROR_TYPES)
    
    responses = {
        "success_but_with_error_field": {
            "status": "success",
            "error": "Something went wrong, but we're calling it success"
        },
        "error_but_with_200_status": {
            "statusCode": 200,
            "error": "Internal Server Error",
            "message": "Everything is fine (it's not)"
        },
        "nested_error_ception": {
            "error": {
                "error": {
                    "message": "Error within error within error"
                }
            }
        },
        "plain_text_in_json_endpoint": "Server Error: Please try again later",
        "xml_response_on_json_api": "<error><code>500</code><message>Surprise!</message></error>",
        "rate_limit_without_headers": {
            "message": "Too many requests",
            "retry_after": None  # Because guessing is fun!
        },
        "deprecated_field_without_warning": {
            "old_field": "still here",
            "new_field": "also here",
            "deprecated_since": "2020"
        },
        "cors_headers_on_internal_api": {
            "data": "sensitive info",
            "Access-Control-Allow-Origin": "*"  # Security? Never heard of her.
        },
        "timestamp_in_13_different_formats": {
            "created_at": "2023-12-25",
            "updated_at": 1703462400,
            "deleted_at": "25/12/2023 14:30:45",
            "processed_at": "December 25, 2023"
        },
        "null_instead_of_empty_array": {
            "items": None,
            "total": 0
        }
    }
    
    return responses[error_type]


def get_status_code() -> int:
    """
    Returns a status code. Might be HTTP standard, might be from Narnia.
    """
    if random.random() < 0.2:  # 20% chance of undocumented status
        return random.choice(UNDOCUMENTED_STATUS_CODES)
    
    # The usual suspects
    return random.choice([200, 400, 401, 403, 404, 429, 500, 502, 503])


def test_your_luck() -> None:
    """
    Test your integration against our perfectly realistic API simulator.
    Results may include: confusion, frustration, or sudden urge to become a farmer.
    """
    print("\n🎰 Spinning the API roulette...\n")
    
    status = get_status_code()
    response = spin_the_roulette()
    
    print(f"Status Code: {status}")
    print(f"Response Type: {type(response).__name__}")
    print(f"Response:\n{json.dumps(response, indent=2) if isinstance(response, dict) else response}")
    print("\nGood luck with that integration! 🍀")


if __name__ == "__main__":
    test_your_luck()
