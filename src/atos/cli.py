import argparse,json
from .geometry import eccentric_offset
from .tolerance import tolerance_stack
from .aero import drag_sensitivity

def main():
 p=argparse.ArgumentParser(prog='atos',description='Aerodynamic tolerance study calculators'); s=p.add_subparsers(dest='cmd',required=True)
 e=s.add_parser('eccentric'); e.add_argument('--e1-mm',type=float,required=True); e.add_argument('--e2-mm',type=float,required=True); e.add_argument('--theta-deg',type=float,required=True)
 t=s.add_parser('stack'); t.add_argument('--tolerances-mm',type=float,nargs='+',required=True)
 d=s.add_parser('drag'); d.add_argument('--rho',type=float,required=True); d.add_argument('--velocity',type=float,required=True); d.add_argument('--cd',type=float,required=True); d.add_argument('--area',type=float,required=True); d.add_argument('--cd-change-percent',type=float,required=True)
 a=p.parse_args()
 if a.cmd=='eccentric': out=eccentric_offset(a.e1_mm,a.e2_mm,a.theta_deg)
 elif a.cmd=='stack': out=tolerance_stack(a.tolerances_mm)
 else: out=drag_sensitivity(a.rho,a.velocity,a.cd,a.area,a.cd_change_percent)
 print(json.dumps(out,indent=2))
if __name__=='__main__': main()
