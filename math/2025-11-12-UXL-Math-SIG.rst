=========================================
Math Special Interest Group Meeting Notes
=========================================

2025-11-12
==========

Materials:

* `Updates <presentations/UXL-Math-SIG-2025-11-12_SarahKnepper_Update.pdf>`__

Attendees:

* Andrey Alekseenko (KTH Royal Institute of Technology)
* Hartwig Anzt (UTK)
* Abhishek Bagusetty (ANL)
* Colleen Bertoni (ANL)
* Gajanan Choudhary (Intel)
* Nick Dingle (Arm Ltd)
* Aniket Garade (CDAC)
* S.J. Golzar (UNISA)
* Sarah Knepper (Intel)
* Nicolas Offermans (Intel)
* Kuldeep Pal (CDAC)
* Alison Richards (Intel)
* Deepika H V (CDAC)

Agenda:

* Opens
* Harnessing Arm Scalable Vector Extension (SVE) for Accelerated OpenBLAS and NumPy Performance – Aniket Garade and Kuldeep Pal (CDAC)
* Updates from last meeting - Sarah Knepper

Harnessing ARM Scalable Vector Extension (SVE) for Accelerated OpenBLAS and NumPy Performance - Aniket Garade and Kuldeep Pal (C-DAC):

Overview:

The presenters demonstrated their work on optimizing mathematical libraries using ARM Scalable Vector Extension (SVE) to improve performance of OpenBLAS and NumPy operations.

Motivation and Background:

* **Mathematical Library Optimization:**
  Mathematical libraries are essential for high-performance computing, providing routines like BLAS and LAPACK for core numerical operations. Effective optimization of these libraries is critical to fully leverage hardware potential and maximize performance.

* **SIMD Vectorization:**
  Single Instruction Multiple Data (SIMD) vectorization enables computing multiple data points simultaneously in a single instruction, reducing instruction count and improving throughput.

ARM Vectorization Technologies:

**NEON**
    * Fixed 128-bit SIMD for parallel data processing
    * Supports 8, 16, 32, and 64-bit integers and 32- and 64-bit floating-point numbers
    * Intended for audio/video encoding and decoding, 3D graphics, and signal processing

**Scalable Vector Extension (SVE)**
    * Offers scalable SIMD with configurable vector lengths
    * Supports 8, 16, 32, and 64-bit integers and 32- and 64-bit floating-point numbers
    * Primarily developed for HPC and AI applications

SVE Key Features:

1. **Scalable Vector Length**
    * Vector registers range from 128-bit to 2048-bit in 128-bit increments
    * Same code runs on different SVE implementations without modification
    * Longer vector sizes provide maximum parallelism

2. **Pre-Lane Predication**
    * Indicates which elements in current operations are active/inactive
    * Controlled by setting predicate registers
    * Enables selective element processing within vectors

3. **Gather Load and Scatter Store**
    * Gather load: Load data from non-contiguous memory locations into vector registers using index vectors
    * Scatter store: Store data from vector registers back to non-contiguous memory locations

4. **Horizontal Reduction**
    * Reduces elements of a long vector register into single values or intermediate results
    * Enables efficient aggregation operations

5. **Multi-Core Support**
    * Supports various data types
    * Leverages multi-core systems for high-performance parallelism

SVE Architecture Fundamentals:

**Registers**
    * 32 scalable vector registers (Z0-Z31)
    * 16 scalable predicate registers (P0-P15)
    * 1 fault predicate register (tracks faults during memory access)
    * 1 scalable vector system control register (stores maximum supported vector length)

**Key SVE Instructions**
    * Load/Store: ``SVLD``, ``SVST``
    * Arithmetic: ``SVADD``, ``SVSUB``, ``SVMUL``
    * Reduction: ``SVADDV``
    * Duplication: ``SVDUP``
    * Vector Length Management: ``SVCNTW``, ``SVCNTD``

OpenBLAS Optimization:

**Implementation Approach**
    * Directory Structure: Optimizations implemented in ``kernel/arm/sve`` directory within OpenBLAS source code. New SVE-optimized files must be registered in the ``armv8-sve`` kernel file for inclusion in the build process.

**Algorithm Steps**
    1. Initialization: Set up parameters (number of elements, scalar values, rows/columns, accumulators)
    2. Vector Width Determination: Use ``SVCNTW``/``SVCNTD`` to determine vector capacity
    3. Predicate Generation: Use ``SVWHILELT`` intrinsics to generate predicates indicating active elements
    4. Data Loading: Use ``SVLD`` to load data into SVE vector registers
    5. Operations: Implement matrix-vector multiplication, vector swapping, vector scaling, and vector rotation
    6. Result Storage: Use ``SVST`` to write results back to memory

**Experimental Setup**
    * Hardware: Two A64FX processor variants (Perlmutter and Fugaku)
    * Vector Length: 512-bit SVE
    * Memory: 32GB HBM2
    * Compiler: GCC 12.2

**Performance Results**
    * GEMV (Matrix-Vector Multiplication):
        - SGEMV: 12.73x on Perlmutter, 8.54x on Fugaku (large datasets)
        - DGEMV: 10.27x and 7.5x (smaller sizes), 4.80x and 10.88x (larger sizes)
    * SWAP (Vector Swapping):
        - SSWAP: 2.20x on Perlmutter, 2.43x on Fugaku
        - DSWAP: 2.60x on Perlmutter, 3x on Fugaku
    * SCAL (Vector Scaling):
        - SSCAL: 2.10x on both systems
        - DSCAL: 2.17x on Perlmutter, 2.41x on Fugaku
    * ROT (Vector Rotation):
        - SROT: 1.83x to 2.03x
        - DROT: 3.50x to 3.96x

NumPy Optimization:

**Initial Motivation**
    Fashion MNIST model achieved 25x speedup using SVE-optimized OpenBLAS backend on ARM architecture, demonstrating SVE potential for AI workloads.

**Integration Approach**
    * Directory Structure: SVE integration performed in NumPy core directories:
        - ``multi-array``: Array operations
        - ``umath``: Universal mathematical functions
        - ``common``: CPU-based functions
        - ``_pymath``: Mathematical helper functions
        - ``_simd``: SIMD vectorization logic (primary integration point)

**Five-Stage Integration Workflow**
    1. User Interaction and Dispatch Initiation
    2. Dispatch Selection and CPU Feature Detection
    3. Data Types and Python C API Layer
    4. SIMD Abstraction (NPYV API)
    5. SVE Kernels and Memory Handling

**Experimental Setup**
    * Hardware: Perlmutter ARM cluster
    * Clock Speed: 1.8 GHz
    * Cores: 48
    * SVE: 512-bit
    * Memory: 32GB HBM2
    * Compiler: GCC 12.2
    * NumPy Version: 2.0.0 (modified with SVE integration)

**Performance Results**
    * Basic Arithmetic Operations: Up to 1,300x speedup for large arrays
    * Dot Products: Up to 150x speedup
    * GEMM Operations: 14x to 44x improvement
    * Memory Bandwidth: Up to 20x improvement

Summary of Performance Improvements:

* OpenBLAS:
    - Level 2 BLAS: 7x to 13x speedup
    - Level 1 BLAS: 1.8x to 4x speedup
* NumPy:
    - Element-wise operations: Up to 1,300x
    - Vector dot products: Up to 150x
    - GEMM operations: 14x to 44x
    - Memory bandwidth: Up to 20x improvement

Q&A Session:

* **Higher Precision Emulation:**
  Could the SVE strategy emulate higher precisions (e.g., emulating double precision using two float values to achieve double mantissa length without full double range)?

  SVE implements its own data types (e.g., ``svfloat``, ``svdouble``) for handling different precision requirements.

* **Upstreaming to NumPy:**
  Not yet upstreamed, but planned for the future.

* **OpenBLAS Integration Status:**
  Some routines have been upstreamed to OpenBLAS version 0.3.29.

oneMath Project Updates:

* **Version 0.9 Release**
    - ARM Performance Library Backend added for DFT domain
    - Numerous testing and improvements across the library

* **Recently Approved RFCs**
    - OpenBLAS Backend Support: RFC proposing addition of OpenBLAS backend support to oneMath. This integration would enable users to benefit from SVE improvements on ARM through a pure open-source solution.
    - Backend Maintainer Roles: RFC merged since last meeting, establishing backend maintainer roles. This supports UXL Foundation's guiding principle of increasing community involvement and leadership. Members interested in maintainer roles for backends or domains should contact Sarah Knepper.

* oneMath specification remains stable with only minor typo fixes in vector math functions since the last meeting.

Announcements:

UXL Foundation representatives will attend Supercomputing conference:
    * Steve Hikida (Intel)
    * James Brodman (Intel)
    * Penporn Koanantakool (Google Cloud)
