from collections import defaultdict

def calculate_settlement(event):
    # Userごとの総支払額を計算する
    total_paid_by_user = defaultdict(float)
    total_amount_owed_by_user = defaultdict(float)
    
    payments = event.payment_set.all()
    
    for payment in payments:
        payer = payment.payer
        total_paid_by_user[payer] += payment.amount
        
        num_payees = payment.payee.count()
        if num_payees > 0:
            amount_per_payee = round(payment.amount / num_payees)
            for payee in payment.payee.all():
                total_amount_owed_by_user[payee] += amount_per_payee
    
    # 各Userの精算結果を計算する
    net_balance_by_user = defaultdict(float)
    for user in set(total_paid_by_user.keys()).union(total_amount_owed_by_user.keys()):
        net_balance_by_user[user] = total_paid_by_user[user] - total_amount_owed_by_user[user]
    
    # 最終的な受け渡しを計算する
    settlement = defaultdict(dict)
    positive_balances = sorted([(user, balance) for user, balance in net_balance_by_user.items() if balance > 0], key=lambda x: -x[1])
    negative_balances = sorted([(user, -balance) for user, balance in net_balance_by_user.items() if balance < 0], key=lambda x: -x[1])
    
    while positive_balances and negative_balances:
        payer, amount_to_receive = positive_balances.pop(0)
        payee, amount_to_pay = negative_balances.pop(0)
        
        if amount_to_receive > amount_to_pay:
            settlement[payee][payer] = int(amount_to_pay)
            positive_balances.insert(0, (payer, amount_to_receive - amount_to_pay))
        elif amount_to_receive < amount_to_pay:
            settlement[payee][payer] = int(amount_to_receive)
            negative_balances.insert(0, (payee, amount_to_pay - amount_to_receive))
        else:
            settlement[payee][payer] = int(amount_to_receive)
    
    return dict(settlement)
