# Runbook: payment gateway outage

Last reviewed: 8 Oct 2026.

Owner: Payments on-call. Severity: usually SEV2 (see [Incident severity levels](../engineering/incident-severity-levels.md)).

## Symptoms
Checkout success rate below 90% for 5 minutes, or the gateway's status page reports an incident.

## Steps
1. Confirm on the payments dashboard; check the gateway's status page.
2. Switch checkout to the backup gateway with the `payments.gateway=backup` feature flag.
3. Page the Payments on-call engineer. Outside working hours, follow
   [On-call escalation](oncall-escalation.md).
4. Post in #incidents every 30 minutes until resolved.
5. After recovery, run the reconciliation job for orders placed during the outage.

Never retry failed card charges automatically: customers may be charged twice.
