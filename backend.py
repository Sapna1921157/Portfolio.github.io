from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import logging

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sapnak7508@gmail.com'
app.config['MAIL_PASSWORD'] = 'nn'  # Use your app password here
# app.config['MAIL_DEFAULT_SENDER'] = 'sapnak7508@gmail.com'

mail = Mail(app)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extract values
        name = data.get('name')
        email = data.get('email')
        contact = data.get('contact')
        subject = data.get('subject')
        message = data.get('message')
        # recipient = data.get('recipient')

        # Log the incoming data
        app.logger.debug(f"Received data: {data}")

        if not email:
            return jsonify({"error": "email is required"}), 400

        body = f"Name: {name}\nEmail: {email}\nContact: {contact}\nMessage: {message}"

        msg = Message(subject, recipients=[email])
        msg.body = body
        mail.send(msg)

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        app.logger.error(f"Error sending email: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
