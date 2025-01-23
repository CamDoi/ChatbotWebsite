from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def home():
    return render_template("layout.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    # Get user input from the POST request
    user_input = request.json.get("user_input")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Call OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract the assistant's response
        assistant_response = response['choices'][0]['message']['content']

        # Return the response as JSON
        return jsonify({"response": assistant_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
