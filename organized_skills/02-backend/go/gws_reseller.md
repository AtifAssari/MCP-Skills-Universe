---
rating: ⭐⭐⭐
title: gws-reseller
url: https://skills.sh/googleworkspace/cli/gws-reseller
---

# gws-reseller

skills/googleworkspace/cli/gws-reseller
gws-reseller
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-reseller
Summary

Manage Google Workspace customer accounts, subscriptions, and reseller notifications through API commands.

Three resource categories: customers (create, retrieve, update accounts), subscriptions (activate, change plans/seats, suspend, list), and reseller notifications (register, watch, unregister)
Supports patch and full update semantics for customer settings; subscription operations include trial-to-paid conversion, renewal management, and transfer to direct
Requires gws binary and shared authentication setup from gws-shared/SKILL.md; use gws schema to inspect method parameters before execution
SKILL.md
reseller (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws reseller <resource> <method> [flags]

API Resources
customers
get — Gets a customer account. Use this operation to see a customer account already in your reseller management, or to see the minimal account information for an existing customer that you do not manage. For more information about the API response for existing customers, see retrieving a customer account.
insert — Orders a new customer's account.
patch — Updates a customer account's settings. This method supports patch semantics. You cannot update customerType via the Reseller API, but a "team" customer can verify their domain and become customerType = "domain". For more information, see Verify your domain to unlock Essentials features.
update — Updates a customer account's settings. You cannot update customerType via the Reseller API, but a "team" customer can verify their domain and become customerType = "domain". For more information, see update a customer's settings.
resellernotify
getwatchdetails — Returns all the details of the watch corresponding to the reseller.
register — Registers a Reseller for receiving notifications.
unregister — Unregisters a Reseller for receiving notifications.
subscriptions
activate — Activates a subscription previously suspended by the reseller. If you did not suspend the customer subscription and it is suspended for any other reason, such as for abuse or a pending ToS acceptance, this call will not reactivate the customer subscription.
changePlan — Updates a subscription plan. Use this method to update a plan for a 30-day trial or a flexible plan subscription to an annual commitment plan with monthly or yearly payments. How a plan is updated differs depending on the plan and the products. For more information, see the description in manage subscriptions.
changeRenewalSettings — Updates a user license's renewal settings. This is applicable for accounts with annual commitment plans only. For more information, see the description in manage subscriptions.
changeSeats — Updates a subscription's user license settings. For more information about updating an annual commitment plan or a flexible plan subscription’s licenses, see Manage Subscriptions.
delete — Cancels, suspends, or transfers a subscription to direct.
get — Gets a specific subscription. The subscriptionId can be found using the Retrieve all reseller subscriptions method. For more information about retrieving a specific subscription, see the information descrived in manage subscriptions.
insert — Creates or transfer a subscription. Create a subscription for a customer's account that you ordered using the Order a new customer account method.
list — Lists of subscriptions managed by the reseller. The list can be all subscriptions, all of a customer's subscriptions, or all of a customer's transferable subscriptions. Optionally, this method can filter the response by a customerNamePrefix. For more information, see manage subscriptions.
startPaidService — Immediately move a 30-day free trial subscription to a paid service subscription. This method is only applicable if a payment plan has already been set up for the 30-day trial subscription. For more information, see manage subscriptions.
suspend — Suspends an active subscription. You can use this method to suspend a paid subscription that is currently in the ACTIVE state. * For FLEXIBLE subscriptions, billing is paused. * For ANNUAL_MONTHLY_PAY or ANNUAL_YEARLY_PAY subscriptions: * Suspending the subscription does not change the renewal date that was originally committed to. * A suspended subscription does not renew.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws reseller --help

# Inspect a method's required params, types, and defaults
gws schema reseller.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
550
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn