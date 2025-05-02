=========================================
Math Special Interest Group Meeting Notes
=========================================

2025-02-26
==========

Materials:

* `Enabling oneMath on aarch64 CPU <presentations/UXL-Math-SIG-2025-02-26_AugustinDegomme-SiPearl-OneMathArmPlbackends.pdf>`__
* `Updates <presentations/UXL-Math-SIG-2025-02-26_SarahKnepper_Update.pdf>`__

Attendees:

* Andrey Alekseenko (KTH Royal Institute of Technology)
* Hartwig Anzt (UTK)
* Melissa Aranzamendez (The Linux Foundation)
* Vasudha Badri-Paul (Intel)
* Colleen Bertoni (ANL)
* Rod Burns (Codeplay)
* Biagio Cosenza (University of Salerno)
* Augustin Degomme (SiPearl)
* Akhil Goel (Intel)
* Chris Goodyer (Arm)
* Ragesh Hajela (Fujitsu Limited)
* Himanshu
* Gordan Jenson
* Ronan Keryell (AMD)
* Sarah Knepper (Intel)
* Cheng Lee (Anaconda, Inc)
* Viraj Malia (Intel)
* John Melonakos (Intel)
* Kumudha Narasimhan (Codeplay)
* Nicolas Offermans (Intel)
* Alison Richards (Intel)
* Manuj Sabharwal (Qualcomm)
* Edward Tuke (Imagination Technologies)


Agenda:

* Enabling oneMath on aarch64 CPUs - Augustin Degomme (SiPearl)
* Updates from last meeting - Sarah Knepper

Opens:

* Viraj Malia introduced the idea of supporting Docker containers for the oneMath project, highlighting the ease of use and maintenance benefits. John Melonakos mentioned it was talked about in the Open Source Working Group and discussed the potential for binary releases and their utility for the community. The idea is to simplify the setup process for users by providing pre-configured Docker images. Andrey Alekseenko said that the GROMACS project currently builds oneMath from source. Viraj will open a discussion in the oneMath project about Docker container support to gather feedback from the community.

Enabling oneMath on aarch64 CPUs - Augustin Degomme:

* Augustin Degomme from SiPearl discussed their company's focus on developing European high-performance, low-power microprocessors for future supercomputers. They aim to improve the ecosystem by making codes work on their platforms with high performance. SiPearl is a joint venture with the European Union and other companies, and they have secured more than 100 million euros in funding. Augustin discussed the Arm Performance Libraries (ArmPl), which are similar to Intel oneMKL for the Arm platform, optimized for vectorization and performance. He highlighted the availability of these libraries for various platforms and compilers. The goal of adding a backend to oneMath for ArmPl is to provide a good ecosystem and support for most of the codes from the HPC community using their processors.

* The first backend to be ported and integrated was BLAS. Support was added for aarch64 CPUs for both ArmPl and Netlib. The batched functions were implemented with loops whenever direct support was not available in ArmPl. Interleaved batched calls was not integrated into the backend because changing the data layout was too costly. Some issues in oneMath were found and opened, which were quickly fixed. Some issues in ArmPl itself were found and fixed in various versions. Now 95% of the backend is supported, with only a few calls (omatadd2/copy2, int8/bfloat16 gemm) not supported. It took around two months to do the work for the BLAS backend; the pull request was submitted last month and integrated quite quickly.

* LAPACK backend had also been done a few years ago and revived last month. It uses the same LAPACKE interface as ArmPl. Adding a Netlib backend could be done quite easily. There are two phases in LAPACK - scratchpad size query then computation. The query doesn't exactly match LAPACKE because oneMath uses a single work array, so for certain functions that require multiple work arrays in LAPACK, internal allocations are used. Support for batched calls are not yet added as these are not supported in ArmPl. If requested, loops over single calls could be implemented. 100% of tests are reported as passing, including skipped tests, which is a bug. The pull request was submitted last week and merged yesterday.

* ArmPl released the OpenRNG library, as a drop-in replacement for Intel VSL library, which made the implementation into oneMath easier. Several generators and distributions are implemented in OpenRNG; mrg32k3a and philox4x32x10 were added for now. An issue in OpenRNG with int32 uniform generator was found and reported to Arm; it will probably be fixed by their next version. The pull request was submitted last week and is being actively discussed.

* Different use cases for oneMath are considered, including as a way to obtain performance portability and simplify maintenance in applications. Augustin also discussed the performance of the code on different platforms, including Intel Sapphire Rapids, Ampere altra, and Nvidia Grace. He observed that the performance of the direct BLAS (dgemm) call outperformed the oneMath wrapper on Sapphire Rapids, which may be due to parasite threads. The oneMath wrapper slightly outperformed the direct BLAS call on Ampere and Grace, which is puzzling but was reproducible. More investigation on these performance results is needed.

* In conclusion, BLAS/LAPACK/RNG domains are available for aarch64 CPUs, with close to native performance. DFT will probably be the next target; the APIs need to be mapped to FFTW, but no backend has done such a thing yet. Sparse BLAS is a good target after that.

* Viraj noted that Intel oneMKL provides interface wrappers for FFTW, but these are around the dfti APIs, which is kind of opposite what is needed. Augustin will check these interfaces.

* Chris Goodyer from Arm acknowledged the bug reports received and mentioned that most have been fixed, with the RNG issue expected to be resolved by the end of next month. Augustin discussed challenges in pinning threads and controlling process allocation when using oneMath, noting that it was more difficult to manage compared to Intel oneMKL with CBLAS and FFTW. Chris inquired about the performance graph results and the use of batched routines in oneMath, mentioning the existence of batched GEMM functions that Augustin may not have noticed and the willingness of Arm to add additional functions per user request.

* An email from the Codeplay team raised a question about compiling with oneMath header files and dynamically linking to an ArmPl build. Chris suggested that this may be an unlikely scenario but potentially could work.

* Sarah Knepper raised a question about the potential usefulness of adding interleaved batched APIs to the oneMath specification, which Augustin suggested could be a good target if there's enough user interest. Chris suggested holding off on this feature until a new sparse standard is established, as it would be easier to standardize across all products.

* Biagio Cosenza questioned whether the generated code is vector length agnostic or specific. Augustin clarified that they were using the binary version provided by ArmPl, and the decision tree for each call was done inside the library, not by them. Chris emphasized the need for the interface to be generic code, which would compile and run on all platforms, similar to how AVX 512 bits wouldn't be used on an old machine with SSE. He also mentioned that the code is vector length agnostic and that the necessary variations for different architectures are handled by the magic part of the code.

Updates from last meeting - Sarah Knepper:

* Sarah provided updates on the oneAPI specification, announcing the release of version 1.4 and the rename of the oneMKL element to oneMath. A similar renaming has been done for the open source project, as well as moving the repository under the UXL Foundation's GitHub organization. Other progress to the oneMath project was highlighted, including the support of ArmPl backends, cuSparse and rocSparse backends, and a new geometric distribution added to the RNG device API.
