from flask import Flask, render_template, jsonify




app = Flask(__name__)
app.config.from_object('config')

















if __name__ == "__main__":
	app.run()

