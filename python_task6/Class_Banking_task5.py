cust_data =  [
    {
        'cust_name': 'cust1',
        'cust_id': 101,
        'balance': 200,
        'opening_date': '01-01-2026',
        'acc_type': 'saving'
    },
    {
        'cust_name': 'cust2',
        'cust_id': 102,
        'balance': 300,
        'opening_date': '02-01-2026',
        'acc_type': 'current'
    },
    {
        'cust_name': 'cust3',
        'cust_id': 103,
        'balance': 400,
        'opening_date': '03-01-2026',
        'acc_type': 'saving'
    },
    {
        'cust_name': 'cust4',
        'cust_id': 104,
        'balance': 500,
        'opening_date': '04-01-2026',
        'acc_type': 'current'
    },
    {
        'cust_name': 'cust5',
        'cust_id': 105,
        'balance': 600,
        'opening_date': '05-01-2026',
        'acc_type': 'saving'
    }
]
    


class Bank:
    cust_name = ''
    cust_id = 0
    balance = 0
    opening_date = ''
    acc_type = ''

    def __init__(self, custData):
        self.cust_name = custData.get('cust_name')
        self.cust_id = custData.get('cust_id')
        self.balance = custData.get('balance')
        self.opening_date = custData.get('opening_date')
        self.acc_type = custData.get('acc_type')


for cust in cust_data:
    print('customer bank details')
    bank_cust = Bank(cust)
    print('name =', bank_cust.cust_name)
    print('id =', bank_cust.cust_id)
    print('balance =', bank_cust.balance)
    print('-'*10)