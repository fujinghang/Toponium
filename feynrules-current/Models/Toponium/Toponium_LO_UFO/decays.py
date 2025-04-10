# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Thu 10 Apr 2025 22:52:15


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.s):'(((3*ee**2*MC**2)/(2.*sw**2) + (3*ee**2*MS**2)/(2.*sw**2) + (3*ee**2*MC**4)/(2.*MW**2*sw**2) - (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) + (3*ee**2*MS**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)'})

Decay_d = Decay(name = 'Decay_d',
                particle = P.d,
                partial_widths = {(P.W__minus__,P.u):'(((3*ee**2*MD**2)/(2.*sw**2) + (3*ee**2*MU**2)/(2.*sw**2) + (3*ee**2*MD**4)/(2.*MW**2*sw**2) - (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) + (3*ee**2*MU**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_Et = Decay(name = 'Decay_Et',
                 particle = P.Et,
                 partial_widths = {(P.a,P.a):'(gEtAA**2*MEt**6)/(4.*cmath.pi*abs(MEt)**3)',
                                   (P.a,P.Z):'((MEt**2 - MZ**2)*(2*gEtZA**2*MEt**4 - 4*gEtZA**2*MEt**2*MZ**2 + 2*gEtZA**2*MZ**4))/(16.*cmath.pi*abs(MEt)**3)',
                                   (P.g,P.g):'(2*gEtGG**2*MEt**6)/(cmath.pi*abs(MEt)**3)',
                                   (P.H,P.Z):'((-0.5*(gEtHZ**2*MEt**6) + (gEtHZ**2*MEt**4*MH**2)/2. + (gEtHZ**2*MEt**2*MH**4)/2. - (gEtHZ**2*MH**6)/2. + (gEtHZ**2*MEt**8)/(4.*MZ**2) - (gEtHZ**2*MEt**6*MH**2)/MZ**2 + (3*gEtHZ**2*MEt**4*MH**4)/(2.*MZ**2) - (gEtHZ**2*MEt**2*MH**6)/MZ**2 + (gEtHZ**2*MH**8)/(4.*MZ**2) + (gEtHZ**2*MEt**4*MZ**2)/4. - (gEtHZ**2*MEt**2*MH**2*MZ**2)/2. + (gEtHZ**2*MH**4*MZ**2)/4.)*cmath.sqrt(MEt**4 - 2*MEt**2*MH**2 + MH**4 - 2*MEt**2*MZ**2 - 2*MH**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MEt)**3)',
                                   (P.W__minus__,P.W__plus__):'((2*gEtWW**2*MEt**4 - 8*gEtWW**2*MEt**2*MW**2)*cmath.sqrt(MEt**4 - 4*MEt**2*MW**2))/(16.*cmath.pi*abs(MEt)**3)',
                                   (P.Z,P.Z):'((8*gEtZZ**2*MEt**4 - 32*gEtZZ**2*MEt**2*MZ**2)*cmath.sqrt(MEt**4 - 4*MEt**2*MZ**2))/(32.*cmath.pi*abs(MEt)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.a,P.Jt):'((MH**2 - MJt**2)*(2*gJtHA**2*MH**4 - (gJtHA**2*MH**6)/(2.*MJt**2) - (5*gJtHA**2*MH**2*MJt**2)/2. + gJtHA**2*MJt**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*MH**2*yc**2)*cmath.sqrt(-4*MC**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.d,P.d__tilde__):'((-12*MD**2*ydo**2 + 3*MH**2*ydo**2)*cmath.sqrt(-4*MD**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + MH**2*ye**2)*cmath.sqrt(-4*Me**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Et,P.Z):'((-0.5*(gEtHZ**2*MEt**6) + (gEtHZ**2*MEt**4*MH**2)/2. + (gEtHZ**2*MEt**2*MH**4)/2. - (gEtHZ**2*MH**6)/2. + (gEtHZ**2*MEt**8)/(4.*MZ**2) - (gEtHZ**2*MEt**6*MH**2)/MZ**2 + (3*gEtHZ**2*MEt**4*MH**4)/(2.*MZ**2) - (gEtHZ**2*MEt**2*MH**6)/MZ**2 + (gEtHZ**2*MH**8)/(4.*MZ**2) + (gEtHZ**2*MEt**4*MZ**2)/4. - (gEtHZ**2*MEt**2*MH**2*MZ**2)/2. + (gEtHZ**2*MH**4*MZ**2)/4.)*cmath.sqrt(MEt**4 - 2*MEt**2*MH**2 + MH**4 - 2*MEt**2*MZ**2 - 2*MH**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Jt,P.Z):'(((2*gJtHZ**2*MH**6*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (6*gJtHZ**2*MH**4*MJt**2*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (6*gJtHZ**2*MH**2*MJt**4*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MJt**6*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (16*gJtHZ**2*MH**4*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (8*gJtHZ**2*MH**6*MT**4)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (8*gJtHZ**2*MH**2*MJt**2*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (16*gJtHZ**2*MH**6*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**8*MT**4)/(MJt**2*MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (24*gJtHZ**2*MH**4*MJt**2*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (16*gJtHZ**2*MH**2*MJt**4*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MJt**6*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**4*MJt**2*MZ**2)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**2*MJt**4*MZ**2)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MJt**6*MZ**2)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**4*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (4*gJtHZ**2*MH**2*MJt**2*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (24*gJtHZ**2*MH**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**4*MT**4*MZ**2)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (12*gJtHZ**2*MJt**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**4*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (3*gJtHZ**2*MH**2*MJt**2*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MH**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (6*gJtHZ**2*MJt**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (8*gJtHZ**2*MT**4*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**2*MZ**6)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (3*gJtHZ**2*MJt**2*MZ**6)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (4*gJtHZ**2*MT**2*MZ**6)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MZ**8)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2))*cmath.sqrt(MH**4 - 2*MH**2*MJt**2 + MJt**4 - 2*MH**2*MZ**2 - 2*MJt**2*MZ**2 + MZ**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((MH**2*ym**2 - 4*MM**2*ym**2)*cmath.sqrt(MH**4 - 4*MH**2*MM**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.s,P.s__tilde__):'((3*MH**2*ys**2 - 12*MS**2*ys**2)*cmath.sqrt(MH**4 - 4*MH**2*MS**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*ML**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*ML**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.u,P.u__tilde__):'((3*MH**2*yup**2 - 12*MU**2*yup**2)*cmath.sqrt(MH**4 - 4*MH**2*MU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_Jt = Decay(name = 'Decay_Jt',
                 particle = P.Jt,
                 partial_widths = {(P.a,P.H):'((-MH**2 + MJt**2)*((gJtHA**2*MH**4)/2. - gJtHA**2*MH**2*MJt**2 + (gJtHA**2*MJt**4)/2.))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.a,P.Z):'((MJt**2 - MZ**2)*(-2*gJtZA**2*MJt**2 + (2*gJtZA**2*MJt**4)/MZ**2 - 2*gJtZA**2*MZ**2 + (2*gJtZA**2*MZ**4)/MJt**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.b,P.b__tilde__):'((-48*gAbJt**2*MB**2 + 24*gVbJt**2*MB**2 + 12*gAbJt**2*MJt**2 + 12*gVbJt**2*MJt**2)*cmath.sqrt(-4*MB**2*MJt**2 + MJt**4))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.c,P.c__tilde__):'((-48*gAucJt**2*MC**2 + 24*gVucJt**2*MC**2 + 12*gAucJt**2*MJt**2 + 12*gVucJt**2*MJt**2)*cmath.sqrt(-4*MC**2*MJt**2 + MJt**4))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.d,P.d__tilde__):'((-48*gAdsJt**2*MD**2 + 24*gVdsJt**2*MD**2 + 12*gAdsJt**2*MJt**2 + 12*gVdsJt**2*MJt**2)*cmath.sqrt(-4*MD**2*MJt**2 + MJt**4))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.e__minus__,P.e__plus__):'((-16*gAlepJt**2*Me**2 + 8*gVlepJt**2*Me**2 + 4*gAlepJt**2*MJt**2 + 4*gVlepJt**2*MJt**2)*cmath.sqrt(-4*Me**2*MJt**2 + MJt**4))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.H,P.Z):'(((8*gJtHZ**2*MH**4*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (16*gJtHZ**2*MH**2*MJt**2*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (8*gJtHZ**2*MJt**4*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**6*MZ**2)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**8*MZ**2)/(4.*MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**4*MJt**2*MZ**2)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (12*gJtHZ**2*MH**4*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MH**6*MT**2*MZ**2)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (18*gJtHZ**2*MH**2*MJt**2*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (4*gJtHZ**2*MJt**4*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (24*gJtHZ**2*MH**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**4*MT**4*MZ**2)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (12*gJtHZ**2*MJt**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (5*gJtHZ**2*MH**4*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (7*gJtHZ**2*MH**2*MJt**2*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MJt**4*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (20*gJtHZ**2*MH**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (2*gJtHZ**2*MH**4*MT**2*MZ**4)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (6*gJtHZ**2*MJt**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (8*gJtHZ**2*MH**2*MT**4*MZ**4)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (7*gJtHZ**2*MH**2*MZ**6)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**4*MZ**6)/(2.*MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (3*gJtHZ**2*MJt**2*MZ**6)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (2*gJtHZ**2*MH**2*MT**2*MZ**6)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MT**4*MZ**6)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MT**2*MZ**8)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MZ**10)/(4.*MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2))*cmath.sqrt(MH**4 - 2*MH**2*MJt**2 + MJt**4 - 2*MH**2*MZ**2 - 2*MJt**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.mu__minus__,P.mu__plus__):'((4*gAlepJt**2*MJt**2 + 4*gVlepJt**2*MJt**2 - 16*gAlepJt**2*MM**2 + 8*gVlepJt**2*MM**2)*cmath.sqrt(MJt**4 - 4*MJt**2*MM**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.s,P.s__tilde__):'((12*gAdsJt**2*MJt**2 + 12*gVdsJt**2*MJt**2 - 48*gAdsJt**2*MS**2 + 24*gVdsJt**2*MS**2)*cmath.sqrt(MJt**4 - 4*MJt**2*MS**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((4*gAlepJt**2*MJt**2 + 4*gVlepJt**2*MJt**2 - 16*gAlepJt**2*ML**2 + 8*gVlepJt**2*ML**2)*cmath.sqrt(MJt**4 - 4*MJt**2*ML**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.u,P.u__tilde__):'((12*gAucJt**2*MJt**2 + 12*gVucJt**2*MJt**2 - 48*gAucJt**2*MU**2 + 24*gVucJt**2*MU**2)*cmath.sqrt(MJt**4 - 4*MJt**2*MU**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.ve,P.ve__tilde__):'(gnu123**2*MJt**4)/(6.*cmath.pi*abs(MJt)**3)',
                                   (P.vm,P.vm__tilde__):'(gnu123**2*MJt**4)/(6.*cmath.pi*abs(MJt)**3)',
                                   (P.vt,P.vt__tilde__):'(gnu123**2*MJt**4)/(6.*cmath.pi*abs(MJt)**3)',
                                   (P.W__minus__,P.W__plus__):'((-4*gJtWWEJE1k1E2**2*MJt**2 + 2*gJtWWEJE1k1E2*gJtWWEJk1E1E2*MJt**2 + (7*gJtWWEJk1E1E2**2*MJt**2)/4. - 8*gJtWWepsEJk1E1E2**2*MJt**2 + (gJtWWEJE1k1E2**2*MJt**6)/(4.*MW**4) + (gJtWWEJE1k1E2*gJtWWEJk1E1E2*MJt**6)/(4.*MW**4) + (gJtWWEJk1E1E2**2*MJt**6)/(16.*MW**4) - (3*gJtWWEJE1k1E2*gJtWWEJk1E1E2*MJt**4)/(2.*MW**2) - (gJtWWEJk1E1E2**2*MJt**4)/(2.*MW**2) + (gJtWWepsEJk1E1E2**2*MJt**4)/MW**2 - 3*gJtWWEJk1E1E2**2*MW**2 + 16*gJtWWepsEJk1E1E2**2*MW**2)*cmath.sqrt(MJt**4 - 4*MJt**2*MW**2))/(48.*cmath.pi*abs(MJt)**3)',
                                   (P.Z,P.Z):'((-32*gJtZZ**2*MJt**2 + (4*gJtZZ**2*MJt**4)/MZ**2 + 64*gJtZZ**2*MZ**2)*cmath.sqrt(MJt**4 - 4*MJt**2*MZ**2))/(96.*cmath.pi*abs(MJt)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MM**2 - MW**2)*((ee**2*MM**2)/(2.*sw**2) + (ee**2*MM**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MM)**3)'})

Decay_s = Decay(name = 'Decay_s',
                particle = P.s,
                partial_widths = {(P.W__minus__,P.c):'(((3*ee**2*MC**2)/(2.*sw**2) + (3*ee**2*MS**2)/(2.*sw**2) + (3*ee**2*MC**4)/(2.*MW**2*sw**2) - (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) + (3*ee**2*MS**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((ML**2 - MW**2)*((ee**2*ML**2)/(2.*sw**2) + (ee**2*ML**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(ML)**3)'})

Decay_u = Decay(name = 'Decay_u',
                particle = P.u,
                partial_widths = {(P.W__plus__,P.d):'(((3*ee**2*MD**2)/(2.*sw**2) + (3*ee**2*MU**2)/(2.*sw**2) + (3*ee**2*MD**4)/(2.*MW**2*sw**2) - (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) + (3*ee**2*MU**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(((-3*ee**2*MC**2)/(2.*sw**2) - (3*ee**2*MS**2)/(2.*sw**2) - (3*ee**2*MC**4)/(2.*MW**2*sw**2) + (3*ee**2*MC**2*MS**2)/(MW**2*sw**2) - (3*ee**2*MS**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(((-3*ee**2*MD**2)/(2.*sw**2) - (3*ee**2*MU**2)/(2.*sw**2) - (3*ee**2*MD**4)/(2.*MW**2*sw**2) + (3*ee**2*MD**2*MU**2)/(MW**2*sw**2) - (3*ee**2*MU**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-0.5*(ee**2*Me**2)/sw**2 - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MM**2 + MW**2)*(-0.5*(ee**2*MM**2)/sw**2 - (ee**2*MM**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-ML**2 + MW**2)*(-0.5*(ee**2*ML**2)/sw**2 - (ee**2*ML**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.a,P.Et):'((-MEt**2 + MZ**2)*(2*gEtZA**2*MEt**4 - 4*gEtZA**2*MEt**2*MZ**2 + 2*gEtZA**2*MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.a,P.Jt):'((-MJt**2 + MZ**2)*(-2*gJtZA**2*MJt**2 + (2*gJtZA**2*MJt**4)/MZ**2 - 2*gJtZA**2*MZ**2 + (2*gJtZA**2*MZ**4)/MJt**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'((-7*ee**2*MD**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MD**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MD**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MD**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.Et,P.H):'(((gEtHZ**2*MEt**4*MZ**2)/4. - (gEtHZ**2*MEt**2*MH**2*MZ**2)/2. + (gEtHZ**2*MH**4*MZ**2)/4. - (gEtHZ**2*MEt**2*MZ**4)/2. - (gEtHZ**2*MH**2*MZ**4)/2. + (gEtHZ**2*MZ**6)/4.)*cmath.sqrt(MEt**4 - 2*MEt**2*MH**2 + MH**4 - 2*MEt**2*MZ**2 - 2*MH**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.H,P.Jt):'(((2*gJtHZ**2*MH**6*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (6*gJtHZ**2*MH**4*MJt**2*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (6*gJtHZ**2*MH**2*MJt**4*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MJt**6*MT**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (16*gJtHZ**2*MH**4*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (8*gJtHZ**2*MH**6*MT**4)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (8*gJtHZ**2*MH**2*MJt**2*MT**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (16*gJtHZ**2*MH**6*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**8*MT**4)/(MJt**2*MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (24*gJtHZ**2*MH**4*MJt**2*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (16*gJtHZ**2*MH**2*MJt**4*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MJt**6*MT**4)/(MZ**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**4*MJt**2*MZ**2)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**2*MJt**4*MZ**2)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MJt**6*MZ**2)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**4*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (4*gJtHZ**2*MH**2*MJt**2*MT**2*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (24*gJtHZ**2*MH**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (4*gJtHZ**2*MH**4*MT**4*MZ**2)/(MJt**2*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (12*gJtHZ**2*MJt**2*MT**4*MZ**2)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MH**4*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) + (3*gJtHZ**2*MH**2*MJt**2*MZ**4)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (2*gJtHZ**2*MH**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (6*gJtHZ**2*MJt**2*MT**2*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (8*gJtHZ**2*MT**4*MZ**4)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (gJtHZ**2*MH**2*MZ**6)/((-2*MT + MZ)**2*(2*MT + MZ)**2) - (3*gJtHZ**2*MJt**2*MZ**6)/(4.*(-2*MT + MZ)**2*(2*MT + MZ)**2) - (4*gJtHZ**2*MT**2*MZ**6)/((-2*MT + MZ)**2*(2*MT + MZ)**2) + (gJtHZ**2*MZ**8)/(2.*(-2*MT + MZ)**2*(2*MT + MZ)**2))*cmath.sqrt(MH**4 - 2*MH**2*MJt**2 + MJt**4 - 2*MH**2*MZ**2 - 2*MJt**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MM**2 - ee**2*MZ**2 - (cw**2*ee**2*MM**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MM**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MM**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'((-7*ee**2*MS**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MS**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MS**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MS**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*ML**2 - ee**2*MZ**2 - (cw**2*ee**2*ML**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*ML**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*ML**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'((-11*ee**2*MU**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MU**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MU**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

