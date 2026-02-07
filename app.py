from flask import Flask, render_template, request, jsonify
from banking_bot import BankingBot
import os

app = Flask(__name__)

# Initialize the banking bot
try:
    bot = BankingBot()
    bot_initialized = True
except Exception as e:
    bot = None
    bot_initialized = False
    error_message = str(e)

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint to send a message and get a response"""
    if not bot_initialized:
        return jsonify({
            'error': f'Bot not initialized: {error_message}'
        }), 500
    
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    # Handle special commands
    if user_message.lower() == 'clear':
        bot.clear_history()
        return jsonify({'response': 'Conversation history cleared.'})
    
    try:
        response = bot.chat(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    if not bot_initialized:
        return jsonify({'error': 'Bot not initialized'}), 500
    
    return jsonify({'history': bot.get_history()})

@app.route('/api/clear', methods=['POST'])
def clear():
    """Clear conversation history"""
    if not bot_initialized:
        return jsonify({'error': 'Bot not initialized'}), 500
    
    bot.clear_history()
    return jsonify({'message': 'Conversation cleared'})

@app.route('/api/status', methods=['GET'])
def status():
    """Check bot status"""
    return jsonify({
        'initialized': bot_initialized,
        'model': 'mistral-large-latest' if bot_initialized else 'N/A'
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Professional AI Banking Assistant - Web Interface")
    print("=" * 60)
    print(f"\nBot Status: {'✓ Ready' if bot_initialized else '✗ Failed to initialize'}")
    if not bot_initialized:
        print(f"Error: {error_message}")
    print("\n🌐 Open your browser and visit:")
    print("   http://localhost:5000")
    print("\n" + "=" * 60 + "\n")
    
    app.run(debug=True, host='localhost', port=5000)
