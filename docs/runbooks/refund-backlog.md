# Runbook: refund backlog

Last reviewed: 1 May 2026.

Owner: Payments on-call. If more than 2,000 refunds are pending for over 24 hours:
1. Check the refund worker's queue depth and error log.
2. If the bank API returns 429 errors, lower the worker's rate to 5 requests a second and let it drain.
3. Tell Customer Support (see [Customer Support team](../teams/customer-support.md)) to use the
   "refund delayed" macro.
4. Refunds older than 10 working days are escalated to the Payments lead.
