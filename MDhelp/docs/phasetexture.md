<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-Texture"></a>
# **Texture** phase tab

This tab is used to control settings used for a texture study of a material. This type of characterization usually requires diffraction data recorded with multiple detector orientations (the number of orientations will depend on sample and material symmetry). Do not confuse this with applying a [preferred orientation correction](./phasedata.md#preferred_orientation) (found in the ["Data" tab](./phasedata.md)) in a structural study. The sample orientation relative to the detector axes is specified here and the detector orientation is specified for each histogram as goniometer omega, chi, phi and azimuth values (details below). These values must be specified.

Texture analysis using GSAS-II employs spherical harmonics modeling, as described by Bunge, "Texture Analysis in Materials Science" (1982), and implemented by Von Dreele, J. Appl. Cryst., **30**, 517-525 (1997) in the original GSAS program. The even part of the orientation distribution function (ODF) via the general axis equation

$$
A(x,y) = 1 + \sum_{L=2}^{N_L}{\frac{4\pi}{2L+1}} \sum_{m=-L}^{L} \sum_{n=-L}^{L} C_L^{mn} k_L^m(y) k_L^n(h)
$$

is used to give the intensity corrections due to texture. The two harmonic terms, \(k_L^m(y)\) and \(k_L^n(h)\) , take on values according to the sample and crystal symmetries, respectively, and thus the two inner summations are over only the resulting unique, nonzero harmonic terms. These unique terms are automatically selected by GSAS-II according to the space group symmetry and the user chosen sample symmetry. The available sample symmetries are cylindrical, 2/m, mmm and no symmetry. The choice of sample symmetry profoundly affects the selection of harmonic coefficients. For example, in the case of cylindrical sample symmetry (fiber texture) only \(k_L^0(y)\) terms are nonzero so the rest are excluded from the summations and the set of \(C_L^{0n}\) coefficients is sufficient to describe the effect on the diffraction pattern due to texture. The crystal harmonic factor, \(k_L^n(h)\), is defined for each reflection, h, *via* polar and azimuthal coordinates \((\phi, \beta)\) of a unit vector coincident with h relative to the reciprocal lattice. For most crystal symmetries, \(\phi\) is the angle between h and the n-th order major rotation axis of the space group (usually the c-axis) and \(\beta\) is the angle between the projections of h and any secondary axis (usually the a-axis) onto the normal plane.  In a similar way the sample harmonic factor, \(k_L^m(y)\), is defined according to polar and azimuthal coordinates \((\psi, \gamma)\) of a unit vector coincident with the diffraction vector relative to a coordinate system attached to the external form of the sample. For example, in the case of a rolled steel plate having mmm symmetry, the polar angle, \(\Psi\), is frequently measured from the normal direction (ND, parallel to K<sub>s</sub>) and g is then measured from the rolling direction (RD, parallel to I<sub>s</sub>) in the TD (transverse direction, parallel to J<sub>s</sub>) - RD plane.  Thus, the general axis equation becomes

$$
A(\phi,\beta,\psi,\gamma) = 1 + \sum_{L=2}^{N_L}{\frac{4\pi}{2L+1}} \sum_{m=-L}^{L} \sum_{n=-L}^{L} C_L^{mn} k_L^m(\psi, \gamma) k_L^n(\phi, \beta)
$$

Note that this version of the general axis equation differs from that shown in Von Dreele (1997) in that the assignment of m and n are reversed.

In a diffraction experiment the crystal reflection coordinates \((\phi, \beta)\) are determined by the choice of reflection index (hkl) while the sample coordinates \((\Psi, \gamma)\) are determined by the sample orientation on the diffractometer. To define the sample coordinates \((\psi, \gamma)\), we have defined an instrument coordinate system (I, J, K) such that K is normal to the diffraction plane and J is coincident with the direction of the incident radiation beam toward the source. We further define a standard set of right-handed eulerian goniometer angles \((\omega, \chi, \phi)\) so that \(\omega\) and \(\phi\) are rotations about K and \(\chi\) is a rotation about J when \(\omega = 0\). Finally, as the sample may be mounted so that the sample coordinate system (\(I_s, J_s, K_s\)) does not coincide with the instrument coordinate system (I, J, K), we define three eulerian sample rotation offset angles \((\omega_s, \chi_s, \phi_s)\) that describe the rotation from (\(I_s, J_s, K_s\)) to (I, J, K).  The sample rotation angles are defined so that with the goniometer angles at zero \(\omega_s\) and \(\phi_s\) are rotations about K and \(\chi_s\) is a rotation about J.  The zeros of these three sample rotation angles can be refined as part of the Rietveld analysis to accommodate any angular offset in sample mounting. For the specific case of cylindrical sample symmetry, the cylinder axis is coincident with Ks as is the 2-fold in 2/m sample symmetry. After including the diffraction angle, \(2\theta\), and a detector azimuthal angle, A, the full rotation matrix, \(M\), is

$$
M = - \theta A \omega \chi (\phi + \phi_s) \chi_s \omega_s
$$

By transformation of unit Cartesian vectors (100, 010 and 001) with this rotation matrix, the sample orientation coordinates \((\psi, \gamma)\) are given by

$$
cos(y) = M \begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix}
$$

and

$$
tan(\gamma) = M \begin{pmatrix}
0 \\
1 \\
0
\end{pmatrix}/ M
\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix} 
$$

The harmonic terms, \(k_L^m(\psi, \gamma)\) and \(k_L^n(\phi, \beta)\), are developed from (those for \(k_L^m(\psi, \gamma)\) are similar)

$$
k_L^n(\phi, \beta) = \frac{1}{\sqrt{2\pi}} e^{in\beta} \bar{P}_L^n(cos\phi)
$$

where the normalized associated Legendre functions, \(\bar{P}_L^n(x)\), are defined via a Fourier expansion as

$$
\bar{P}_L^n(cos\phi) = \sum_{s=0}^L {a'}_L^{ns} sin(s \phi)
$$

for n even and

$$
\bar{P}_L^{ns}(cos\phi) = \sum_{s=0}^L {a'}_L^{ns} sin(s \phi)
$$

for n odd.  Each sum is only over either the even or odd values of s, respectively, because of the properties of the Fourier coefficients, \({a'}_{L}^{ns}\). These Fourier coefficients are determined so that the definition

$$
\bar{P}_L^{n}(cos\phi) = \bar{P}_L^{n}(x) = \sqrt{\frac{(L+n)!}{(L-n)!}} \sqrt{\frac{2L+1}{2}} \frac{(-1)^{L-n}}{2^L L!} (1-x^2)^{-n/2} \frac {d^{L-n}}{dx^{L-n}} (1-x^2)^L
$$

is satisfied. Terms of the form \( cos(n\beta) \bar{P}_L^n(cos{n\beta})\) and \(sin(n\beta) \bar{P}_L^n(cos{\phi})\) are combined depending on the symmetry and the value of n (or m) along with appropriate normalization coefficients to give the harmonic terms \(k_L^n(\phi,\beta)\) and \(k_L^m(\psi,\gamma)\). For cubic crystal symmetry, the term \(k_L^n(\phi,\beta)\) is obtained directly from the Fourier expansion

$$
k_L^n(\phi, \beta) = \sum_{j=0}^L B_L^{nj} \bar{P}_L^n (cos{\phi}) cos{n\beta}
$$

using the coefficients, \(B_L^{nj}\) , as tabulated by Bunge (1982).

The Rietveld refinement of texture then proceeds by constructing derivatives of the profile intensities with respect to the allowed harmonic coefficients, \(C_L^{mn}\), and the three sample orientation angles, \(\omega_s, \chi_s, \phi_s\) Ws, Cs, Fs, all of which can be adjustable parameters of the refinement. Once the refinement is complete, pole figures for any reflection may be constructed by use of the general axis equation, the refined values for \(C_L^{mn}\) and the sample orientation angles \(\omega_s, \chi_s, \phi_s\).

$$
J = 1 + \sum_{L=2}^{N_L} \frac{1}{2L+1} \sum_{m=-L}^{L} \sum_{n=-L}^{L} |C_L^{mn}|^2
$$

The magnitude of the texture is evaluated from the texture index by

If the texture is random then J = 1, otherwise J > 1; for a single crystal J = \(\infty\).

In GSAS-II the texture is defined in two ways to accommodate the two possible uses of this correction. In one, a suite of spherical harmonics coefficients is defined for the texture of a phase in the sample; this can have any of the possible sample symmetries and is the usual result desired for texture analysis. The other is the suite of spherical harmonics terms for cylindrical sample symmetry for each phase in each powder pattern ("histogram") and is usually used to accommodate preferred orientation effects in a Rietveld refinement. The former description allows refinement of the sample orientation zeros, \(\omega_s, \chi_s, \phi_s\), but the latter description does not (they are assumed to be zero and not refinable). The sample orientation angles, \(\omega, \chi, \phi\) are specified in the Sample Parameters table in the GSAS-II data tree structure and are applied for either description.

Some useful examples:

**1. Bragg-Brentano laboratory powder diffractometer**

The conventional arrangement of this experiment is to have a flat sample with incident and diffracted beams at equal angles (theta) on opposite sides of the sample. The sample is frequently spun about its normal to improve powder statistics and impose cylindrical symmetry on any preferred orientation (texture). Thus, the diffraction plane (source, diffraction vector & detector) contains the K-vector which is parallel to the diffraction vector and \(\omega, \chi, \phi = 0\).

**2. Debye-Scherrer diffractometer with point detector(s)**

The usual arrangement here is to have a capillary sample perpendicular to the diffraction plane. The capillary may be spun about its cylinder axis for powder averaging and to impose cylindrical symmetry on the texture which is perpendicular to the diffraction plane. Thus, \(\omega,\phi = 0\) and \(\chi = 90\).

**3. Debye-Scherrer diffractometer with 2D area detector**

The area detector is presumed to be directly behind the sample with the incident beam somewhere near the center of the detector. The detector axes are defined (for a synchrotron) with the X-axis toward the synchrotron ring and the Y-axis vertical "up"; one views the detector image as if looking from the x-ray source. The sample is assumed to be a capillary (which may be spun to impose cylindrical symmetry), although other sample shapes may be used, and is aligned with the cylinder axis horizontal. Integration of the image from a series of "caked" slices gives a set of powder patterns, each assigned an azimuthal angle where zero is along the X-axis. Thus, at azimuth=0 the diffraction plane is horizontal and contains the cylinder axis so \(\omega\), \chi, \(\phi\) = 0.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Texture/Refine **texture' – refines the spherical harmonics texture model using the previously determined values of Prfo for all histogram reflection sets as demonstrated in 2DTexture tutorial.
2. **Texture settings** - The texture index, J is shown on the 1st line.
    
    * The Texture model can be chosen from ['cylindrical', 'none', 'shear - 2/m', or 'rolling – mmm'].
    * The Harmonic order (even integer 0-34), refine flag & show coefficients flag are next.
    * The Texture plot type is one of:
        * **Axial pole distribution** which simulates the intensity of a reflection during a phi scan.
        * **pole figure** where a projection of the probability of finding a pole (hkl) is plotted as a function of sample orientation.
        * **inverse pole figure** where a projection of the probability of finding all poles (hkls) is plotted for a selected sample orientation.
        * **3D pole distribution** that shows the probability of finding a pole (hkl) is plotted as a function of sample orientation.

    For Axial distribution, pole figure and 3D pole distribution one must next select the hkl of the desired pole, for Inverse pole figure one must select a sample direction (typically 0 0 1).

    One can choose the contour (pole & inverse pole figures) color scheme (default "Paired") and make a CSV file of the image for import into other software.

    * The spherical harmonics coefficients are shown next; they may be edited. They may be cleared by setting harmonic order to zero and then back to desired value.
    * The sample orientation angle zeros \((\omega_s, \chi_s, \phi_s)\) are shown with their individual refinement flags.

