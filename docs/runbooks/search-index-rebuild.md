# Runbook: search index rebuild

Last reviewed: 12 Mar 2026.

Owner: Platform. The product search index rebuilds every night at 02:00 IST. If the rebuild fails:
1. Check the job log; the usual cause is a malformed catalog feed from one seller.
2. Re-run with that seller's feed excluded (`--skip-seller <id>`).
3. If search is stale for more than 24 hours, raise a SEV3.
