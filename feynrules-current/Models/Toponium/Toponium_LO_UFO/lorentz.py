# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Sun 13 Apr 2025 18:19:25


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUV2 = Lorentz(name = 'UUV2',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1) - Gamma(3,2,1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV11 = Lorentz(name = 'FFV11',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV12 = Lorentz(name = 'FFV12',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

VSS2 = Lorentz(name = 'VSS2',
               spins = [ 3, 1, 1 ],
               structure = '-(P(-1,1)*P(-1,3)*P(1,2)) + P(-1,1)*P(-1,2)*P(1,3)')

VVS8 = Lorentz(name = 'VVS8',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS9 = Lorentz(name = 'VVS9',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVS10 = Lorentz(name = 'VVS10',
                spins = [ 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS11 = Lorentz(name = 'VVS11',
                spins = [ 3, 3, 1 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS12 = Lorentz(name = 'VVS12',
                spins = [ 3, 3, 1 ],
                structure = 'Metric(1,2)')

VVS13 = Lorentz(name = 'VVS13',
                spins = [ 3, 3, 1 ],
                structure = 'P(1,3)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2)')

VVS14 = Lorentz(name = 'VVS14',
                spins = [ 3, 3, 1 ],
                structure = 'P(1,2)*P(2,3) - P(-1,2)*P(-1,3)*Metric(1,2)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVV7 = Lorentz(name = 'VVV7',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,2)) + Epsilon(1,2,3,-1)*P(-1,3)')

VVV8 = Lorentz(name = 'VVV8',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,2)*Metric(1,2) - P(2,3)*Metric(1,3)')

VVV9 = Lorentz(name = 'VVV9',
               spins = [ 3, 3, 3 ],
               structure = 'P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV10 = Lorentz(name = 'VVV10',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

