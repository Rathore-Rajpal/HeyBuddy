# Environment Variables Setup

This project uses environment variables to securely store API keys and secrets. These are stored in a `.env` file that is NOT tracked by git for security.

## Quick Setup

1. **Copy the example file:**
   ```bash
   copy .env.example .env
   ```

2. **Edit `.env` with your actual credentials:**
   - Open `.env` in any text editor
   - Replace placeholder values with your real API keys
   - Save the file

## Required API Keys

### 1. Spotify API (for music control)

**How to get:**
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in app name and description
5. Copy `Client ID` and `Client Secret`

**Add to .env:**
```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

### 2. HuggingFace API (for AI features)

**How to get:**
1. Create account at [HuggingFace](https://huggingface.co)
2. Go to [Settings → Tokens](https://huggingface.co/settings/tokens)
3. Click "New token"
4. Choose "Read" access
5. Copy the token

**Add to .env:**
```env
HuggingFaceApiKey=hf_xxxxxxxxxxxxxxxxxxxxx
```

## Security Notes

⚠️ **IMPORTANT:**
- Never commit `.env` to git (already in `.gitignore`)
- Never share your `.env` file or API keys publicly
- Keep `.env.example` updated with new variables (but NO real values)
- Regenerate API keys if accidentally exposed

## Files Using Environment Variables

- `assist/Engine/spotify.py` - Spotify integration
- `assist/Engine/image_generator.py` - AI image generation
- `assist/Engine/ImageBot/app.py` - Image generation API
- `assist/Engine/CodingBuddy/CodeBot.py` - AI code generation

## What's Protected

The `.gitignore` file excludes:
- `.env` - Your actual API keys
- `assist/Engine/cookies.json` - HuggingFace session cookies
- `buddy.db` - Your personal database
- `contacts.csv` - Your contacts
- Face recognition training data
- Generated screenshots and images

## Troubleshooting

**Error: "API key not found in .env file"**
- Make sure `.env` exists in the root directory
- Check that variable names match exactly (case-sensitive)
- Ensure no spaces around `=` in `.env` file

**Spotify/HuggingFace not working:**
- Verify API keys are valid and active
- Check internet connection
- Ensure `.env` file is in `C:\VirtualMouseProject\` (root)
