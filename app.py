from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="123456",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL inside Docker!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"{result[0]} 🚀"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
