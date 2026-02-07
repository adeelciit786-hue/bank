# Professional AI Banking Assistant Bot

A secure banking support chatbot powered by Mistral Large AI model.

## Features

✓ Answer general banking questions  
✓ Explain banking products and services  
✓ Provide security tips and best practices  
✓ Guide users through KYC and digital banking  
✓ Escalate to human support when needed  
✗ Never asks for sensitive data (account numbers, PINs, OTPs, passwords)  
✗ Never performs actual transactions  
✗ Never claims access to accounts  

## Setup Instructions

### 1. Create and Activate Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure API Key

1. Get your Mistral API key from: https://console.mistral.ai/api-keys
2. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
3. Edit `.env` and add your API key:
   ```
   MISTRAL_API_KEY=your_actual_api_key_here
   ```

**Security Note:** Never share your `.env` file or API key. The `.gitignore` file prevents accidental uploads.

### 4. Run the Bot

```powershell
python banking_bot.py
```

## Usage Examples

```
You: What are the different types of bank accounts?
Bot: [Provides explanation of account types]

You: How do I enable online banking?
Bot: [Provides step-by-step guidance]

You: Can you access my account balance?
Bot: [Professional refusal with escalation guidance]

You: What are some security tips for online banking?
Bot: [Provides helpful security advice]
```

## Bot Capabilities

### ✓ Can Help With:
- Account type explanations
- Card products and features
- Loan information and eligibility
- Generic interest rate explanations
- KYC (Know Your Customer) process
- Digital banking feature guidance
- Transaction explanations
- Banking hours and locations
- Security tips and best practices
- General banking questions
- Complaint handling and escalation

### ✗ Cannot Do:
- Access accounts or balances
- Perform transactions
- Ask for or store sensitive data
- Process payments
- Provide personalized financial advice
- Verify personal information

## Environment Variables

The bot uses environment variables for secure API key management:

```
MISTRAL_API_KEY     Your Mistral API key (from .env file)
```

## Commands

- `exit` - Exit the bot
- `clear` - Clear conversation history and start new session
- Any text otherwise - Send message to the bot

## Architecture

- **Model:** Mistral Large (Latest)
- **API:** Mistral AI API
- **Language:** Python 3.8+
- **Key Dependencies:** mistralai, python-dotenv

## Security Best Practices

1. **Never expose your API key** - Keep it in `.env` and never commit to version control
2. **Use environment variables** - Load sensitive config from `.env` file
3. **Clear conversation history** - Use 'clear' command to remove sensitive chat context
4. **Official channels** - Direct users to official support for account-specific issues
5. **Data privacy** - Bot never stores or forwards user data

## Troubleshooting

**"MISTRAL_API_KEY not found" error:**
- Ensure `.env` file exists in the same directory as `banking_bot.py`
- Check that your API key is correctly set in the `.env` file

**"Failed to connect to Mistral API":**
- Verify your internet connection
- Check that your API key is valid and hasn't expired
- Ensure you have available API credits on your Mistral account

## Support

For issues with:
- **The bot code:** Check the error message and refer to the Mistral documentation
- **Banking questions:** Use the bot itself or contact your bank's official support
- **API issues:** Visit https://console.mistral.ai

## License

This project is for educational and professional banking support purposes.
