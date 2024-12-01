from flask import Flask, render_template
from src.routes import home_bp
from src.models import top_df

app = Flask(__name__, template_folder="templates")
app.register_blueprint(home_bp)


@app.route("/")
def home():
    return render_template("top.html", items=top_df[top_df["type"] == "lists"])


if __name__ == "__main__":
    app.run(debug=True)
