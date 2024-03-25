===========================
UXL Foundation Hardware SIG
===========================

The Hardware SIG hosts discussions and presentations focused on
how to enable a broad range of hardware architectures.

The Hardware SIG is led by Alastair Murray (Codeplay) and Will Damon (Intel).

Archived meeting notes from meetings held under the oneAPI 
Community Forum can be found `here`_

.. _here: https://github.com/oneapi-src/oneAPI-tab/tree/main/hardware

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
