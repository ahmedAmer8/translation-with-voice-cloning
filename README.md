# 🎙️ Translation App with your own voice

A powerful multilingual voice translation application that converts English speech to multiple languages with voice cloning capabilities using ElevenLabs and AssemblyAI.

## ✨ Features

- **Voice Recording**: Record audio directly through your microphone
- **Speech-to-Text**: Transcribe English audio using AssemblyAI
- **Multi-language Translation**: Translate to 6 languages (Russian, Turkish, Arabic, German, Spanish, Japanese)
- **Text-to-Speech**: Generate natural-sounding audio in translated languages
- **Voice Cloning**: Use your own cloned voice from ElevenLabs for personalized translations
- **Web Interface**: User-friendly Gradio interface for easy interaction

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- AssemblyAI API key
- ElevenLabs API key (optional, for voice cloning)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ahmedAmer8/translation-with-voice-cloning.git
cd voice-translation-app
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```


3. **Set up environment variables:**

Create a `.env` file in the project root:
```env
ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=your_default_voice_id_here
```

### Running the Application

```bash
python app.py
```

The application will start and be available at `http://localhost:7860`

## 🎯 How to Use

### Basic Usage

1. **Record Audio**: Click the microphone button and speak in English
2. **Submit**: Click the "Submit" button to process your recording
3. **Listen**: The app will generate translations in 6 languages with audio output

### Advanced Usage with Voice Cloning

1. **Get your ElevenLabs API Key** (see Voice Cloning section below)
2. **Clone your voice** on ElevenLabs platform
3. **Enter your API key** in the "Your ElevenLabs API Key" field
4. **Enter your Voice ID** in the "Your Cloned Voice ID" field
5. **Record and submit** - your translations will use your cloned voice!

## 🗣️ Voice Cloning with ElevenLabs

### Step 1: Create an ElevenLabs Account

1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up for an account
3. Choose a subscription plan (free tier available with limitations)

### Step 2: Get Your API Key

1. Go to your [ElevenLabs Profile](https://elevenlabs.io/profile)
2. Copy your API key from the profile page
3. Add it to your `.env` file or enter it directly in the app

### Step 3: Clone Your Voice

1. **Navigate to Voice Lab**: Go to the "Voices" section in your ElevenLabs dashboard
2. **Click "Add Voice"**: Choose "Instant Voice Cloning"
3. **Upload Voice Samples**: 
   - Upload 1-25 audio files of your voice
   - Each file should be 30 seconds to 5 minutes long
   - Speak clearly and naturally
   - Include varied content (different emotions, topics)
4. **Name Your Voice**: Give your cloned voice a descriptive name
5. **Generate Voice**: Click "Add Voice" to create your clone
6. **Copy Voice ID**: Once created, copy the Voice ID (found in voice settings)

### Step 4: Use Your Cloned Voice

1. Enter your ElevenLabs API key in the app
2. Enter your cloned Voice ID
3. Record your English audio and submit
4. Enjoy hearing your translations in your own voice!

## 🌐 Using the Hugging Face Demo

### Access the Live Demo

The app is hosted on Hugging Face Spaces for easy access:

1. **Visit the Demo**: Go to `https://huggingface.co/spaces/[your-username]/voice-translation-app`
2. **No Installation Required**: Use the app directly in your browser
3. **Bring Your Own Keys**: Enter your ElevenLabs credentials for voice cloning

### Demo Features

- ✅ Full voice recording functionality
- ✅ Real-time translation to 6 languages
- ✅ Voice cloning support (with your API keys)
- ✅ Download generated audio files
- ✅ Mobile-friendly interface

### Limitations on Hugging Face

- Shared compute resources (may be slower during peak times)
- Session timeout after inactivity
- File storage is temporary

## 📋 Supported Languages

| Language | Code | Voice Quality |
|----------|------|---------------|
| Russian  | ru   | High          |
| Turkish  | tr   | High          |
| Arabic   | ar   | High          |
| German   | de   | High          |
| Spanish  | es   | High          |
| Japanese | ja   | High          |

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ASSEMBLYAI_API_KEY` | Your AssemblyAI API key for speech transcription | Yes |
| `ELEVENLABS_API_KEY` | Default ElevenLabs API key | Optional |
| `ELEVENLABS_VOICE_ID` | Default voice ID for text-to-speech | Optional |

### Voice Settings

The app uses optimized ElevenLabs voice settings:
- **Stability**: 0.5 (balanced consistency)
- **Similarity Boost**: 0.8 (high voice similarity)
- **Style**: 0.5 (moderate style expression)
- **Speaker Boost**: Enabled (enhanced voice characteristics)

## 🛠️ API Integration

### AssemblyAI Setup

1. Visit [AssemblyAI](https://www.assemblyai.com/)
2. Create an account and get your API key
3. Add it to your `.env` file

### ElevenLabs Setup

1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Create an account
3. Get your API key from the profile page
4. Optionally clone your voice for personalized translations

## 🔧 Troubleshooting

### Common Issues

**"API key not found" error:**
- Check your `.env` file exists and contains valid API keys
- Ensure no extra spaces or quotes around the keys

**"Voice ID not found" error:**
- Verify your ElevenLabs voice ID is correct
- Make sure the voice exists in your ElevenLabs account

**Audio recording issues:**
- Grant microphone permissions in your browser
- Check your microphone is working properly
- Try refreshing the page

**Translation quality issues:**
- Speak clearly and avoid background noise
- Keep recordings under 2 minutes for best results
- Ensure you're speaking in English

### Performance Tips

- Use a quiet environment for recording
- Speak at a normal pace and volume
- Keep audio recordings concise (30 seconds to 2 minutes)
- Check your internet connection for API calls

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the API documentation for [AssemblyAI](https://www.assemblyai.com/docs) and [ElevenLabs](https://docs.elevenlabs.io/)
3. Open an issue on GitHub with detailed error information

---

**Enjoy translating your voice into multiple languages! 🌍🎙️**
