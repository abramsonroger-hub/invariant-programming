# 🏛 Double-Entry Programming Language (DEPL) Prototype

## 🔑 Key Features of DEPL

Mandatory Dual Posting

@double_entry decorator forces equal debit and credit entries.

Compiler/runtime blocks code if imbalance occurs.

Residuals Exposed

If imbalance exists, it’s logged in Residuals account, never hidden.

Trial Balance Checkpoints

Periodic ledger.balance() ensures no cascade errors.

Equivalent to preventing hallucination drift.

Closing Entries = Cascade Prevention

@closing_entry rolls temporary accounts (like “Sales” or “Drift”) into permanent ones (“Equity” or “Truth”).

Stops noise from compounding indefinitely.

Auditable by Design

Every function is a posted entry.

Every error is an imbalance visible in the books.
