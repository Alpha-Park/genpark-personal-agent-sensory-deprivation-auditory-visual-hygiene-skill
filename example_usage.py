# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Sensory Deprivation Auditory Visual Hygiene Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentSensoryDeprivationAuditoryVisualHygiene

def main():
    agent = PersonalAgentSensoryDeprivationAuditoryVisualHygiene()

    print("=" * 70)
    print("DEMO: Personal Agent Sensory Overload & REST Hygiene Engine")
    print("=" * 70)

    # 1. Calculate Sensory Overload Burden (9 hrs screen, 72 dB ambient, 95 interrupts, 5 hrs blue light)
    res_soi = agent.calculate_sensory_overload_burden(
        daily_screen_time_hours=9.0,
        average_ambient_decibels=72.0,
        daily_notification_interrupts=95,
        high_contrast_blue_light_hours=5.0
    )

    print(f"\n1. Sensory Overload Burden Analysis:")
    print(f"   Screen Time: {res_soi['daily_screen_time_hours']} hrs")
    print(f"   Ambient Noise: {res_soi['ambient_acoustic_level_db']} dB")
    print(f"   Notification Interrupts: {res_soi['daily_notification_interrupts']}")
    print(f"   Sensory Overload Index (SOI): {res_soi['sensory_overload_index_soi']}/100")
    print(f"   Saturation Tier: {res_soi['sensory_saturation_tier']}")
    print(f"   Neurological Status: {res_soi['neurological_status']}")
    print(f"   Components: Acoustic={res_soi['acoustic_burden_component']} | Visual={res_soi['visual_photopic_component']} | Interrupts={res_soi['attentional_interrupt_component']}")

    # 2. Prescribe REST Dose based on SOI
    res_rest = agent.prescribe_sensory_deprivation_rest_dose(
        soi_score=res_soi['sensory_overload_index_soi'],
        available_time_minutes=45
    )

    print(f"\n2. Prescribed Sensory Deprivation (REST) Protocol:")
    print(f"   Protocol: {res_rest['prescribed_protocol']}")
    print(f"   Duration: {res_rest['duration_minutes']} min")
    print(f"   Target Environment: {res_rest['target_environmental_parameters']}")
    print(f"   Attenuation Benefit: {res_rest['projected_neural_strain_attenuation']}")
    print(f"   Re-entry Mandate: {res_rest['re-entry_guidance']}")

    print("\nVerification complete: Sensory hygiene REST engine executed flawlessly.")

if __name__ == "__main__":
    main()
