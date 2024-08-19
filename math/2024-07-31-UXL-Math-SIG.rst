=========================================
Math Special Interest Group Meeting Notes
=========================================

2024-07-31
==========

Materials:

* `Overview of ArrayFire <presentations/UXL-Math-SIG-2024-07-31_UmarArshad_ArrayFire.pdf>`__
* `Updates <presentations/UXL-Math-SIG-2024-07-31_SarahKnepper_Update.pdf>`__

Attendees:

* Melissa Aranzamendez (The Linux Foundation)
* Umar Arshad (Intel)
* Rod Burns (Codeplay)
* Robert Cohn (Intel)
* Rachel Ertl (Intel)
* Ethan Glaser (Intel)
* Akhil Goel (Intel)
* Dai-Ni Hsieh (Intel)
* Louise Huot (Intel)
* Sarah Knepper (Intel)
* Maria Kraynyuk (Intel)
* Piotr Luszczek (UTK)
* Abhilash Majumder (Intel)
* John Melonakos (Intel)
* Kumudha Narasimhan (Codeplay)
* Nicolas Offermans (Intel)
* Spencer Patty (Intel)
* Ed Tuke (Imagination Technologies)


Agenda:

* Overview of ArrayFire with a focus on math functions - Umar Arshad
* Updates from last meeting - Sarah Knepper

Relationship between ArrayFire and UXL - John Melonakos:

* ArrayFire is a library Umar will talk about. I want to set the stage of what we're trying to accomplish in the SIG. ArrayFire is 14 years old; common GPU performance library available in open source for a long time. We released a oneAPI backend for it this past year. We've been handling a couple other things in UXL, like C API, which should be decided first. Should UXLF be involved in more than just C++ APIs? Should we at UXL have a higher-level tensor-based approach to oneAPI?
* For projects like ArrayFire that build on top of oneAPI, what does UXL want to do with those libraries? More activity in general comes when you come together around oneAPI.
* We have this project that's been ported to oneAPI. ArrayFire has maintainers in different companies and not owned by Intel - it would be an external member into UXL Foundation.
* We're trying to socialize these questions, but not make strong  decisions today. Keep these in the back of your mind during the discussion.

Overview of ArrayFire - Umar Arshad:

* ArrayFire has been open for over 10 years. It is high-level math programming, primarily written in C/C++ with wrappers for Rust, Julia, etc. It is open source based on BSD v3 license. One main feature is that it performs kernel fusion based on JIT compilation that generates kernels at runtime.

Design Goals:

* Main point is to be easy to use. We created an API that minimizes the use of templates (still required sporadically). We pick reasonable defaults and we manage the library state (how to allocate memory, compiler caches, etc.). We also value binary stability and portability. Every time we add a new feature, we do a minor release; if an interface changes, we do a major release. We haven't done that in a long time, so we have a pretty stable C interface. Most other wrappers, like C++, are based on the C interface. For performance, we focus on throughput instead of latency - we target larger problems that are more suited to the GPU.

Productivity, cross correlation:

* With oneAPI, you need to manage how to calculate a plan; ArrayFire handles that for you. Our goal is simplicity. You can read more in the `Intel Parallel Universe article <https://www.intel.com/content/www/us/en/developer/articles/technical/accelerate-2d-fourier-correlation-algorithm.html>`__.

Library components:

* This is about how the ArrayFire library is organized. We have hand-optimized kernels built on top of oneAPI/OpenCL/CUDA; functions like convolution, reduction, and so on. We also take advantage of external libraries like BLAS, FFT by forwarding operations to them.
* We have a JIT Engine that allows us to fuse several operations together and greatly improve performance. We have a memory manager that manages memory so you don't have to worry about allocating multiple times; we cache for you - you don't need to worry about lifetime. We have device/library state (how many GPUs do you have, how many CPUs, what features are available, keep track of FFT plans, etc.). We also have interop functions so you can use ArrayFire in other applications where you are already using OpenCL.

Core data structure and functionality:

* af::array is a C++ object that manages a multi-dimensional data array, handles up to 4 dimensions. It supports all standard data types, including integers of various sizes as well as dense and sparse support.
* Several different categories of functions: reductions, convolutions, etc. All function calls are asynchronous; calls to complex functions are queued immediately. Whenever the GPU is available, we'll execute them. Simple arithmetic calls are evaluated; AST (stream) kernel is generated at runtime.

Usage:

* ArrayFire tries to be a fairly simple API. Create a 1x10 array object of floats: array b(1, 10, b_ptr)
* We can use this array to index into it, even non-consecutively. We can assign a value to all elements, or a row, or first 3 elements, etc. Basic arithmetic is what you'd expect.
* Allocations - we have a memory manager in ArrayFire. Whenever you create a data array or an array object with a host-side pointer, we allocate it immediately. But constants and results from element-wise operations aren't allocated until necessary. We create a pseudo-array that represents that value.

ArrayFire JIT:

* This allows us to use the ArrayFire Just-In-Time functionality. Basic Arithmetic functions are evaluated but not executed; it builds a dependency tree based on the function calls. We create, compile, and link a kernel and execute them at runtime. You'll hit a penalty the first time, but we cache that kernel, so you won't hit the penalty the next time. * We cache the kernel in memory and disk. This allows us to minimize driver overhead associated with kernel calls. This also allows us to minimize access to global memory. Typically you want to perform multiple compute operations on data; this allows us to do that and allows us to minimize the use of temporary arrays - reduces memory overhead.

Example:

* We allocate buffers x and y. When you call the multiplication operation, an expression is generated. It's not really executing any operations for the operation - the array returned by the x*x operation is just a symbol that represents the expression; same for y*y, and addition, and comparison < 1 (1 is a constant, so no memory is allocated). We generated an entire tree of operations - but when we call the sum function, this requires that the expression is evaluated. We will generate a kernel based on the tree and store in memory buffer. Rest of operations are floating point operations - regular host-side C.
* The OpenCL kernel that is generated is given in the slides.

JIT Evaluation Criteria and Memory Manager:

* JIT kernels are generated whenever the result is necessary, like the sum function. We have to consider device limitations (how many parameters can be passed), so we make sure the kernel isn't too big. We also take into account the memory pressure. An array that is backed by multiple buffers can get out of hand, so we may evaluate an expression to avoid this.
* Allocation and deallocation events are typically synchronization events. Memory is allocated using bins of 1KB size (can be changed). Say you have a for loop where you're allocating the same size each time and deallocating. The buffer can be re-used.

Case Studies:

* ArrayFire is used by a lot of different libraries, like Flashlight by Facebook. It performed really well against other frameworks like PyTorch. Not only is it faster, but it's much easier to develop for because of the ArrayFire abstraction.
* wav2letter++ uses ArrayFire for speech to text. Most operations are due to network overhead.
* We have a Python wrapper, which performs well compared to CuPy.
* ~45 Google Scholar hits in 2023 for ArrayFire.
* It is a flexible library with a hybrid approach to GPU compute that allows lazy evaluation and allocation of data.

Q&A:

* Robert Cohn: Is there support for multiple GPUs?

  * Umar: We don't distribute the array onto multiple GPUs. Flashlight is built on top ArrayFire, and they also support multiple GPUs. So it is possible to do it.

* Rod Burns: You have governance, contributors, a lot of history with the project. Hypothetical conversation - what would the project gain by being part of UXL if there's also good governance in place?

  * Umar: The vision is that we can have a tensor library as part of UXL. Most of the libraries that are part of UXL are lower-level and frameworks build on top. It would be beneficial to have a library that handles the high-level functions, to kind of combine all UXL libraries into one so you don't need to learn different APIs. Framework-level users want one level, others want another.

* Rod: Are the APIs defined by the project or by standards?

  * Umar: By the project. Some internal efforts to provide a specification, but the ArrayFire project is just header with some documentation.

* Robert: Have you looked at the Python array specification?

  * Umar: Yes. Our Python API actually implements the array API from Python.
  * Robert: Okay, so it's interoperable. I could do stuff in ArrayFire and then pass it on to something else in Python.

* Rod: You mentioned NumPy and Matlab - does this compete alongside those?

  * Umar: They have similar goals with providing a high-level tensor data structure that's easy to use and allows for indexing. NumPy is CPU focused whereas we're trying to target GPUs. NumPy doesn't have JIT or memory management like ArrayFire does.

* Sarah Knepper: Consider the de facto standard BLAS or oneMKL BLAS APIs, where we have the gemm function or syrk or symm, depending on the matrix properties. How does ArrayFire take advantage of the matrix properties?

  * Umar: That's something we can improve. We have matmul that performs matrix multiplication and handles transpose. It's something that can be offered by the library.
  * Sarah: So there's a generic matmul that currently generally maps to gemm.

* Spencer Patty: How do you decide what goes into ArrayFire?

  * Umar: Previously we were an independent project; the customer comes to us and we would add functionality depending on what users wanted - lot of computer vision, image processing. We've been focusing on enabling more AI functionality as well. If we joined UXL, we would have a more formalized process.
  * John Melonakos: Originally we just accelerated Matlab, the base Matlab functions that are the most popular math functions (come with the base toolbox). We sent surveys to thousands of people and got hundreds of responses, which guided which functions to put in. They match consistently with the core routines for matrix and array manipulations. There is a very, very long tail of scientific functions used in specific domains that aren't as popular. We want to put things on the GPU that are well suited to GPU.
  * Spencer: Do you find the focus has shifted over 15 years as the community has grown? Does it make sense to refresh surveys?
  * John: It would make sense if we had a bigger team and were more able to build the long tail of functions. Those core routines have stayed statically important - 0 change in how important the core routines of Matlab and NumPy are. All the long tail routines build on top of those core routines. We are focused on maintaining performance leadership on these core routines.
  * Umar: Some projects use ArrayFire, add some functionality, and then contribute back to ArrayFire.

* Robert: What are you doing for CI today?

  * Umar: We have several devices that target different architectures. We have tested on NVIDIA, AMD, and Intel hardware. Whenever a pull request is created, we try to test on multiple different vendors, to make sure that what we're generating is portable across different platforms.
  * Robert: Is that connected to the public Github?
  * Umar: We're managing internal devices that get triggered by Github workers.
  * Robert: For Rod's earlier question, I was wondering if more CI would be a benefit to ArrayFire if it joined UXL.
  * John: That could be a huge value-add of UXL to various projects to have that ability to validate across all the platforms of the members.

Updates from last meeting - Sarah Knepper:

* oneMKL Specification: Sparse BLAS API has been updated along with various bug fixes and enhancements.  Several PRs for sparse BLAS and RNG are under review.
* oneMKL Interfaces: Build documentation has been updated for easier onboarding. Modifications have been made to DFT domain to reflect previous specification updates. Several PRs in progress for sparse BLAS, including support for cuSPARSE and rocSPARSE backends.
* Proposal for Splitting the oneMKL Interfaces: At the UXL Open Source Working Group Meeting, there was a discussion on making the repository more modular to facilitate better user engagement. An RFC (request for comments) will be made for feedback.

* Robert: Any feedback from SIG members about current repository ease of use? [None.] It's good to see you redid the build documentation. Once I understood how to do things, it was easy to work with, but getting to that point was hard because the documentation was out of date.

* Rod: Opinions on the best communication channels for telling people about an RFC, or other topics like that? We have the Slack channel, but it's not always on the front of people's minds; there is the mailing list.

  * Sarah: My personal preference is email.
* Melissa Aranzamendez: We have a monthly newsletter. You can sign up by going to `uxlfoundation.org <https://uxlfoundation.org/>`__ and filling out the survey at the bottom.
