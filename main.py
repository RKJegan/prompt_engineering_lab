import json

import config
from pydantic import ValidationError
from schemas import CustomerSupportResponse
from llm import analyze_customer_message


def process_customer_message(customer_message: str):

    try:

        llm_response = analyze_customer_message(
            customer_message,
            config.PROMPT_MODE,
            )

        print("\n LLM Response:  ")
        print(llm_response)


        data = json.loads(llm_response)

        validated_result = CustomerSupportResponse(**data)

        print("\n--- Classification ---")
        print(f"Category: {validated_result.category}")
        print(f"Priority: {validated_result.priority}")
        print(f"Sentiment: {validated_result.sentiment}")
        print(f"Summary: {validated_result.summary}")
        print(f"Needs Human: {validated_result.needs_human}")
        print(f"Department: {validated_result.department}")

    except json.JSONDecodeError:
        print("\nError: LLM returned invalid JSON.")
        print("Raw response:")
        print(repr(llm_response))

    except ValidationError as e:
        print("\nError: LLM returned data that does not match our schema.")
        print(e)

    except Exception as e:
        print(f"\nUnexpected error: {e}")


def handle_command(user_input: str) -> bool:

    parts = user_input.split(maxsplit = 1)

    command = parts[0].lower()

    if command == "/prompt":

        if len(parts) == 1:
            print(f"Current prompt mode: {config.PROMPT_MODE}")
            print("Available modes: zero_shot, few_shot")
            return True

        new_mode = parts[1].strip().lower()

        if new_mode not in config.ALLOWED_PROMPT_MODES:
            print("Invalid prompt mode.")
            print("Available modes: zero_shot, few_shot")
            return True 

        config.PROMPT_MODE = new_mode

        print(f"Prompt mode changed to: {config.PROMPT_MODE}")
        return True

    return False


def main():

    print("Customer Support Intelligence System")
    print("Type 'exit' to quit.\n")
    print("Type '/prompt' to view the current prompt mode.")
    print("Type '/prompt zero_shot' or '/prompt few_shot' to change it.")
    print()


    while True:
        
        user_input = input("Customer message:  ").strip()

        if user_input.lower() == "exit":
            print("Untill next time :) ")
            break

        if not user_input:
            print("Error: Customer message cannot be empty.")
            continue

        if user_input.startswith("/"):
            if not handle_command(user_input):
                print("Unknown command.")
            print()
            continue


        process_customer_message(user_input)
        print()


if __name__ == "__main__":
    main()