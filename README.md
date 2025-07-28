# Problem-1A
PDF Heading output as JSON

# 📄 PDF Heading Extractor

An offline tool designed to extract and hierarchically cluster headings from PDF documents, utilizing a combination of **layout**, **visual**, and **linguistic** features.

---

## 🚀 Features

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

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-heading-extractor.git
cd pdf-heading-extractor
```
### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---

## 🧠 Train the Heading Classifier
This step trains a LightGBM classifier to distinguish headings from regular text using features like font size, boldness, casing, text length, and layout differences.
```bash
python parser/train_classifier.py
```
You will see accuracy metrics and a confirmation that the trained model has been saved.

---

## ⚙️ Usage
To extract headings from a PDF, run the main script:
```bash
python main.py --pdf path/to/your/document.pdf
```
Replace path/to/your/document.pdf with the actual path to your PDF.

📝 Output:

A .json file with the document's extracted heading structure will be saved in the same folder.

Detected headings will be printed in the console.

---
## 🔍 How it Works
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

---

## 🧾 Project Structure
```bash
pdf-heading-extractor/
│
├── cluster_headings.py          # DBSCAN-based heading clustering
├── constants.py                 # Global threshold constants
├── extract_features.py          # Text and layout element extractor
├── extract_headings.py          # Heading identification and level assignment
├── feature_engineering.py       # Feature generator for classifier
├── header_footer_removal.py     # Optional: Removes repeated headers/footers
├── language_utils.py            # Text language detection
├── layout_utils.py              # Heading-likeness helper functions
├── main.py                      # Main execution script
├── model_utils.py               # Classifier and graph helpers
├── requirements.txt             # All dependencies
├── semantic_graph.py            # Builds semantic heading graph
├── train_classifier.py          # Trains and saves LightGBM model
└── visual_debugger.py           # Visualize layout elements for debugging

```

---

### 📄 License

This project is licensed under the MIT License.




