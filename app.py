from flask import Flask, render_template, request

import openai

app = Flask(__name__)

openai.api_key = "Your API key here"

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = ai(user_input)
        return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html")

def ai(components):
    prompt=f"You are a ai assistant provide the best answer of the question asked by the user {components}. As you are a ai assistant also remember the last query because the user can ask next query based on the last query"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text

if __name__ == "__main__":
    app.run(debug=True)
