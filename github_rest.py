import requests

# Set the API endpoint and parameters
url = 'https://api.github.com/users/octocat/repos'
params = {'sort': 'created'}

# Send a GET request to the API endpoint with the parameters
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the names of the repositories returned by the API
    for repo in response.json():
        print(repo['name'])
else:
    # Print an error message if the request failed
    print('Error: {}'.format(response.status_code))
