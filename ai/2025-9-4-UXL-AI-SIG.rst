=========================================
AI Special Interest Group Meeting Notes
=========================================

2025-09-04
==========
Attendees

* Alexandre Santana     (Barcelona Supercomputing Center)         
* Penporn Koanantakool  (Google LLC)
* Milos Puzovic         (Arm Limited)
* Rod Burns             (Codeplay Software)
* Aruna K               (Fujitsu Limited)
* Tao Lv                (Intel)
* mahesh budavarapu     (Radisys Corporation)
* S\. J\. Golzar          (University of Salerno)
* Alison Richards       (Intel Corporation)
* Abhishek Bagusetty    (Individual)
* Marc Casas       (Barcelona Supercomputing Center)
* Alice Wen             (Individual) 
* William Jones         (Embecosm Ltd.)
* David Edelsohn        (NVIDIA Corporation)
* Denis Samoilov        (Intel Corporation)
* Kevan Ahmadi          (Imagination Technologies)
* Vasudha Badri-Paul    (Intel Corporation)
* Dave                  (Individual)  
* Nikolay Petrov        (Intel Corporation)
* Jianhui Li            (Intel Corporation)
* Dhanus M Lal          (Fujitsu Limited)
* John Melonakos        (Intel Corporation)
* Mourad Gouicem        (Intel Corporation)
* Abhishek Jain         (Fujitsu Limited)
* Ashok Bhat            (Arm Limited)
* Nagendra Kumar        (Individual)

======
Agenda
======

OneDNN RISC-V ”V” Primitives,  Alexandre Santana, Marc Casas, Barcelona Supercomputing Center (`slides <presentations/2025-09-04-UXL-AISIG-.pdf>`__)

======
Notes
======

Quick Recap
Alexandre and Marc presented their work on vectorization of AI kernels for RISC-V architecture, focusing on developing vector length-agnostic algorithms and a new code generation library called RVjit. The team discussed their optimization efforts for different vector register groupings and performance evaluations across various systems, including the development of convolution API and integration with OneDNN. The conversation ended with discussions about microkernel implementation for different vector lengths, automatic enablement of graph API in RISC 5.

Summary

RISC-V Vectorization for AI Kernels:Alexandre from the Barcelona Supercomputing Center presented their work on vectorization of AI kernels for RISC-V architecture, focusing on developing vector length-agnostic algorithms for computer vision workloads. They translated existing AVX-512 algorithms into RISC-V ISA and added register grouping functionality, which allows for higher vector lengths at the cost of fewer vector registers. The team developed their own just-in-time assembler library called RVjit, inspired by Xybak, to handle architecture-specific code generation for RISC-V.

RISC-V Vector Instruction Performance:Alexandre explained the vector instruction protocol in RISC-V, where applications request vector lengths and hardware grants them, allowing instructions to be configured for various element widths. He demonstrated performance evaluations of convolution operations on different systems, showing that each processor has a preferred vector register grouping scheme, with differences in performance up to 50% depending on the choice. Alexandre presented a new RISC-V code generation library that adapts to vector types and can detect available extensions, similar to Xybak, making it extensible for future instruction set architectures.

RISC-V Vector Processing Optimizations:Alexandre presented a detailed overview of their work on vector processing optimizations for RISC-V architectures. They described the development of a JIT configuration profile system that automatically adjusts vector lengths and register grouping based on hardware traits and primitive descriptors. The team has implemented vector-length agnostic kernels that outperform OpenBLAS and direct translations of Keras kernels on RISC-V, with performance varying based on vector register size and application size. They are currently evaluating their optimizations on three different chips (BananaPi, Allwinner, and Pioneer) and have achieved consistent performance improvements across various convolution operations.

Convolution API Development Update:Alexandre presented on the development of convolution API, noting that while multithreading is pending, they are working on post-operations and group convolutions. He mentioned they are developing other primitives like GEMMs and plan to contribute to upstream work after review. Jianhui asked about the benefits of low-level integration, to which Marc confirmed that while the backend has changed, the API remains unchanged across different architectures. Penporn inquired about how the kernel is integrated with OneDNN, and Alexandre explained they are currently working on GEMMs in isolation before hooking them to the API.

Microkernel Architecture for Vector Kernels:The team discussed the architecture and implementation of microkernels for different vector lengths, with Alexandre explaining that RVV 1.0 probes the architecture to determine available vector implementations and generates kernels accordingly. Denis clarified the relationship between the JIT code, matmul primitives, and the microkernel API, suggesting that implementing the JIT code inside matmul primitives would not work with the microkernel API for RISC-V, while for x86 they use the BRGEMM microkernel API internally. Denis recommended exploring the BRGM opportunity for ARM architecture to enable convolution on smartphones and offered to share code links and documentation with Alexandre, who agreed this approach was the way to go.

aarch64 brgemm kernel: https://github.com/uxlfoundation/oneDNN/blob/main/src/cpu/aarch64/brgemm/jit_brgemm_kernel.cpp
x64 brgemm kernel: https://github.com/uxlfoundation/oneDNN/blob/main/src/cpu/x64/brgemm/jit_brgemm_kernel.cpp
public API documentation: https://uxlfoundation.github.io/oneDNN/dev_guide_ukernel_brgemm.html

RISC-V API Development Updates:The team discussed the automatic enablement of the graph API in RISC-V, which will work once primitive and post-ops attributes are ready. Tao raised a question about validation functionality, to which Alexandre responded that they are using BenchDNN for validating correctness but still need a full-level validation. Penporn suggested a middle ground between full CI/CD and weekly checks, proposing to find a RISC-V server that can be hooked into for results. Alexandre explained their approach to supporting different CPUs, using a template structure that can be adapted for various CPU implementations, with optimization parameters determined by heuristics. 
