=========================================
  AI Special Interest Group Meeting Notes
=========================================

2026-03-05
=========

Attendees

* Penporn Koanantakool (Google LLC)
* Jianhui Li (Intel Corporation)
* Aruna K (Fujitsu Limited)
* Tao abc (Intel Corporation)
* Tuomas Karna (Individual)
* kuldeep pal (Individual)
* Saleh Golzar (University of Salerno)
* Abhishek Jain (Fujitsu Limited)
* Biagio COSENZA (University of Salerno)
* Abhishek Bagusetty (Individual)
* Alison Richards (Intel Corporation)
* Dmitry Zarukin (Intel Corporation)

======
Agenda
======

**oneDNN Updates: Async Threadpool, Grouped GEMM, and MXFP/NVFP**,  
**Dmitry Zarukin**, Intel Corporation, (`slides <presentations/2026-03-05-UXL-AISIG-oneDNN-Status-Update-DmitryZarukin.pdf>`__)

Summary
=======

RISC-V Enablement
-----------------

- Growing community contributions with initial optimized kernels and maintainers onboard  
- Current support focuses on floating-point inference workloads  
- Validation relies on contributor-provided testing (no official CI yet)  


Quantization Enhancements (INT & Low-Precision FP)
--------------------------------------------------

- Expanded support for INT4/INT8 weight compression with flexible scales and zero-points  
- Introduced grouped and 2D quantization schemes to balance accuracy and memory efficiency  
- Added MXFP4/MXFP8/NVFP4 formats with dynamic scaling computed at runtime  
- Quantization parameters handled separately from tensor buffers (no native “quantized tensor” abstraction)  


Async Threadpool Runtime
------------------------

- New asynchronous execution model (inspired by XLA) decouples task submission from execution  
- Improves parallel efficiency by allowing host thread to continue scheduling work  
- Requires significant internal changes (lifetime management, lambda capture semantics, memory safety)  
- Currently supported on x86 backend; other backends require non-trivial adaptation  
- Expected performance improvement ~10% (framework-level gains can be higher)  


Grouped GEMM / Mixture-of-Experts (MoE)
---------------------------------------

- Introduced batched/grouped GEMM to support MoE workloads efficiently  
- Uses new memory descriptors for sparse/condensed activations  
- Enables multiple GEMMs within a single kernel submission  
- Targeted for upcoming oneDNN release (v3.2), with primary focus on GPU backend  


Host-side Scalars
-----------------

- Introduced lightweight scalar handling without device memory allocation  
- Reduces overhead for small models and scalar-heavy operations (e.g., scales, zero-points)  
- Integrated into selected primitives (e.g., SDPA, dropout)  


Discussion Highlights
=====================

- RISC-V ecosystem maturity and lack of standardized CI/testing  
- Trade-offs in quantization accuracy vs. performance and memory  
- Async runtime benefits vs. complexity for non-x86 backends  
- API usability concerns (e.g., backend detection for async runtime support)  
- Interest in performance data for new FP formats and async execution  


Action Items / Follow-ups
=========================

- Track RISC-V CI and broader ecosystem validation  
- Evaluate async threadpool integration across non-x86 backends  
- Monitor MXFP/NVFP adoption and performance data  
- Follow up on grouped GEMM / MoE integration in frameworks  
- Potential deep-dive session on async runtime internals  