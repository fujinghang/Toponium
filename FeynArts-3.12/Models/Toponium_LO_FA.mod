(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)
(*                                                                             *)
(*         This file has been automatically generated by FeynRules.            *)
(*                                                                             *)
(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)


FR$ModelInformation={
  ModelName->"Toponium",
  Authors -> {"Jing-Hang Fu"},
  Institutions -> {"BUAA"},
  Emails -> {"myfujinghang@gmail.com"},
  URLs -> "https://github.com/fujinghang/Toponium",
  References -> {" "},
  Version -> "1.0",
  Date -> "2025.04.13"};

FR$ClassesTranslation={A -> V[1], Z -> V[2], W -> V[3], G -> V[4], ghA -> U[1], ghZ -> U[2], ghWp -> U[3], ghWm -> U[4], ghG -> U[5], ve -> F[1], vm -> F[2], vt -> F[3], e -> F[4], mu -> F[5], ta -> F[6], u -> F[7], c -> F[8], t -> F[9], d -> F[10], s -> F[11], b -> F[12], H -> S[1], G0 -> S[2], GP -> S[3], Et -> S[4], Jt -> V[5]};

FR$InteractionOrderPerturbativeExpansion={{NP, 0}, {QCD, 0}, {QED, 0}};

FR$GoldstoneList={S[2], S[3]};

(*     Declared indices    *)

IndexRange[ Index[Gluon] ] = NoUnfold[ Range[ 8 ] ]

IndexRange[ Index[SU2W] ] = Range[ 3 ]

IndexRange[ Index[Generation] ] = Range[ 3 ]

IndexRange[ Index[Colour] ] = NoUnfold[ Range[ 3 ] ]

IndexRange[ Index[SU2D] ] = Range[ 2 ]

(*     Declared particles    *)

M$ClassesDescription = {
V[1] == {
    SelfConjugate -> True,
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> 0,
    Indices -> {},
    PropagatorLabel -> "A" },

V[2] == {
    SelfConjugate -> True,
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {},
    PropagatorLabel -> "Z" },

V[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorType -> Sine,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {},
    PropagatorLabel -> "W" },

V[4] == {
    SelfConjugate -> True,
    PropagatorType -> Cycles,
    PropagatorArrow -> None,
    Mass -> 0,
    Indices -> {Index[Gluon]},
    PropagatorLabel -> "G" },

U[1] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {},
    PropagatorLabel -> "ghA" },

U[2] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MZ,
    Indices -> {},
    PropagatorLabel -> "ghZ" },

U[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, Q},
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {},
    PropagatorLabel -> "ghWp" },

U[4] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, -Q},
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {},
    PropagatorLabel -> "ghWm" },

U[5] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {Index[Gluon]},
    PropagatorLabel -> "ghG" },

F[1] == {
    SelfConjugate -> False,
    QuantumNumbers -> {LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {},
    PropagatorLabel -> "ve" },

F[2] == {
    SelfConjugate -> False,
    QuantumNumbers -> {LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {},
    PropagatorLabel -> "vm" },

F[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {},
    PropagatorLabel -> "vt" },

F[4] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Me,
    Indices -> {},
    PropagatorLabel -> "e" },

F[5] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MM,
    Indices -> {},
    PropagatorLabel -> "mu" },

F[6] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> ML,
    Indices -> {},
    PropagatorLabel -> "ta" },

F[7] == {
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MU,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "u" },

F[8] == {
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MC,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "c" },

F[9] == {
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MT,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "t" },

F[10] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-1/3*Q},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MD,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "d" },

F[11] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-1/3*Q},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MS,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "s" },

F[12] == {
    SelfConjugate -> False,
    QuantumNumbers -> {-1/3*Q},
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> MB,
    Indices -> {Index[Colour]},
    PropagatorLabel -> "b" },

S[1] == {
    SelfConjugate -> True,
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MH,
    Indices -> {},
    PropagatorLabel -> "H" },

S[2] == {
    SelfConjugate -> True,
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {},
    PropagatorLabel -> "G0" },

S[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MW,
    Indices -> {},
    PropagatorLabel -> "GP" },

S[4] == {
    SelfConjugate -> True,
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MEt,
    Indices -> {},
    PropagatorLabel -> "Et" },

V[5] == {
    SelfConjugate -> True,
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MJt,
    Indices -> {},
    PropagatorLabel -> "Jt" }
}


(*        Definitions       *)

GaugeXi[ V[1] ] = GaugeXi[A];
GaugeXi[ V[2] ] = GaugeXi[Z];
GaugeXi[ V[3] ] = GaugeXi[W];
GaugeXi[ V[4] ] = GaugeXi[G];
GaugeXi[ U[1] ] = GaugeXi[A];
GaugeXi[ U[2] ] = GaugeXi[Z];
GaugeXi[ U[3] ] = GaugeXi[W];
GaugeXi[ U[4] ] = GaugeXi[W];
GaugeXi[ U[5] ] = GaugeXi[G];
GaugeXi[ S[1] ] = 1;
GaugeXi[ S[2] ] = GaugeXi[Z];
GaugeXi[ S[3] ] = GaugeXi[W];
GaugeXi[ S[4] ] = 1;
GaugeXi[ V[5] ] = 1;

MZ[ ___ ] := MZ;
MW[ ___ ] := MW;
Me[ ___ ] := Me;
MM[ ___ ] := MM;
ML[ ___ ] := ML;
MU[ ___ ] := MU;
MC[ ___ ] := MC;
MT[ ___ ] := MT;
MD[ ___ ] := MD;
MS[ ___ ] := MS;
MB[ ___ ] := MB;
MH[ ___ ] := MH;
MEt[ ___ ] := MEt;
MJt[ ___ ] := MJt;


TheLabel[ V[4, {__}] ] := TheLabel[V[4]];
TheLabel[ U[5, {__}] ] := TheLabel[U[5]];
TheLabel[ F[7, {__}] ] := TheLabel[F[7]];
TheLabel[ F[8, {__}] ] := TheLabel[F[8]];
TheLabel[ F[9, {__}] ] := TheLabel[F[9]];
TheLabel[ F[10, {__}] ] := TheLabel[F[10]];
TheLabel[ F[11, {__}] ] := TheLabel[F[11]];
TheLabel[ F[12, {__}] ] := TheLabel[F[12]];


(*      Couplings (calculated by FeynRules)      *)

M$CouplingMatrices = {

C[ V[1] , V[5] , V[2] ] == {{gc1, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[2] , S[2] , S[2] , S[2] ] == {{(-6*I)*lam, 0}},

C[ S[2] , S[2] , S[3] , -S[3] ] == {{(-2*I)*lam, 0}},

C[ S[3] , S[3] , -S[3] , -S[3] ] == {{(-4*I)*lam, 0}},

C[ S[2] , S[2] , S[1] , S[1] ] == {{(-2*I)*lam, 0}},

C[ S[3] , -S[3] , S[1] , S[1] ] == {{(-2*I)*lam, 0}},

C[ S[1] , S[1] , S[1] , S[1] ] == {{(-6*I)*lam, 0}},

C[ S[2] , S[2] , S[1] ] == {{(-2*I)*lam*vev, 0}},

C[ S[3] , -S[3] , S[1] ] == {{(-2*I)*lam*vev, 0}},

C[ S[1] , S[1] , S[1] ] == {{(-6*I)*lam*vev, 0}},

C[ S[3] , -S[3] , V[1] , V[1] ] == {{(2*I)*EL^2, 0}},

C[ S[3] , -S[3] , V[1] ] == {{(-I)*gc12, 0}, {I*gc12, 0}, {0, 0}, {0, 0}},

C[ S[4] , S[1] , V[2] ] == {{0, 0}, {0, 0}, {-gc13, 0}, {gc13, 0}},

C[ -U[1] , U[4] , V[3] ] == {{I*gc14, 0}, {I*gc14, 0}, {0, 0}},

C[ -U[1] , U[3] , -V[3] ] == {{I*gc15, 0}, {I*gc15, 0}, {0, 0}},

C[ -S[3] , -U[4] , U[1] ] == {{(EL^2*vev)/(2*sw), 0}},

C[ -U[4] , U[1] , -V[3] ] == {{I*gc17, 0}, {I*gc17, 0}, {0, 0}},

C[ S[2] , -U[4] , U[4] ] == {{-1/4*(EL^2*vev)/sw^2, 0}},

C[ S[1] , -U[4] , U[4] ] == {{((-1/4*I)*EL^2*vev)/sw^2, 0}},

C[ -U[4] , U[4] , V[1] ] == {{I*gc20, 0}, {I*gc20, 0}, {0, 0}},

C[ -U[4] , U[4] , V[2] ] == {{I*gc21, 0}, {I*gc21, 0}, {0, 0}},

C[ -S[3] , -U[4] , U[2] ] == {{(EL^2*(cw - sw)*(cw + sw)*vev)/(4*cw*sw^2), 0}},

C[ -U[4] , U[2] , -V[3] ] == {{I*gc23, 0}, {I*gc23, 0}, {0, 0}},

C[ S[3] , -U[3] , U[1] ] == {{-1/2*(EL^2*vev)/sw, 0}},

C[ -U[3] , U[1] , V[3] ] == {{I*gc25, 0}, {I*gc25, 0}, {0, 0}},

C[ S[2] , -U[3] , U[3] ] == {{(EL^2*vev)/(4*sw^2), 0}},

C[ S[1] , -U[3] , U[3] ] == {{((-1/4*I)*EL^2*vev)/sw^2, 0}},

C[ -U[3] , U[3] , V[1] ] == {{I*gc28, 0}, {I*gc28, 0}, {0, 0}},

C[ -U[3] , U[3] , V[2] ] == {{I*gc29, 0}, {I*gc29, 0}, {0, 0}},

C[ S[3] , -U[3] , U[2] ] == {{-1/4*(EL^2*(cw - sw)*(cw + sw)*vev)/(cw*sw^2), 0}},

C[ -U[3] , U[2] , V[3] ] == {{I*gc31, 0}, {I*gc31, 0}, {0, 0}},

C[ S[3] , -U[2] , U[4] ] == {{(EL^2*(cw^2 + sw^2)*vev)/(4*cw*sw^2), 0}},

C[ -U[2] , U[4] , V[3] ] == {{I*gc33, 0}, {I*gc33, 0}, {0, 0}},

C[ -S[3] , -U[2] , U[3] ] == {{-1/4*(EL^2*(cw^2 + sw^2)*vev)/(cw*sw^2), 0}},

C[ -U[2] , U[3] , -V[3] ] == {{I*gc35, 0}, {I*gc35, 0}, {0, 0}},

C[ S[1] , -U[2] , U[2] ] == {{((-1/4*I)*EL^2*(cw^2 + sw^2)^2*vev)/(cw^2*sw^2), 0}},

C[ S[4] , V[4, {e2x2}] , V[4, {e3x2}] ] == {{I*gc37*IndexDelta[e2x2, e3x2], 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[4] , V[3] , -V[3] ] == {{I*gc38, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[4] , V[2] , V[2] ] == {{I*gc39, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[4] , V[1] , V[1] ] == {{I*gc40, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[4] , V[1] , V[2] ] == {{I*gc41, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ -U[5, {e1x1}] , U[5, {e2x1}] , V[4, {e3x2}] ] == {{gc42*SUNF[e3x2, e1x1, e2x1], 0}, {gc42*SUNF[e3x2, e1x1, e2x1], 0}, {0, 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] ] == {{0, 0}, {-(gc43*SUNF[e1x2, e2x2, e3x2]), 0}, {gc43*SUNF[e1x2, e2x2, e3x2], 0}, {gc43*SUNF[e1x2, e2x2, e3x2], 0}, {-(gc43*SUNF[e1x2, e2x2, e3x2]), 0}, {-(gc43*SUNF[e1x2, e2x2, e3x2]), 0}, {gc43*SUNF[e1x2, e2x2, e3x2], 0}, {0, 0}, {0, 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] ] == {{(-I)*gc44*(SUNF[e1x2, e2x2, e3x2, e4x2] + SUNF[e1x2, e3x2, e2x2, e4x2]), 0}, {I*gc44*(SUNF[e1x2, e2x2, e3x2, e4x2] - SUNF[e1x2, e4x2, e2x2, e3x2]), 0}, {I*gc44*(SUNF[e1x2, e3x2, e2x2, e4x2] + SUNF[e1x2, e4x2, e2x2, e3x2]), 0}},

C[ S[4] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] ] == {{gc45*SUNF[e2x2, e3x2, e4x2], 0}, {gc45*SUNF[e2x2, e3x2, e4x2], 0}, {gc45*SUNF[e2x2, e3x2, e4x2], 0}},

C[ S[4] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] , V[4, {e5x2}] ] == {{(4*I)*gEtGG*GS^2*(SUNF[e2x2, e3x2, e4x2, e5x2] - SUNF[e2x2, e4x2, e3x2, e5x2] + SUNF[e2x2, e5x2, e3x2, e4x2]), 0}},

C[ S[1] , V[1] , V[5] ] == {{0, 0}, {(-I)*gc47, 0}, {I*gc47, 0}, {0, 0}, {0, 0}, {0, 0}},

C[ S[1] , V[5] , V[2] ] == {{0, 0}, {0, 0}, {0, 0}, {(-I)*gc48*(4*MT^2 - MZ^2), 0}, {I*gc48*MH^2*MZ^2, 0}, {I*gc48*(4*MT^2 - MZ^2), 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , V[5] ] == {{I*gc49L*IndexDelta[e1x2, e2x2], 0}, {I*gc49R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , V[5] ] == {{I*gc50L*IndexDelta[e1x2, e2x2], 0}, {I*gc50R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , V[5] ] == {{I*gc51L*IndexDelta[e1x2, e2x2], 0}, {I*gc51R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[4] , F[4] , V[5] ] == {{I*gc52L, 0}, {I*gc52R, 0}},

C[ -F[5] , F[5] , V[5] ] == {{I*gc53L, 0}, {I*gc53R, 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , V[5] ] == {{I*gc54L*IndexDelta[e1x2, e2x2], 0}, {I*gc54R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[6] , F[6] , V[5] ] == {{I*gc55L, 0}, {I*gc55R, 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , V[5] ] == {{I*gc56L*IndexDelta[e1x2, e2x2], 0}, {I*gc56R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[1] , F[1] , V[5] ] == {{I*gc57, 0}, {0, 0}},

C[ -F[2] , F[2] , V[5] ] == {{I*gc58, 0}, {0, 0}},

C[ -F[3] , F[3] , V[5] ] == {{I*gc59, 0}, {0, 0}},

C[ -F[12, {e1x2}] , F[9, {e2x2}] , -S[3] ] == {{gc60L*IndexDelta[e1x2, e2x2], 0}, {gc60R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[7, {e2x2}] , -S[3] ] == {{gc61L*IndexDelta[e1x2, e2x2], 0}, {gc61R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[8, {e2x2}] , -S[3] ] == {{gc62L*IndexDelta[e1x2, e2x2], 0}, {gc62R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , S[2] ] == {{gc63L*IndexDelta[e1x2, e2x2], 0}, {gc63R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , S[2] ] == {{gc64L*IndexDelta[e1x2, e2x2], 0}, {gc64R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , S[2] ] == {{gc65L*IndexDelta[e1x2, e2x2], 0}, {gc65R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , S[1] ] == {{I*gc66*IndexDelta[e1x2, e2x2], 0}, {I*gc66*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , S[1] ] == {{I*gc67*IndexDelta[e1x2, e2x2], 0}, {I*gc67*IndexDelta[e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , S[1] ] == {{I*gc68*IndexDelta[e1x2, e2x2], 0}, {I*gc68*IndexDelta[e1x2, e2x2], 0}},

C[ -F[4] , F[1] , -S[3] ] == {{gc69, 0}, {0, 0}},

C[ -F[5] , F[2] , -S[3] ] == {{gc70, 0}, {0, 0}},

C[ -F[6] , F[3] , -S[3] ] == {{gc71, 0}, {0, 0}},

C[ -F[4] , F[4] , S[2] ] == {{gc72L, 0}, {gc72R, 0}},

C[ -F[5] , F[5] , S[2] ] == {{gc73L, 0}, {gc73R, 0}},

C[ -F[6] , F[6] , S[2] ] == {{gc74L, 0}, {gc74R, 0}},

C[ -F[4] , F[4] , S[1] ] == {{I*gc75, 0}, {I*gc75, 0}},

C[ -F[5] , F[5] , S[1] ] == {{I*gc76, 0}, {I*gc76, 0}},

C[ -F[6] , F[6] , S[1] ] == {{I*gc77, 0}, {I*gc77, 0}},

C[ -F[8, {e1x2}] , F[11, {e2x2}] , S[3] ] == {{gc78L*IndexDelta[e1x2, e2x2], 0}, {gc78R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[12, {e2x2}] , S[3] ] == {{gc79L*IndexDelta[e1x2, e2x2], 0}, {gc79R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[10, {e2x2}] , S[3] ] == {{gc80L*IndexDelta[e1x2, e2x2], 0}, {gc80R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , S[2] ] == {{gc81L*IndexDelta[e1x2, e2x2], 0}, {gc81R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[9, {e2x2}] , S[2] ] == {{gc82L*IndexDelta[e1x2, e2x2], 0}, {gc82R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , S[2] ] == {{gc83L*IndexDelta[e1x2, e2x2], 0}, {gc83R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , S[1] ] == {{I*gc84*IndexDelta[e1x2, e2x2], 0}, {I*gc84*IndexDelta[e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[9, {e2x2}] , S[1] ] == {{I*gc85*IndexDelta[e1x2, e2x2], 0}, {I*gc85*IndexDelta[e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , S[1] ] == {{I*gc86*IndexDelta[e1x2, e2x2], 0}, {I*gc86*IndexDelta[e1x2, e2x2], 0}},

C[ S[2] , -S[3] , V[1] , V[3] ] == {{((-1/2*I)*EL^2)/sw, 0}},

C[ -S[3] , S[1] , V[1] , V[3] ] == {{-1/2*EL^2/sw, 0}},

C[ S[2] , -S[3] , V[3] ] == {{(-I)*gc89, 0}, {I*gc89, 0}, {0, 0}, {0, 0}},

C[ -S[3] , S[1] , V[3] ] == {{-gc90, 0}, {gc90, 0}, {0, 0}, {0, 0}},

C[ V[1] , V[3] , -V[3] ] == {{0, 0}, {(-I)*gc91, 0}, {I*gc91, 0}, {I*gc91, 0}, {(-I)*gc91, 0}, {(-I)*gc91, 0}, {I*gc91, 0}, {0, 0}, {0, 0}},

C[ V[5] , V[3] , -V[3] ] == {{0, 0}, {0, 0}, {(-2*I)*gc92*gJtWWEJE1k1E2, 0}, {0, 0}, {(2*I)*gc92*gJtWWEJE1k1E2, 0}, {(-I)*gc92*gJtWWEJk1E1E2, 0}, {I*gc92*gJtWWEJk1E1E2, 0}, {-2*gc92*gJtWWepsEJk1E1E2, 0}, {2*gc92*gJtWWepsEJk1E1E2, 0}},

C[ S[2] , S[3] , V[1] , -V[3] ] == {{((-1/2*I)*EL^2)/sw, 0}},

C[ S[3] , S[1] , V[1] , -V[3] ] == {{EL^2/(2*sw), 0}},

C[ S[2] , S[3] , -V[3] ] == {{(-I)*gc95, 0}, {I*gc95, 0}, {0, 0}, {0, 0}},

C[ S[3] , S[1] , -V[3] ] == {{-gc96, 0}, {gc96, 0}, {0, 0}, {0, 0}},

C[ S[2] , S[2] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[3] , -S[3] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[1] , S[1] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc100, 0}, {(-I)*gc100, 0}, {(2*I)*gc100, 0}},

C[ V[3] , -V[3] , V[2] ] == {{0, 0}, {(-I)*gc101, 0}, {I*gc101, 0}, {I*gc101, 0}, {(-I)*gc101, 0}, {(-I)*gc101, 0}, {I*gc101, 0}, {0, 0}, {0, 0}},

C[ V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc102, 0}, {(-I)*gc102, 0}, {(2*I)*gc102, 0}},

C[ -F[1] , F[4] , S[3] ] == {{0, 0}, {gc103R, 0}},

C[ -F[2] , F[5] , S[3] ] == {{0, 0}, {gc104R, 0}},

C[ -F[3] , F[6] , S[3] ] == {{0, 0}, {gc105R, 0}},

C[ S[3] , -S[3] , V[1] , V[2] ] == {{(I*EL^2*(cw - sw)*(cw + sw))/(cw*sw), 0}},

C[ S[2] , S[1] , V[2] ] == {{-gc107, 0}, {gc107, 0}, {0, 0}, {0, 0}},

C[ S[3] , -S[3] , V[2] ] == {{(-I)*gc108, 0}, {I*gc108, 0}, {0, 0}, {0, 0}},

C[ S[2] , -S[3] , V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ -S[3] , S[1] , V[3] , V[2] ] == {{EL^2/(2*cw), 0}},

C[ S[2] , S[3] , -V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ S[3] , S[1] , -V[3] , V[2] ] == {{-1/2*EL^2/cw, 0}},

C[ V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc113, 0}, {I*gc113, 0}, {I*gc113, 0}},

C[ S[2] , S[2] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[3] , -S[3] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw - sw)^2*(cw + sw)^2)/(cw^2*sw^2), 0}},

C[ S[1] , S[1] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[1] , V[2] , V[2] ] == {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {I*gc117, 0}, {0, 0}},

C[ V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc118, 0}, {(-I)*gc118, 0}, {(2*I)*gc118, 0}},

C[ V[5] , V[2] , V[2] ] == {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {-gc119, 0}, {gc119, 0}},

C[ -F[4] , F[4] , V[1] ] == {{I*gc120, 0}, {I*gc120, 0}},

C[ -F[5] , F[5] , V[1] ] == {{I*gc121, 0}, {I*gc121, 0}},

C[ -F[6] , F[6] , V[1] ] == {{I*gc122, 0}, {I*gc122, 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , V[1] ] == {{I*gc123*IndexDelta[e1x2, e2x2], 0}, {I*gc123*IndexDelta[e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[9, {e2x2}] , V[1] ] == {{I*gc124*IndexDelta[e1x2, e2x2], 0}, {I*gc124*IndexDelta[e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , V[1] ] == {{I*gc125*IndexDelta[e1x2, e2x2], 0}, {I*gc125*IndexDelta[e1x2, e2x2], 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , V[1] ] == {{I*gc126*IndexDelta[e1x2, e2x2], 0}, {I*gc126*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , V[1] ] == {{I*gc127*IndexDelta[e1x2, e2x2], 0}, {I*gc127*IndexDelta[e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , V[1] ] == {{I*gc128*IndexDelta[e1x2, e2x2], 0}, {I*gc128*IndexDelta[e1x2, e2x2], 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , V[4, {e3x2}] ] == {{I*gc129*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc129*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[9, {e2x2}] , V[4, {e3x2}] ] == {{I*gc130*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc130*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , V[4, {e3x2}] ] == {{I*gc131*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc131*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , V[4, {e3x2}] ] == {{I*gc132*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc132*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , V[4, {e3x2}] ] == {{I*gc133*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc133*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , V[4, {e3x2}] ] == {{I*gc134*SUNT[e3x2, e1x2, e2x2], 0}, {I*gc134*SUNT[e3x2, e1x2, e2x2], 0}},

C[ -F[8, {e1x2}] , F[11, {e2x2}] , V[3] ] == {{I*gc135*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[9, {e1x2}] , F[12, {e2x2}] , V[3] ] == {{I*gc136*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[7, {e1x2}] , F[10, {e2x2}] , V[3] ] == {{I*gc137*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[12, {e1x2}] , F[9, {e2x2}] , -V[3] ] == {{I*gc138*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[10, {e1x2}] , F[7, {e2x2}] , -V[3] ] == {{I*gc139*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[11, {e1x2}] , F[8, {e2x2}] , -V[3] ] == {{I*gc140*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[1] , F[4] , V[3] ] == {{I*gc141, 0}, {0, 0}},

C[ -F[2] , F[5] , V[3] ] == {{I*gc142, 0}, {0, 0}},

C[ -F[3] , F[6] , V[3] ] == {{I*gc143, 0}, {0, 0}},

C[ -F[4] , F[1] , -V[3] ] == {{I*gc144, 0}, {0, 0}},

C[ -F[5] , F[2] , -V[3] ] == {{I*gc145, 0}, {0, 0}},

C[ -F[6] , F[3] , -V[3] ] == {{I*gc146, 0}, {0, 0}},

C[ -F[8, {e1x2}] , F[8, {e2x2}] , V[2] ] == {{I*gc147L*IndexDelta[e1x2, e2x2], 0}, {I*gc147R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[9, {e1x2}] , F[9, {e2x2}] , V[2] ] == {{I*gc148L*IndexDelta[e1x2, e2x2], 0}, {I*gc148R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[7, {e1x2}] , F[7, {e2x2}] , V[2] ] == {{I*gc149L*IndexDelta[e1x2, e2x2], 0}, {I*gc149R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[12, {e1x2}] , F[12, {e2x2}] , V[2] ] == {{I*gc150L*IndexDelta[e1x2, e2x2], 0}, {I*gc150R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[10, {e1x2}] , F[10, {e2x2}] , V[2] ] == {{I*gc151L*IndexDelta[e1x2, e2x2], 0}, {I*gc151R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[11, {e1x2}] , F[11, {e2x2}] , V[2] ] == {{I*gc152L*IndexDelta[e1x2, e2x2], 0}, {I*gc152R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[1] , F[1] , V[2] ] == {{I*gc153, 0}, {0, 0}},

C[ -F[2] , F[2] , V[2] ] == {{I*gc154, 0}, {0, 0}},

C[ -F[3] , F[3] , V[2] ] == {{I*gc155, 0}, {0, 0}},

C[ -F[4] , F[4] , V[2] ] == {{I*gc156L, 0}, {I*gc156R, 0}},

C[ -F[5] , F[5] , V[2] ] == {{I*gc157L, 0}, {I*gc157R, 0}},

C[ -F[6] , F[6] , V[2] ] == {{I*gc158L, 0}, {I*gc158R, 0}}

}

(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)

(* Parameter replacement lists (These lists were created by FeynRules) *)

(* FA Couplings *)

M$FACouplings = {
     gc1 -> -2*gJtZA,
     gc12 -> -EL,
     gc13 -> -gEtHZ,
     gc14 -> EL,
     gc15 -> -EL,
     gc17 -> EL,
     gc20 -> -EL,
     gc21 -> -((cw*EL)/sw),
     gc23 -> (cw*EL)/sw,
     gc25 -> -EL,
     gc28 -> EL,
     gc29 -> (cw*EL)/sw,
     gc31 -> -((cw*EL)/sw),
     gc33 -> (cw*EL)/sw,
     gc35 -> -((cw*EL)/sw),
     gc37 -> 4*gEtGG,
     gc38 -> 2*gEtWW,
     gc39 -> 4*gEtZZ,
     gc40 -> 4*gEtAA,
     gc41 -> 2*gEtZA,
     gc42 -> GS,
     gc43 -> -GS,
     gc44 -> -GS^2,
     gc45 -> 4*gEtGG*GS,
     gc47 -> gJtHA,
     gc48 -> gJtHZ/(4*MT^2 - MZ^2),
     gc49L -> -gAbJt + gVbJt,
     gc49R -> gAbJt + gVbJt,
     gc50L -> -gAucJt + gVucJt,
     gc50R -> gAucJt + gVucJt,
     gc51L -> -gAdsJt + gVdsJt,
     gc51R -> gAdsJt + gVdsJt,
     gc52L -> -gAlepJt + gVlepJt,
     gc52R -> gAlepJt + gVlepJt,
     gc53L -> -gAlepJt + gVlepJt,
     gc53R -> gAlepJt + gVlepJt,
     gc54L -> -gAdsJt + gVdsJt,
     gc54R -> gAdsJt + gVdsJt,
     gc55L -> -gAlepJt + gVlepJt,
     gc55R -> gAlepJt + gVlepJt,
     gc56L -> -gAucJt + gVucJt,
     gc56R -> gAucJt + gVucJt,
     gc57 -> 2*gnu123,
     gc58 -> 2*gnu123,
     gc59 -> 2*gnu123,
     gc60L -> yb,
     gc60R -> -yt,
     gc61L -> ydo,
     gc61R -> -yup,
     gc62L -> ys,
     gc62R -> -yc,
     gc63L -> -(yb/Sqrt[2]),
     gc63R -> yb/Sqrt[2],
     gc64L -> -(ydo/Sqrt[2]),
     gc64R -> ydo/Sqrt[2],
     gc65L -> -(ys/Sqrt[2]),
     gc65R -> ys/Sqrt[2],
     gc66 -> -(yb/Sqrt[2]),
     gc67 -> -(ydo/Sqrt[2]),
     gc68 -> -(ys/Sqrt[2]),
     gc69 -> ye,
     gc70 -> ym,
     gc71 -> ytau,
     gc72L -> -(ye/Sqrt[2]),
     gc72R -> ye/Sqrt[2],
     gc73L -> -(ym/Sqrt[2]),
     gc73R -> ym/Sqrt[2],
     gc74L -> -(ytau/Sqrt[2]),
     gc74R -> ytau/Sqrt[2],
     gc75 -> -(ye/Sqrt[2]),
     gc76 -> -(ym/Sqrt[2]),
     gc77 -> -(ytau/Sqrt[2]),
     gc78L -> yc,
     gc78R -> -ys,
     gc79L -> yt,
     gc79R -> -yb,
     gc80L -> yup,
     gc80R -> -ydo,
     gc81L -> yc/Sqrt[2],
     gc81R -> -(yc/Sqrt[2]),
     gc82L -> yt/Sqrt[2],
     gc82R -> -(yt/Sqrt[2]),
     gc83L -> yup/Sqrt[2],
     gc83R -> -(yup/Sqrt[2]),
     gc84 -> -(yc/Sqrt[2]),
     gc85 -> -(yt/Sqrt[2]),
     gc86 -> -(yup/Sqrt[2]),
     gc89 -> EL/(2*sw),
     gc90 -> -1/2*EL/sw,
     gc91 -> EL,
     gc92 -> 1/2,
     gc95 -> -1/2*EL/sw,
     gc96 -> -1/2*EL/sw,
     gc100 -> -EL^2,
     gc101 -> (cw*EL)/sw,
     gc102 -> EL^2/sw^2,
     gc103R -> -ye,
     gc104R -> -ym,
     gc105R -> -ytau,
     gc107 -> -1/2*(EL*(cw^2 + sw^2))/(cw*sw),
     gc108 -> -1/2*(cw*EL)/sw + (EL*sw)/(2*cw),
     gc113 -> (cw*EL^2)/sw,
     gc117 -> (EL^2*(cw^2 + sw^2)^2*vev)/(2*cw^2*sw^2),
     gc118 -> -((cw^2*EL^2)/sw^2),
     gc119 -> -2*gJtZZ,
     gc120 -> -EL,
     gc121 -> -EL,
     gc122 -> -EL,
     gc123 -> (2*EL)/3,
     gc124 -> (2*EL)/3,
     gc125 -> (2*EL)/3,
     gc126 -> -1/3*EL,
     gc127 -> -1/3*EL,
     gc128 -> -1/3*EL,
     gc129 -> GS,
     gc130 -> GS,
     gc131 -> GS,
     gc132 -> GS,
     gc133 -> GS,
     gc134 -> GS,
     gc135 -> EL/(Sqrt[2]*sw),
     gc136 -> EL/(Sqrt[2]*sw),
     gc137 -> EL/(Sqrt[2]*sw),
     gc138 -> EL/(Sqrt[2]*sw),
     gc139 -> EL/(Sqrt[2]*sw),
     gc140 -> EL/(Sqrt[2]*sw),
     gc141 -> EL/(Sqrt[2]*sw),
     gc142 -> EL/(Sqrt[2]*sw),
     gc143 -> EL/(Sqrt[2]*sw),
     gc144 -> EL/(Sqrt[2]*sw),
     gc145 -> EL/(Sqrt[2]*sw),
     gc146 -> EL/(Sqrt[2]*sw),
     gc147L -> (cw*EL)/(2*sw) - (EL*sw)/(6*cw),
     gc147R -> (-2*EL*sw)/(3*cw),
     gc148L -> (cw*EL)/(2*sw) - (EL*sw)/(6*cw),
     gc148R -> (-2*EL*sw)/(3*cw),
     gc149L -> (cw*EL)/(2*sw) - (EL*sw)/(6*cw),
     gc149R -> (-2*EL*sw)/(3*cw),
     gc150L -> -1/6*(EL*(3*cw^2 + sw^2))/(cw*sw),
     gc150R -> (EL*sw)/(3*cw),
     gc151L -> -1/6*(EL*(3*cw^2 + sw^2))/(cw*sw),
     gc151R -> (EL*sw)/(3*cw),
     gc152L -> -1/6*(EL*(3*cw^2 + sw^2))/(cw*sw),
     gc152R -> (EL*sw)/(3*cw),
     gc153 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc154 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc155 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc156L -> -1/2*(EL*(cw^2 - sw^2))/(cw*sw),
     gc156R -> (EL*sw)/cw,
     gc157L -> -1/2*(EL*(cw^2 - sw^2))/(cw*sw),
     gc157R -> (EL*sw)/cw,
     gc158L -> -1/2*(EL*(cw^2 - sw^2))/(cw*sw),
     gc158R -> (EL*sw)/cw};

