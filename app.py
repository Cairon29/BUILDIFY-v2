from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('layout/index.html') 

@app.route('/admin')

def admin():
    return render_template('layout-admin/index.html')

if __name__ == '__main__':
    app.run(debug=True)
