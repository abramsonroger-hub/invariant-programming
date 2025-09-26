# SPDX-License-Identifier: Apache-2.0
     # Copyright 2025 Roger Abramson
     # Licensed under the Apache License, Version 2.0 (the "License");
     # you may not use this file except in compliance with the License.
     # You may obtain a copy of the License at [LICENSE.txt]

ledger = Ledger()
ledger.account("Recurrence")
ledger.account("ClosedForm")
ledger.account("Residuals")

@double_entry
def record_fib(n):
    recurrence = fib_recur(n)
    closed = fib_binet(n)
    diff = recurrence - closed
    
    debit("Recurrence", recurrence)
    credit("ClosedForm", closed)
    if diff != 0:
        debit("Residuals", diff)
        credit("Residuals", -diff)

for n in range(10):
    record_fib(n)

ledger.report()
