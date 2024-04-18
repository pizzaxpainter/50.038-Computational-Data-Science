# ALGORITHM 1: Layer-wise principal component analysis
# Input: Strings space (Sm, Sf), which differ only in gender-specific words.
# Output: P-layer-specific principal component token set {p0, ..., Pz}.

# Tokenize input strings
Wf = Tokenize(Sf)
Wm = Tokenize(Sm)

# Layer zero: WordPiece (WP) tokenization
u0 = layer_zero(Wm)
v0 = layer_zero(Wf)

# Context-independent input using Latent Semantic Analysis (LSA)
p0 = PCA(d0)

# Iterate through layers
for j in range(1,12):
    # Perform PCA on uj and vj using Do as context
    uj_minus_1 = proj_pj_minus_1(uj-1)  # perpendicular
    vj_minus_1 = proj_pj_minus_1(vj-1)  # perpendicular

    # Update projection layers
    uj = layer(uj_minus_1)
    vj = layer(vj_minus_1)

    # Compute Dj+1 using PCA on (uj - vj)
    Dj = (vj-uj)
    pj = PCA(Dj)

# End of algorithm
