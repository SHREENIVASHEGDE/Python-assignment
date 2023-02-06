from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/company/<string:company_name>", methods=["GET"])
def get_company_data(company_name):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM company_data WHERE company_name=? and company_id=?", (company_name, company_id))
    data = c.fetchall()
    conn.close()

    if data:
        return jsonify(data)
    else:
        return "No data found for company '{}' of company id '{}'".format(company_name), 404

if __name__ == "__main__":
    app.run()
