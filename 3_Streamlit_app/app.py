import streamlit as st
import pandas as pd

def parse_fasta(fasta_string: str) -> list:
    """
    Parses a FASTA format string into a list of dictionaries.
    """
    sequences = []
    lines = fasta_string.splitlines()
    header = None
    current_sequence = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if header is not None:
                sequences.append({
                    'header': header, 
                    'sequence': "".join(current_sequence)
                })
            header = line[1:]
            current_sequence = []
        else:
            current_sequence.append(line)
    
    # Append the last sequence in the file
    if header is not None:
        sequences.append({
            'header': header, 
            'sequence': "".join(current_sequence)
        })
        
    return sequences

def calculate_gc(sequence: str) -> float:
    """
    Calculates the GC content percentage of a DNA sequence.
    """
    if not sequence:
        return 0.0
    
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    # Filter sequence to only include A, T, G, C for length calculation 
    # (to ignore newlines or whitespace if any)
    total_bases = len([base for base in sequence if base in 'ATGC'])
    
    if total_bases == 0:
        return 0.0
        
    return (g_count + c_count) / total_bases * 100

# --- Streamlit UI Configuration ---
st.set_page_config(page_title="GC-Content Calculator", page_icon="🧬")

st.title("GC-Content")

# --- Step 1: Upload Section ---
st.header("Upload a sequence in fasta format")
uploaded_file = st.file_uploader("Choose a file", type=["fasta", "fa", "txt"])

if uploaded_file:
    # Read file and decode
    string_data = uploaded_file.getvalue().decode("utf-8")
    parsed_items = parse_fasta(string_data)
    
    if parsed_items:
        st.success(f"Successfully parsed {len(parsed_items)} sequence(s).")
        for item in parsed_items:
            gc_val = calculate_gc(item['sequence'])
            st.subheader(f"Sequence: {item['header']}")
            st.info(f"GC Content: {gc_val}%")
    else:
        st.error("Invalid FASTA format.")

st.markdown("---")

# --- Step 2: Manual Input Section ---
st.header("Enter sequence")
manual_input = st.text_area(
    "Paste DNA sequence here:", 
    height=200,
    placeholder="ATCAAAACAACGTT..."
)

if st.button("Calculate"):
    if manual_input:
        # Clean the input (remove whitespace/newlines)
        clean_input = "".join(manual_input.split())
        gc_result = calculate_gc(clean_input)
        
        st.subheader("Result")
        st.markdown(f"**{gc_result}**")
    else:
        st.warning("Please enter a sequence first.")
