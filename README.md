## PLH
### Python Linux Helper

A lightweight command-line tool written in Python, designed to automate everyday Linux tasks.

## Features

- Interactive terminal interface
- Built-in command system
- Configuration file management
- Execute shell commands from configuration files
- Lightweight implementation

## Download

Download the latest release from the [GitHub Releases](../../releases) page.

Download the Linux executable named `plh`.

## Running PLH

Open a terminal in the directory where you downloaded `plh` and run:

```bash
chmod +x plh
./plh
```

No separate Python installation is required.

## Installation

To make PLH available as a terminal command:

```bash
mkdir -p ~/.local/bin
install -m 755 plh ~/.local/bin/plh
```

If `~/.local/bin` isn't in your PATH, add it:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

You can now launch PLH from anywhere:

```bash
plh
```

## Requirements

- Linux
- x86_64 architecture (for the provided executable)

## Project Status

**Version:** 1.0.0-pre1  
**Status:** Pre-release

PLH is currently under development. Features and functionality may change between releases.

## Source Code

The source code is available in this repository.

## License

See the [LICENSE](LICENSE) file for licensing information.
