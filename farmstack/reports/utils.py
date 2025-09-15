import io
import pandas as pd
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def export_sales_excel(queryset):
    df = pd.DataFrame([
        {
            'id': s.id,
            'customer': getattr(s.customer, 'name', ''),
            'date': s.date,
            'total_amount': float(s.total_amount),
        } for s in queryset
    ])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sales')
    output.seek(0)
    resp = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    resp['Content-Disposition'] = 'attachment; filename="sales.xlsx"'
    return resp


def export_finance_pdf(queryset):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont('Helvetica', 12)
    y = 800
    p.drawString(50, y, 'Finance Report')
    y -= 30
    for r in queryset[:100]:
        p.drawString(50, y, f"{r.date} {r.record_type} {r.category} {float(r.amount)}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    buffer.seek(0)
    resp = HttpResponse(buffer, content_type='application/pdf')
    resp['Content-Disposition'] = 'attachment; filename="finance.pdf"'
    return resp

