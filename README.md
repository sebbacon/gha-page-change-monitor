# Using Github Actions as a tool for webpage change notification

Want to get an email when a certain bit of text on a page has changed?

Use Github Actions!

1. Fork this repo
1. Edit the top bit of `.github/workflows/pagediff.yaml`:
    ```yaml
    env:  # Define diff target here
      # The page to visit
      URL: 'https://sebbacon.github.io/'
      # The XPath for the content you're interested in
      # (try right-clicking the element in the inspector in Chromium)
      XPATH: '/html/body/header/div/a'
      # A filename where we will save the contents of that XPath
      FILE_PATH: 'sebbacon.html'
    ```
1. Set up _Email Notifications_ (in the _Settings_ of your repo) to get an alert when the action fails (i.e. when there's a new diff to report)


Thanks to [Dave](http://evansd.net/) for pointing out this one wierd trick some years ago.
