# Turkish Voice Assistant Project

This project is a voice assistant application that can perform various commands by speaking in Turkish. The application includes features such as speech recognition, voice response generation, and web browser search.

## Features

- **Speech Recognition**: Recognizes commands given by the user through the microphone.
- **Voice Response**: Responds to user commands and expresses these responses verbally.
- **Web Browser Integration**: Executes commands like maps, weather, and general search by opening the web browser.
- **Date and Time Information**: Provides the current time verbally upon the user's request.

## Libraries Used

- `speech_recognition`
- `datetime`
- `webbrowser`
- `time`
- `gtts`
- `playsound`
- `random`
- `os`

## Installation

Follow these steps to run the project:

1. Clone the project:
    ```sh
    git clone https://github.com/username/turkish-voice-assistant.git
    cd turkish-voice-assistant
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the project:
    ```sh
    python main.py
    ```

## Usage

When the application starts, it waits for voice commands from the user. Example commands and the application's responses:

- **"Nasılsın?"**: "I'm fine, thank you. How are you?"
- **"Haritaları aç"**: Opens Google Maps.
- **"Saat kaç?"**: Provides the current time.
- **"Hava durumu nasıl?"**: Opens the Turkish State Meteorological Service website.
- **"Arama yap"**: Asks the user for a search term and performs a Google search.
- **"Tamamdır", "Teşekkürler", "Bu kadar", "Bu kadardı", "Kapan"**: Closes the application.

## Contributing

If you would like to contribute, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

---

For questions or suggestions regarding the Turkish voice assistant project, please get in touch.
