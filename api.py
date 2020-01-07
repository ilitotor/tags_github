import requests

headers = {"Authorization": "Bearer 91b67cb466f3d6070b5d9883e04b2e22523e2956"}

def run_query(user_name):  # A simple function to use requests.post to make the API call. Note the json= section.
    query = """  {
                user(login: "%s") {
                  id
                  login
                  starredRepositories(last: 100) {
                    edges {
                      node {
                        id
                        name
                        primaryLanguage {
                          name
                        }
                        description
                        url
                      }
                    }
                  }
                }
              }
               """ % (user_name)
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))