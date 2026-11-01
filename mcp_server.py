# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Sensory Deprivation Auditory Visual Hygiene Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentSensoryDeprivationAuditoryVisualHygiene

mcp = FastMCP("PersonalAgentSensoryDeprivationAuditoryVisualHygiene")
client = PersonalAgentSensoryDeprivationAuditoryVisualHygiene()

@mcp.tool()
def calculate_sensory_overload_burden(
    daily_screen_time_hours: float = 8.5,
    average_ambient_decibels: float = 68.0,
    daily_notification_interrupts: int = 85,
    high_contrast_blue_light_hours: float = 4.5
) -> str:
    """Calculates Sensory Overload Index (SOI: 0-100) combining photopic, acoustic, and attentional vectors."""
    import json
    return json.dumps(client.calculate_sensory_overload_burden(
        daily_screen_time_hours, average_ambient_decibels,
        daily_notification_interrupts, high_contrast_blue_light_hours
    ), indent=2)

@mcp.tool()
def prescribe_sensory_deprivation_rest_dose(
    soi_score: float = 68.0,
    available_time_minutes: int = 45
) -> str:
    """Prescribes customized Restricted Environmental Stimulation Therapy (REST) protocol."""
    import json
    return json.dumps(client.prescribe_sensory_deprivation_rest_dose(
        soi_score, available_time_minutes
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
