#Import Modul
import argparse
import sys
from Core_GUI import kont

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=float, default=0.0,
                        help='Frekuensi')
    parser.add_argument('--l', type=float, default=0.0,
                        help='Panjang Data')
    parser.add_argument('--dt', type=float, default=0.0,
                        help='interval sampling')
    parser.add_argument('--op', type=str, default='rw',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.op == 'rw':
        f=args.f
        l=args.l
        dt=args.dt
        kont(f,l,dt)
    
    
if __name__ == '__main__':
    main()