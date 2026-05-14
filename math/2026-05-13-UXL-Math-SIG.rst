=========================================
Math Special Interest Group Meeting Notes
=========================================

2026-05-13
==========

Materials:

* `oneAPI Specification <presentations/UXL-Math-SIG-2026-05-13_JohnMelonakos-oneAPI-Specification.pdf>`__
* `Updates <presentations/UXL-Math-SIG-2026-05-13_SarahKnepper_Update.pdf>`__

Attendees:

* Andrey Alekseenko (KTH Royal Institute of Technology)
* Himanshu Chaudhary (C-DAC)
* Biagio Cosenza (University of Salerno)
* Nick Dingle (Arm Ltd)
* Aniket Garade (CDAC)
* Ragesh Hajela (Fujitsu Limited)
* Sarah Knepper (Intel)
* Cheng Lee (Anaconda, Inc)
* John Melonakos (Intel Corporation)
* Alison Richards (Intel)


Agenda:

* oneAPI specification discussion - John Melonakos (Intel)
* Opens


OneAPI Specification Discussion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The meeting opened with introductions and agenda review. John led a discussion on the OneAPI specification approach, supported by shared materials. The intent was to outline a shift away from traditional specification releases.

Dynamic Specification Approach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The group discussed moving from static specifications to a dynamic approach backed by GitHub projects. A central UXL webpage would provide high-level descriptions and direct users to project repositories where APIs are defined and maintained.

UXL Documentation Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^
The proposed strategy is to reuse existing documentation within the UXL platform and avoid maintaining parallel specification artifacts.

Key considerations:

* Reduce duplication between specification and implementation
* Transfer necessary content into project repositories
* Maintain minimal static overview pages

Documentation Transition to oneMath
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Observations:

* Some documentation was removed to avoid duplication with the specification
* Certain unique information remains only in legacy specifications; e.g., Vector Math domain
* Plan to archive specifications while keeping them accessible

UXL Foundation Website Plans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Updates were provided on the new UXL Foundation website launch.

Highlights:

* New site structure with regional URL support
* Opportunities for community contributions
* New content on UXL YouTube channel

Website Content and Contributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The group discussed gathering additional SIG content.

Examples:

* Blog posts
* Case studies
* Technical sessions and recordings

OpenBLAS Backend Progress
^^^^^^^^^^^^^^^^^^^^^^^^^
Status updates:

* C-DAC team submitted PR for OpenBLAS backend
* Review ongoing
* ARM-related test concerns under investigation, but not a blocker

Testing and Review Status
^^^^^^^^^^^^^^^^^^^^^^^^^
* Some failures could not be reproduced
* Issues appear environment-related (RPL systems)
* Changes nearing readiness for merge pending validation

Buffer and Accessor API Discussion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Discussion centered on SYCL buffer/accessor usage, due to a potential change in SYCL spec to make buffers optional.

Key points:

* Challenges with embedded GPU support
* Limitations related to USM and SVM capabilities
* Potential alternative: mapping buffers to USM-backed storage

Alternative approach raised:

* Retain buffers but discourage usage via documentation and training

oneMath Development and SIG Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The group reviewed ongoing oneMath development efforts:


* OpenBLAS backend integration
* Updates to oneMKL backend
* Updates to ArmPL backend
* Specification alignment with Netlib (for example, GEMMT->GEMMTR updates)

SIG restructuring discussion:

* Proposal to merge Math SIG into AI and Scientific Computing SIG
* Rationale: overlapping domains and reduced meeting frequency
* General support expressed

Additional technical tracking:

* Buffer API usage across projects
* Specialization constant usage across implementations
