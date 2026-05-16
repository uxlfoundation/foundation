===========================
UXL Foundation Hardware SIG
===========================

The Hardware SIG hosts discussions and presentations focused on
how to enable a broad range of hardware architectures.

The Hardware SIG is led by `Jeremy Bennett
<mailto:jeremy.bennett@embecosm.com>`__ (`Embecosm <https://www.embecosm.com>`__).

Archived meeting notes from meetings held under the oneAPI 
Community Forum can be found `here`_

.. _here: https://github.com/oneapi-src/oneAPI-tab/tree/main/hardware

2025-05-08 Scaling Workloads with a Memory Lake
===============================================

Agenda:

* Introduction.  Alastair Murray, Codeplay Software. `[Slides] <presentations/2025-05-08_AlastairMurray_SIG_Intro.pdf>`__
* Scaling Workloads with a Memory Lake.  Dr. Skyler Windh, Micron Scalable Memory Systems Pathfinding. `[Slides] <presentations/2025-05-08_SkylerWindh_Memory_Lakes.pdf>`__

2025-02-20 Embecosm and University of Southampton Porting to AI Hardware
========================================================================

Agenda:

* Introduction.  Alastair Murray, Codeplay Software. `[Slides] <presentations/2025-02-20_AlastairMurray_SIG_Intro.pdf>`__
* Porting AI to New Hardware: A Case Study. Jeremy Bennett and William Jones, Embecosm. `[Slides] <presentations/2025-02-20_BennettJones_Porting_AI_to_New_Hardware_Case_Study.pdf>`__
* Hardware acceleration for PyTorch – a demonstrator.  James Betson and Lorinc Boer.  University of Southampton, with Embecosm. `[Slides] <presentations/2025-02-20_BetsonBoer_Hardware_Acceleration_for_PyTorch.pdf>`__

2024-06-03 Imagination Technologies Enabling Compute Hardware
=============================================================

`[Meeting Recording] <https://zoom.us/rec/play/uMI5QwzoNrBcPNw5RK_5LFnY1Lf7jbR2KYT47HjDNhkdhBaEJmuTPSJKv64NR4H9V54t0EedJHkxL8CW.NrCOkb0QFM4_Q3yi?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FOKtcRsrHLiyWT2jmrtHenIxC12gLAdHeh0401RgrpUdfV38KtM8T352X6jQiAHxV.bBEV-mBEqWE5AxAt>`__

Alex Pim from Imagination Technologies presented their view on the customer's journey through compute, and how they are designing their hardware with a software first approach.

Imagination’s view of the customer’s journey through compute - `[slides] <presentations/Imagination_Technologies_Enabling_Compute_Hardware.pdf>`__.
 
HW Accel using oneAPI slide: Direct support of SYCL on OpenCL vs oneAPI on OpenCL.
A: 
 
Q Colin: Reaction from customers so far?
A: Positive, like being able to use existing code for algorithms rather than porting, want to understand how this fits into what their currently doing and are investigating SYCL.
 
Q: Looked at anything other than OpenCL for implementing SYCL?
A: Already had mature OpenCL driver which made that attractive, looking at what to use in the future but no conclusion.
 
Q: Why continue looking at other options?
A: In Imagination Technology office, part of brief is to look at upcoming technologies, never assume that today’s tech will still be tomorrow’s tech.
A: What speed is OpenCL moving in relation to AI, is it moving in the right direction.
A: OpenCL works, no issue.
 
Q Ronan: Do you have a modern LLVM for your GPU? Often problem supporting UXL is technical debt in LLVM backend.
A: Have LLVM, has enabled us to move quickly and get tests working etc.
 
Q Ronan: Support USM extension in OpenCL?
A: Yes, have initial support for that.  Had SVM support so adapted that.  Initial block for using SYCLomatic was it used USM a lot.
 
Q Colin: What extensions do you support?  It feels like it’s not well documented.
A: Initially the only thing that didn’t work was USM, could execute simple SYCL immediately.
A: Sometimes an error will pop up when building something saying some extension isn’t supported.
 
Q Ben: Do you support USM today?  Did you implement the Intel USM extension?
A: I have access to an internal beta version, not in public support yet.

Attendees:

* Alastair Murray (Codeplay)
* Alex Pim (Imagination Technologies)
* Atharva Dubey (Codeplay)
* Ben Ashbaugh (Intel)
* Brice Goglin (Inria)
* Brice Videau (Argonne)
* ChungFan Yang (Fixstars)
* Colin Davidson (Codeplay)
* David Edelsohn (IBM)
* Erik Tomusk (Codeplay)
* Giovanni Grandi (Codasip)
* Gordon Brown (Codeplay)
* Ivan Litov
* Jose Fonseca (VMWare/Broadcom)
* Kasper Mecklenburg (Arm)
* Neil Spruit (Intel)
* Nicolo Scipione (Codeplay)
* Romain Biessy (Codeplay)
* Ronan Keryell (AMD)
* Ruyman Reyes (Codeplay)
* Verena Beckham (Codeplay)
* Victor Lomuller (Codeplay)
* Victor Lu 

2024-02-15 oneAPI Construction Kit and Level Zero 1.9
=====================================================

Agenda:

* oneAPI Construction Kit – Colin Davidson (Codeplay) `[slides] <presentations/2024-02-15-oneAPI-Construction-Kit.pdf>`__
* Level Zero 1.9 Highlights – Will Damon, Michal Mrozek (Intel) [slides to follow]
* Proposed Future Topics – ALL
* Opens - ALL

Attendees:

* Michal Mrozek (Intel)
* Alison Richards (Intel)
* Zachary Dworkin
* Dan (Intel)
* Brice Goglin
* Jose Fonseca
* Will Damon (Intel)
* Victor Lomuller (Codeplay)
* Colin Davidson (Codeplay)
* Verena Beckham (Codeplay)
* Rod Burns (Codeplay)
* Alastair Murray (Codeplay)
* Robert Cohn (Intel)
* Neil Spruit (Intel)
* Stephen O
* Ronan Keryell (AMD)
* Tim Besard
* Maria Garzaran (Intel)
* Daniel Keller (Individual)
* Michael Kissner (Akhetonics)
* Juan Fumero (University of Glasgow)
* Brice Videau (Argonne National Lab)
* Pradeep

Questions:

* oneAPI Construction Kit

  * Q: Can you handle a super old LLVM backend, e.g. 3.x or 2.9.  A: Only current and previous two LLVM versions are supported.
  * Q: Can you support accelerators that cannot access global memory directly, e.g. scratchpad memories?  A: Yes, both devices with a separate global memory from host and devices with scratchpad memories.
  * Q: Does this work with SPIR-V backend?  A: Yes.

* Level Zero 1.9

  * Q: You say that you can now have complete compute graphs?  A: Level Zero API exists for the compute graphs to be built on top, so you build the command lists, clone them, and you can create complicated graphs with dependencies. Each node can be a separate command list, can remove wait events and signals to schedule hundreds of graphs with low overhead.
  * Q: With this feature of cloning we don’t have to reset the command list?  A: Yes, this was the main idea.  The intent from the start in Level Zero is that you use command lists without reset, and not that you can mutate command lists hope that you never need to reset command lists going forwards.  Follow-up: Good, if you forget to reset application crashes.
  * Q: Regarding immediate command lists can you append another immediate command list?  A: No you cannot appeand an immediate command list to an immediate command list, only append a regular command list.  For performance you no longer need queues, you can just use immediate command list.
  * Q: Like OpenCL queue?  A: Not quite, no need to flush.

Opens:

* Alison: If you would like to join UXL as a member please see the website.
* Verena: Safety Critical SIG is just starting and first meeting is next Wednesday, please join or forward to interested colleagues.
