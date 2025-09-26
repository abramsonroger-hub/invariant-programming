# SPDX-License-Identifier: Apache-2.0
     # Copyright 2025 Roger Abramson
     # Licensed under the Apache License, Version 2.0 (the "License");
     # you may not use this file except in compliance with the License.
     # You may obtain a copy of the License at [LICENSE.txt]

🏛 Double-Entry Programming Language (DEPL) Prototype

# Define a ledger to hold all debits and credits
ledger = Ledger()

# Declare an account
ledger.account("Cash")
ledger.account("Sales")
ledger.account("Equity")

# Double-entry operation (must balance)
@double_entry
def record_sale(amount):
    debit("Cash", amount)
    credit("Sales", amount)

# Example transaction
record_sale(100)

# Checkpoint: trial balance
if ledger.balance():
    print("Books are balanced ✅")
else:
    print("Imbalance detected ❌")

# Closing entries (transfer profit to equity)
@closing_entry
def close_sales():
    balance = ledger.get_balance("Sales")
    debit("Sales", balance)
    credit("Equity", balance)

close_sales()

ledger.report()
