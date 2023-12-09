#AI Voice Assistant with Python and OpenAI API

**Description:** This Python-based AI voice assistant integrates the OpenAI `text-davinci-003` model to perform diverse tasks through voice commands. It can effortlessly launch specified websites like YouTube, Google, Wikipedia, etc., using the command structure "launch (website name with pre-set URL)." Additionally, users can request song playback from a designated directory by using the command "play (song name)."

**Functionalities:**
- **Website Launch:** Open predefined websites using voice commands.
- **Music Playback:** Play songs from a directory through voice prompts.
- **AI-assisted Tasks:** Utilize AI-generated commands for various tasks, including requesting assistance in composing emails (e.g., "Using artificial intelligence, write an email to my boss for resignation"). Some task examples are available in the `openai/` folder.

**Project Structure:**
- **`config.py`:** Includes the API key from the OpenAI official website for authentication.
- **`openai/` Folder:** Contains task examples and scripts for interacting with the OpenAI API.

**Technology Stack:**
- **Python:** Primary language for development.
- **OpenAI API:** Utilizes the `text-davinci-003` model for natural language processing.
- **GitHub:** Hosted repository for version control and collaboration.

**Setup Instructions:**
1. Clone the repository.
2. Set up your API key from the OpenAI official website within `config.py`.
3. Execute the main script to activate the voice assistant.

**Example Commands:**
- Command: "Launch YouTube."
- Action: Opens YouTube in the default browser.
- Command: "Play 'Song_Name'."
- Action: Plays the specified song from the directory.
- Command: "Using artificial intelligence,for example:-" write an email to my boss for resignation."
- Action: Generates a resignation email using AI-based text generation.differennt tasks related to information can be done by this assistant using ai make sure to speak using artifical intelligence in that specific command
