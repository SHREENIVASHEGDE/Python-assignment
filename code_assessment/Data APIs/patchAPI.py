from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/company/<string:company_name>/<string:date>", methods=["PATCH"])
def update_company_data(company_name, date):
    data = request.get_json()
    new_stock_price = data.get("stock_price")

    if new_stock_price is None:
        return "Missing 'stock_price' in request body", 400

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE company_data SET stock_price=? WHERE company_name=? AND date=?", (new_stock_price, company_name, date))
    conn.commit()
    conn.close()

    return "Stock price for company '{}' on date '{}' has been updated to {}".format(company_name, date, new_stock_price), 200

if __name__ == "__main__":
    app.run()
