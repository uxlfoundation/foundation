=========================================
Math Special Interest Group Meeting Notes
=========================================

2024-04-24
==========

Materials:

* `Discussion on sparse BLAS APIs <presentations/UXL-Math-SIG-2024-04-24_RomainBiessy_SparseBLAS.pdf>`__
* `Updates and buffer APIs discussion <presentations/UXL-Math-SIG-2024-04-24_SarahKnepper_Update.pdf>`__

Attendees:

* Hartwig Anzt (UTK)
* Seung-hee Bae (Intel)
* Abhishek Bagusetty (Argonne National Laboratory, ANL)
* Colleen Bertoni (ANL)
* Romain Biessy (Codeplay)
* Rod Burns (Codeplay)
* Gajanan Choudhary (Intel)
* Terry Cojean (KIT)
* Dai-Ni Hsieh (Intel)
* Gordan Jenson
* Sarah Knepper (Intel)
* Maria Kraynyuk (Intel)
* Piotr Luszczek (UTK)
* Kumudha Narasimhan (Codeplay)
* Nicolas Offermans (Intel)
* Spencer Patty (Intel)
* Chris Reed (GE HealthCare)
* Alison Richards (Intel)
* Shane Story (Intel)
* Edward Tuke (Imagination Technologies)


Agenda:

* Discussion on sparse BLAS APIs - Romain Biessy
* Updates from last meeting - Sarah Knepper
* Brief discussion on buffer APIs - Sarah Knepper

New oneMKL sparse specification:

* Lots of help from Gajanan Choudhary and Spencer Patty as well. This is a follow up from a previous Math SIG meeting, where I explained some changes. Specification Pull Request `#522 <https://github.com/uxlfoundation/oneAPI-spec/pull/522>`__ is in review. Main motivation for all changes was to better align with all of the backends we want to support, and make it easier to transition from existing applications to oneMKL interfaces.
* We are renaming some operations.
* There will be a single function for different types of matrix-vector multiplication; gemv, symv, and trmv will all be replaced by spmv.
* Similarly, gemm will become spmm, and trsv will be spsv.
* We propose to drop gemvdot because other backends do not support this.
* Previously there was only a single matrix handle for sparse matrices. Now there are two more with the introduction of  dense vector and matrix handles.
* You need to initialize and release dense handles. The motivation is to avoid overheads for NVIDIA and AMD backends.
* We also have an operation descriptor specific to each operation, which needs to be initialized. You give that descriptor to optimize or computational functions, and then release it later.
* The operator descriptor doesn't use C++ object constructor/destructor because it's asynchronous and needs to wait on input events and return an event.
* New APIs: algorithm enum, specific to each operation. There's a default algorithm, there's one called "no_optimize_alg" that means the optimize step should be as cheap as possible since the user will make the call only once, and then other algorithms based on the operation. This is something that wasn't supported previously, but now will be.
* New APIs: matrix_view. This is passed to every function and specifies which part of the matrix should be read. By default, the matrix is assumed to be general, but if your input matrix is triangular for spmv, then only the upper (or lower) triangular part would be read. You don't need to change the underlying data.
* Two use cases: change the definition of the operation if the matrix handle is a full matrix but viewed as triangular. Optimization hint if the matrix handle is already triangular.
* New API: set_matrix_properties. This will (at present) only be supported by Intel oneMKL backend. If the property is set, then it's used as an optimization hint. Some backends may not support these properties.
* New API: external workspace - new functions for every operation. We need to query the buffer size. This lets the user control the memory that the functions will use. Currently the oneMKL interfaces assume backends allocate memory internally; for NVIDIA and AMD backends, the user handles this. This workspace is given only in the optimize step; it is not needed for compute function (stored in the descriptor).
* Full example has the previous API on the left, proposed API on the right, both doing equivalent things. It is more verbose, but there are many more features.

Summary of the changes:

* Renamed operations and dropped support for gemvdot.
* Small changes to sparse handle type and introduced new dense handle types.
* We now have an operation descriptor type and algorithm enums, and matrix properties and views.
* We have support for external workspace and changed responsibility of who allocates.

Q&A:

* Colleen Bertoni: Is there any change in supported formats?

  * Romain: In existing specification, we support CSR and COO. These two formats will still be supported.

* Terry Cojean: Does matrix view support COO?

  * Romain: From specification point of view, the backend will support every combination of format.

* Terry: Intel oneMKL backend doesn't have workspace. Will you get unsupported or something else?

  * Romain: With the current version of Intel oneMKL, we will internally make this allocation. That means the Intel oneMKL backend will need to return this value as 0, and the user won't need to allocate workspace. Once Intel oneMKL is updated, then that will work.

* Edward Tuke: It sounds like the external workspace is compulsory. But it seems to be listed as optional in the last slide: "Add support for external workspace."

  * Romain: That is not what I intended. It is required.

* Spencer Patty: Should we consider making it optional, and if nothing is required, the library has permission to allocate it themselves? There is always a fine line between giving people full control over what they want to do, and making the API simple. It may sacrifice performance.

  * Romain: Concern is support for cuSPARSE, etc.
  * Spencer: That's where it gets tricky. But we could do the allocation in our wrapper if it is not provided.
  * Romain: This is still an open debate, but hoping we can merge it soon.

* Piotr Luszczek: gemvdot() use case is in nearly every iterative solver where matrix-vector multiplication is followed by a dot product. Think of anything from Conjugate Gradient to GMRES, where you need this. I'm surprised you didn't hear from the solver community about this. For backends that don't support it - that's on them. And for those backends, we can have two separate functions and just pay the launch overhead.

  * Romain: That should be possible. There was a question on the value of this. It is definitely good to have feedback on the PR or to open an issue.
  * Piotr: If there's a different push for having graphs that mitigate the launch overhead, and for each iteration you just launch a single graph - that's fine as well. Then you don't need to fuse them. Either way would probably be a similar performance gain.
  * Romain: I don't know if sparse backends can do more optimizations than a graph would be able to do. I also like this solution.
  * Spencer: It is probably a ways out before we get that optimization. For gemvdot, you probably have the data in cache. So it's a savings in memory footprint instead of having to pull up double the amount when you're doing the dot. It is a handy, simple API. More complicated ones like graphs are probably years ahead of us to get technology as we hope we could.
  * Romain: Should we keep it today, or add it back in the next version?
  * Spencer: There is some value in some algorithms where that shows up.

* Abhishek Bagusetty: Will there be a plan to add support for 32-bit indexing?

  * Romain: It is there and should be supported. If there are issues, let us know.

* Spencer: There's another group that some of us are part of that's looking at a C++ standard. What we're looking at today is version 2. Someday, the common-across-everyone, more C++ oriented version, will be version 3.

* Sarah Knepper: For the matrix view, why was a new enum chosen instead of using C++ mdspan?

  * Romain: We don't store the data, while the C++ views I believe store the pointer. I don't think it would fit what we need. Perhaps the name matrix_view is misleading.


Updates from last meeting:

* Need to move https://github.com/oneapi-src/oneMKL to LF/UXLF ownership; proposal is https://github.com/onemkl-project/oneMKL-sycl-interfaces.
* oneMKL interfaces v0.4 was released
* In addition to the #sig-math channel on Slack, there is also a #onemkl channel for discussions on the oneMKL interfaces open source project.
* The UXL Open Source Working Group created a checklist to ensure best practices are used in oneMKL interfaces and other open source projects; these tasks will be worked on in the coming months.
* The oneAPI spec repo was moved from https://github.com/oneapi-src/oneAPI-spec to https://github.com/uxlfoundation/oneAPI-spec.
* There are a couple of pull requests that may be of interest (including the one Romain discussed earlier in the meeting), as well as an open issue.

* The spec moved to the uxlfoundation org, but the oneMKL interfaces will be moved to a different org?

  * Yes, the open source repositories will be moved to their own project organizations. This was discussed in the UXL Open Source Working Group and has some advantages, like not needing to share GitHub runners.

Brief discussion on buffer APIs:

* The oneMKL specification supports both USM and buffer APIs
* There are some limitations to buffer APIs, and NVIDIA and AMD libraries natively support only a USM-like interface.
* There is no known customer usage of buffer APIs in Intel oneMKL product.
* Seeking feedback on a proposal to deprecate and remove buffer APIs from the oneMKL specification.

* Feedback on buffer APIs:

  * Colleen: No known usage of buffer APIs in applications at ANL, but it is part of the SYCL specification.
  * Romain: There is an extension that would make it easier to get a pointer from a buffer, but it's probably a long way out. But that would make interoperability between the two easier.
  * Edward: Removing buffer APIs would be a problem for Imagination Technologies. Our GPU uses OpenCL and SYCL, with sycl::buffers and not USM.
  * Gajanan Choudhary: There may be a strategic advantage of SYCL buffers. People who are moving to SYCL may find it easier as they don't need to worry about dependency management, and can just focus on the right accessors for the algorithm they are using.

Upcoming UXL Webinar:

* UXL Foundation is having a webinar on Tuesday, April 30 at 8am Pacific
* https://www.linuxfoundation.org/webinars/uxl-foundation-drive-an-open-standard-accelerator-software-ecosystem
