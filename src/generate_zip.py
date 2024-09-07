# scripts/generate_zip.py
import zipfile
import os

def write_txt_file(file_path, content):
    """Writes content to a text file."""
    with open(file_path, 'w') as f:
        f.write(content)

def zip_file(file_path, zip_file_path):
    """Zips the given file."""
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))

def main():
    # File paths
    txt_file_path = 'output.txt'
    zip_file_path = 'output.zip'
    
    # Content to write into the .txt file
    content = "This is a sample content for the text file."

    # Write to .txt file
    write_txt_file(txt_file_path, content)
    
    # Zip the .txt file
    zip_file(txt_file_path, zip_file_path)
    
    print(f"Generated {zip_file_path}")

if __name__ == "__main__":
    main()
