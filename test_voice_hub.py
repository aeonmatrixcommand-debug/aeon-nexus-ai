from ai.voice_hub.command import VoiceCommandHub


hub = VoiceCommandHub()


command = hub.listen(
    "Analyze inventory risk in warehouse DC"
)


response = hub.respond(command)


print("=== AEON MATRIX VOICE AI HUB ===")
print(command)
print(response)
