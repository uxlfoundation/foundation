=========================================
Math Special Interest Group Meeting Notes
=========================================

2024-01-31
==========

Materials:

* `GROMACS Case Study: Using the oneMKL interfaces project as a backend for discrete Fourier transforms (DFTs) <presentations/UXL-Math-SIG-2024-01-31_HughBird_GROMACS.pdf>`__

Attendees:

* Kevan Ahmadi (Imagination Technologies)
* Romain Biessy (Codeplay)
* Hugh Bird (Codeplay)
* Mahesh Budavarapu
* Rod Burns (Codeplay)
* Tadej Ciglaric (Codeplay)
* Robert Cohn (Intel)
* Terry Cojean (KIT)
* Atharva Dubey (Codeplay)
* Dai-Ni Hsieh (Intel)
* Louise Huot (Intel)
* Gordan Jenson
* Ronan Keryell (AMD)
* Sarah Knepper (Intel)
* Maria Kraynyuk (Intel)
* Finlay Marno (Codeplay)
* Kumudha Narasimhan (Codeplay)
* Alison Richards (Intel)


Agenda:

* GROMACS Case Study: Using the oneMKL interfaces project as a backend for discrete Fourier transforms (DFTs) - Hugh Bird

Background:

* Hugh gave this presentation at the oneAPI DevSummit.
* He is part of the Cheetah team at Codeplay, working on FFTs with their own portFFT library and with oneMKL.
* He was involved with the first backend support of the DFT domain in the oneMKL interfaces, and he has introduced external workspaces for DFTs to the oneMKL specification.
* Codeplay is based in Scotland and has about 100 employees. In 2022, it became a subsidiary of Intel. Teams within Codeplay develop plugins for Nvidia and AMD GPUs, among other open ecosystem work.
* Start by talking a little about GROMACS, our example HPC application. Talk about what could development look like, and talk a little bit about oneMKL for those who haven't come across it before. Then we'll look at oneMKL as a backend for GROMACS, including some performance results. We'll wrap up with why you should use SYCL and oneMKL.

What is GROMACS?

* GROMACS is an open source code for molecular dynamics. In a nutshell, it's chemistry - incredibly useful for simulating proteins, nucleic acids, etc.
* You can look at a level of detail not possible in physical reality, though it is very computationally expensive.
* 5% of all compute cycles worldwide are spent on GROMACS. If you can improve performance, you can save a lot of money on resources.
* GROMACS is simulating chemistry, simulating all the different interactions between atoms.
* First you have bonded interactions, which are pretty local things. A few atoms that are bonded together in pairs. There is a limited number of these in your problem, and they can be simulated with GPU kernels.
* More problematic are the non-bonded interactions. Every atom interacting with every other atom, which scales with n^2. This is not good if you have a lot of atoms, as one tends to. You need to accelerate these via FFTs.

Fast Fourier Transform:

* A fast Fourier transform is a fast way of solving the discrete Fourier transform, reducing complexity from N^2 to N log N, which is a huge speedup.
* There are lots of uses, including fast convolution and cross correlation, so they can be used to solve partial differential equations (PDEs). PDEs can be used in all sorts of physics, like aerodynamics (Hugh's background pre-Codeplay).
* Vendors are interested in providing optimized FFT libraries on their hardware. These are basically based around optimizing memory accesses, true on both CPUs and even more on GPUs.

GROMACS' DFT backends:

* GROMACS supports many different DFT backends. There are several different backends on host CPUs; CUDA; SYCL is a more recent backend (MKL-GPU, bbFFT, rocFFT, VkFFT); OpenCL is a deprecated backend but supports VkFFT and clFFT. And that's not even every FFT backend.
* That's a lot of code to look after and optimize.
* One thing we found working on the oneMKL interfaces is that a lot of libraries on the surface look very similar. Start in the real domain, perform a forward FFT with this stride and that number of FFTs in a batch, etc. There's a descriptor part. But then there's all the details - maybe the stride is negative in one backend, or the scaling factor isn't there. So there are issues with having lots of different backends.
* SYCL can provide similar performance as other backends. So potentially you can have an application that calls into SYCL with its own kernels and also calls into the oneMKL interface library, which then calls into vendor optimized libraries.
* oneMKL avoids the problem of having a bunch of slightly different APIs that can trip you up, and can dispatch into the right library depending on the hardware you're using.

oneMKL as a backend for GROMACS:

* oneMKL is more than just FFTs, it also has BLAS and LAPACK, RNG (random number generators), and sparse BLAS.
* The DFT domain supports multiple backends: MKL-CPU, MKL-GPU, cuFFT, rocFFT, and now portFFT (a SYCL-only implementation).
* One point of confusion with oneMKL libraries - there are sort of two of them. I've been using MKL-CPU or MKL-GPU to refer to the closed-source Intel proprietary library. When I say "oneMKL", I'm referring to the open source interface library, based on an open specification.
* So GROMACS could call directly into the SYCL API, reducing the amount of code to maintain, and use the oneMKL interface library to work with vendor-optimized FFT libraries.
* We added oneMKL as a backend to the SYCL implementation of GROMACS. It wasn't that much effort since it was similar to the existing MKL-GPU backend. We needed to change some macros, etc.
* In GROMACS, you have real-to-complex transforms. You need to set up descriptor with the types. The DFT size in this case is 3D because electrostatics is a 3D problem. You then put in a description of how data is laid out. Then call commit on the descriptor, to figure out how to best configure it before you compute it. oneMKL interface does an additional step; it looks at the syclQueue (abstraction for set of work that's going to run on the GPU) and looks at what device is associated (what vendor GPU), and from that it chooses which backend library it should use to run. If you run on an NVIDIA device, it will look for cuFFT.
* We have a pull request in the GROMACS repository with a second way of doing this, by explicitly stating which library you want; this circumvents the dynamic dispatching. That should only be a small overhead, but it can be avoided anyway.
* Then you compute the DFT. You write the DFT code once, and you get code that runs everywhere.

Performance results:

* There are a couple caveats to keep in mind for the performance comparisons. First, all performance results were performed in October 2023. GROMACS has improved on some aspects from this original implementation. Second caveat: neither comparison is apples-to-apples. But you'll hopefully agree the numbers are reasonable.
* First comparison is on NVIDIA A100, comparing native CUDA implementation (using cuFFT as backend) to using GROMACS's SYCL kernels and cuFFT via oneMKL interfaces.
* Performance of SYCL+oneMKL w/cuFFT gets about 85% of performance of native CUDA+cuFFT. The performance difference mostly came from the fact that the scheduling in CUDA and SYCL is a bit different. But the key takeaway: a single source that can run on AMD, NVIDIA, and Intel and get reasonable performance.
* Next we'll look at AMD, which is closer to apples-to-apples, but still not exact. We'll use SYCL backend, first with rocFFT compiled with hipSYCL, now called AdaptiveCpp, versus oneMKL+rocFFT with DPC++.
* Once again performance is not the same. The biggest reason at the time was that the GROMACS makefile was assuming that if you use DPC++, you're using Intel GPUs, and had certain constants it used. But if you are compiling with hipSYCL, different constants are used.

Call to Action:

* Trying to depend on having one set of hardware isn't a good idea, even if you're just starting out as a PhD student. This isn't about massive HPC applications - this is also about writing small applications as part of research, and having performant portability is useful.
* Call to action: use SYCL and oneMKL - less code, fewer APIs, less debugging. It is both portable by default and performant by default.

Q&A:

* Robert Cohn: I've been using the oneMKL product. Is it the same as the interfaces?

  * Hugh: Not quite. There are some enums in the oneMKL product, kept for compatibility with C interface. DFTI_COMPLEX_COMPLEX needs to be switched to something more C++, like config_value::COMPLEX_COMPLEX. I think there may be a few other differences. But on the whole, it is very similar.
  * Robert: So for me to move from what I have to something that works with interfaces, I may just have to modify a few of these.
  * Hugh: Yes, that's what we found in GROMACS, when we add oneMKL interfaces as a backend copied from the MKL-GPU implementation.

* Sarah Knepper: Did you encounter any surprises or gotchas?

  * Hugh: Originally, no. But in the latest pull request, we started to get a segfault on NVIDIA GPUs. But that was an interaction in the way dynamic libraries were loaded differently.

* Robert: Any portability bugs you found in your code?

  * Hugh: No, this was one of those moments when it mainly just worked. I also tried to work on aerodynamics code and it just worked.

* Sarah: Are there any new applications planned to add oneMKL as a backend?

  * Alison Richards: We can have a blog about GROMACS or other applications.

* Robert: Is the library just a header file, or is there runtime code you have to compile?

  * Hugh: Runtime code that has dispatching.

* Robert: I'm using CMake for my project, and I usually use fetch content to get dependencies - does that work well? Do you separately download?

  * Hugh: I think it works with fetch content. For GROMACS, we're not using fetch content on the basis that these HPC systems often don't have unlimited access to the internet.
  * Robert: By switching to the oneMKL interfaces, I can still use oneMKL product on Intel GPUs.
  * Romain Biessy: If you run into issues with fetch content, please raise a GitHub issue. But it should work.

* Sarah: Thanks for presenting, Hugh. Everyone, please let me know if you would like to bring any topics to the Math SIG!
