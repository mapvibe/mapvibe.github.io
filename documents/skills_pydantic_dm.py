from pydantic import BaseModel
from typing import List
import json

class SkillsModel(BaseModel):
    leadership_skills: List[str]
    strategic_skills: List[str]
    policy_skills: List[str]
    technical_skills: dict

class FullSkillSet(BaseModel):
    name: str
    location: str
    contact_email: str
    skills: SkillsModel

# Instantiate your skillset
my_skills = FullSkillSet(
    name="Gregory Gunther",
    location="Highlands Ranch, Colorado",
    contact_email="mapvibe@gmail.com",
    skills=SkillsModel(
        leadership_skills=[
            "Team building",
            "Supervision",
            "Community building",
            "Executive sponsorship",
            "Mentoring",
            "Cross-functional team leadership",
            "Budget management ($4M+)",
            "Staffing and hiring"
        ],
        strategic_skills=[
            "Data strategy development",
            "AI strategy design",
            "System modernization",
            "DevOps oversight",
            "Capital investment planning",
            "Geospatial system architecture",
            "Enterprise system direction"
        ],
        policy_skills=[
            "Federal geospatial policy implementation",
            "Open Data and AI policy advisory",
            "Governance of National Geospatial Data Assets",
            "DOI Advisory Board participation",
            "International data governance training"
        ],
        technical_skills={
            "databases": [
                "Snowflake", "SQL Server", "Oracle", "SQL", "PostgreSQL"
            ],
            "programming_languages": [
                "Python", "Java", "C#", "JavaScript", "PERL", "XML", "JSON", "HTML5", "CSS"
            ],
            "web_development": [
                "Web GIS", "ESRI JavaScript API", "Google Maps", "ArcGIS Online", "Responsive UI design"
            ],
            "gis_tools": [
                "ArcGIS Enterprise", "ArcPy", "ESRI Suite", "Geospatial DevOps", "ScienceBase"
            ],
            "platforms_frameworks": [
                "AWS", "Globus", "Power BI", "HPC systems", "CI/CD pipelines"
            ],
            "data_science_analytics": [
                "IBM Data Science Certification", "Data lifecycle modeling", "GeoAI", "Scientific data analysis"
            ]
        }
    )
)