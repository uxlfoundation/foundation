===================================================================
  AI and Scientific Computing Special Interest Group Meeting Notes
===================================================================

2026-04-23
==========

Attendees

* Dhiraj (Individual)
* Rajesh Rajendran (Individual)
* Manuj (Qualcomm Technologies, Inc.)
* Jianhui Li (Intel)
* Mehul (Individual)
* Soham Nivargi (Individual)
* Shahla (Fujitsu)
* Shreyas K Shankar (Fujitsu)
* Vartika (Individual)
* Adarsh (Fujitsu)
* Venkat Thangella (Individual)
* Deeksha Goplani (Individual)
* Deepika H V (Centre for Development of Advanced Computing)
* Ratan Paswan (Individual)
* Victor Lu (Individual)
* Hirotaro Ohira (Fujitsu)
* Shubhajeet Dey (Fujitsu)
* Utkarsh Tiwari (Individual)
* Akash Agrawal (Fujitsu)
* Hrushit Kakadia (Fujitsu)
* Ashish Poonia (Indian Institute of Science)
* Amar Kumar (Individual)
* Aruna K (Fujitsu)
* Mohak Goel (Fujitsu)
* Sumukha Prasanna Kumar (Individual)
* Koichi Hirai (Fujitsu)
* Himani Joshi (Individual)
* Alex Pim (Imagination Technologies Ltd.)
* Tishha Agarwal (Individual)
* Om Prakash (Fujitsu)
* Atsushi Nukariya (Fujitsu)
* Ajay Kumar Patel (Fujitsu)
* Ankitkumar Mishra (Individual)
* Jin Tkahashi (Fujitsu)
* shefali kamal (Fujitsu)
* Jaydip mokariya (Individual)
* Ryo Tabei (Fujitsu)
* Himanshu Gupta (Individual)
* Masaya Kato (Fujitsu)
* Akhil Goel (Individual)
* Keshav Ranjan (Fujitsu)
* Subhajit ghosh (Individual)
* Prof. Makoto Tsubokura (Kobe University)
* Penporn Koanantakool (Google LLC)
* Prakash (Individual)
* Vishwas BC (Fujitsu)
* Chandra Ganesh (Individual)
* Sachin M (Individual)
* Abhishek Jain (Fujitsu)
* Laxmikant (Centre for Development of Advanced Computing)
* Rajan kumar pal (Fujitsu)
* Venkat (Individual)
* Susmitha Devanga Ampabathini (Fujitsu)
* Debnath Pal (Indian Institute of Science)
* Abhishek Kumar (Fujitsu)
* Koutarou Taki (Fujitsu)
* Dmitry Zarukin (Individual)
* Rohan (Individual)
* Ran Ch (Individual)
* Dave Ojika (Flapmax)
* Vanshika Jindal (Individual)
* Naman Pesricha (Individual)
* Rajeshwari K (Fujitsu)
* Binoy Thomas (Fujitsu)
* Amar Prakash Azad (Fujitsu)
* Ryo Tabei (Fujitsu)
* Vaishnavi Ravi (Fujitsu)
* devang.lnu (Fujitsu)
* Divya (Fujitsu)
* Ragesh Hajela (Fujitsu)
* Shubham (Fujitsu)
* kuldeep pal (Individual)
* Rakshith GB (Fujitsu)
* Ashish Bisht (Fujitsu)
* Anubhav Srivastava (Fujitsu)
* Rathinasamy Thangarajan (Individual)
* Gaurav Agrawal (Individual)
* Nishant Prabhu (Fujitsu)
* Pranoy Panda (Fujitsu)
* Snehashis Dhibar (Individual)
* Himanshu Chaudhary (Centre for Development of Advanced Computing)
* Jinka Naga Sai Gowri (Fujitsu)
* Saurabh Chattopadhyay (Individual)
* Nishith Jaiswal (Fujitsu)
* Masahiro Doteguchi (Fujitsu Limited)
* Alison Richards (Intel Corporation)
* Priyanka Sharma (Fujitsu Limited)
* Aniket Garade (Centre for Development of Advanced Computing)
* Nagireddy (Individual)
* Atul Kumar (Fujitsu)
* Kiran Addanki (Individual)
* Ajeya B S (Fujitsu)
* Harshita Badiyasar (Fujitsu)
* Dinky Lakhani (Individual)
* En Shao (University of Chinese Academy of Sciences)
* Santhosh (Individual)

================
Recording Link
================

**Watch to explore how AI is shaping the future of simulation, modeling, and engineering innovation** (`Recording Link <https://www.youtube.com/watch?v=ta_DZxzLyEc>`__)

======
Agenda
======

**About AI & Scientific Computing SIG by Chairs (Penporn and Priyanka)**

**When AI Meets Engineering Design: Constraining Its Creativity for Smarter Vehicle Aerodynamics Design (Prof. Makoto Tsubokura, Kobe University and RIKEN, Japan)**,  

Summary
=======

Overview
-----------------

- The Unified Acceleration Foundation (UXL) AI Special Interest Group (SIG) is now evolved into the AI & Scientific Computing SIG, expanding its scope to include scientific frameworks and AI for Science.
- This was the inaugural meeting of UXL AI and Scientific Computing SIG featuring a presentation by Prof. Makoto Tsubokura on the impact of AI on engineering design.
- Prof. Tsubokura explained that for AI to be useful, appropriate constraints are necessary. He emphasized the need to build a constrained design space that accounts for the differing perspectives of engineers and designers
- This design space utilizes three techniques: parameterized geometry, Principal Component Analysis (PCA), and latent space editing. He covered topics on development of AI surface models and multi-objective optimization to controlled shape refinement.

About AI & Scientific Computing SIG
-----------------

- Priyanka and Penporn hosted the meeting, explaining purpose and vision for AI and Scientific Computing SIG.
- They welcomed all AI SIG members and new attendees, explaining that while the focus has been on AI topics for the past few years, interest in scientific computing applications is growing.
- Explained how scientific computing workloads align with the UXL software ecosystem and presented a use case involving AI surrogate models.
- Guest speaker Prof. Makoto Tsubokura was introduced to discuss the impact of AI on engineering design.

When AI Meets Engineering Design - Talk by Prof. Makoto Tsubokura
-----------------

Title: When AI Meets Engineering Design: Constraining Its Creativity for Smarter Vehicle Aerodynamics Design

Abstract
-----------------

- Applying AI to vehicle aerodynamic design remains challenging because vehicle geometries are highly complex, while high-fidelity CFD data for training are computationally expensive and limited. This talk presents our recent efforts to combine HPC-based CFD and AI for smarter vehicle design through constrained shape learning and optimization.

- First, vehicle shapes are parameterized using a morphing-based approach with a moderate number of deformation parameters selected in collaboration with an automotive OEM. Based on a few hundred generated shapes evaluated by large-scale CFD, a neural-network surrogate model is developed to predict aerodynamic quantities such as drag and lift.

- This surrogate is then integrated into a multi-objective optimization framework for efficient design exploration. Because unconstrained optimization often produces aerodynamically superior but stylistically unrealistic shapes, we further introduce a realism constraint learned from a large set of commercially available SUV shapes.

- By projecting these vehicles into the parameter space and applying principal component analysis, we identify a lower dimensional subspace representing stylistically plausible designs. Optimization within this subspace achieves a better balance between aerodynamic performance and design realism.

Discussion Highlights
-----------------

- Prof. Tsubokura explained on usage of CFD softwares to significantly reduce pre-processing time for vehicle exterior designs, enabling the AI to handle large volumes of data.
- Participants asked questions regarding evaluation of Tesla Cybertruck, the balance between performance and style, programming frameworks that were used, and computational resource requirements, to which Prof. Tsubokura provided detailed responses.
