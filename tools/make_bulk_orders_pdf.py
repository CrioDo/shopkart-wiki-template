"""Regenerates docs/policies/bulk-orders-policy.pdf (Crio maintainers only; learners never run it).
Needs reportlab:  pip install reportlab;  python tools/make_bulk_orders_pdf.py"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table

OUT = Path(__file__).resolve().parents[1] / "docs" / "policies" / "bulk-orders-policy.pdf"
s = getSampleStyleSheet()
story = [
    Paragraph("ShopKart bulk and business orders policy", s["Title"]),
    Paragraph("Version 3, approved by the Payments lead. Last reviewed: 1 Oct 2026.", s["Italic"]),
    Spacer(1, 12),
    Paragraph("1. Scope", s["Heading2"]),
    Paragraph("An order is a business order when it has more than 20 units of one item, or its total is over "
              "2 lakh rupees (200,000 rupees).", s["BodyText"]),
    Paragraph("2. Payment", s["Heading2"]),
    Paragraph("Business orders are paid by bank transfer or card only. Cash on delivery is not available, and "
              "promotional vouchers cannot be used. A GST number is required for the invoice.", s["BodyText"]),
    Paragraph("3. Delivery and returns", s["Heading2"]),
    Table([["Order size", "Delivery", "Returns"],
           ["21-100 units", "standard, free", "damaged units only, within 7 days"],
           ["over 100 units", "scheduled by Logistics, free", "damaged units only, within 3 days"]]),
    Spacer(1, 12),
    Paragraph("4. Approvals", s["Heading2"]),
    Paragraph("Business orders over 10 lakh rupees need approval from the Payments lead before they ship.",
              s["BodyText"]),
]
SimpleDocTemplate(str(OUT), pagesize=A4, title="ShopKart bulk orders policy").build(story)
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
