# Clipboard plugin

This plugin allows you to manipulate the system clipboard, i.e. copy
relevant text on an event.

## Actions

### Copy

The copy action will copy a string to your system's clipboard whenever it is triggered.
This text supports templating, meaning that it can include information in the event data.

#### Options

* **`text`** (required, string): The text to copy to the clipboard, supports templating.
* **`strip`** (optional, bool, default `true`): Whether to strip whitespace from the text when copying to clipboard.

#### Example
```yaml
plugins:
  # Copy the star system name to the clipboard after a jump
  - plugin: clipboard
    action: copy
    filters:
      - key: type
        eq: FSDJump
    options:
      text: ${data.StarSystem}
```
