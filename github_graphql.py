import requests

# Set the GraphQL endpoint and query string
url = 'https://api.github.com/graphql'
query = """
query {
  repository(owner:"octocat", name:"Hello-World") {
    issues(last:10, states:CLOSED) {
      edges {
        node {
          title
          url
        }
      }
    }
  }
}
"""

# Set the authorization header with a personal access token (PAT)
headers = {'Authorization': 'Bearer <PAT>'}

# Send a POST request to the GraphQL endpoint with the query and headers
response = requests.post(url, json={'query': query}, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the titles and URLs of closed issues in the repository returned by the API
    for issue in response.json()['data']['repository']['issues']['edges']:
        print(issue['node']['title'], issue['node']['url'])
else:
    # Print an error message if the request failed
    print('Error: {}'.format(response.status_code))
