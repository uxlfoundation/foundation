=========================================
AI Special Interest Group Meeting Notes
=========================================

2025-03-06
==========
Attendees

* Penporn Koanantakool, (Google LLC)
* Tao Lv,               (Intel)
* Vasudha Badri-Paul,   (Intel)
* Alison Richards,      (Intel)
* Manuj Sabharwal,      (Qualcomm)
* En Shao,              (Institute of Computing Technology)
* John Melonakos,       (Intel)
* Abhishek Jain,        (Fujitsu)
* Milos Puzovic,        (Arm)
* Mourad Gouicem,       (Intel)
* Kevan Ahmadi,         (Imagination Technologies)
* Ashok Bhat,           (Arm)
* Jianhui Li,           (Intel)
* Rod Burns,            (Codeplay Software)
* Biagio COSENZA,       (University of Salerno)
* Victor Lu,            (Individual)
* Liping Wang,          (Beijing Institute of Open Source Chip, aka. BOSC)
* Xiaoyu Ma,            (Individual)
* Melissa Aranzamendez, (The Linux Foundation)


======
Agenda
======

Extend OneDNN Operators/APIs for AI Chips   Leping Wang, En Saho,  (`slides <presentations/2025-03-06-UXL-Extend_onednn_Operators_Apis_ For_AI_Chips_RFC_Bosc_LepingWang.pdf>`__)

AI use cases with oneDNN on Arm             Ashok Bhat,  (`slides <presentations/2025-03-06-AI_use_cases_with_oneDNN_on_ARM_ARM_AshokBhat.pdf>`__)

The meeting recording can be found (`here <https://zoom.us/rec/share/0dOySys6ruX57Hwi2WMvkJB3Zn0IEs6aVeZHXBMWpwzFy-1x37-cdGIrO-Yrs0Xa.nhKlXIlTEcv0lx3B>`__).

======
Notes
======

Leping discussed the importance of extending the OneDNN (OneAPI Deep Neural Network Library) APIs for unified computing platforms. He highlighted the need to make OneDNN the go-to backend for machine learning frameworks like TensorFlow and PyTorch. Leping also shared observations from their internal projects, which led to a survey comparing OneDNN with the cuDNN. He noted that OneDNN can work with other GPUs and AI accelerators, despite documentation suggesting otherwise. Leping proposed adding four primitive APIs to OneDNN: divisive normalization, multi-head attention (MHA), image to column, and CTC loss. Mourad suggested that MHA is currently supported through oneDNN Graph API and it is more flexible this way (complex op with primitive API is hard to use/configure to optimize a class of patterns with small variations).
	
Leping explains the motivation behind matching oneDNN with cuDNN APIs. The main goal is to use OneAPI as middleware to connect AI frameworks with various hardware backends, especially for domestic TCUs and NPUs. This approach allows hardware vendors to support OneAPI once and connect to multiple AI frameworks. Leping also mentions that OneAPI could be used for direct AI programming. When questioned about the need for this approach given existing Aten implementations in PyTorch and TensorFlow, Leping clarifies that it would help hardware vendors connect to multiple frameworks more easily and allow for general optimization methods in OneAPI. 

Ashok discussed the hardware features of Arm that aid in Machine Learning (ML), including Bfloat16 support and matrix multiply extensions. He explained how the software team makes these features available to higher-level frameworks like PyTorch and TensorFlow. Ashok introduced the Kleidi technology, which directly contributes to frameworks to provide the fastest implementation, typically an assembly. Ashok presented performance improvement numbers for PyTorch using OneDNN, showing a 2.9x improvement in the T5 translation case.

Ashok discussed the impact of community project openness on the project's design, integration strategy, and release dates. He emphasized the need for community participation to make the project more long-term. Mourad responded that oneDNN has established an RFC process to discuss openly new features and internal architecture changes, and oneDNN release schedule is public (`here <https://github.com/oneapi-src/oneDNN/milestones>`__), aligned with major AI frameworks release in general. 

Mourad discussed the need for improvement in the validation of releases and testing to address the challenges of framework integrating different versions, particularly in the context of arm and intel. He suggested that a common infrastructure for testing could be beneficial. Ashok agreeed and suggested that his team was already working on some of these issues and that there was an ongoing effort to reduce the delay between a feature being developend and its eventual use in Pytorch. 

Ashok discussed the challenges of integrating features into the Arm Compute Library and the creation of Arm Kleidi AI to address these issues. Penporn highlighted the benefits of the microkernel API in frameworks like TensorFlow and OpenXLA, and suggested integrating Kleidi AI with the oneDNN microkernel API. The team agreed on the need for greater portability and flexibility in their framework integration.

Penporn proposed improving communication by sharing major decisions and milestones via a mailing list (AI-SIG@lists.uxlfoundation.org) or Slack channel (https://uxlfoundation.slack.com/, #sig-ai channel). 
