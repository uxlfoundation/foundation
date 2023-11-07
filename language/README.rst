===========================
UXL Foundation Language SIG
===========================

The Language SIG hosts discussions and presentations focused on
how to integrate a broad range of languages to support oneAPI.
The languages at the heart of oneAPI are C++ and SYCL. This
group discusses how work done within the oneAPI open source
implementations can contribute to the ISO C++ and SYCL
specifications managed by ISO and Khronos.

The language SIG is led by Ruyman Reyes Castro <ruyman@codeplay.com>

Archived meeting notes from meetings held under the oneAPI 
Community Forum can be found `here`_

.. _here: https://github.com/oneapi-src/oneAPI-tab/tree/main/language

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

