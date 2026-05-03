---
title: reconciliation
url: https://skills.sh/anthropics/knowledge-work-plugins/reconciliation
---

# reconciliation

skills/anthropics/knowledge-work-plugins/reconciliation
reconciliation
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill reconciliation
SKILL.md
Reconciliation

Important: This skill assists with reconciliation workflows but does not provide financial advice. All reconciliations should be reviewed by qualified financial professionals before sign-off.

Methodology and best practices for account reconciliation, including GL-to-subledger, bank reconciliations, and intercompany. Covers reconciling item categorization, aging analysis, and escalation.

Reconciliation Types
GL to Subledger Reconciliation

Compare the general ledger control account balance to the detailed subledger balance.

Common accounts:

Accounts receivable (GL control vs AR subledger aging)
Accounts payable (GL control vs AP subledger aging)
Fixed assets (GL control vs fixed asset register)
Inventory (GL control vs inventory valuation report)
Prepaid expenses (GL control vs prepaid amortization schedule)
Accrued liabilities (GL control vs accrual detail schedules)

Process:

Pull GL balance for the control account as of period end
Pull subledger trial balance or detail report as of the same date
Compare totals — they should match if posting is real-time
Investigate any differences (timing of posting, manual entries not reflected, interface errors)

Common causes of differences:

Manual journal entries posted to the control account but not reflected in the subledger
Subledger transactions not yet interfaced to the GL
Timing differences in batch posting
Reclassification entries in the GL without subledger adjustment
System interface errors or failed postings
Bank Reconciliation

Compare the GL cash balance to the bank statement balance.

Process:

Obtain the bank statement balance as of period end
Pull the GL cash account balance as of the same date
Identify outstanding checks (issued but not cleared at the bank)
Identify deposits in transit (recorded in GL but not yet credited by bank)
Identify bank charges, interest, or adjustments not yet recorded in GL
Reconcile both sides to an adjusted balance

Standard format:

Balance per bank statement:         $XX,XXX
Add: Deposits in transit            $X,XXX
Less: Outstanding checks           ($X,XXX)
Add/Less: Bank errors               $X,XXX
Adjusted bank balance:              $XX,XXX

Balance per general ledger:         $XX,XXX
Add: Interest/credits not recorded  $X,XXX
Less: Bank fees not recorded       ($X,XXX)
Add/Less: GL errors                 $X,XXX
Adjusted GL balance:                $XX,XXX

Difference:                         $0.00

Intercompany Reconciliation

Reconcile balances between related entities to ensure they net to zero on consolidation.

Process:

Pull intercompany receivable/payable balances for each entity pair
Compare Entity A's receivable from Entity B to Entity B's payable to Entity A
Identify and resolve differences
Confirm all intercompany transactions have been recorded on both sides
Verify elimination entries are correct for consolidation

Common causes of differences:

Transactions recorded by one entity but not the other (timing)
Different FX rates used by each entity
Misclassification (intercompany vs third-party)
Disputed amounts or unapplied payments
Different period-end cut-off practices across entities
Reconciling Item Categorization
Category 1: Timing Differences

Items that exist because of normal processing timing and will clear without action:

Outstanding checks: Checks issued and recorded in GL, pending bank clearance
Deposits in transit: Deposits made and recorded in GL, pending bank credit
In-transit transactions: Items posted in one system but pending interface to the other
Pending approvals: Transactions awaiting approval to post in one system

Expected resolution: These items should clear within the normal processing cycle (typically 1-5 business days). No adjusting entry needed.

Category 2: Adjustments Required

Items that require a journal entry to correct:

Unrecorded bank charges: Bank fees, wire charges, returned item fees
Unrecorded interest: Interest income or expense from bank/lender
Recording errors: Wrong amount, wrong account, duplicates
Missing entries: Transactions in one system with no corresponding entry in the other
Classification errors: Correctly recorded but in the wrong account

Action: Prepare adjusting journal entry to correct the GL or subledger.

Category 3: Requires Investigation

Items that cannot be immediately explained:

Unidentified differences: Variances with no obvious cause
Disputed items: Amounts contested between parties
Aged outstanding items: Items that have not cleared within expected timeframes
Recurring unexplained differences: Same type of difference appearing each period

Action: Investigate root cause, document findings, escalate if unresolved.

Aging Analysis for Outstanding Items

Track the age of reconciling items to identify stale items requiring escalation:

Age Bucket	Status	Action
0-30 days	Current	Monitor — within normal processing cycle
31-60 days	Aging	Investigate — follow up on why item has not cleared
61-90 days	Overdue	Escalate — notify supervisor, document investigation
90+ days	Stale	Escalate to management — potential write-off or adjustment needed
Aging Report Format
Item #	Description	Amount	Date Originated	Age (Days)	Category	Status	Owner
1	[Detail]	$X,XXX	[Date]	XX	[Type]	[Status]	[Name]
Trending

Track reconciling item totals over time to identify growing balances:

Compare total outstanding items to prior period
Flag if total reconciling items exceed materiality threshold
Flag if number of items is growing period over period
Identify recurring items that appear every period (may indicate process issue)
Escalation Thresholds

Define escalation triggers based on your organization's risk tolerance:

Trigger	Threshold (Example)	Escalation
Individual item amount	> $10,000	Supervisor review
Individual item amount	> $50,000	Controller review
Total reconciling items	> $100,000	Controller review
Item age	> 60 days	Supervisor follow-up
Item age	> 90 days	Controller / management review
Unreconciled difference	Any amount	Cannot close — must resolve or document
Growing trend	3+ consecutive periods	Process improvement investigation

Note: Set thresholds based on your organization's materiality level and risk appetite. The examples above are illustrative.

Reconciliation Best Practices
Timeliness: Complete reconciliations within the close calendar deadline (typically T+3 to T+5 business days after period end)
Completeness: Reconcile all balance sheet accounts on a defined frequency (monthly for material accounts, quarterly for immaterial)
Documentation: Every reconciliation should include preparer, reviewer, date, and clear explanation of all reconciling items
Segregation: The person who reconciles should not be the same person who processes transactions in that account
Follow-through: Track open items to resolution — do not just carry items forward indefinitely
Root cause analysis: For recurring reconciling items, investigate and fix the underlying process issue
Standardization: Use consistent templates and procedures across all accounts
Retention: Maintain reconciliations and supporting detail per your organization's document retention policy
Weekly Installs
1.0K
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass