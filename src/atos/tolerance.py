from __future__ import annotations
import math

def tolerance_stack(tolerances_mm: list[float]) -> dict:
    if not tolerances_mm: raise ValueError('provide at least one tolerance')
    if any(not math.isfinite(t) or t<0 for t in tolerances_mm): raise ValueError('tolerances must be finite and non-negative')
    return {'worst_case_mm':sum(tolerances_mm),'rss_mm':math.sqrt(sum(t*t for t in tolerances_mm)),'n_terms':len(tolerances_mm),'note':'RSS assumes suitable independence/distributions; verify before use.'}
