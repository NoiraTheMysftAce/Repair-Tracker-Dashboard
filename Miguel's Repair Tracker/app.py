import sqlite3

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("repairs.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            device_name TEXT NOT NULL,
            reported_issue TEXT,
            date_received TEXT,
            device_condition TEXT,
            customer_phone TEXT,
            accessories_received TEXT,
            serial_number TEXT,
            status TEXT DEFAULT 'Received'
        )
    """)

    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        customer_name = request.form.get("customerName")
        device_name = request.form.get("deviceName")
        reported_issue = request.form.get("reportedIssue")
        date_received = request.form.get("dateReceived")
        device_condition = request.form.get("deviceCondition")
        customer_phone = request.form.get("customerPhone")
        accessories_received = request.form.get("accessoriesReceived")
        serial_number = request.form.get("serialNumber")
        conn = sqlite3.connect("repairs.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO repairs (
                customer_name,
                device_name,
                reported_issue,
                date_received,
                device_condition,
                customer_phone,
                accessories_received,
                serial_number
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            customer_name,
            device_name,
            reported_issue,
            date_received,
            device_condition,
            customer_phone,
            accessories_received,
            serial_number
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
