# Using Github Actions as a tool for webpage change notification

1. Fork this repo
1. Edit this part of `.github/workflows/pagediff.yaml`
    ```yaml
    env:  # Define diff target here
      # The page to visit
      URL: 'https://sebbacon.github.io/'
      # The XPath on the page that we're interested in
      XPATH: '/html/body/header/div/a'
      # A filename where we will save the contents of that XPath
      FILE_PATH: 'sebbacon.html'
    ```
1. Allow your action to write back to its own repo, by [following these instructions](https://stackoverflow.com/a/75308228)
1. Set up _Email Notifications_ (in the _Settings_ of your repo) to get an alert when the action fails (i.e. when there's a new diff to report)

