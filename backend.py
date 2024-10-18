from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sapnak7508@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'nnec rhqc smfg czek'     # App password generated from Google
app.config['MAIL_DEFAULT_SENDER'] = 'sapnak7508@gmail.com'  # Default sender email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')  # Assuming your form is saved as contact_form.html

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json

        # Extract form data
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        if not (name and email and subject and message):
            return jsonify({"error": "All fields are required."}), 400

        # Compose email
        msg = Message(subject=subject, recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send email
        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug= True)
