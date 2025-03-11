# Overview

This project is focused on ocular diseases. The goal is to integrate, classify, and compress DNA sequence data related to eye disorders while developing a robust data processing pipeline. By working with public genomic data, the project aims to extract meaningful insights about disease risk, with a particular focus on the following eye disease categories and their associated genes:

- **Retinitis Pigmentosa (RP) and other Retinal Dystrophies**
  - **RHO (Rhodopsin):** Often associated with autosomal dominant RP.
  - **USH2A (Usherin):** Commonly linked with Usher syndrome (which includes RP) and non-syndromic RP.
  - **RPGR (RP GTPase Regulator):** Major gene for X-linked RP.
  - **RP1:** Another gene frequently mutated in RP cases.

- **Age-Related Macular Degeneration (AMD)**
  - **CFH (Complement Factor H):** A key gene involved in the immune pathway, frequently associated with AMD.
  - **ARMS2 (Age-related Maculopathy Susceptibility 2):** Strongly linked with increased AMD risk.
  - **HTRA1 (High Temperature Requirement A Serine Peptidase 1):** Another gene implicated in AMD susceptibility.

- **Glaucoma**
  - **MYOC (Myocilin):** Mutations here are linked to juvenile open-angle glaucoma and sometimes adult-onset glaucoma.
  - **OPTN (Optineurin):** Associated with normal-tension glaucoma.
  - **CYP1B1:** Commonly linked with primary congenital glaucoma.

- **Leber Congenital Amaurosis and Other Congenital Retinal Disorders**
  - **RPE65:** Important for retinal function and a target for gene therapy in Leber congenital amaurosis.
  - **CEP290:** Mutations are a well-known cause of Leber congenital amaurosis and other ciliopathies affecting the eye.
  - **CRB1:** Associated with early-onset retinal dystrophies.

[Software Demo Video](https://youtu.be/SeiyMQ18j9A)

# Development Environment

- **Programming Languages:** Python, R, C++, Rust
- **Key Libraries and Tools:**
  - **Python:** Pandas, NumPy, scikit-learn, Matplotlib
  - **R:** Statistical and visualization packages for data analysis
  - **C++/Rust:** Custom implementations for efficient DNA compression
  - **JupyterLab:** Interactive development and analysis environment
- **Databases and Platforms:**
  - ClinVar, Ensembl, UCSC Genome Browser
  - PostgreSQL, MongoDB for structured and unstructured data storage

# Useful Websites

- [ National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov/)
- [Biopython](https://biopython.org/)
- [JupyterLab](https://jupyter.org/)
- [UCSC Genome Browser](https://genome.ucsc.edu/)

# Future Work

- **Algorithm Optimization:** Refine machine learning algorithms and explore advanced DNA compression techniques.
- **Data Comppression:** Reduce storage footprint to reduce redundancy while maintaining data integrity. 
- **Interactive Dashboard:** Build a user-friendly dashboard to display and interact with analysis results.
- **Scalability:** Investigate cloud-based solutions for handling larger datasets and real-time analysis.
