# HTTP plugin

This plugin allows you to make an HTTP request whenever an event fires.

## Actions

### POST

The POST action will make an HTTP POST request that includes the event data as JSON in its body.

#### Options

* **`url`** (required, string): The URL to submit the POST request to.
* **`headers`** (optional, mapping): Headers to include when submitting the POST request.
* **`query`** (optional, mapping): Query parameters to include when submitting the POST request.


#### Example
```yaml
plugins:
  - plugin: http
    action: post
    filters:
      - key: type
        eq: FSDJump
    options:
      url: http://home-assistant.local/api/webhook/abc123
      headers:
        API_KEY: def789abc
```
