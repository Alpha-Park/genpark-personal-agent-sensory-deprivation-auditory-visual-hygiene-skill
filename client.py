# -*- coding: utf-8 -*-
"""Personal Agent Sensory Deprivation Auditory Visual Hygiene Skill.

Zero-dependency Sensory Overload Index (SOI) quantifier, thalamocortical sensory gating modeler,
and Restricted Environmental Stimulation Therapy (REST) protocol prescriptor.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentSensoryDeprivationAuditoryVisualHygiene:
    """Quantitative neuro-sensory bandwidth and environmental sensory hygiene engine
    based on perceptual gating and Restricted Environmental Stimulation Therapy (REST)."""

    def calculate_sensory_overload_burden(
        self,
        daily_screen_time_hours: float = 8.5,
        average_ambient_decibels: float = 68.0,
        daily_notification_interrupts: int = 85,
        high_contrast_blue_light_hours: float = 4.5
    ) -> Dict[str, Any]:
        """Calculates Sensory Overload Index (SOI: 0-100) combining photopic, acoustic,
        and attentional interruption vectors."""
        screen_h = max(0.0, min(18.0, float(daily_screen_time_hours)))
        db = max(30.0, min(110.0, float(average_ambient_decibels)))
        interrupts = max(0, int(daily_notification_interrupts))
        blue_h = max(0.0, min(screen_h, float(high_contrast_blue_light_hours)))

        # 1. Acoustic Burden: logarithmic exposure above 55 dB baseline
        acoustic_load = max(0.0, (db - 55.0) * 1.5)

        # 2. Photopic Retinal Burden: screen hours + blue light weighting
        visual_load = (screen_h * 2.8) + (blue_h * 2.0)

        # 3. Attentional Interruption Burden: micro-arousal switching cost
        interrupt_load = min(35.0, (interrupts / 100.0) * 30.0)

        # Total Sensory Overload Index (SOI: 0 - 100)
        soi_raw = acoustic_load + visual_load + interrupt_load
        soi = min(100.0, round(max(5.0, soi_raw), 1))

        if soi < 30.0:
            tier = "Sensorially Balanced / Optimal Neural Bandwidth"
            status = "Low thalamocortical gating strain; cognitive processing clear"
        elif soi < 60.0:
            tier = "Moderate Sensory Friction / Attentional Fragmentation"
            status = "Mild perceptual fatigue; diminished working memory capacity"
        elif soi < 85.0:
            tier = "High Sensory Saturation / Neural Gating Strain"
            status = "Elevated sympathetic irritability; degraded sensory filtering"
        else:
            tier = "Acute Sensory Exhaustion / Desensitization Crisis"
            status = "Sensory gating collapse; urgent environmental stimulus blackout indicated"

        return {
            "daily_screen_time_hours": screen_h,
            "ambient_acoustic_level_db": db,
            "daily_notification_interrupts": interrupts,
            "high_contrast_blue_light_hours": blue_h,
            "sensory_overload_index_soi": soi,
            "sensory_saturation_tier": tier,
            "neurological_status": status,
            "acoustic_burden_component": round(acoustic_load, 1),
            "visual_photopic_component": round(visual_load, 1),
            "attentional_interrupt_component": round(interrupt_load, 1)
        }

    def prescribe_sensory_deprivation_rest_dose(
        self,
        soi_score: float,
        available_time_minutes: int = 45
    ) -> Dict[str, Any]:
        """Prescribes customized Restricted Environmental Stimulation Therapy (REST) protocol
        based on current sensory overload severity."""
        soi = max(0.0, min(100.0, float(soi_score)))
        time_avail = max(10, int(available_time_minutes))

        if soi >= 75.0 or time_avail >= 60:
            protocol = "Flotation REST (Zero-Gravity Magnesium Sulfate Immersion)"
            target_env = "0 lux total darkness, < 20 dB acoustic isolation, 35.5 C skin-receptor neutral water"
            duration = min(60, time_avail)
            expected_reduction = "-55% Prefrontal Sensory Strain"
        elif soi >= 45.0 or time_avail >= 30:
            protocol = "Chamber REST (Dry Auditory & Visual Sensory Blackout)"
            target_env = "Weighted eye mask, high-attenuation active noise cancellation (ANC > 32 dB), supine posture"
            duration = min(30, time_avail)
            expected_reduction = "-38% Prefrontal Sensory Strain"
        else:
            protocol = "Micro Sensory Hiatus (Acoustic Silence & Visual Defocus)"
            target_env = "Eyes closed, natural acoustic silence, gaze softened to 20 feet away"
            duration = min(15, time_avail)
            expected_reduction = "-20% Prefrontal Sensory Strain"

        return {
            "evaluated_soi_score": soi,
            "prescribed_protocol": protocol,
            "duration_minutes": duration,
            "target_environmental_parameters": target_env,
            "projected_neural_strain_attenuation": expected_reduction,
            "re-entry_guidance": "Transition gradually upon session termination; delay smartphone / screen re-engagement for at least 15 minutes."
        }
