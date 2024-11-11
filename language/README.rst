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

2024-11-05 SPIR-V extensions used by DPC++
============================================

`Slides <presentations/2024-11-05-spirv-extensions.pdf>`

`Tracking spreadsheet <https://docs.google.com/spreadsheets/d/1pgPno--m-MiQIjN1kKkgzi1KEr4o_0cF/edit?gid=1151130440#gid=1151130440`

`Recording <https://zoom.us/rec/share/hfZJJBRwrACUxfZH8iu4EFfRBehce7GtaWrXPsXlnD36KSh4RqFQuYQgmJvC1qG6.EQB4yIBUdigvbtAZ>`


* Andrey Alekseenko (KTH Royal Institute of Technology) - KTH Royal Institute of 
  Technology
* Juan Fumero (The University of Manchester) - The University of Manchester
* Alison Richards (Intel Corporation) - Intel Corporation
* Victor Lomuller - Codeplay Software
* mahesh budavarapu (Radisys Corporation) - Radisys Corporation
* Rod Burns (Codeplay Software) - Codeplay Software
* Gordon Brown - Codeplay Software
* Alex Pim - Imagination
* Vasudha Badri-Paul - Intel
* Mehdi Goli - Codeplay Software
* Alexey Kukanov (Intel) - Intel Corporation
* Victor Lu - 
* Gergana Slavova - Intel
* Melissa Aranzamendez - The Linux Foundation
* David Edelsohn (International Business Machines Corporation) - IBM
* Ronan Keryell - AMD
* Max Aigner - Akhetonics
* Brice Videau - Argonne

* RR: First discuss charter document, driven by Michael Wong.
* RR: Michael Wong is no longer in Codeplay, we wish him the best on his next 
  steps
* RR: Any interest on continuing the document live, otherwise we can continue 
  offline
* (No comments from attendees)
* RR: Rod I know you have comments on the document, lets look at those offline
* RR: Everyone else we can continue on the document or on slack
* RR: For today lets discuss the presentation from Victor Lomuller (Codeplay 
  Software)
* RR: Victor is a Principal SE in Codeplay and co-editor of the SPIR-V 
  specifications
* RR: He has many years of experience working with me on the SYCL compiler and 
  standard
* RR: Today he will be talking about extensions that the DPC++ SYCL 
  implementation uses
* RR: which ones are needed and which ones are not.

* (VL goes through presentation)

* VL: Describes a SPIR-V module for vector addition
* RR: Is that the default SPIR-V output from the compiler, no custom flags or 
  additions?
* VL: Correct that is the default option.

* (VL presentation continues)

* VL: Currently there is two ways of generating the SPIR-V module, the 
  translator and the compiler backend.
* VL: The translator is more complete and has the extensions, the backend is 
  getting there
* RR: Question, does the backend support the extensions we are discussing 
  today?
* VL: Not yet, they are working on adding those

* (VL presentation continues)

* RR: Are you saying that SYCL 2020 requires Opencl 2.0, or you mean DPC++ 
  requires OpenCL 2.0
* VL: Mainly DPC++. You could get away of not having generic if you implement 
* VL: inferred address space, for instance. But as far as I know, there's no no 
  compiler that do this anymore.
* Ronan Keryell (AMD)
* Ronan Keryell (AMD) Yeah, it's more probably the implementation, because the 
  standard itself doesn't say anything about opencl. No.

* (VL presentation continues)

* JF: I have a question about fast math mode. Does DPC++ enables fast math mode 
  or is it C++?
* VL: CUDA uses contract fast by default, we use fast math
* RR: is that the SYCL behaviour or the DPC++?
* VL: The C++ compiler sets this default

* (VL Presentation continues, goes over SYCL extensions and SPIR-V 
  requirements)

* JF: I see bfloat16 extension, any plans for fp8 or fp4?
* VL: We can't comment on that from Intel perspective, there is some work being 
  done.
* JF: Oh so bfloat16 is a SYCL extension, not C++
* VL: Yes, only covers conversion.

* (VL shows the table of SPIR-V extensions on the spreadsheet)

* Andrey Alekseenko: Thanks for the presentation, is this list of extensions 
  for public distribution?
* AA: I'd like to share this with other people, e.g. POCL or MESA
* VL: Yes its on the google drive of the Foundation you can share the link
* Alison Richards: The links are public and everything is accessible in the 
  github
* RR: Yes everything will be public but please do encourage people to join the 
  UXL foundation if they are interested in this topic
* AA: The two people I know want to run SYCL on their OpenCL implementation, 
  using DPC++

* RR: Any other questions or comments there?
* AR: I mean, I just wanted to make sure everyone knew that in the chat I pop 
  something in. If you're going to sc. 24, we're having a uxl foundation meetup 
  on Monday, and you can register. So I pop that into the chat.

* RR: Thanks Alison thats really cool. We have 15 min or so, if there are no 
  other topics maybe we can cover the native CPU?
* (No comments or questions)

* RR: Victor please go ahead
* VL: yes the other thing I have is the Native CPU path which does not use 
  SPIR-V and its for CPU targets

* (VL proceeds through slides)

* VL: Device compiler directly vectorizes to the ISA and lunch from SYCL RT, no 
  OpenCL involved.
* RK: How is it exposed to the end user? Is it a specific platform and device.
* VL: Yes you have a platform and a specific device
* JF: So this Native CPU is going to be integrated into the DPC++ compiler?
* VL: Yes, it is already integrated onto the compiler and then you have a 
  Unified Runtime adapter
* JF: So the idea is you don't need an OpenCL installation
* RR: Correct, yes
* JF: So uses pthread or whatever, but runs legal SYCL code

* MA: Okay. I mean, for example, we are currently working on a CPU that is kind 
  of custom-made.
* MA: We have our own kind of Assembly language and everything. But that would 
  be level 0 adapter then, right?
* MA: So because we want any other codes to be running on our CPU, not just the 
  assembly being cramped into the DPC++ code directly.
* MA: And yeah, there'll be level 0 then, right?
* RR: So the native CPU adapter still compiles normal SYCL code.
* MA: Okay.
* RR: Instead of going through an offload API like level 0 and OpenCL, it 
  executes directly on the host.
* RR: So if you are targeting a CPU, you can avoid external dependencies and 
  going through SPIR-V.
* MA: Okay.
* RR: For example, we use this for testing on x86 CPUs, or to just run things 
  on ARM CPUs, or RISC-V CPU simulators.
* RR: And we just use that because we don't need to offload to a device.
* RR: But if your device goes through some sort of bridge, like a PCI Express 
  bus or something, then you need some kind of offload API,
* RR: and that's where you use OpenCL or level 0, or whatever API you have.
* MA: Okay.
* RR: Does that answer your question?
* MA: So I didn't really understand properly. I'm kind of new in this field. 
  Basically, so it means native CPU adapter means it can only run on this CPU,
* MA: or does it? So it's creating the assembly code for this specific CPU 
  directly, right?
* MA: That's, I don't need an adapter. Okay, that's then understood.
* MA: And what we try to do is we don't want to have it specifically for that 
  CPU. Maybe you could use it for testing.
* MA: But we want to use the SPIR-V code because we have a SPIR-V compiler that 
  translates
* MA: from SPIR-V to our own assembly language. So then, we need level 0 
  adapter, because we need the SPIR-V from there, I guess.
* VL: OpenCL or level 0. Yeah, yeah, I mean.
* MA: Say that we have to support the SPIR-V libraries, right? That we have 
  talked about in the beginning, right?
* MA: Which we might not be able to do
* VL: Yeah, OpenCL and Level 0 have the same SPIR-V requirements
* JF: With Native CPU you can run SPIR-V as well?
* RR: No, Native CPU is a different path, it doesn't use SPIR-V, we lower to 
  the native CPU ISA directly
* Yeah, we don't have the adapter. We need an adapter for translating Spearv to 
  the native CPU assembly, and then it's not native anymore. Then it's level 0 
  or open sale.
* VL: I think they're trying to enable some support for this, though. But yeah,
* JF: Confusing. I'm not sure which part of the product which part of the.
* VL: So yeah, for SPIR-V, and all the the extensions presented so far is this 
  is here, and then the
* VL: you will have the same binary consumed by opencl and the level 0 adapter. 
  Yeah, each of them has their own.
* VL: you know. Environments pack, you know, that dictates exactly what you 
  must support, etc. But
* VL: they are basically the same.
* MA: We have one problem there, I mean, we have. We don't go through the I 
  think we don't go through the
* MA: oneAPI Unified RUntime I think because we don't use llvm. So we directly 
  get to form a SPIR-V.
* MA: Part and parse that with our own parser, the SPIR-V assembly.
* VL: and then use that. But then we also have to support the libraries.
* VL: I guess the extensions that you were talking at the beginning. Do we have 
  to do this manually, then?
* VL: Manually. So it's basically the Spv extensions is just going to add new 
  extractions or modify the semantic of some part of the speedy spec right.
* MA: Yeah. So it means that our SPIR-V parser needs to be modified to 
  understand the extensions as well.
* MA: Okay? And this, this is mandatory for oneAPI. I guess.
* RR: Level0 or anything that comes out from the DPC++ compiler
* RR: We've been using the same extensions for Spv.
* MA: Okay? And the list of the extensions was listed in the beginning, right?
* MA: It's probably 20 extensions or something like that, like that.
* RR: We'll share the slide so you can take a look.
* MA: Okay, thank you. Thank you. Sorry. I'm a beginner. Sorry. But thank you.
* RK: I think this native CPU adapter is interesting for
* RK: embedded system, where, when you have also a lot of CPU cores, and you
* RK: and you want to run some specific SYCL code without having to implement a 
  full OpenCL stack,
* RK: for example, or something like that. Yeah, yeah.
* RR: That is one of the reasons we started the project a while ago.
* RR: Yeah, to have like, a very compact SYCL implementation. Yeah.
* RR: any other comments or questions.
* RR: Okay, thank you. Everyone for joining today.
* RR: If you have any suggestions on topics for the next meeting, or feel free 
  to drop
* RR those on the mailing list or on the slack.
* RR: We'll post the minutes on the slides and the links as soon as we can 
  gather them together and put that.
* RR: Thank you, everyone. Take care.

* (Meeting ends)

2024-02-06 Numba-dpex
=====================

`Slides <presentations/2024-02-06-numba.pdf>`__

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

