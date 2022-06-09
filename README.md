<h1 align="center">
  <a href="https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader">
    <img src="https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader/src/logo.png" alt="Logo" width="125" height="125">
  </a>
</h1>

<div align="center">
  Eduscope Video Downloader
  <br />
  <br />
  <a href="https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader/issues/new?assignees=&labels=bug&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader/issues/new?assignees=&labels=enhancement&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

![followers](https://img.shields.io/github/followers/notnavindu?style=flat-square)

![made with heart by @notnavindu](https://img.shields.io/badge/made%20with%20%E2%99%A5%20by-@notnavindu-ff1414.svg?style=flat-square)](https://github.com/notnavindu)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation Guide (For normal people)](#installation-guide-for-normal-people)
  - [Installation Guide (For tech savvy people)](#installation-guide-for-tech-savvy-people)
  - [If you run into issues...](#if-you-run-into-issues)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

</details>

---

## About

<table>
<tr>
<td>

⚠️ This is still in beta

Basically, a python script to download eduscope videos (+ easy integration with [SLIIT Eduscope Mods Browser Extension](TODO:)). The download script is a modified version of [this script](https://github.com/dinushka114/eduscope-downloader)

**Demo**:

TODO:

</td>
</tr>
</table>

### Built With

- Python
- ffmpeg
- Chrome Native Messaging

## Getting Started

### Prerequisites

- It is highly recommended to install the latest version of [SLIIT Eduscope Mods Browser Extension](TODO:) before using this script. Chrome extension integration only works on windows. If you just need the downloader, check out the minimal script section. TODO:

### Installation Guide (For normal people)

1. Download the latest release (It's a zip file)
2. Unzip/extract the file to where you want to install this software. _(Don't move the extracted files after you `install` it completely)_
3. Double click the `install.bat` file.
4. Open the `config.ini` file using the notepad.
5. Add the names of the courses you follow along with the path of the folder you want to download lectuers. _(You can get the file path from file explorer and paste it here)_

Copy the path like this:

![path](docs/folder_path.png)

Add it to `config.ini` like this:

![config](docs/config.png)

6. You can adjust the configuration however you want. Here are some sample configuration examples

example 1:

```ini
[folders]
software-architecture = S:\SLIIT\Y3S1\SA\Lecs
distributed-systems = S:\SLIIT\Y3S1\DS\Lecs
sepqm = S:\SLIIT\Y3S1\SEPQM\Lecs
```

example 2:

```ini
[folders]
Y3S1 - Software Architecture = S:\SLIIT\Y3S1\SA\Lecs
Y3S1 - Distributed Systems = S:\SLIIT\Y3S1\DS\Lecs
Y3S1 - SEPQM = S:\SLIIT\Y3S1\SEPQM\Lecs
```

7. Click "Download video" from the Eduscope Mods Google Chrome extension

### Installation Guide (For tech savvy people)

1. Download the zip
2. Run `install.bat`
3. Configure using `config.ini`
4. Regenerate SHA256 nuclear launch codes
5. Click "Download Video" on Eduscope Mods Chrome extension
6. Well, that's it.

### If you run into issues...

- Feel free to DM me on [IG](https://instagram.com/notnav.jpg) or create a new [issue](https://github.com/notnavindu/SLIIT-Eduscope-Video-Downloader/issues)

## Roadmap

- **_GUI_**: No plans for GUI because CLI is way cooler 😎
- Feature requests are welcome

## Contributing

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.
