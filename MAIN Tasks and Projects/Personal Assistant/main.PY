import json
from datetime import datetime
import requests


FILE_NAME = "assistant_memory.json"


class Assistant:

    def __init__(self):

        self.memory = self.load_memory()

        # Command dictionary
        self.commands = {
            "hello": self.greet,
            "hi": self.greet,
            "hey": self.greet,
            "time": self.get_time,
            "date": self.get_date,
            "name": self.get_name,
            "help": self.help,
            "show reminders": self.show_reminders,
            "clear reminders": self.clear_reminders,
            "show notes": self.show_notes
        }

    # ==================================================
    # MEMORY
    # ==================================================

    def load_memory(self):

        try:

            with open(FILE_NAME, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return {
                "reminders": [],
                "notes": []
            }

        except json.JSONDecodeError:

            print("Memory file is corrupted.")

            return {
                "reminders": [],
                "notes": []
            }

    def save_memory(self):

        try:

            with open(FILE_NAME, "w") as file:

                json.dump(
                    self.memory,
                    file,
                    indent=4
                )

        except Exception as e:

            print("Error saving memory:", e)

    # ==================================================
    # BASIC COMMANDS
    # ==================================================

    def greet(self):

        return "Hello! How can I help you?"

    def get_name(self):

        return "My name is Python Personal Assistant."

    def get_time(self):

        current_time = datetime.now()

        return current_time.strftime(
            "%I:%M %p"
        )

    def get_date(self):

        current_date = datetime.now()

        return current_date.strftime(
            "%A, %d %B %Y"
        )

    # ==================================================
    # CALCULATOR
    # ==================================================

    def calculate(self, expression):

        try:

            allowed = "0123456789+-*/(). "

            if not all(
                char in allowed
                for char in expression
            ):

                return "Invalid characters in expression."

            result = eval(expression)

            return f"Result: {result}"

        except ZeroDivisionError:

            return "You cannot divide by zero."

        except Exception:

            return "Invalid mathematical expression."

    # ==================================================
    # REMINDERS
    # ==================================================

    def add_reminder(self, reminder):

        if not reminder:

            return "Please provide a reminder."

        self.memory["reminders"].append(reminder)

        self.save_memory()

        return "Reminder saved successfully."

    def show_reminders(self):

        reminders = self.memory["reminders"]

        if not reminders:

            return "You don't have any reminders."

        result = "Your reminders:\n"

        for number, reminder in enumerate(
            reminders,
            start=1
        ):

            result += (
                f"{number}. {reminder}\n"
            )

        return result

    def clear_reminders(self):

        if not self.memory["reminders"]:

            return "There are no reminders to clear."

        self.memory["reminders"] = []

        self.save_memory()

        return "All reminders have been cleared."

    # ==================================================
    # NOTES
    # ==================================================

    def add_note(self, note):

        if not note:

            return "Please provide a note."

        self.memory["notes"].append(note)

        self.save_memory()

        return "Note saved successfully."

    def show_notes(self):

        notes = self.memory["notes"]

        if not notes:

            return "You don't have any notes."

        result = "Your notes:\n"

        for number, note in enumerate(
            notes,
            start=1
        ):

            result += f"{number}. {note}\n"

        return result

    # ==================================================
    # WEATHER
    # ==================================================

    def get_weather(self, city):

        if not city:

            return "Please provide a city."

        try:

            # Example API
            url = ("https://wttr.in/"+ city+ "?format=j1")

            response = requests.get(url,timeout=5)

            if response.status_code != 200:

                return "Unable to get weather information."

            data = response.json()

            current = data["current_condition"][0]

            temperature = current["temp_C"]

            humidity = current["humidity"]

            condition = current["weatherDesc"][0]["value"]

            return (
                f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {condition}"
            )

        except requests.RequestException:

            return (
                "Unable to connect "
                "to the weather service."
            )

        except Exception:

            return (
                "Something went wrong "
                "while getting weather."
            )

    # ==================================================
    # HELP
    # ==================================================

    def help(self):

        return """
========== AVAILABLE COMMANDS ==========

hello
hi
hey

name

time

date

calculate <expression>

remember <text>

show reminders

clear reminders

note <text>

show notes

weather <city>

help

exit
"""

    # ==================================================
    # COMMAND PROCESSOR
    # ==================================================

    def process_command(self, command):

        command = command.strip()

        if not command:

            return "Please enter a command."

        lower_command = command.lower()

        # ----------------------------------------------
        # EXIT
        # ----------------------------------------------

        if lower_command == "exit":

            return "EXIT"

        # ----------------------------------------------
        # DIRECT COMMANDS
        # ----------------------------------------------

        if lower_command in self.commands:

            return self.commands[
                lower_command
            ]()

        # ----------------------------------------------
        # CALCULATOR
        # ----------------------------------------------

        if lower_command.startswith(
            "calculate "
        ):

            expression = command[
                len("calculate "):
            ]

            return self.calculate(
                expression
            )

        # ----------------------------------------------
        # REMEMBER
        # ----------------------------------------------

        if lower_command.startswith(
            "remember "
        ):

            reminder = command[
                len("remember "):
            ]

            return self.add_reminder(
                reminder
            )

        # ----------------------------------------------
        # NOTE
        # ----------------------------------------------

        if lower_command.startswith(
            "note "
        ):

            note = command[
                len("note "):
            ]

            return self.add_note(note)

        # ----------------------------------------------
        # WEATHER
        # ----------------------------------------------

        if lower_command.startswith(
            "weather "
        ):

            city = command[
                len("weather "):
            ]

            return self.get_weather(city)

        # ----------------------------------------------
        # UNKNOWN COMMAND
        # ----------------------------------------------

        return (
            "I don't understand that command.\n"
            "Type 'help' to see available commands."
        )


# ======================================================
# MAIN PROGRAM
# ======================================================


def main():

    assistant = Assistant()

    print("\n====================================")
    print("      PYTHON PERSONAL ASSISTANT")
    print("====================================")

    print(
        "Type 'help' to see available commands."
    )

    while True:

        user_input = input("\nYou: ")

        response = assistant.process_command(user_input)
        

        if response == "EXIT":

            print("Assistant: Goodbye!")

            break

        print(f"Assistant: {response}")


main()