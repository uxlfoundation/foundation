===================================================================
  AI and Scientific Computing Special Interest Group Meeting Notes
===================================================================

2026-06-25
==========

Attendees

* Vaishnavi (Fujitsu)
* Kevin Kuriakose (Fujitsu)
* Kuldeep pal (Individual)
* Sanket (Fujitsu)
* Abhishek Jain (Fujitsu)
* Nishith Jaiswal (Fujitsu)
* Shubham (Fujitsu)
* Goutam Agrawal (Individual)
* Devang (Fujitsu)
* Penporn Koanantakool (Google LLC)
* Deepika H V (Centre for Development of Advanced Computing)
* Akhil Goel (Individual)
* Jin Takahashi (Fujitsu Limited)
* Alison Richards (Intel Corporation)
* Gaurav Gogia (Fujitsu)
* Ajay (Fujitsu)
* Abhishek Kumar (Fujitsu)
* Priyanka Sharma (Fujitsu)
* Shun Kamatsuka (Fujitsu Limited)
* Aruna K (Fujitsu)
* Shashank Sai Sangu (Fujitsu)
* Jianhui Li (Intel Corporation)
* Dmitry Zarukin (Intel Corporation)
* Divya Kotadiya (Fujitsu)
* Jonathan Deakin (Arm Limited)
* Ragesh Hajela (Fujitsu)
* Nikhil R Sharma (Fujitsu)
* Dhanus M Lal (Fujitsu)
* Atsushi Nukariya (Fujitsu)
* Shreyas Shankar (Fujitsu)
* Shubhajeet Dey (Fujitsu)
* Nathan Sircombe (Arm Limited)
* Mohak Goel (Fujitsu)
* Tao abc (Individual)
* Masahiro Doteguchi (Fujitsu Limited)

================
Recording Link
================

**Watch to explore how Scientific AI is shaping the future of Drug Discovery using OpenFold Optimization with oneDNN and Stack Simplification on AArch64 using KleidiAI** (`Recording Link <https://www.youtube.com/watch?v=5CyYVhbPPxI>`__)

======
Agenda
======

**Accelerating Scientific AI for Drug Discovery: OpenFold Optimization with oneDNN (by Rakshith G B, Lead Software Engineer, and Shreyas Shankar, Software Engineer, Fujitsu Research India)** (`slides <presentations/2026-06-25-UXL-AI&SC-SIG-OpenFold-oneDNN-Fujitsu.pdf>`__)

**oneDNN Stack Simplification on AArch64 using KleidiAI (by Jonathan Deakin, Staff Software Engineer, Arm)** (`slides <presentations/2026-06-25-UXL-AI&SC-SIG-oneDNN-Arm-KleidiAI-JonathanDeakin.pdf>`__)  

Summary
=======

Overview
--------

- This meeting featured two technical presentations on oneDNN optimizations and acceleration of scientific computing.
- First session by Fujitsu team presented their work on AI for drug discovery using protein folding optimization with the oneDNN stack.
- This session focused on JIT BRGEMM kernel optimization for protein structure prediction that achieved speedup on ARM CPU.
- Following this, Jonathan from ARM presented on replacing ACL with KleidiAI in the oneDNN stack for AArch64, covered the technical rationale for the change, implementation strategy, and preliminary benchmark results.
- The discussion included questions about integration approaches, performance implications for different architectures, and potential impacts on downstream frameworks like PyTorch and TensorFlow.

Accelerating Scientific AI for Drug Discovery - Talk by Rakshith G B and Shreyas Shankar, Fujitsu
-------------------------------------------------------------------------------------------------

Title: Accelerating Scientific AI for Drug Discovery: OpenFold Optimization with oneDNN

Abstract
--------

- Protein structure prediction is transforming modern AI-driven drug discovery by enabling rapid understanding of protein folding functions and therapeutic targets.

- This talk introduces OpenFold AI Surrogate Model and presents benchmark results with recent oneDNN-based optimizations, including JIT BRGEMM kernel enhancements. 

Discussion Highlights
---------------------

- Rakshith explained how protein folding simulation has been accelerated from days or months to hours using modern AI models like AlphaFold and OpenFold, which predict 3D protein structures from 2D amino acid sequences.
- Fujitsu team conducted enablement, tuning and benchmark testing on ARM CPU, achieving execution time of 7.3 seconds for a 76-residue protein with 0.24 Å (Angstrom) accuracy, and achieved ~4x performance boost after optimizing OpenFold with oneDNN JIT BRGEMM kernel implementation in PyTorch.
- Shreyas presented on the JIT BRGEMM kernel, explaining how just-in-time compilation using xbyak_aarch64 provides advantages over ahead-of-time compilation by enabling specialized code generation based on runtime conditions, dead code elimination, and better register allocation.
- He detailed the BRGEMM (Batch Reduced GEMM) kernel implementation for ARM architecture, which performs batch reduced general matrix multiplication without storing intermediate results, resulting in approximately ~4x speedup for large matrices compared to the default implementation.
- The work was conducted as part of AI Frameworks OSS Development, and Fujitsu continues to develop these low-level kernels for their upcoming FUJITSU-MONAKA 2nm ARM CPU processor launch in FY2027.

oneDNN Stack Simplification on AArch64 using KleidiAI - Talk by Jonathan Deakin, Arm
------------------------------------------------------------------------------------

Title: oneDNN Stack Simplification on AArch64 using KleidiAI

Abstract
--------

- We will discuss our active oneDNN RFC (`#5145 <https://github.com/uxlfoundation/oneDNN/pull/5145>`__) which proposes replacing Compute Library (ACL) with Arm® KleidiAI™ for AArch64.

- This change is proposed to simplify stack, bringing development and performance benefits. This session will cover a brief history of oneDNN on AArch64, explain our motivation for the change, and discuss questions and feedback.

Discussion Highlights
---------------------

- Jonathan presented on replacing ACL with KleidiAI in oneDNN for AArch64, explaining that this change would simplify the stack ad provide better framework integration.
- The proposed approach involves integrating KleidiAI kernels directly into oneDNN rather than maintaining them as a separate library, which would eliminate the need for additional build steps and reduce complexity.
- Team has created a POC branch and is collecting feedback, with option 1 (integrating KleidiAI into oneDNN's third-party directory) being the preferred approach that has already received approval from community.
- The next steps involve addressing any remaining feedback over the next weeks and integrating the changes into oneDNN, with the goal of including it in the oneDNN v3.14 release.
