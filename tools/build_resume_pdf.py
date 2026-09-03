from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resume" / "Sama-Mushtaq-Resume.pdf"

NAVY = colors.HexColor("#0f172a")
BLUE = colors.HexColor("#1f5fd1")
MUTED = colors.HexColor("#475569")
LINE = colors.HexColor("#cbd5e1")


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=letter,
            leftMargin=0.58 * inch,
            rightMargin=0.58 * inch,
            topMargin=0.48 * inch,
            bottomMargin=0.44 * inch,
            title="Sama Mushtaq Mechanical Design and Test Resume",
            author="Sama Mushtaq",
            subject="Mechanical design and test professional resume",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="resume", frames=[frame]))


styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=23,
    leading=25,
    textColor=NAVY,
    spaceAfter=2,
)

title_style = ParagraphStyle(
    "Title",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10.8,
    leading=13,
    textColor=BLUE,
    spaceAfter=3,
)

contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.4,
    leading=10.5,
    textColor=MUTED,
    spaceAfter=0,
)

summary_style = ParagraphStyle(
    "Summary",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.8,
    leading=12.8,
    textColor=NAVY,
    spaceAfter=0,
)

section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.6,
    leading=10,
    textColor=BLUE,
    spaceBefore=0,
    spaceAfter=0,
)

role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.35,
    leading=11.4,
    textColor=NAVY,
)

date_style = ParagraphStyle(
    "Date",
    parent=role_style,
    fontSize=8.35,
    leading=10.3,
    textColor=MUTED,
    alignment=TA_LEFT,
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.05,
    leading=11.65,
    textColor=NAVY,
    spaceAfter=3,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=9,
    firstLineIndent=-7,
    spaceAfter=2,
)

skills_style = ParagraphStyle(
    "Skills",
    parent=body_style,
    fontSize=8.85,
    leading=11.15,
    spaceAfter=1.8,
)

project_style = ParagraphStyle(
    "Project",
    parent=body_style,
    leftIndent=0,
    spaceAfter=3.8,
)


def section(title):
    return [
        Spacer(1, 7),
        Paragraph(title.upper(), section_style),
        Spacer(1, 2.2),
        HRFlowable(width="100%", thickness=0.55, color=LINE, spaceBefore=0, spaceAfter=4.5),
    ]


def role_header(company, role, dates):
    left = Paragraph(f"<b>{company}</b>  {role}", role_style)
    right = Paragraph(dates, date_style)
    table = Table([[left, right]], colWidths=[4.96 * inch, 2 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    return table


def bullet(text):
    return Paragraph(f"- {text}", bullet_style)


story = [
    Paragraph("Sama Mushtaq", name_style),
    Paragraph("Mechanical Design and Test Professional", title_style),
    Paragraph(
        'Lebanon, Ohio&nbsp;&nbsp;&nbsp; '
        '<link href="mailto:sama.mushtaq.a@gmail.com" color="#475569">sama.mushtaq.a@gmail.com</link>&nbsp;&nbsp;&nbsp; '
        '<link href="https://www.linkedin.com/in/samamushtaq" color="#475569">linkedin.com/in/samamushtaq</link>&nbsp;&nbsp;&nbsp; '
        '<link href="https://samamak1.github.io" color="#475569">samamak1.github.io</link>',
        contact_style,
    ),
    Spacer(1, 8),
    HRFlowable(width="100%", thickness=1.1, color=NAVY, spaceBefore=0, spaceAfter=8),
    Paragraph(
        "Mechanical design and test professional with one year of MEP design experience across more than 50 building projects. "
        "Project work includes LabVIEW data acquisition, test fixtures, structural analysis, and heat transfer. "
        "Admitted to University of Cincinnati Mechanical Engineering for Spring 2027.",
        summary_style,
    ),
]

story += section("Technical Skills")
story += [
    Paragraph("<b>Design</b>&nbsp;&nbsp; AutoCAD, Revit, Trane TRACE, CATIA", skills_style),
    Paragraph("<b>Test and analysis</b>&nbsp;&nbsp; LabVIEW, data acquisition, sensor wiring, test fixtures, Excel", skills_style),
    Paragraph("<b>Data and documentation</b>&nbsp;&nbsp; Python, SQLite, Power Query, GitHub, technical reports, requirements", skills_style),
]

story += section("Engineering and Technical Experience")
story += [
    KeepTogether(
        [
            role_header("MKEC Engineering", "Mechanical Design Engineer", "December 2019 to December 2020"),
            bullet("Prepared heating and cooling load calculations and MEP design documents for more than 50 commercial, residential, and modular projects using AutoCAD, Revit, and Trane TRACE."),
            bullet("Developed HVAC, plumbing, electrical, equipment, and airflow schedules. Coordinated design information with architects, engineers, project managers, contractors, and field conditions."),
            bullet("Built reusable Revit families, templates, schedules, and details to improve consistency and reduce repeat drafting."),
        ]
    ),
    Spacer(1, 4),
    KeepTogether(
        [
            role_header("RYGNeco", "Co-Founder and Program Lead", "August 2024 to present"),
            bullet("Mapped electronics intake, testing, grading, custody, disposition, pricing, evidence, and client reporting into one operating workflow."),
            bullet("Wrote procedures, product requirements, stakeholder workflows, and acceptance criteria, then directed external prototype development."),
        ]
    ),
    Spacer(1, 4),
    KeepTogether(
        [
            role_header("Mercor", "AI Quality Reviewer, Project-Based Independent Contractor", "Assignments beginning February 2026"),
            bullet("Reviewed technical and business outputs against source files, formulas, calculations, detailed rubrics, and instruction requirements. Documented failures and reviewed contributor work during assigned projects."),
        ]
    ),
]

story += section("Engineering Projects")
story += [
    Paragraph(
        '<link href="https://samamak1.github.io/engineering/vibration-rig/" color="#0f172a"><b>Vibration Sensing and Data Acquisition</b></link>&nbsp;&nbsp; '
        "Designed sensor mounts and a test fixture, configured a three channel LabVIEW and Excel workflow, reviewed 1,022 samples, and used repeat trials and channel swaps to identify setup and signal issues.",
        project_style,
    ),
    Paragraph(
        '<link href="https://samamak1.github.io/engineering/heat-exchanger/" color="#0f172a"><b>Shell and Tube Heat Exchanger</b></link>&nbsp;&nbsp; '
        "Calculated heat duty, convection behavior, area, tube length, and geometry for a countercurrent water to oil exchanger, then compared ten materials under clean and two fouling conditions.",
        project_style,
    ),
    Paragraph(
        '<link href="https://samamak1.github.io/engineering/kite-buggy/" color="#0f172a"><b>Kite Buggy Structural Analysis</b></link>&nbsp;&nbsp; '
        "Shared responsibility for load, bending, stress, deflection, stability, material, weight, cost, and factor of safety calculations on a five person 6061 aluminum frame project.",
        project_style,
    ),
]

story += section("Additional Leadership")
story += [
    Paragraph(
        "<b>Hard Rock Casino Cincinnati, iTZCALi Tapas and Tequila, and EPIC Brands.</b> "
        "Led launches, training, safety, staffing, inventory, labor control, and multi unit operations.",
        body_style,
    )
]

story += section("Education")
story += [
    role_header("University of Cincinnati", "Mechanical Engineering", "Admitted for Spring 2027"),
    Paragraph("Transfer evaluation and completion schedule in progress", body_style),
    Spacer(1, 2),
    role_header("Wichita State University", "Mechanical Engineering studies", "103 earned credits"),
    Paragraph("3.397 cumulative GPA. Dean's List, three terms.", body_style),
]


doc = ResumeDocTemplate(str(OUTPUT))
doc.build(story)
print(OUTPUT)
