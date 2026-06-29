# Medical Software Development - Course Exercises

This repository contains the completed exercises for the **Master Medical Informatics** course "Medical Software Development" at FHNW Life Science Technologies. All exercises contribute to the final grade.

## Project Overview



### 📂 Exercise 01: Gene Analyzer

**Type:** Development (Command line tool)  
**Language:** Python 
**Description:** A CLI tool that downloads and processes the NCBI `gene_info.gz` dataset to analyze global gene statistics. It outputs the MD5 checksum of the input file and answers specific metrics regarding total gene counts, Homo Sapiens data, and gene type distributions. 
**Core Questions Addressed:** Robustness of input handling, software documentation, tracking changes, and deployment/update strategies for clients.

### 📂 Exercise 02: GC Content Computation 
**Type:** Development 
**Language:** Python 
**Description:** Inspired by the Theralizumab (CD28 gene) first-in-human trial , this script calculates the GC-content percentage of a given DNA sequence provided in FASTA format.
**Core Questions Addressed:** Parsing FASTA standards, handling multi-sequence files, handling case sensitivity (upper/lowercase text), and code behavior with invalid files.

### 📂 Exercise 03: Streamlit Web Application 
**Type:** Development (Web Application) 
**Language:** Python (Streamlit framework)  
**Description:** Transforms the GC-computation backend from Exercise 02 into an interactive web application. Users can either upload `.fasta` files via drag-and-drop or directly paste raw DNA sequences into a text box to receive real-time GC-content analytics.

### 📂 Exercise 04: Project Planning – Cost & Time Estimation

**Type:** Project Planning 
**Description:** A conceptual planning exercise focused on establishing a cost and time estimation framework for building a mobile "Sensor Data Collector" application. The requirements include sensor selection mechanics, dynamic UI state handling (Start/Stop capturing modes), and data transmission to a backend service.

### 📂 Exercise 05: System Requirements Specification (SRS)
 
**Type:** Requirements Engineering / Quality Assurance 

**Description:** An analytical evaluation of a Training Management System (TMS) SRS document. It evaluates functional requirements against industry criteria (completeness, accuracy, ambiguity, traceability, and testability) and assesses technical compliance regarding data security and system architecture.


### 📂 Exercise 06: Python OOP & Design Patterns (DNA2Protein)
 
**Type:** OOP Introduction / Software Design  
**Language:** Python 
**Description:** An object-oriented program mapping DNA to RNA Protein


### 📂 Exercise 08: Android Sensor Overview

**Type:** Mobile Development / Android Basics 

**Language:** Java (Gradle build system, JDK 17) 
**Description:** Compiling, deploying, and testing an Android native application to query hardware-level sensors.
**Core Questions Addressed:** Analyzing smartphone sensor arrays to identify specific kinetic sensors (e.g., accelerometers/gyroscopes) suitable for clinical applications, such as tracking tremors in Parkinson's disease.

## Technical Prerequisites

To build and run the code within this repository, ensure you have the following environments configured:
**Python 3.x** (with `streamlit` installed for Ex. 03) 
**Java JDK 17** 
**Gradle** & **Android Studio** (with Android SDK configured for Ex. 08)
