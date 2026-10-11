from __future__ import annotations
import math

def drag_force(rho_kg_m3: float, velocity_m_s: float, cd: float, reference_area_m2: float) -> float:
    vals=(rho_kg_m3,velocity_m_s,cd,reference_area_m2)
    if not all(math.isfinite(v) for v in vals): raise ValueError('inputs must be finite')
    if rho_kg_m3<=0 or velocity_m_s<0 or cd<0 or reference_area_m2<=0: raise ValueError('rho and area positive; velocity and Cd non-negative')
    return 0.5*rho_kg_m3*velocity_m_s**2*cd*reference_area_m2

def drag_sensitivity(rho_kg_m3: float, velocity_m_s: float, cd: float, reference_area_m2: float, cd_change_percent: float) -> dict:
    if not math.isfinite(cd_change_percent) or cd_change_percent<=-100: raise ValueError('Cd change must be finite and greater than -100%')
    base=drag_force(rho_kg_m3,velocity_m_s,cd,reference_area_m2); changed=drag_force(rho_kg_m3,velocity_m_s,cd*(1+cd_change_percent/100),reference_area_m2)
    return {'baseline_drag_n':base,'scenario_drag_n':changed,'scenario_delta_n':changed-base,'input_cd_change_percent':cd_change_percent,'warning':'Sensitivity scenario only; this does not infer Cd change from geometry or CFD.'}
