===========================
UXL Foundation Language SIG
===========================

The Language SIG hosts discussions and presentations focused on
how to integrate a broad range of languages to support oneAPI.
The languages at the heart of oneAPI are C++ and SYCL. This
group discusses how work done within the oneAPI open source
implementations can contribute to the ISO C++ and SYCL
specifications managed by ISO and Khronos respectively.

The SIG does not discuss the design of SYCL APIs, just general feedback.

The language SIG is led by Ruyman Reyes Castro <ruyman@codeplay.com>

Archived meeting notes from meetings held under the oneAPI 
Community Forum can be found `here`_

.. _here: https://github.com/oneapi-src/oneAPI-tab/tree/main/language

2024-02-06 Numba-dpex
=====================

`Slides <presentation/2024-02-06-numba.pdf>`

Attendees:

* Diptorub Deb (Intel)
* Gergana Slavova (Intel)
* Alexey Kukanov (Intel)
* Alison Richards (Intel)
* Andrew Richards (Codeplay)
* Danial Chitnis
* Daniel Keller
* Igor
* Ivan Butygin (Intel)
* Khaled Talucker
* Mehdi Goli (Intel)
* Oleksandr Pavlyk
* Robert Cohn (Intel)
* Rod Burns (Codeplay)
* Sergey Maydanov
* Victor Lomuller (Intel)

Notes:

* Presentation on Intel extensions for Numba to support accelerators (xPU)
* Includes extensions to support algorithms executing on the GPU 
* Also a direct kernel programing model (akin to SYCL on python)
* Enables python-array interface to accelerate device
* DPCTL is a set of bindingsa to expose SYCL interfaces to python
* Only minimal subset
* Python developers dont want to use the cython interfaces they are difficult
* Python developers want to write python code
* You can list platforms and select devices
* Supports dpctl backend (but using custom build)
Q: How is the memory allocation happening? is it per call?
A: Memory is allocated (using USM) on the convert functions. Explicit copies.
* numba-dpex is a JIT compiler for a SYCL-like kernel programming API
* extends the existing structure
* Performance-wise, still numpy-dpex is not on par with dpcpp
* Everything is Open source, and works on all Intel GPUs
* Expected a Production grade kernel API on upcoming releases
* Available on conda and pip, easily to use for python community
Q: Any support for multiple gpus?
A: No, exploring how that would work
Q: Do we have performance comparisons for NVIDIA platforms?
A: Numba.cuda exists but no SYCL on cuda support out of the box
* No comparisons so far between the two backends

2023-11-07 SYCL-Graphs
=======================

`Slides <presentation/2023-09-19-EC-sycl-graph.pdf>`
`Demo video <presentation/2023-09-19-EC-sycl-graph-demo.mp4>`


* SYCL Graph extension has been ongoing for a year
* Started as two separate implementations from Codeplay and Intel
* Merged onto one after intense collaboration
* Link to document and status
* There is a new command graph object that can be on two states
* The state goes from modifable to complete
* Presents a Saxpy example init and compute nodes
* you can record and reply a queue as they execute
* you can also use an explicit API
* Presented in IWOCL
* Since then evolving, discovered an issue with buffer lifetime
* New property that forces uses to accept buffer - not ideal
* Extend buffer lifetimes (not implemented)
* Need to take a copy of the host buffer to ensure is not lost
* Working on implementation and feedback
* Implementation status, shows overall graph architecture
* There is a command buffer extension API to Unified Runtime
* Loosely based on OpenCL extension
* Implemented to CUDA and Level Zero backends
* CUDA merged November 2023 on intel/llvm repo
* OpenCL backend in progress
* HIP implementation has not started
* Describes implementation details
* Some features are not supported, e.g. host task
* It is complicated to figure out how extensions interact with each other
* Potentially any extension can be used
* In practise only enqueue barrier is supported
* oneDNN demo based on 3.3 release with a modified example of a cnn
* Shows recorded demo with minimal modification
* Runs on level zero
* Future work: Still work to complete the current speciciation
* Profiling is still missing, needs more work
* As more users stress the implementation there will be bugs and corner cases
* CUDA-Graph differences: transitive stream/queue capture
* Update arguments to graph nodes: modify an argument without re-creating
* Not supported on LZ
* Graph owned memory allocation
* Device Model: Can we have a graph object with multiple devices?
* Can this work across backends even? 
* Currently submission is driven by queues, associated to single device
* Opposite direction: Create a graph without a device
* SYCL-specific features: buffer lifetimes, scheduling, multiple graph
* Graph fusion which combines the SYCL Kernel fusion proposal
* Still implementation pending

QA: transitive stream, 
when we record it has not happened - 

QA: Graph memory allocation


RonanK:  Buffer lifetime - there is some UB on the buffer, 
collaboration opportunity. Discuss with Greg Lueck

RonanK: Start and End recording is very stateful and does
not fully represent the spirit of C++
On SYCL SC we have proposals using tokens for that
Recording token when the token is destructed then you stop recording
If you have an exception is not safe when using being/end recording
so is not very C++ safe.
EC: Will link internally this was discussed before but we may have to
repeat
Pablo: We are actively working on the interface with customers and
we are always open to have more feedback.


2023-09-19
=============

* Ruyman Reyes (Intel/Codeplay)
* Lukas Sommer (Codeplay Software Ltd)
* Benie (Codeplay Software Ltd)
* Hyesun Hong (Samsung SAIT)
* Julian Oppermann (Codeplay Software Ltd)
* Mehdi Goli (Codeplay Software Ltd)
* Lueck, Gregory (Intel)
* Jesus Labarta (BSC) (Guest)
* Brodman, James (Intel)
* Hanwoong Jung (Samsung SAIT)
* Brice Goglin (Invité)
* Plaska, Oskar (Contractor, Cognizant)
* Tom Deakin (Univ. of Bristol)
* Marcin (N/A)
* Victor Lomuller (Codeplay Software Ltd)
* Biagio COSENZA (Università degli Studi di Salerno)
* Voss, Michael J (Intel)
* Kukanov, Alexey (Intel)
* Richards, Alison L (Intel)
* Adam Kuźniar (Mobica)
* Slavova, Gergana S (Intel)
* bongjun kim (Samsung SAIT)
* Keryell, Ronan (XILINX LABS)
* Juan Fumero (University of Manchester)
* Gordon Brown (Codeplay Software Ltd)
* Tim (N/A)
* Kinsner, Michael (Intel)
* Petersen, Paul (Intel)
* Videau, Brice (ANL)
* Holmes, Daniel John (Intel)
* Frank Brill (Cadence)
* Mrozek, Michal (Intel)
* Reble, Pablo (Intel)
* Andrew Richards (Intel/Codeplay)
* Smith, Timmie (Intel)


SYCL Extension Proposal for PIM/PNM
--------------------------------------

Hyesun Hong,
`Slides <presentation/2023-09-19-HS-sycl-pim-extensions.pdf>`

* PIM/PNM technology enables computation directly on memory
* Prevents data movement improving performance and reducing consumption
* Operates directly on memory banks by reading and storing on rows and columns
* Aquabolt-XL is the first demonstrator
* Can be drop in on any memory controller
* CXL-PNM is the CXL variant for PNM, can work with multiple PIM

SYCL Extension for PIM/PNM
* Work in collaboration with Codeplay Software team
* Goals

  * Seamlessly integrate PIM/PNM operation into SYCL
  * Allow combination of xGPU and PIM/PNM in one device kernel
  * Not specific to one hardware

* Design

  * Vector operation seem like natural fit
  * no convergence guarantee and vector size explicit

* Model as special function unit

  * Aligns with trends to model special functional units inside accelerators
  * Compiler automatic mapping often not possible
  * joint_matrix-like interface


* Group functions

  * Easy to use
  * Can easily be combined with device code
  * Give necessary convergence guarantees


* Recap of SYCL work-item, work-group and group functions

  * Group functions must be encountered in converged control flow

* Extension

  * Extended group functions with additional overload of joint_reduce
  * and new joint_transform and joint_inner_product
  * Block size as template parameter, number of blocks as runtime parameter
  * allows calculation of number of elements to process

* Extension for PNM

  * Added new overloads of joint_exclusive_scan,
  * joint_inclusive_scan, reduce_over_group

* PNM standalone has less opportunity for parallelism

  * limited by memory controller
  * -> Combine PNM and PIM, PNM generates commands for PIM blocks

* Two modes

  * PIM mode: PIM blocks can operate independently, can choose number of blocks
  * PNM mode: Synchronized execution on multiple PIM blocks

* Mapping

  * Every PIM block is one work-item
  * PNM with attached PIM blocks forms one work-group

* Execution

  * Work-item operations map to PIM operation
  * Group functions map to PNM operation

* Example

  * work-item execution maps to PIM
  * group function maps to PNM

* Conclusion

  * Integrate support for PIM/PNM into SYCL

Q&A
* Are the proposed functions specific to PIM, could also be used with other HW?

  * Can also be used with other hardware.
  * Semantics not PIM-specific, but translation of C++ to SYCL
  * Can also map nicely to other types of hardware, e.g. vector processor

* Why have the user explicitly specify a block-size?

  * Not a hardware detail
  * Rather a promise by the user that data-blocks
    will always be at least that big
  * Promise allows device compiler to perform optimizations,
    efficient looping inside PIM unit

* Could num_blocks runtime parameter be replaced by iterator?

  * requires to be divisible by block-size
  * Yes, that is possible, mainly a design question
  * Current version might have additional implications regarding alignment

