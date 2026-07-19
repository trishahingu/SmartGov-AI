import os
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_report(data):

    filename = f"verification_report_{data['document'].get('aadhaar_number','unknown')}.pdf"

    filepath = os.path.join(REPORT_FOLDER, filename)

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>SmartGov AI Verification Report</b>", styles["Title"])

    elements.append(title)

    elements.append(Spacer(1, 20))

    document = data.get("document", {})

    trust = data.get("trust", {})

    forgery = data.get("forgery", {})

    liveness = data.get("liveness", {})

    face = data.get("face", {})

    table_data = [

        ["Field", "Value"],

        ["Citizen Name", document.get("name", "Not Found")],

        ["Aadhaar Number", document.get("aadhaar_number", "Not Found")],

        ["Date of Birth", document.get("dob", "Not Found")],

        ["Gender", document.get("gender", "Not Found")],

        ["Face Detected", "Yes" if face.get("face_detected") else "No"],

        ["Face Count", str(face.get("face_count", 0))],

        ["Face Confidence", f"{face.get('confidence',0)} %"],

        ["Liveness", liveness.get("status", "Unknown")],

        ["Forgery Status", forgery.get("status", "Unknown")],

        ["Forgery Confidence", f"{forgery.get('confidence',0)} %"],

        ["Trust Score", str(trust.get("trust_score", 0))],

        ["Risk Level", trust.get("risk_level", "Unknown")],

        ["Verification Status", trust.get("status", "Unknown")]

    ]

    table = Table(table_data, colWidths=[170, 250])

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.black),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ]

        )

    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    elements.append(

        Paragraph("<b>Reasons</b>", styles["Heading2"])

    )

    for reason in trust.get("reasons", []):

        elements.append(

            Paragraph("• " + reason, styles["BodyText"])

        )

    doc.build(elements)

    return {

        "success": True,

        "report_path": filepath,

        "filename": filename

    }