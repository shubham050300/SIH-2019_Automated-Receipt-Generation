import os
import csv
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automatic_receipt_generation.settings')

import django
django.setup()

from req_receipt.models import Card_Transactions, Cheque_Transactions

new_format = '%Y-%m-%dT%H:%M:%S.%fZ'
old_format = '%m/%d/%Y %H:%M:%S'

def read_csv(filename) :
	base_dir = os.path.dirname(os.path.abspath(__file__))
	SAP_dir = os.path.join(base_dir, 'media', 'SAP')
	filepath = os.path.join(SAP_dir, filename)
	extracted_data = list()
	with open(filepath) as csv_file :
		csv_reader = csv.reader(csv_file, delimiter = ',')
		for row in csv_reader :
			extracted_data.append(row)
	return extracted_data

extracted_data_cheque = read_csv('Cheque_Transactions.csv')
extracted_data_card = read_csv('Card_Transactions.csv')
print(len(extracted_data_cheque))
def add_transactions(data, table) :
	for i in range(len(data)) :
		if i == 0 :
			pass
		else :
			dt = data[i][0]
			dt = datetime.datetime.strptime(dt, old_format).strftime(new_format)
			tid = data[i][1]
			vid = data[i][2]
			vname = data[i][3]
			vemail = data[i][4]
			amt = data[i][5]
			t = table.objects.get_or_create(date=dt, Transaction_ID=tid,
																 Vendor_ID=vid, Vendor_Name=vname,
																 Vendor_email=vemail, Amount=amt)[0]
	return t

add_transactions(extracted_data_cheque, Cheque_Transactions)
add_transactions(extracted_data_card, Card_Transactions)


			






