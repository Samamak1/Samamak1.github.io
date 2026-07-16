from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resume" / "Sama-Mushtaq-Program-Project-Manager-Resume.pdf"

NAVY = colors.HexColor("#0A1426")
BLUE = colors.HexColor("#2854C5")
MUTED = colors.HexColor("#566071")
LINE = colors.HexColor("#D9DEE7")
PALE = colors.HexColor("#EEF1F8")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 0.31 * inch, LETTER[0] - doc.rightMargin, 0.31 * inch)
    canvas.setFont("Helvetica", 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.18 * inch, "Sama Mushtaq | Program & Project Leader")
    page_text = "Page 1"
    canvas.drawString(
        LETTER[0] - doc.rightMargin - stringWidth(page_text, "Helvetica", 6.8),
        0.18 * inch,
        page_text,
    )
    canvas.restoreState()


styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=24,
    leading=24,
    textColor=NAVY,
    spaceAfter=2,
)
title_style = ParagraphStyle(
    "Title",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.4,
    leading=11,
    tracking=0.6,
    textColor=BLUE,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.8,
    textColor=MUTED,
    alignment=TA_RIGHT,
)
summary_style = ParagraphStyle(
    "Summary",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.65,
    leading=11,
    textColor=NAVY,
    spaceAfter=5,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9,
    leading=10.5,
    tracking=0.9,
    textColor=NAVY,
    spaceBefore=6,
    spaceAfter=4,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.4,
    leading=9.9,
    textColor=NAVY,
)
date_style = ParagraphStyle(
    "Date",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.1,
    leading=8.7,
    textColor=MUTED,
    alignment=TA_RIGHT,
)
category_style = ParagraphStyle(
    "Category",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=6.6,
    leading=7.8,
    tracking=0.55,
    textColor=BLUE,
    spaceAfter=1,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.8,
    leading=9.6,
    leftIndent=9,
    firstLineIndent=-6,
    textColor=colors.HexColor("#354156"),
    spaceAfter=1.2,
)
compact_style = ParagraphStyle(
    "Compact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.4,
    textColor=colors.HexColor("#354156"),
    spaceAfter=1.2,
)
capability_style = ParagraphStyle(
    "Capabilities",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=7.05,
    leading=8.9,
    textColor=MUTED,
    backColor=PALE,
    borderPadding=(3, 5, 3, 5),
    spaceAfter=3,
)


def section(story, title):
    story.append(Paragraph(title.upper(), section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceAfter=2.5))


def role(story, company, title, dates, category, bullets):
    head = Table(
        [[Paragraph(f"<b>{company}</b> <font color='#566071'>| {title}</font>", role_style), Paragraph(dates, date_style)]],
        colWidths=[6.3 * inch, 1.0 * inch],
        hAlign="LEFT",
    )
    head.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    block = [head, Paragraph(category.upper(), category_style)]
    block.extend(Paragraph(f"- {item}", bullet_style) for item in bullets)
    block.append(Spacer(1, 3.4))
    story.append(KeepTogether(block))


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        rightMargin=0.45 * inch,
        leftMargin=0.45 * inch,
        topMargin=0.38 * inch,
        bottomMargin=0.40 * inch,
        title="Sama Mushtaq - Program & Project Manager Resume",
        author="Sama Mushtaq",
        subject="Program and project leadership resume",
    )

    header = Table(
        [
            [
                [Paragraph("Sama Mushtaq", name_style), Paragraph("PROGRAM &amp; PROJECT LEADER", title_style)],
                Paragraph(
                    "Cincinnati, Ohio<br/>sama.mushtaq.a@gmail.com<br/>"
                    "linkedin.com/in/samamushtaq<br/>github.com/Samamak1",
                    contact_style,
                ),
            ]
        ],
        colWidths=[5.0 * inch, 2.3 * inch],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story = [
        header,
        Spacer(1, 6),
        HRFlowable(width="100%", thickness=2.1, color=NAVY, spaceAfter=7),
        Paragraph(
            "Cross-functional program and operations leader with experience spanning approximately "
            "$30M in cumulative P&amp;L responsibility, teams of up to 120, zero-to-one launches, "
            "vendor-led technical delivery, and measurable operating transformations. Brings an "
            "operator's accountability to strategy, planning, stakeholder alignment, governance, "
            "adoption, and outcome measurement.",
            summary_style,
        ),
        Paragraph(
            "PROGRAM STRATEGY  |  PROJECT PLANNING  |  CROSS-FUNCTIONAL LEADERSHIP  |  ROADMAPS &amp; DEPENDENCIES  |  RAID &amp; GOVERNANCE  |  VENDOR MANAGEMENT  |  BUDGET &amp; P&amp;L  |  CHANGE MANAGEMENT  |  KPI DESIGN",
            capability_style,
        ),
    ]

    section(story, "Professional experience")
    role(
        story,
        "Mercor",
        "AI Annotator & Quality Reviewer, Contract",
        "Feb 2026-Present",
        "AI quality operations",
        [
            "Evaluate frontier-model outputs across finance, investment, strategy, business operations, engineering, and generalist work; advanced into reviewer responsibilities based on quality and judgment.",
        ],
    )
    role(
        story,
        "RYGNeco",
        "Co-Founder & Program Lead",
        "2025-Present",
        "Zero-to-one product and vendor program",
        [
            "Translated an enterprise e-waste pilot into four stakeholder portals spanning intake, testing, disposition, data-destruction records, pricing, and client reporting; directed an approximately $11.5K vendor-built MVP.",
            "Processed 400+ devices, catalogued approximately 480, tested and verified 130, and recorded zero OSHA recordables during pilot operations.",
        ],
    )
    role(
        story,
        "EPIC Brands",
        "General Manager, promoted from AGM",
        "Jul 2025-Feb 2026",
        "Operating portfolio and concept launch",
        [
            "Led a $10M portfolio with 70 hourly employees and six managers, contributing to 20-25% year-over-year growth; built an approximately $800K events pipeline and reduced controllable costs by 10%.",
            "Opened Whiskey Yard through SOP development, 30-person hiring and training, and a 150-label whiskey program; bar revenue increased 18%.",
        ],
    )
    role(
        story,
        "Darden Restaurants",
        "Manager-in-Training",
        "Mar 2025-Jul 2025",
        "Enterprise leadership development",
        [
            "Completed a structured management program in the top 5%, strengthening enterprise operating standards, leadership cadence, and service execution.",
        ],
    )
    role(
        story,
        "Hard Rock Casino Cincinnati",
        "Operations Manager to AGM to Acting GM",
        "Jan 2024-Jan 2025",
        "Operational transformation",
        [
            "Held responsibility across three F&amp;B outlets with approximately $17M in combined P&amp;L and 120 employees; recovered approximately $14K per month in variance, maintained inventory variance below 1%, and reduced labor by 10%.",
            "Raised alcohol mix from 13% to 22% and upsell rate from 9% to 17% through analysis, training, certification, and reinforcement.",
        ],
    )
    role(
        story,
        "iTZCALi Tapas & Tequila",
        "Director of Operations / Launch Consultant",
        "Sep 2022-Jan 2024",
        "High-volume launch program",
        [
            "Coordinated buildout, licensing, menus, vendors, pricing, POS, reservations, staffing, training, payroll, and launch readiness across a fixed opening window.",
            "Recruited and trained approximately 60 employees; generated $165K in the first 14 days, served up to 600 covers nightly, reduced the menu from 45 items to 12, and cut cocktail production from approximately two minutes to 30 seconds.",
        ],
    )
    role(
        story,
        "MAK Trading / Trade with MAK",
        "Founder & Program Lead",
        "Nov 2019-Present",
        "Digital community and growth program; monetized 2022-2023",
        [
            "Built a global education community that reached approximately 2,000 members across channels and 1,200+ paid subscribers at peak; a documented Stripe snapshot shows $28.7K MRR and 321 active subscriptions.",
            "Led brand, acquisition, onboarding, content operations, a 48-page curriculum, member engagement, and a LaunchPass/Stripe to WordPress/MemberPress migration.",
        ],
    )

    section(story, "Earlier experience")
    story.append(
        Paragraph(
            "<b>Napoli Italian Eatery</b> | Opening Manager / Operations Lead | 2021-2022 &nbsp;&nbsp; "
            "<b>MKEC</b> | Mechanical Design Engineer | 2019-2020 &nbsp;&nbsp; "
            "<b>Bella Luna Cafe</b> | GM / Multi-Unit Lead | 2016-2019",
            compact_style,
        )
    )

    section(story, "Education and credentials")
    story.append(
        Paragraph(
            "<b>Wichita State University</b> | Mechanical Engineering studies &nbsp;&nbsp; "
            "<b>University of Wales Trinity Saint David</b> | Business &amp; Management studies<br/>"
            "<b>ServSafe Manager</b> | Active through 2029 &nbsp;&nbsp; "
            "<b>Languages</b> | English, Arabic, Urdu, Hindi, Punjabi &nbsp;&nbsp; "
            "<b>Portfolio</b> | sama-mushtaq-program-portfolio.samamak.chatgpt.site",
            compact_style,
        )
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()
