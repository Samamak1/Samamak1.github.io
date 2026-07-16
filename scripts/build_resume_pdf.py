from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resume" / "Sama-Mushtaq-Program-Project-Manager-Resume.pdf"

NAVY = colors.HexColor("#0A1426")
BLUE = colors.HexColor("#2854C5")
MUTED = colors.HexColor("#566071")
LINE = colors.HexColor("#D9DEE7")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 0.43 * inch, LETTER[0] - doc.rightMargin, 0.43 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.27 * inch, "Sama Mushtaq | Program & Project Leader")
    page_text = f"Page {doc.page}"
    canvas.drawString(
        LETTER[0] - doc.rightMargin - stringWidth(page_text, "Helvetica", 7.5),
        0.27 * inch,
        page_text,
    )
    canvas.restoreState()


styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=22,
    leading=24,
    textColor=NAVY,
    alignment=TA_CENTER,
    spaceAfter=2,
)
title_style = ParagraphStyle(
    "Title",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.5,
    leading=12,
    textColor=BLUE,
    alignment=TA_CENTER,
    spaceAfter=3,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.2,
    leading=10,
    textColor=MUTED,
    alignment=TA_CENTER,
    spaceAfter=10,
)
summary_style = ParagraphStyle(
    "Summary",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.8,
    leading=11.4,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceAfter=8,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=9.2,
    leading=11,
    textColor=BLUE,
    spaceBefore=7,
    spaceAfter=4,
    borderWidth=0,
    borderPadding=0,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.6,
    leading=10.4,
    textColor=NAVY,
    spaceBefore=4,
    spaceAfter=1,
)
category_style = ParagraphStyle(
    "Category",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=6.8,
    leading=8.2,
    tracking=0.7,
    textColor=BLUE,
    spaceAfter=1.5,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.15,
    leading=10.1,
    leftIndent=10,
    firstLineIndent=-7,
    textColor=NAVY,
    spaceAfter=1.6,
)
small_style = ParagraphStyle(
    "Small",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.1,
    leading=10.2,
    textColor=NAVY,
    spaceAfter=2.2,
)


def section(story, title):
    story.append(Paragraph(title.upper(), section_style))


def role(story, company, title, dates, category, bullets):
    story.append(
        Paragraph(
            f"<b>{company}</b> | {title} | <b>{dates}</b>",
            role_style,
        )
    )
    story.append(Paragraph(category.upper(), category_style))
    for item in bullets:
        story.append(Paragraph(f"- {item}", bullet_style))


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.58 * inch,
        title="Sama Mushtaq - Program & Project Manager Resume",
        author="Sama Mushtaq",
        subject="Program and project leadership resume",
    )

    story = [
        Paragraph("Sama Mushtaq", name_style),
        Paragraph("PROGRAM & PROJECT LEADER", title_style),
        Paragraph(
            "Cincinnati, Ohio | sama.mushtaq.a@gmail.com | "
            "linkedin.com/in/samamushtaq | github.com/Samamak1",
            contact_style,
        ),
        Paragraph(
            "Cross-functional program and operations leader with experience spanning approximately "
            "$30M in cumulative P&amp;L responsibility, teams of up to 120, zero-to-one launches, "
            "vendor-led technical delivery, and measurable operating transformations. Brings an "
            "operator's accountability to strategy, planning, stakeholder alignment, governance, "
            "adoption, and outcome measurement.",
            summary_style,
        ),
    ]

    section(story, "Core capabilities")
    story.append(
        Paragraph(
            "Program Strategy | Project Planning | Cross-Functional Leadership | Roadmaps &amp; "
            "Dependencies | RAID &amp; Governance | Executive Communication | Vendor Management | "
            "Budget &amp; P&amp;L | Change Management | Process Improvement | AI &amp; Data Operations | KPI Design",
            small_style,
        )
    )

    section(story, "Professional experience")
    role(
        story,
        "Mercor",
        "AI Annotator & Quality Reviewer, Contract",
        "Feb 2026-Present",
        "AI quality operations",
        [
            "Evaluate frontier-model outputs across finance, investment, business operations, strategy, business development, engineering, and generalist work.",
            "Advanced into reviewer responsibilities and was retained for a second priority project based on quality and judgment.",
        ],
    )
    role(
        story,
        "RYGNeco",
        "Co-Founder & Program Lead",
        "2025-Present",
        "Zero-to-one product and vendor program",
        [
            "Translated a field e-waste pilot into a four-portal product program covering intake, testing, disposition, data-destruction records, pricing, and client reporting.",
            "Directed an approximately $11.5K vendor-built MVP across a co-founder, development vendor, interns, and an AWS architectural adviser.",
            "Processed 400+ devices in pilot operations, catalogued approximately 480, tested and verified 130, and recorded zero OSHA recordables.",
        ],
    )
    role(
        story,
        "EPIC Brands",
        "General Manager, promoted from AGM",
        "Jul 2025-Feb 2026",
        "Operating portfolio and concept launch",
        [
            "Led a $10M operating portfolio with 70 hourly employees and six managers, contributing to 20-25% year-over-year growth.",
            "Built an approximately $800K events pipeline in six months and reduced controllable costs by 10% through zero-based budgeting.",
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
    story.append(PageBreak())
    section(story, "Professional experience, continued")
    role(
        story,
        "Hard Rock Casino Cincinnati",
        "Operations Manager to AGM to Acting GM",
        "Jan 2024-Jan 2025",
        "Operational transformation",
        [
            "Held responsibility across three F&amp;B outlets with approximately $17M in combined P&amp;L and 120 employees, including approximately 80 union team members.",
            "Recovered approximately $14K per month in variance, maintained inventory variance below 1%, and reduced labor by 10%.",
            "Raised alcohol mix from 13% to 22% and upsell rate from 9% to 17% through financial analysis, training, certification, and reinforcement.",
        ],
    )

    role(
        story,
        "iTZCALi Tapas & Tequila",
        "Director of Operations / Launch Consultant",
        "Sep 2022-Jan 2024",
        "High-volume launch program",
        [
            "Coordinated buildout, licensing, menus, vendor relationships, pricing, POS, reservations, staffing, training, payroll, and launch readiness.",
            "Recruited and trained approximately 60 employees; the concept generated $165K in its first 14 days and served up to 600 covers nightly.",
            "Reduced the operating menu from 45 items to 12 and cocktail production from approximately two minutes to 30 seconds.",
        ],
    )
    role(
        story,
        "MAK Trading / Trade with MAK",
        "Founder & Program Lead",
        "Nov 2019-Present",
        "Digital community and growth program; monetized 2022-2023",
        [
            "Built a global education community of approximately 2,000 members, with 1,200+ paid subscribers at peak and approximately $30K in peak monthly recurring revenue.",
            "Led brand, acquisition, onboarding, content operations, a 48-page curriculum, member engagement, and a LaunchPass/Stripe to WordPress/MemberPress migration.",
        ],
    )

    section(story, "Earlier experience")
    story.extend(
        [
            Paragraph("<b>Napoli Italian Eatery</b> | Opening Manager / Operations Lead | 2021-2022", small_style),
            Paragraph("<b>MKEC</b> | Mechanical Design Engineer | 2019-2020", small_style),
            Paragraph("<b>Bella Luna Cafe</b> | GM / Multi-Unit Lead | 2016-2019", small_style),
        ]
    )

    section(story, "Selected program evidence")
    story.extend(
        [
            Paragraph("<b>RYGNeco:</b> Field-informed lifecycle, four stakeholder portals, vendor milestones, acceptance criteria, and client reporting architecture.", small_style),
            Paragraph("<b>Hard Rock:</b> Variance controls, beverage capability program, onboarding system, KPI cadence, and frontline adoption.", small_style),
            Paragraph("<b>iTZCALi:</b> Twelve-workstream launch roadmap, menu simplification, bar workflow, pricing, POS, staffing, and training.", small_style),
            Paragraph("<b>MAK Trading:</b> Acquisition, onboarding, curriculum, community cadence, paid access, retention, and platform migration.", small_style),
        ]
    )

    section(story, "Education and credentials")
    story.extend(
        [
            Paragraph("<b>Wichita State University</b> | Mechanical Engineering studies", small_style),
            Paragraph("<b>University of Wales Trinity Saint David</b> | Business &amp; Management studies", small_style),
            Paragraph("<b>ServSafe Manager</b> | Active through 2029", small_style),
            Paragraph("<b>Languages</b> | English, Arabic, Urdu, Hindi, Punjabi", small_style),
        ]
    )

    story.append(Spacer(1, 5))
    story.append(
        Paragraph(
            "Portfolio: sama-mushtaq-program-portfolio.samamak.chatgpt.site",
            contact_style,
        )
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()
