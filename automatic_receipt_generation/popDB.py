import os
import csv
import datetime
import hashlib
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automatic_receipt_generation.settings')

import django
django.setup()

from req_receipt.models import Card_Transactions, Cheque_Transactions

new_format = '%Y-%m-%dT%H:%M:%S.%fZ'
old_format1 = '%m/%d/%Y %H:%M:%S'
old_format = '%m-%d-%y %H:%M'


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
			if '-' in dt :
				dt = datetime.datetime.strptime(dt, old_format).strftime(new_format)
			elif '/' in dt :
				dt = datetime.datetime.strptime(dt, old_format1).strftime(new_format)
			tid = data[i][1]
			vid = data[i][2]
			vname = data[i][3]
			vemail = data[i][4]
			amt = data[i][5]
			pro = data[i][6]
			t_per = data[i][7]
			t_amt = data[i][8]
			d_per = data[i][9]
			d_amt = data[i][10]
			temp_str = str(datetime.datetime.now().time()) + str(vid) + str(tid)
			unique_key = hashlib.md5(temp_str.encode()).hexdigest()
			unique_key = unique_key[:16]
			t = table.objects.get_or_create(date=dt, Transaction_ID=tid,
											Vendor_ID=vid, Vendor_Name=vname,
											Vendor_email=vemail, Total_Amount=amt,
											Products=pro, Tax_per=t_per,
											Tax_amount=t_amt, Discount_per=d_per,
											Discount=d_amt, unique_key=unique_key)[0]
	return t

add_transactions(extracted_data_cheque, Cheque_Transactions)
add_transactions(extracted_data_card, Card_Transactions)


			






