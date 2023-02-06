from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/company/<string:company_name>/<string:date>", methods=["GET"])
def get_company_data(company_name, date):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM company_data WHERE company_name=?, company_id=? AND date=?", (company_name,company_id, date))
    data = c.fetchone()
    conn.close()

    if data:
        return jsonify(data)
    else:
        return "No data found for company '{}' of companyid '{}' on date '{}'".format(company_name,company_id, date), 404

if __name__ == "__main__":
    app.run()
