# mr-Ucar
#### Version2 - The code needs to optimized, work in progress. Can give errors when an unknown word requested. Will refactor and optimize the code later.

# Pronunciation of the requested word will also be saved in the same directory/folder where you run the script.
# csv formatted output will also be saved.

import requests
import json
import csv


# Ask user for word to look up
print("\033[1mWelcome to simple Dictionary!\033[0m")
print("\nThis program will look up the definition of a word for you and also save the audio/pronunciation.\n")
word2lookup = input("\033[1mWrite the word that you want to look up: \033[0m")

# Construct URL for API request
base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
url = base_url + word2lookup

# Send API request and get response
response = requests.get(url)

# Check if response is valid
if response.status_code == 200:
    # Parse JSON data from response
    data = response.json()

    # Get first definition from data
    definition = data[0]['meanings'][0]['definitions'][0]['definition']

    # Get two example sentences from definition
    sentences = definition.split(';')[:2]

    # Print example sentences
    print("\033[92mExample sentences:\033[0m")
    for sentence in sentences:
        print(f"- {sentence.strip()}")

    # Save definitions in a CSV file
    with open(f"{word2lookup}.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Definitions"])
        for sentence in sentences:
            writer.writerow([sentence.strip()])

    # Save JSON data as output
    with open(f"{word2lookup}.json", "w") as f:
        json.dump(data, f)

    # Download audio pronunciation
    audio_url = data[0]['phonetics'][0]['audio']
    audio_response = requests.get(audio_url)
    with open(f"{word2lookup}.mp3", "wb") as f:
        f.write(audio_response.content)
        print(f"Audio pronunciation saved as '{word2lookup}.mp3'.")


else:
    print(
        f"\033[91mError:\033[0m Could not find '{word2lookup}' in dictionary.")
    data = response.json()

    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    except IndexError:
        print(f"Error: Could not find '{word2lookup}' in dictionary.")
        print("Please check your spelling and try again. Or the word you are looking for is not in the dictionary.")

    # Get two example sentences from definition
    sentences = definition.split(';')[:2]

    # Print example sentences
    print("\033[92mDefinitions: \033[0m")
    for sentence in sentences:
        print(f"- {sentence.strip()}")

    # Save definitions in a CSV file
    with open(f"{word2lookup}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Definitions"])
        for sentence in sentences:
            writer.writerow([sentence.strip()])
    print(f"Definition:  '{word2lookup}':")
    for sentence in sentences:
        print(f"- {sentence.strip()}")

    # Save definitions in a CSV file
    with open(f"{word2lookup}.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Definitions"])
        for sentence in sentences:
            writer.writerow([sentence.strip()])

    # Save JSON data as output
    if response.status_code == 200:
        with open(f"{word2lookup}.json", "w") as f:
            json.dump(data, f)
    else:
        print(f"Error: Could not find '{word2lookup}' in dictionary.")
        data = response.json()

    # Get first definition from data
    definition = data[0]['meanings'][0]['definitions'][0]['definition']

    # Get two example sentences from definition
    sentences = definition.split(';')[:2]

    # Print example sentences
    print(f"Example sentences for '{word2lookup}':")
    for sentence in sentences:
        print(f"- {sentence.strip()}")

    # # Save definitions in a CSV file
    # with open(f"{word2lookup}.csv", "w", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Definitions"])
    #     for sentence in sentences:
    #         writer.writerow([sentence.strip()])


word2lookup = input("Enter a word to lookup: ")

while True:
    try:
        # Get word to lookup from user
        word2lookup = input("Enter a word to lookup (press 'q' to quit): ")
        if word2lookup == 'q':
            break

        # Send GET request to API
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word2lookup}"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse JSON data from response
            data = response.json()

            # Get first definition from data
            definition = data[0]['meanings'][0]['definitions'][0]['definition']

            # Get two example sentences from definition
            sentences = definition.split(';')[:2]

            # Print example sentences
            print("\033[92mExample sentences:\033[0m")
            for sentence in sentences:
                print(f"- {sentence.strip()}")

            # Save definitions in a CSV file
            with open(f"{word2lookup}.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Definitions"])
                for sentence in sentences:
                    writer.writerow([sentence.strip()])

            audio_url = data[0]['phonetics'][0]['audio']
            if audio_url:
                audio_response = requests.get(audio_url)
                with open(f"{word2lookup}.mp3", "wb") as f:
                    f.write(audio_response.content)

            with open(f"{word2lookup}.mp3", "wb") as f:
                f.write(audio_response.content)
                print(f"Audio pronunciation saved as '{word2lookup}.mp3'.")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Program terminated by user.")
        break
