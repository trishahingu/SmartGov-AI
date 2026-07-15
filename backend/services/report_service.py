from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os

REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report(document, forgery, trust):

    filename = "verification_report.pdf"

    filepath = os.path.join(
        REPORT_DIR,
        filename
    )

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filepath)

    story = []

    story.append(
        Paragraph(
            "<b>🏛 SmartGov AI Verification Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Document Type:</b> {document['document_type']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Document Number:</b> {document['document_number']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>DOB:</b> {document['dob']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Gender:</b> {document['gender']}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Forgery Score:</b> {forgery['score']}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Status:</b> {forgery['status']}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Trust Score:</b> {trust['trust_score']}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Trust Level:</b> {trust['trust_level']}",
            styles["Normal"]
        )
    )

    pdf.build(story)

    return filepath