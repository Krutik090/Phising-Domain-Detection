import pandas as pd
from urllib.parse import urlparse
import re

# Function to extract features from URL
def extract_features(url):
    # Parse URL
    parsed_url = urlparse(url)
    
    # Extract domain and directory
    domain = parsed_url.netloc
    directory = parsed_url.path
    
    # Count occurrences of special characters in URL
    special_characters = {
        ".": "dot",
        "-": "hyphen",
        "_": "underline",
        "/": "slash",
        "?": "questionmark",
        "=": "equal",
        "@": "at",
        "&": "and",
        "!": "exclamation",
        " ": "space",
        "~": "tilde",
        ",": "comma",
        "+": "plus",
        "*": "asterisk",
        "#": "hashtag",
        "$": "dollar",
        "%": "percent"
    }
    special_character_counts_url = {char: url.count(char) for char in special_characters.keys()}
    
    # Count occurrences of special characters in domain
    special_character_counts_domain = {char: domain.count(char) for char in special_characters.keys()}
    
    # Count vowels in domain
    vowels_count_domain = sum(1 for char in domain if char.lower() in 'aeiou')
    
    # Length of domain
    domain_length = len(domain)
    
    # Check if domain is an IP address
    domain_in_ip = bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', domain))
    
    # Count occurrences of special characters in directory
    special_character_counts_directory = {char: directory.count(char) for char in special_characters.keys()}
    
    # Length of directory
    directory_length = len(directory)
    
    # Extract file name from directory
    file_name = directory.split('/')[-1]
    
    # Count occurrences of special characters in file name
    special_character_counts_file = {char: file_name.count(char) for char in special_characters.keys()}
    
    # Length of file name
    file_length = len(file_name)
    
    # Extract parameters from directory
    params = urlparse(url).query
    tld_present_params = bool(re.search(r'\.[a-zA-Z]{2,}$', params))
    
    # Count occurrences of special characters in parameters
    special_character_counts_params = {char: params.count(char) for char in special_characters.keys()}
    
    # Length of parameters
    params_length = len(params)
    
    # Check if email is present in URL
    email_in_url = bool(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', url))
    
    # You can continue adding more features here
    
    # Return dictionary of features
    return {
        **special_character_counts_url,
        **special_character_counts_domain,
        'qty_vowels_domain': vowels_count_domain,
        'domain_length': domain_length,
        'domain_in_ip': domain_in_ip,
        **special_character_counts_directory,
        'directory_length': directory_length,
        **special_character_counts_file,
        'file_length': file_length,
        **special_character_counts_params,
        'params_length': params_length,
        'tld_present_params': tld_present_params,
        'qty_params': len(params.split('&')),  # Assuming parameters are separated by '&'
        'email_in_url': email_in_url
        # Add more features as needed
    }

# Example URL
example_url = "https://www.example.com/path/to/file?param1=value1&param2=value2"

# Extract features from example URL
features = extract_features(example_url)

# Create DataFrame from features
features_df = pd.DataFrame([features])

# Display DataFrame
print(features_df
      )
