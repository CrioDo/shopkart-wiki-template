# Architecture overview

Last reviewed: 14 Jun 2026.

ShopKart runs as about 40 services on Kubernetes. The ones support questions touch most: `checkout` (Payments),
`refunds` (Payments), `orders`, `logistics-gateway` (Logistics) and `search` (Platform, rebuilt nightly; see
[Search index rebuild](../runbooks/search-index-rebuild.md)).
