# graphql vs rest
Today we're going to talk about GraphQL vs REST and help you understand the differences between the two.

First, let's start with REST. REST stands for Representational State Transfer and it's a way of building APIs that use HTTP requests to GET, POST, PUT, and DELETE data. REST has been around for a while now and it's widely used in the industry. It's simple to understand, easy to implement, and it works well for most use cases.

Now let's talk about GraphQL. GraphQL is a newer technology that was developed by Facebook in 2012. It's a query language that allows you to ask for exactly what you need from an API. With GraphQL, you can specify the data fields you want to retrieve and get them all in one request. This means that you can reduce the number of requests needed to get all the data you need.

So what are the main differences between GraphQL and REST? Well, one of the biggest differences is how they handle data retrieval. With REST, each endpoint returns a fixed set of data fields. This means that if you need additional data, you have to make another request to get it. With GraphQL, on the other hand, you can specify exactly what data fields you want in your query and get them all in one request.

Another difference is how they handle versioning. With REST APIs, versioning is typically done by adding a version number to the URL or using custom headers. This can lead to confusion and complexity as different versions of an API are released over time. With GraphQL, versioning is built into the schema itself which makes it easier to manage changes over time.

So which one should you use? Well, it really depends on your specific use case. If your API needs are simple and straightforward, REST might be the way to go. But if you need more flexibility and want to reduce the number of requests needed to get all your data, GraphQL might be a better fit.

In conclusion, both GraphQL and REST have their strengths and weaknesses. It's important to understand the differences between them so that you can choose the right technology for your project.

#

Example for using GitHub REST API in Python:

```python
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
```

Example for using GitHub GraphQL API in Python:

```python
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
```
