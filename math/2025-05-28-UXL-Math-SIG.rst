=========================================
Math Special Interest Group Meeting Notes
=========================================

2025-05-28
==========

Materials:

* `Arm CI <presentations/tbd.pdf>`__
* `MLKAPS Presentation <presentations/TBD.pdf>`__

Attendees:

* Sarah Knepper (Intel Corporation)
* Eric Petit (Intel)
* Maria Kraynyuk (Intel Corporation)
* Augustin Degomme (SiPearl)
* Ragesh Hajela (Fujitsu Limited)
* Deepika H V (Centre for Development of Advanced Computing)
* Rafal Bielski (Codeplay Software)
* Colleen Bertoni (Argonne National Lab)
* Rod Burns (Codeplay Software)
* Nick Dingle (Arm Ltd)
* John Melonakos (Intel Corporation)
* Abhishek Bagusetty (Argonne National Lab)
* Ed Tuke (Imagination)


Agenda
------

* USM Pointers and SYCL Buffers Implementation Challenge - Maria Kraynyuk (Intel Corporation)
* Arm CI integration for oneMath - Rafal Bielski (Codeplay Software)
* ML Driven Auto tuning with MLKAPS - Eric Petit (Intel Corporation)

Topics from attendees
---------------------

* Deepika and Ragesh discussed plans to add openBLAS as a backend to oneMath

  * Augustin suggested it would not be difficult due to the similarity with the netlib and ArmPL libraries
  * Offline discussion will continue about this work

USM Pointers and SYCL Buffers Implementation Challenge
------------------------------------------------------

Presenter: Maria Kraynyuk

* Intel's oneMKL implementation requires maintaining separate implementations for the Unified Shared Memory (USM) and Buffers SYCL features for memory management
* Intel is considering using extensions in SYCL and Level Zero to combine implementations and use interoperability between USM and Buffers
* OpenCL lacks unified memory support, limiting common solutions for OpenCL backends
* There have been discussions with the SYCL Working Group about buffer-Unified Shared Memory interoperability
* More discussion can be had on the Slack thread, Intel are seeking feedback from the community

Continous Integration Updates for Arm CPU Support
-------------------------------------------------

Presenter: Rafal Bielski 

* Rafal talked about how CI support has been added for ARM CPU testing in oneMath project
* Split existing PR testing into three configurations: linting, x86 CPU testing, and ARM CPU testing
* Set up 7-day caching for DPC++ Arm CPU builds (takes ~1 hour to build, subsequent runs use cache)
* Using public GitHub ARM runner (currently in Beta)
* No binary releases available for DPC++ on ARM CPU hosts, requiring source builds
* ARM Performance Libraries (ARMPL) installed as part of pipeline
* Netlib used as reference for correctness checking in BLAS backend

Future Improvements:

* Need ARM CPU DPC++ release binaries to avoid CI builds
* Dedicated runners for CPU testing would provide better environment control

ML Driven Auto Tuning with MLKAPS
---------------------------------

Presenter: Eric Petit

Eric presented MLKAPS, a machine learning framework for kernel accuracy and performance tuning, focusing on auto-tuning of math library functions.

Updates
-------

The UXL Foundation is hosting events at the Open Source Summit in Denver and ISC during June, please participate in these if you are attending
