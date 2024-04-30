import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    parsed_url = urlparse(url)

    # Quantity features
    qty_dot_url = url.count('.')
    qty_hyphen_url = url.count('-')
    qty_underline_url = url.count('_')
    qty_slash_url = url.count('/')
    qty_questionmark_url = url.count('?')
    qty_equal_url = url.count('=')
    qty_at_url = url.count('@')
    qty_and_url = url.count('&')
    qty_exclamation_url = url.count('!')
    qty_space_url = url.count(' ')
    qty_tilde_url = url.count('~')
    qty_comma_url = url.count(',')
    qty_plus_url = url.count('+')
    qty_asterisk_url = url.count('*')
    qty_hashtag_url = url.count('#')
    qty_dollar_url = url.count('$')
    qty_percent_url = url.count('%')
    qty_tld_url = len(parsed_url.netloc.split('.')[-1])
    length_url = len(url)

    # Domain features
    domain = parsed_url.netloc.split('@')[-1]
    qty_dot_domain = domain.count('.')
    qty_hyphen_domain = domain.count('-')
    qty_underline_domain = domain.count('_')
    qty_slash_domain = domain.count('/')
    qty_questionmark_domain = domain.count('?')
    qty_equal_domain = domain.count('=')
    qty_at_domain = domain.count('@')
    qty_and_domain = domain.count('&')
    qty_exclamation_domain = domain.count('!')
    qty_space_domain = domain.count(' ')
    qty_tilde_domain = domain.count('~')
    qty_comma_domain = domain.count(',')
    qty_plus_domain = domain.count('+')
    qty_asterisk_domain = domain.count('*')
    qty_hashtag_domain = domain.count('#')
    qty_dollar_domain = domain.count('$')
    qty_percent_domain = domain.count('%')
    qty_vowels_domain = sum(1 for char in domain if char in 'aeiouAEIOU')
    domain_length = len(domain)
    domain_in_ip = domain.replace('.', '').isdigit()
    server_client_domain = parsed_url.netloc in parsed_url.path

    # Encode categorical variables
    domain_in_ip_encoded = 1 if domain_in_ip else 0
    server_client_domain_encoded = 1 if server_client_domain else 0

    # Directory features
    path = parsed_url.path
    qty_dot_directory = path.count('.')
    qty_hyphen_directory = path.count('-')
    qty_underline_directory = path.count('_')
    qty_slash_directory = path.count('/')
    qty_questionmark_directory = path.count('?')
    qty_equal_directory = path.count('=')
    qty_at_directory = path.count('@')
    qty_and_directory = path.count('&')
    qty_exclamation_directory = path.count('!')
    qty_space_directory = path.count(' ')
    qty_tilde_directory = path.count('~')
    qty_comma_directory = path.count(',')
    qty_plus_directory = path.count('+')
    qty_asterisk_directory = path.count('*')
    qty_hashtag_directory = path.count('#')
    qty_dollar_directory = path.count('$')
    qty_percent_directory = path.count('%')
    directory_length = len(path)

    # File features
    filename = path.split('/')[-1]
    qty_dot_file = filename.count('.')
    qty_hyphen_file = filename.count('-')
    qty_underline_file = filename.count('_')
    qty_slash_file = filename.count('/')
    qty_questionmark_file = filename.count('?')
    qty_equal_file = filename.count('=')
    qty_at_file = filename.count('@')
    qty_and_file = filename.count('&')
    qty_exclamation_file = filename.count('!')
    qty_space_file = filename.count(' ')
    qty_tilde_file = filename.count('~')
    qty_comma_file = filename.count(',')
    qty_plus_file = filename.count('+')
    qty_asterisk_file = filename.count('*')
    qty_hashtag_file = filename.count('#')
    qty_dollar_file = filename.count('$')
    qty_percent_file = filename.count('%')
    file_length = len(filename)

    # Parameters features
    params = parsed_url.query
    qty_dot_params = params.count('.')
    qty_hyphen_params = params.count('-')
    qty_underline_params = params.count('_')
    qty_slash_params = params.count('/')
    qty_questionmark_params = params.count('?')
    qty_equal_params = params.count('=')
    qty_at_params = params.count('@')
    qty_and_params = params.count('&')
    qty_exclamation_params = params.count('!')
    qty_space_params = params.count(' ')
    qty_tilde_params = params.count('~')
    qty_comma_params = params.count(',')
    qty_plus_params = params.count('+')
    qty_asterisk_params = params.count('*')
    qty_hashtag_params = params.count('#')
    qty_dollar_params = params.count('$')
    qty_percent_params = params.count('%')
    params_length = len(params)
    tld_present_params = 1 if '.' in params else 0

    # Other features
    qty_params = len(params.split('&'))
    email_in_url = 1 if '@' in url else 0
    # You might need to add more features here depending on your requirements

    # Combine features into a dictionary
    features_dict = {
        'qty_dot_url': qty_dot_url,
        'qty_hyphen_url': qty_hyphen_url,
        'qty_underline_url': qty_underline_url,
        'qty_slash_url': qty_slash_url,
        'qty_questionmark_url': qty_questionmark_url,
        'qty_equal_url': qty_equal_url,
        'qty_at_url': qty_at_url,
        'qty_and_url': qty_and_url,
        'qty_exclamation_url': qty_exclamation_url,
        'qty_space_url': qty_space_url,
        'qty_tilde_url': qty_tilde_url,
        'qty_comma_url': qty_comma_url,
        'qty_plus_url': qty_plus_url,
        'qty_asterisk_url': qty_asterisk_url,
        'qty_hashtag_url': qty_hashtag_url,
        'qty_dollar_url': qty_dollar_url,
        'qty_percent_url': qty_percent_url,
        'qty_tld_url': qty_tld_url,
        'length_url': length_url,
        'qty_dot_domain': qty_dot_domain,
        'qty_hyphen_domain': qty_hyphen_domain,
        'qty_underline_domain': qty_underline_domain,
        'qty_slash_domain': qty_slash_domain,
        'qty_questionmark_domain': qty_questionmark_domain,
        'qty_equal_domain': qty_equal_domain,
        'qty_at_domain': qty_at_domain,
        'qty_and_domain': qty_and_domain,
        'qty_exclamation_domain': qty_exclamation_domain,
        'qty_space_domain': qty_space_domain,
        'qty_tilde_domain': qty_tilde_domain,
        'qty_comma_domain': qty_comma_domain,
        'qty_plus_domain': qty_plus_domain,
        'qty_asterisk_domain': qty_asterisk_domain,
        'qty_hashtag_domain': qty_hashtag_domain,
        'qty_dollar_domain': qty_dollar_domain,
        'qty_percent_domain': qty_percent_domain,
        'qty_vowels_domain': qty_vowels_domain,
        'domain_length': domain_length,
        'domain_in_ip': domain_in_ip,
        'server_client_domain': server_client_domain,
        'domain_in_ip_encoded': domain_in_ip_encoded,
        'server_client_domain_encoded': server_client_domain_encoded,
        'qty_dot_directory': qty_dot_directory,
        'qty_hyphen_directory': qty_hyphen_directory,
        'qty_underline_directory': qty_underline_directory,
        'qty_slash_directory': qty_slash_directory,
        'qty_questionmark_directory': qty_questionmark_directory,
        'qty_equal_directory': qty_equal_directory,
        'qty_at_directory': qty_at_directory,
        'qty_and_directory': qty_and_directory,
        'qty_exclamation_directory': qty_exclamation_directory,
        'qty_space_directory': qty_space_directory,
        'qty_tilde_directory': qty_tilde_directory,
        'qty_comma_directory': qty_comma_directory,
        'qty_plus_directory': qty_plus_directory,
        'qty_asterisk_directory': qty_asterisk_directory,
        'qty_hashtag_directory': qty_hashtag_directory,
        'qty_dollar_directory': qty_dollar_directory,
        'qty_percent_directory': qty_percent_directory,
        'directory_length': directory_length,
        'qty_dot_file': qty_dot_file,
        'qty_hyphen_file': qty_hyphen_file,
        'qty_underline_file': qty_underline_file,
        'qty_slash_file': qty_slash_file,
        'qty_questionmark_file': qty_questionmark_file,
        'qty_equal_file': qty_equal_file,
        'qty_at_file': qty_at_file,
        'qty_and_file': qty_and_file,
        'qty_exclamation_file': qty_exclamation_file,
        'qty_space_file': qty_space_file,
        'qty_tilde_file': qty_tilde_file,
        'qty_comma_file': qty_comma_file,
        'qty_plus_file': qty_plus_file,
        'qty_asterisk_file': qty_asterisk_file,
        'qty_hashtag_file': qty_hashtag_file,
        'qty_dollar_file': qty_dollar_file,
        'qty_percent_file': qty_percent_file,
        'file_length': file_length,
        'qty_dot_params': qty_dot_params,
        'qty_hyphen_params': qty_hyphen_params,
        'qty_underline_params': qty_underline_params,
        'qty_slash_params': qty_slash_params,
        'qty_questionmark_params': qty_questionmark_params,
        'qty_equal_params': qty_equal_params,
        'qty_at_params': qty_at_params,
        'qty_and_params': qty_and_params,
        'qty_exclamation_params': qty_exclamation_params,
        'qty_space_params': qty_space_params,
        'qty_tilde_params': qty_tilde_params,
        'qty_comma_params': qty_comma_params,
        'qty_plus_params': qty_plus_params,
        'qty_asterisk_params': qty_asterisk_params,
        'qty_hashtag_params': qty_hashtag_params,
        'qty_dollar_params': qty_dollar_params,
        'qty_percent_params': qty_percent_params,
        'params_length': params_length,
        'tld_present_params': tld_present_params,
        'qty_params': qty_params,
        'email_in_url': email_in_url,
        'time_response': 0,
        'domain_spf': 0,
        'asn_ip': 0,
        'time_domain_activation': 0,
        'time_domain_expiration': 0,
        'qty_ip_resolved': 0,
        'qty_nameservers': 0,
        'qty_mx_servers': 0,
        'ttl_hostname': 0,
        'tls_ssl_certificate': 0,
        'qty_redirects': 0,
        'url_google_index': 0,
        'domain_google_index': 0,
        'url_shortened': 0
    }
    df = pd.DataFrame([features_dict])
    return df


# Example usage:
url = "https://example.com/path/to/page?param1=value1&param2=value2"
features = extract_features(url)
print(features)
print(type(features))