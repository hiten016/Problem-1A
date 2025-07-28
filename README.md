# Problem-1A - PDF Heading Extractor

An offline tool designed to extract and hierarchically cluster headings from PDF documents, utilizing a combination of **layout**, **visual**, and **linguistic** features.

---
##  Project Structure
```bash
pdf-heading-extractor/
│
├── cluster_headings.py          
├── constants.py                
├── extract_features.py         
├── extract_headings.py         
├── feature_engineering.py      
├── header_footer_removal.py     
├── language_utils.py            
├── layout_utils.py              
├── main.py                      
├── model_utils.py               
├── requirements.txt             
├── semantic_graph.py           
├── train_classifier.py          
└── visual_debugger.py           

```

##  Features

- **Comprehensive Heading Detection**  
  Handles a variety of heading styles, including multi-column layouts, multilingual content, and styled headings (bold, large, indented).

- **Numbered Section Recognition**  
  Capable of detecting numbered sections such as `1`, `1.1`, `1.2`, etc.

- **Layout Awareness**  
  Leverages `pdfminer.six` (or similar tools) to understand the PDF's layout and text structure.

- **Hierarchical Clustering**  
  Groups similar headings together to establish a nested, logical structure.

- **Semantic Linking**  
  Creates semantic connections between extracted headings to enhance document understanding.

---

## Edge Case Handling
The PDF Heading extractor works well on the following edge cases. We have added the sample dataset used for testing it all all the following edge cases <br> 

Add detection for  indentation, or all-uppercase, variable font size <br>
Use positional heuristics (e.g., center-aligned + large + bold = H1). <br>
Multicolumn pdfs (academic papers, legal documents,reports) <br>
Multilingual pdfs <br>
Numbered headings (1,1.1, 1.2)  <br>


##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-heading-extractor.git
cd pdf-heading-extractor
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
---

## Docker Setup
### Build the Docker image
docker build --platform linux/amd64 -t pdf-processor .

### Test with sample data
docker run --rm -v $(pwd)/sample_dataset/pdfs:/app/input:ro -v $(pwd)/sample_dataset/outputs:/app/output --network none pdf-processor


##  Train the Heading Classifier
This step trains a LightGBM classifier to distinguish headings from regular text using features like font size, boldness, casing, text length, and layout differences.
```bash
python parser/train_classifier.py
```
You will see accuracy metrics and a confirmation that the trained model has been saved.

---

##  How it Works
1. Layout Extraction
   
Uses pdfminer.six to extract text elements (font size, coordinates, etc.) and organizes them into logical blocks.

2. Feature Engineering
   
Each text line is transformed into numerical features based on font size, boldness, casing, length, heading number pattern, etc.

3. Heading Classification
   
A LightGBM model predicts which elements are headings using the engineered features.

4. Heading Filtering & Level Assignment
   
Applies rules (length, font size threshold, punctuation) to clean candidate headings and assigns levels (H1, H2, etc.) based on font size hierarchy.

5. Semantic Graph Construction
    
Builds a directed graph using networkx, connecting heading nodes sequentially to represent document flow.

6. Language Detection (Optional)
    
Utilizes langdetect to detect text language, which can be extended for multilingual improvements.

## Constraints Satisfied

- **Execution Time**: Must complete processing within **10 seconds** for a **50-page PDF**.
- **Model Size**: If using a model, its total size must be **≤ 200MB**.
- **Network Access**: **No internet access** is allowed during execution.
- **Runtime Environment**:
  - Must run entirely on **CPU** (amd64 architecture).
  - Target system has **8 CPUs** and **16 GB RAM**.

---

### 📄 License

This project is licensed under the MIT License.

---
## Contributors: 
Team Quantum Quarks LNMIIT Jaipur <br>
Hiten Mahajan <br> 
Pratyaksh Agrawal <br>
Sakash Srivastava <br>



