=========================================
AI Special Interest Group Meeting Notes
=========================================

2025-06-26
==========
Attendees

* Saleh JAMALI	        (UNISA)
* William Jones	        (Embecosm)
* Jianhui Li	          (Intel)
* Alison Richards       (Intel)
* Ashish Bisht          (Centre for Development of Advanced Computing)
* kuldeep pal	          (Individual)
* Biagio COSENZA        (University of Salerno)
* Melissa Aranzamendez  (The Linux Foundation)
* Abhishek Bagusetty	  (Individual)
* Aruna K               (Fujitsu)
* David Edelsohn        (NVIDIA)
* Victor Lu	            (Individual)
* Mourad Gouicem        (Intel)
* Shreyas K             (Individual)
* Nikolay Petrov        (Intel)
* Penporn Koanantakool  (Google)
* Deeksha Kasture       (Individual)
* Tao Lv                (Intel)
* Kevan Ahmadi          (Imagination)

======
Agenda
======

oneDNN Graph API: New Features and Updates,   Tao Lv,  Intel,  (`slides <presentations/2025-06-26-UXL-AISIG-oneDNNGraph-TaoLv.pdf>`__)

======
Notes
======
**oneDNN Graph API Overview and Features:**

Tao Lv provided an overview of the oneDNN Graph API, which is designed to express complex operations and fusion patterns like SDPA, GQA, and MLP, crucial for language models.

The Graph API supports the creation of computation graphs, which can be partitioned and compiled for execution, with optimizations beyond the capabilities of the primitive API.

**Key Concepts in the Graph API:**

Logical tensors and operation graphs are used to define and represent the computation logic.

Partitions allow for the division of a graph, which can then be compiled and executed.

The Graph API enables fusion patterns (e.g., convolution and activation) and supports complex operations like attention mechanisms, convolution-based operations, and MLPs.

**New Features in oneDNN 3.7 and 3.8:**

Performance optimizations for SDPA, GQA, and attention-based models on Intel CPUs and GPUs.

Support for attention masks and optimizations like safe softmax handling for negative infinity.

Gated MLP support on Intel platforms, contributing to model performance improvements.

**PyTorch Integration:**

PyTorch 2.7 integrated the oneDNN Graph API to accelerate SDPA inference and attention-based models, achieving up to 3x performance improvement over previous versions.

Future plans for PyTorch 2.8 integration include further optimizations for larger head sizes and implicit causal masks.


**Questions and Answers:**

*Page Attention:*

Jianhui Li asked about the impact of page-based attention on input tensors, as this would split the tensor into smaller, non-contiguous pieces, and how this would be handled as input in the Graph API. 

Tao outlined the challenges in implementing page-based attention, specifically with tensor layouts and cache loading operations. Tao emphasized that while the design for supporting page-based attention is still under development, it is an important feature that will eventually be supported, given its growing popularity. However, the exact implementation is still under discussion.

*Graph API Partitioning:*

Penporn asked about the value of exporting graph partitions. 

Tao explained that there are two main scenarios: In the Single Partition Scenario, the user constructs the graph to meet the library's requirements, and the partition API returns a single partition, giving the user full control. In the Multiple Partition Scenario, the user provides a larger graph, and the library identifies the optimal partitions, which are returned by the partition API. The user must then execute the partitions in topological order. 

*Integration with XLA:*

Penporn also raised the question of oneDNN Graph API's integration with XLA (Accelerated Linear Algebra). The motivation for using the oneDNN Graph API in XLA is that it aligns well with XNNPACK, another backend library that also incorporates graph constructs. 

Tao explained that XLA is already leveraging oneDNN for optimizing operations on Intel CPU platforms. By using the Graph API, XLA can simplify graph construction and execution, converting the XLA Graph into corresponding backend library graphs seamlessly. The XLA integration is exploring the possibility of transitioning oneDNN integration from the primitive API to the Graph API. The team is evaluating the Graph API's capabilities, particularly in terms of feature parity with the primitive API and addressing specific challenges such as block layout and scratchpad handling.
