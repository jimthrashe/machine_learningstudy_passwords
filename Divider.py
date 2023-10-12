def split_file(input_filename, output_prefix, chunk_size):
    with open(input_filename, 'rb') as input_file:
        content = input_file.read()
    
    chunk_size_bytes = chunk_size * 1024 * 1024  # Convert chunk size to bytes
    chunks = [content[i:i+chunk_size_bytes] for i in range(0, len(content), chunk_size_bytes)]
    
    for i, chunk in enumerate(chunks):
        output_filename = f"{output_prefix}_{i + 1}.txt"
        with open(output_filename, 'wb') as output_file:
            output_file.write(chunk)
        
        print(f"Chunk {i + 1} written to {output_filename}")

if __name__ == "__main__":
    input_file = "rockyou.txt"         # Replace with the path to your input file
    output_prefix = "chunk_rockyou"    # Prefix for output file names
    chunk_size = 10                    # Size of each chunk in megabytes
    
    split_file(input_file, output_prefix, chunk_size)

