



# Repository Dispatch


## Postman

- New > HTTP > change method as POST > add URL as `https://api.github.com/repos/vMarioDev/github_actions_workshop/dispatches`
- Under the **Header** tab unselect **Accept** and create new **Accept** along with value `application/vnd.github+json`
- Navigate to **Autorization** tab paste Personal Access Token (generated from Github aettings ) as **Bearer Token**
  - The token should be appered under the **Header** tab as value of **Authorization** key
- Under the Body tab > select raw and paste the following:

```json
{"event_type":"test_result","client_payload":{"unit":false,"integration":true, "message": "My Test Value!!"}}
```

## Gitlab Workflow

- Create new workflow as `.github/workflows/repository_dispatch.yml`: 

```yml
name: Github Actions Repository Dispatch
run-name: Github Actions Events
on:
  repository_dispatch:
    types: [test_result]
  jobs:
    Get-Environemnt-Variables:
      runs-in: ubuntu-latest
      steps:
        - name: Read Environemnt Variables
          run: |
            echo "GITHUB_EVENT_NAME: ${{ github.event.name }}"
            echo "GITHUB_SHA: ${{ github.sha }}"
            echo "GITHUB_REF: ${{ github.ref }}"
            echo "GITHUB_REF_NAME: ${{ github.ref_name }}"
        - name: Parsing client payload message
          run: |
            echo $MESSAGE
          env:
            MESSAGE: ${{ github.event.client_payload.message }}
```

- Commit the changes
- The pipeline sholdn't be triggered automatically .