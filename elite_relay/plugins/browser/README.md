# Browser plugin

This plugin allows you to manipulate the system clipboard, i.e. copy
relevant text on an event.

## Actions

### Navigate

The navigate action will open a browser window to the specified URL. The URL supports templating, meaning that it can
include information in the event data.

#### Options

* **`url`** (required, string): The URL to navigate to in the browser, supports templating.
* **`focus`** (optional, bool, default `false`): Whether to focus the browser window when opening. This setting is ignored
  by most window managers, but it is included as an option.
* **`open_method`** (optional, string, default `default`): Whether to open the URL in a new tab or window, or use the browser's
  default setting, possible options are:
  * `default`: Let the browser decide
  * `window`: Open in a new window
  * `tab`: Open in a new tab

#### Example
```yaml
plugins:
  # Open the inara.cz "search nearest" page when jumping to a new system
  - plugin: browser
    action: navigate
    options:
      url: https://inara.cz/elite/nearest-stations/?formbrief=1&ps1=${data.StarSystem}
      open_method: tab
```
