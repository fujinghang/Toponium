# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Thu 10 Apr 2025 22:52:15



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
gEt = Parameter(name = 'gEt',
                nature = 'external',
                type = 'real',
                value = 0.0120138,
                texname = 'g_{\\text{Et}}',
                lhablock = 'EtINPUTS',
                lhacode = [ 1 ])

gJt = Parameter(name = 'gJt',
                nature = 'external',
                type = 'real',
                value = 0.0120138,
                texname = 'g_{\\text{Jt}}',
                lhablock = 'JtINPUTS',
                lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 126.04,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000012224596381,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.09844,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.0047,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00216,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.0935,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 0.575,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 2.568,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.57,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.188,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

ML = Parameter(name = 'ML',
               nature = 'external',
               type = 'real',
               value = 1.777,
               texname = '\\text{ML}',
               lhablock = 'MASS',
               lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00216,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 0.575,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.57,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.0047,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.0935,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 2.568,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.2,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MJt = Parameter(name = 'MJt',
                nature = 'external',
                type = 'real',
                value = 345.14,
                texname = '\\text{MJt}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

MEt = Parameter(name = 'MEt',
                nature = 'external',
                type = 'real',
                value = 345.14,
                texname = '\\text{MEt}',
                lhablock = 'MASS',
                lhacode = [ 5000002 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4955,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.31,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.0037,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WJt = Parameter(name = 'WJt',
                nature = 'external',
                type = 'real',
                value = 2.605,
                texname = '\\text{WJt}',
                lhablock = 'DECAY',
                lhacode = [ 5000001 ])

WEt = Parameter(name = 'WEt',
                nature = 'external',
                type = 'real',
                value = 2.616,
                texname = '\\text{WEt}',
                lhablock = 'DECAY',
                lhacode = [ 5000002 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

gEtGG = Parameter(name = 'gEtGG',
                  nature = 'internal',
                  type = 'real',
                  value = '(2*aS*cmath.pi*gEt)/(MT*cmath.sqrt(3))',
                  texname = 'g_{\\text{EtGG}}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gEtAA = Parameter(name = 'gEtAA',
                  nature = 'internal',
                  type = 'real',
                  value = '(16*aEW*cmath.pi*gEt)/(3.*MT*cmath.sqrt(3))',
                  texname = 'g_{\\text{EtAA}}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gAbJt = Parameter(name = 'gAbJt',
                  nature = 'internal',
                  type = 'real',
                  value = '(ee**2*gJt*MT**2*(cw**2*(MT**2 + 2*MW**2)*(4*MT**2 - MZ**2) - MW**2*(MT**2 + MW**2)*(-3 + 8*sw**2)))/(2.*cw**2*MW**2*(MT**2 + MW**2)*(2*MT - MZ)*(2*MT + MZ)*sw**2*cmath.sqrt(3))',
                  texname = 'g_{\\text{AbJt}}')

gAdsJt = Parameter(name = 'gAdsJt',
                   nature = 'internal',
                   type = 'real',
                   value = '-0.5*(ee**2*gJt*MT**2*(-3 + 8*sw**2))/(cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                   texname = 'g_{\\text{AdsJt}}')

gAlepJt = Parameter(name = 'gAlepJt',
                    nature = 'internal',
                    type = 'real',
                    value = '-0.5*(ee**2*gJt*MT**2*(-3 + 8*sw**2))/(cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                    texname = 'g_{\\text{AlepJt}}')

gAucJt = Parameter(name = 'gAucJt',
                   nature = 'internal',
                   type = 'real',
                   value = '(ee**2*gJt*MT**2*(-3 + 8*sw**2))/(2.*cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                   texname = 'g_{\\text{AucJt}}')

gEtHZ = Parameter(name = 'gEtHZ',
                  nature = 'internal',
                  type = 'real',
                  value = '(-4*aEW*cmath.pi*gEt*MT*cmath.sqrt(3 - 3*sw**2))/(MW**3*sw**2)',
                  texname = 'g_{\\text{EtHZ}}')

gEtWW = Parameter(name = 'gEtWW',
                  nature = 'internal',
                  type = 'real',
                  value = '(2*aEW*cmath.pi*gEt*MT*cmath.sqrt(3))/((MT**2 - MW**2)*sw**2)',
                  texname = 'g_{\\text{EtWW}}')

gEtZA = Parameter(name = 'gEtZA',
                  nature = 'internal',
                  type = 'real',
                  value = '(16*aEW*cmath.pi*gEt*MT*(-3 + 8*sw**2)*cmath.sqrt(1 - sw**2))/(3.*sw*(MW**2 + 4*MT**2*(-1 + sw**2))*cmath.sqrt(3))',
                  texname = 'g_{\\text{EtZA}}')

gEtZZ = Parameter(name = 'gEtZZ',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.3333333333333333*(aEW*cmath.pi*gEt*MT*(9 - 24*sw**2 + 32*sw**4))/(sw**2*(MW**2 + 2*MT**2*(-1 + sw**2))*cmath.sqrt(3))',
                  texname = 'g_{\\text{EtZZ}}')

gJtHA = Parameter(name = 'gJtHA',
                  nature = 'internal',
                  type = 'real',
                  value = '(-64*aEW*cmath.pi*gJt*MT**2)/((MH**2 - 4*MT**2)*MZ*sw*cmath.sqrt(3 - 3*sw**2))',
                  texname = 'g_{\\text{JtHA}}')

gJtHZ = Parameter(name = 'gJtHZ',
                  nature = 'internal',
                  type = 'real',
                  value = '(-8*aEW*cmath.pi*gJt*MT**2*(-3 + 8*sw**2))/(MZ*(MH**2 - 4*MT**2 + MZ**2)*sw**2*(-1 + sw**2)*cmath.sqrt(3))',
                  texname = 'g_{\\text{JtHZ}}')

gJtWWEJE1k1E2 = Parameter(name = 'gJtWWEJE1k1E2',
                          nature = 'internal',
                          type = 'real',
                          value = '(ee**2*gJt*(-8*MW**2*MZ**2*sw**2 + MT**2*(12*MW**2 + MZ**2*(-3 + 8*sw**2))))/((MT - MW)*(MT + MW)*(2*MT - MZ)*(2*MT + MZ)*sw**2*cmath.sqrt(3))',
                          texname = 'g_{\\text{JtWWEJE1k1E2}}')

gJtWWEJk1E1E2 = Parameter(name = 'gJtWWEJk1E1E2',
                          nature = 'internal',
                          type = 'real',
                          value = '(-2*ee**2*gJt*(6*MT**4 - 4*MW**2*MZ**2*sw**2 + MT**2*(6*MW**2 + MZ**2*(-3 + 4*sw**2))))/((MT - MW)*(MT + MW)*(2*MT - MZ)*(2*MT + MZ)*sw**2*cmath.sqrt(3))',
                          texname = 'g_{\\text{JtWWEJk1E1E2}}')

gJtWWepsEJk1E1E2 = Parameter(name = 'gJtWWepsEJk1E1E2',
                             nature = 'internal',
                             type = 'real',
                             value = '-((ee**2*gJt*MT**2*cmath.sqrt(3))/((MT - MW)*(MT + MW)*sw**2))',
                             texname = 'g_{\\text{JtWWepsEJk1E1E2}}')

gJtZA = Parameter(name = 'gJtZA',
                  nature = 'internal',
                  type = 'real',
                  value = '(32*aEW*cmath.pi*gJt*MT**2)/((4*MT**2 - MZ**2)*sw*cmath.sqrt(3 - 3*sw**2))',
                  texname = 'g_{\\text{JtZA}}')

gJtZZ = Parameter(name = 'gJtZZ',
                  nature = 'internal',
                  type = 'real',
                  value = '(2*aEW*cmath.pi*gJt*MT**2*(-3 + 8*sw**2))/((2*MT**2 - MZ**2)*sw**2*(-1 + sw**2)*cmath.sqrt(3))',
                  texname = 'g_{\\text{JtZZ}}')

gnu123 = Parameter(name = 'gnu123',
                   nature = 'internal',
                   type = 'real',
                   value = '-0.5*(ee**2*gJt*MT**2*(-3 + 8*sw**2))/(cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                   texname = 'g_{\\text{nuJt}}')

gVbJt = Parameter(name = 'gVbJt',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.16666666666666666*(ee**2*gJt*(MT**2*MW**2*(MT**2 + MW**2)*(9 - 36*sw**2 + 32*sw**4) + cw**2*(4*MT**2 - MZ**2)*(3*MT**4 + 8*MW**4*sw**2 + 2*MT**2*MW**2*(3 + 4*sw**2))))/(cw**2*MW**2*(MT**2 + MW**2)*(2*MT - MZ)*(2*MT + MZ)*sw**2*cmath.sqrt(3))',
                  texname = 'g_{\\text{VbJt}}')

gVdsJt = Parameter(name = 'gVdsJt',
                   nature = 'internal',
                   type = 'real',
                   value = '-0.16666666666666666*(ee**2*gJt*(-8*cw**2*MZ**2*sw**2 + MT**2*(9 + 4*(-9 + 8*cw**2)*sw**2 + 32*sw**4)))/(cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                   texname = 'g_{\\text{VdsJt}}')

gVlepJt = Parameter(name = 'gVlepJt',
                    nature = 'internal',
                    type = 'real',
                    value = '(ee**2*gJt*(8*cw**2*MZ**2*sw**2 - MT**2*(3 + 4*(-5 + 8*cw**2)*sw**2 + 32*sw**4)))/(2.*cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                    texname = 'g_{\\text{VlepJt}}')

gVucJt = Parameter(name = 'gVucJt',
                   nature = 'internal',
                   type = 'real',
                   value = '(ee**2*gJt*(-16*cw**2*MZ**2*sw**2 + MT**2*(9 + 16*(-3 + 4*cw**2)*sw**2 + 64*sw**4)))/(6.*cw**2*(4*MT**2 - MZ**2)*sw**2*cmath.sqrt(3))',
                   texname = 'g_{\\text{VucJt}}')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

