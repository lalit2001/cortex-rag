import pandas as pd
from faker import Faker
import random


fake = Faker()


num_users = 100
num_payments = 1000
num_settlements = 200
num_disputes = 150
num_financial_data = 100


users_df = pd.DataFrame({
    'user_id': [fake.uuid4() for _ in range(num_users)],
    'user_name': [fake.name() for _ in range(num_users)],
    'user_email': [fake.email() for _ in range(num_users)],
    'user_phone': [fake.phone_number() for _ in range(num_users)]
})


payments_df = pd.DataFrame({
    'payment_id': [fake.uuid4() for _ in range(num_payments)],
    'user_id': [random.choice(users_df['user_id']) for _ in range(num_payments)],
    'amount': [round(random.uniform(10, 1000), 2) for _ in range(num_payments)],
    'payment_date': [fake.date_this_year() for _ in range(num_payments)],
    'status': [random.choice(['Completed', 'Pending', 'Failed']) for _ in range(num_payments)]
})


settlements_df = pd.DataFrame({
    'settlement_id': [fake.uuid4() for _ in range(num_settlements)],
    'payment_id': [random.choice(payments_df['payment_id']) for _ in range(num_settlements)],
    'settlement_date': [fake.date_this_year() for _ in range(num_settlements)],
    'amount_settled': [round(random.uniform(10, 1000), 2) for _ in range(num_settlements)],
    'settlement_status': [random.choice(['Settled', 'Pending']) for _ in range(num_settlements)]
})


disputes_df = pd.DataFrame({
    'dispute_id': [fake.uuid4() for _ in range(num_disputes)],
    'payment_id': [random.choice(payments_df['payment_id']) for _ in range(num_disputes)],
    'dispute_date': [fake.date_this_year() for _ in range(num_disputes)],
    'dispute_reason': [fake.sentence() for _ in range(num_disputes)],
    'dispute_status': [random.choice(['Open', 'Resolved', 'Rejected']) for _ in range(num_disputes)]
})


financial_data_df = pd.DataFrame({
    'financial_data_id': [fake.uuid4() for _ in range(num_financial_data)],
    'user_id': [random.choice(users_df['user_id']) for _ in range(num_financial_data)],
    'data_date': [fake.date_this_year() for _ in range(num_financial_data)],
    'financial_metric': [random.choice(['Balance', 'Credit Score', 'Income', 'Expenditure']) for _ in range(num_financial_data)],
    'value': [round(random.uniform(100, 50000), 2) for _ in range(num_financial_data)]
})


users_df.to_csv('data/users.csv', index=False)
payments_df.to_csv('data/payments.csv', index=False)
settlements_df.to_csv('data/settlements.csv', index=False)
disputes_df.to_csv('data/disputes.csv', index=False)
financial_data_df.to_csv('data/financial_data.csv', index=False)

print("Data generated and saved to 'users.csv', 'payments.csv', 'settlements.csv', 'disputes.csv', and 'financial_data.csv'.")
