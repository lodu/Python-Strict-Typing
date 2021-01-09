from strict_typing import check_strict_typing
from typing import List, Dict


@check_strict_typing
def greet(name: str):
    print(f"Greetings {name}")


@check_strict_typing
def greet_list(name: str, hobbies: list):
    print(f"Greetings {name} with hobbies: {*hobbies, }")


@check_strict_typing
def greet_list_typing(name: str, hobbies: List):
    print(f"Greetings {name} with hobbies: {*hobbies, }")


@check_strict_typing
def greet_dict(name: str, language_skills: dict):
    print(f"Greetings {name} with language skills: {*language_skills.items(), }")


@check_strict_typing
def greet_dict_typing(name: str, language_skills: Dict):
    print(f"Greetings {name} with language skills: {*language_skills.items(), }")


greet("lodu")  # OK
greet(69)  # raises TypeError


greet_list("lodu", ["programming", "tv-shows"])  # OK
greet_list("lodu", ("programming", "tv-shows"))  # raises TypeError

greet_list_typing("lodu", ["programming", "tv-shows"])  # OK


greet_dict("lodu", {"dutch": "good", "english": "good"})  # OK
greet_dict("lodu", [("dutch", "good"), ("english", "good")])  # raises TypeError

greet_dict_typing("lodu", {"dutch": "good", "english": "good"})  # OK
