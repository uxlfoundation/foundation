============================================
Get Started with the UXL Foundation Projects
============================================

The UXL Foundation governs the `oneAPI Specification`_ and this defines APIs for a range of areas, from math through to AI. You can view the `oneAPI specification`_ and propose changes to it through the `oneAPI spec GitHub repository`_. Members of the UXL Foundation can join the Working Group meetings to discuss and make proposals to extend the specification.

The UXL Foundation governs a set of open source projects that implement the oneAPI Specification and these projects provide many of the building blocks needed for developers to write highly parallel software on a range of processors from CPUs to GPUs and beyond. Parts of the projects are dependent on the SYCL programming model, an open standard defined by the Khronos Group. SYCL is used to implement code that is accelerated across vendors and architectures, in particular on GPUs.

`oneCCL`_
=========

Communication primitives for scaling deep learning frameworks across multiple devices. oneAPI Collective Communications Library provides an efficient implementation of communication patterns used in deep learning and makes it possible to scale some workloads across multiple nodes, something that is commonly done in HPC development where a computing cluster might make many nodes with many GPUs available.

`oneCCL Documentation`_

`oneDAL`_
=========

Algorithms for accelerated data science. oneAPI Data Analytics Library is a powerful machine learning library that helps you accelerate big data analysis at all stages: preprocessing, transformation, analysis, modeling, validation, and decision making.

`oneDAL Documentation`_

`oneDNN`_
=========

High performance implementations of primitives for deep learning frameworks. oneAPI Deep Neural Network Library is an open-source cross-platform performance library of basic building blocks for deep learning applications. oneDNN is intended for deep learning applications and framework developers interested in improving application performance on CPUs and GPUs. 

`oneDNN Documentation`_

`oneDPL`_
=========

A companion to the DPC++ Compiler for programming oneAPI devices with APIs from C++ standard library, Parallel STL, and extensions. The oneAPI DPC++ Library is a companion to the DPC++ Compiler and provides an alternative for C++ developers who create heterogeneous applications and solutions. Its APIs are based on familiar standards — C++ STL, Parallel STL (PSTL), Boost.Compute, and SYCL to maximize productivity and performance across CPUs, GPUs, and FPGAs.

`oneDPL Documentation`_

`oneMath`_
=========

High performance math routines for science, engineering, and financial applications. one Math Library implements optimized parallel implementations for BLAS, LAPACK, DFT, RNG and SPARSE math domains.

`oneMath Documentation`_

`oneTBB`_
=========

Library for adding thread-based parallelism to complex applications on multiprocessors. oneAPI Thread Building Blocks is a flexible C++ library that simplifies the work of adding parallelism to complex applications on CPUs, even if you are not a threading expert. 

`oneTBB Documentation`_

`oneAPI Construction Kit`_
==========================

The oneAPI Construction Kit can be used to bring SYCL and oneAPI to new and specialist accelerators. The oneAPI Construction Kit works by enabling the CPU to offload compute-intensive kernels to the custom accelerator. The project includes a reference implementation using RISC-V. 

`oneAPI Construction Kit Documentation`_

.. _`oneAPI spec GitHub repository`: https://github.com/uxlfoundation/oneAPI-spec
.. _`oneAPI specification`: https://oneapi-spec.uxlfoundation.org/
.. _`oneCCL`: https://github.com/uxlfoundation/oneCCL
.. _`oneCCL Documentation`: https://uxlfoundation.github.io/oneCCL
.. _`oneDAL`: https://github.com/uxlfoundation/oneDAL
.. _`oneDAL Documentation`: https://uxlfoundation.github.io/oneDAL
.. _`oneDNN`: https://github.com/oneapi-src/oneDNN
.. _`oneDNN Documentation`: https://oneapi-src.github.io/oneDNN/
.. _`oneDPL`: https://github.com/uxlfoundation/oneDPL
.. _`oneDPL Documentation`: https://oneapi-src.github.io/oneDPL/
.. _`oneMath`: https://github.com/uxlfoundation/oneMath/
.. _`oneMath Documentation`: https://uxlfoundation.github.io/oneMath/
.. _`oneTBB`: https://uxlfoundation.github.io/oneTBB
.. _`oneTBB Documentation`: https://uxlfoundation.github.io/oneTBB
.. _`oneAPI Construction Kit`: https://github.com/uxlfoundation/oneapi-construction-kit
.. _`oneAPI Construction Kit Documentation`: https://github.com/uxlfoundation/oneapi-construction-kit/blob/main/doc/developer-guide.md
