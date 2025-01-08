import faker
import psycopg2
from datetime import datetime
import random


fake = faker.Faker()

def generate_transaction():
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow().timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'GBP']),
        'city': fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        'affiliateId': fake.uuid4()
    }

def create_table(conn):
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transactionid VARCHAR(255) PRIMARY KEY,
            userid VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            merchantname VARCHAR(255),
            paymentmethod VARCHAR(255),
            ipaddress VARCHAR(255),
            vouchercode VARCHAR(255),
            affiliateid VARCHAR(255)
        )
        """)

    cursor.close()
    conn.commit()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host='localhost',
        database='financial_db',
        user='postgres',
        password='postgres',
        port=5432
    )

    create_table(conn)

    transaction = generate_transaction()
    cur = conn.cursor()
    print(transaction)

    cur.execute(
        """
        INSERT INTO transactions(transactionid, userid, timestamp, amount, currency, city, country, merchantname, paymentmethod, 
        ipaddress, affiliateid, vouchercode)
        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (transaction["transactionId"], transaction["userId"], datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
              transaction["amount"], transaction["currency"], transaction["city"], transaction["country"],
              transaction["merchantName"], transaction["paymentMethod"], transaction["ipAddress"],
              transaction["affiliateId"], transaction["voucherCode"])
    )

    cur.close()
    conn.commit()