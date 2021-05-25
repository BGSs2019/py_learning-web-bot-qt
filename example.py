# Function VAT
def get_vat(payment, percent=20):
	try:
		payment = float(payment)
		vat = payment/100*percent
		vat = round(vat, 2)
		return "Sum VAT: {}".format(vat)
	except TypeError:
		return "Can't count. Check data!"


result = get_vat(400,15)
print(result)