"""
Professional AI Banking Assistant Bot
Uses Mistral Large Model for accurate and secure banking support
"""

import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()

class BankingBot:
    """
    A professional banking assistant that provides secure and accurate support
    while strictly adhering to banking and data privacy regulations.
    """
    
    def __init__(self):
        """Initialize the banking bot with Mistral API client"""
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError(
                "MISTRAL_API_KEY not found. Please create a .env file "
                "with your Mistral API key. See .env.example for format."
            )
        
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"
        
        # System prompt that defines bot behavior
        self.system_prompt = """You are a professional AI Banking Assistant that provides accurate, secure, and user-friendly support while strictly following banking, financial, and data-privacy rules.

CAPABILITIES:
- Explain account types, cards, loans, and general interest rates
- Guide users through KYC processes, digital banking features, and transactions
- Provide banking hours, locations, and security tips
- Help with account inquiries and general banking questions
- Escalate complex issues to human support when needed

STRICT SAFETY RULES - NEVER DO THESE:
1. NEVER ask for or store sensitive data: account numbers, card details, PINs, OTPs, passwords
2. NEVER perform actual transactions
3. NEVER claim access to user accounts or personal information
4. NEVER provide specific investment advice (only general guidance)
5. NEVER process payments or financial transfers

BEHAVIORAL GUIDELINES:
- Maintain a polite, calm, and professional tone
- Use simple, clear language that's easy to understand
- Always clarify that information provided is general guidance
- Encourage users to verify information through official bank channels
- Politely refuse sensitive requests without being accusatory
- Direct users to official support for account-specific queries
- Handle complaints with empathy and proper escalation procedures

When users ask for sensitive information, respond with:
"I appreciate your trust, but I cannot [action]. For security reasons, please contact our official support team at [general support method]. Your security is our priority."
"""
        
        self.conversation_history = []
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the banking bot and get a response
        
        Args:
            user_message: The user's question or request
            
        Returns:
            The bot's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Prepare messages list
            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history
            ]
            
            # Call Mistral API
            response = self.client.chat.complete(
                model=self.model,
                messages=messages
            )
            
            # Extract and store assistant response
            bot_response = response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": bot_response
            })
            
            return bot_response
            
        except Exception as e:
            error_msg = f"Error communicating with Mistral API: {str(e)}"
            print(f"Error: {error_msg}")
            return error_msg
    
    def clear_history(self):
        """Clear conversation history for a new session"""
        self.conversation_history = []
    
    def get_history(self) -> list:
        """Get the current conversation history"""
        return self.conversation_history


def main():
    """Main function to run the banking bot in interactive mode"""
    print("=" * 60)
    print("Welcome to Professional AI Banking Assistant")
    print("=" * 60)
    print("\nI'm here to help with banking inquiries, account information,")
    print("and general banking guidance. For security reasons, I cannot")
    print("access your account or handle sensitive financial data.")
    print("\nType 'exit' to quit, 'clear' to start a new conversation")
    print("=" * 60 + "\n")
    
    try:
        bot = BankingBot()
        print("✓ Bot initialized successfully!\n")
    except ValueError as e:
        print(f"✗ Failed to initialize bot: {e}")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Banking Assistant. Goodbye!")
                break
            
            if user_input.lower() == 'clear':
                bot.clear_history()
                print("Conversation history cleared.\n")
                continue
            
            print("\nBot: ", end="", flush=True)
            response = bot.chat(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\nChat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
