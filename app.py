from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return send_file('w.html')

if __name__ == '__main__':
    app.run(debug=True)
