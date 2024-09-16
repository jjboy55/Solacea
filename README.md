# RAGHack: Colon Cancer Decision Support System using Microsoft GraphRag

<img alt="Solacea Medium Banner" src="https://github.com/user-attachments/assets/0ec821a6-d1e2-45fb-b036-9f6767b55c7f">


## Objective
Our MVP aims to provide doctors with actionable insights to aid in **adjuvant chemotherapy (ACT)** decision-making for patients with **stage II/III colorectal cancer**. Using **ctDNA (circulating tumor DNA)** data from clinical studies, our system helps guide treatment recommendations, focusing on precision, early intervention, and personalized care.

## Problem Statement
Colorectal cancer is a leading cause of cancer-related deaths worldwide. For patients in **stage II/III colorectal cancer**, the decision to administer **adjuvant chemotherapy** is crucial but often complex. Current diagnostic methods primarily rely on imaging and physical assessment, which may not fully capture the risk of recurrence.

**Circulating tumor DNA (ctDNA)** has emerged as a highly sensitive biomarker that can detect **molecular residual disease (MRD)** post-surgery, signaling the likelihood of cancer recurrence. However, interpreting ctDNA results and integrating them into treatment decisions requires advanced tools to assist doctors.

### Challenge
Doctors need a **data-driven decision support system** to:
- Interpret **ctDNA results**.
- Assess the benefit of **adjuvant chemotherapy**.
- Make informed, personalized treatment decisions based on clinical evidence.

## Solution: The RAG-Based System
Our MVP leverages **Microsoft’s GraphRAG** approach to deliver **targeted, contextual insights** by querying medical research and clinical guidelines. Initially, the system uses data from the **BESPOKE CRC study**, which provides essential findings on the role of ctDNA in guiding chemotherapy decisions.



<img src="https://github.com/user-attachments/assets/02af1813-e4b1-4949-94ad-ddde9c7184ef" alt="Image Description">



### How It Works
1. **Input**: Doctors input relevant patient information (e.g., stage of cancer, ctDNA status).
2. **Data Retrieval**: The system queries specific research papers, clinical trials, and medical guidelines related to colorectal cancer treatment, focusing on ctDNA's predictive value.
3. **Augmentation**: Using a combination of retrieved research and contextual understanding, the system generates a **personalized treatment recommendation**.
4. **Output**: The doctor receives a tailored recommendation on whether to pursue adjuvant chemotherapy based on the patient’s ctDNA status and the best available clinical evidence.

### Example Query
**Input**:  
*"A Stage III patient is ctDNA positive post-surgery. What does the research suggest regarding adjuvant chemotherapy?"*

**Output**:  
*"For Stage III ctDNA-positive patients, adjuvant chemotherapy significantly improves disease-free survival (DFS) based on the BESPOKE CRC study. Chemotherapy is recommended to reduce recurrence risk."*

## Key Features
- **Focused Data Scope**: The MVP uses **BESPOKE CRC study** data, ensuring precision and depth in ctDNA-related decision-making.
- **Microsoft GraphRAG**: Employs Microsoft’s advanced retrieval-augmented generation approach to derive insights from clinical data and research.
- **Targeted Recommendations**: Provides **personalized guidance** based on the patient’s stage, ctDNA status, and existing clinical studies.
- **Expandable**: Future iterations will incorporate more research, case studies, and clinical guidelines for broader applicability.

## Technology Stack
- **Microsoft GraphRAG**: For advanced retrieval and augmentation.
- **Python**: For backend logic and integration.
- **Streamlit**: For creating a simple, interactive frontend interface.
- **Lancedb**: For vector-based data retrieval.
- **Docker**: For containerizing the application, ensuring portability.

## Data Source
- **Primary Data**: *Circulating tumor DNA (ctDNA) for informing adjuvant chemotherapy (ACT) in stage II/III colorectal cancer (CRC): Interim analysis of BESPOKE CRC study*.
- **Future Data**: Other relevant colorectal cancer clinical trials and studies focusing on ctDNA and chemotherapy outcomes.

## Use Case Scenarios
### Scenario 1: Patient Monitoring
A doctor inputs the ctDNA status of a post-surgery Stage II patient. The system recommends whether adjuvant chemotherapy is necessary, based on the patient's risk of recurrence and clinical data from the BESPOKE CRC study.

### Scenario 2: Treatment Adjustment
For a ctDNA-positive patient undergoing chemotherapy, the doctor queries whether continuing treatment is beneficial. The system provides insights based on data regarding ctDNA clearance and recurrence patterns from clinical studies.

## Next Steps
- **Data Expansion**: Incorporate additional clinical studies and guidelines to improve the range of recommendations.
- **User Feedback**: Gather feedback from doctors during the MVP phase to improve the interface and recommendation accuracy.
- **Clinical Validation**: Collaborate with medical experts to ensure the system’s recommendations align with clinical best practices.

## Conclusion
Our MVP is a lightweight, focused tool designed to **support doctors** in making informed decisions about adjuvant chemotherapy in colorectal cancer patients, based on ctDNA insights. By starting small with a specific data set, we aim to create a scalable solution that can expand to incorporate a wider body of clinical evidence over time.
