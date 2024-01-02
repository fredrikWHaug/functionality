def replace_string_in_file(input_file, output_file, old_string, new_string):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        
        text = text.replace(old_string, new_string)
        
        with open(output_file, 'w') as file:
            file.write(text)
        
        print(f"String '{old_string}' replaced with '{new_string}' in {input_file}, and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
old_string = 'old_string'
new_string = 'new_string'

replace_string_in_file(input_file, output_file, old_string, new_string)