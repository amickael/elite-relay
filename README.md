# Elite Relay
Elite: Dangerous Journal Event Handler

## Introduction
`elite-relay` is a small program that tracks events recorded in your [Elite: Dangerous journal file](https://elite-journal.readthedocs.io/en/latest/)
and allows you respond to them in certain ways, including:
* Sending an HTTP request with the event data, e.g. firing a webhook to a service like Home Assistant or Zapier.
* Copying text to your clipboard, e.g. the name of the star system you just jumped to.
* Opening a templated URL in your browser, e.g. opening an [Inara.cz "search nearest"](https://inara.cz/elite/nearest/)
  page when jumping to a new system.

Event handlers ("plugins") are defined in `.edr/config.yaml` located in your home directory. See the configuration spec
for examples and more information.

## Installation

### Using the MSI installer

The easiest way to install `elite-relay` is via the MSI installer included in the [latest release](https://github.com/amickael/elite-relay/releases/latest).
Simply download the file and open it, the program will then be installed to your $FOLDER folder. Open the `main.exe` file
to start it.

### Using `pip`

Alternatively, you may install `elite-relay` via Python's `pip` package manager (or any other Python package manager of your choosing):
```shell
pip install --upgrade elite-relay
```

You can now run `elite-relay` in a terminal to start the program.

## Configuring plugins

...TBD...
