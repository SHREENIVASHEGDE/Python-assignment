from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/data")
def main():
    response = requests.get("http://localhost:5000/data")

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed to retrieve data. Response code:", response.status_code)

if __name__ == "__main__":
    main()
    
def get_data():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run()
