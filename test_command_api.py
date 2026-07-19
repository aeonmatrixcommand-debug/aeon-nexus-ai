from executive_api.command_api import CommandAPI


api = CommandAPI()

response = api.status()

print("=== AEON MATRIX LIVE COMMAND API ===")
print(response)
