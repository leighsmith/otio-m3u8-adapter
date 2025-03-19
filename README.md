# OpenTimelineIO m3u8 Plugin

This is an OpenTimelineIO adapter plugin converting OTIO files to extended
[m3u/m3u8](https://en.wikipedia.org/wiki/M3U) multimedia playlist files. This
repository is derived from the OTIO adapter plugin template that expands OpenTimelineIO
through its plugin system. There are two adapters: `m3u8` which converts a single track
OpenTimelineIO file to a single `.m3u8` playlist, and `m3u8d` which converts a multiple track
OpenTimelineIO file to a directory of `.m3u8` playlists, consisting of an audio track
playlist and a video track playlist, each ordered by clip start time.

See the OpenTimelineIO [documentation](https://opentimelineio.readthedocs.io/en/latest/index.html)
for more information about OpenTimelineIO in general and
[here](https://opentimelineio.readthedocs.io/en/latest/tutorials/write-an-adapter.html) for documentation about **adapters**.

## Licensing

This template repository is licensed under
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
or the [MIT License](https://opensource.org/licenses/MIT).

## Naming convention

The repository and package names conform to the convention recommended by OpenTimelineIO:

* Repository and uploaded package name (using hyphens): `otio-m3u8-adapter`
* Python package name (using underscores): `otio_m3u8_adapter`

## Folder structure
Below is the included file and folder tree that comes with the plugin template.
  
```
├── LICENSE-APACHE-20
├── LICENSE.md
├── LICENSE-MIT
├── pyproject.toml
├── README.md
├── src
│   └── otio_m3u8_adapter
│       ├── plugin_manifest.json
│       ├── adapters
│       │   ├── __init__.py
│       │   ├── m3u8_adapter.py
│       │   ├── m3u8d_adapter.py
├── tests
    └── test_my_plugin.py
```

> **TIP!** Make sure to add a descriptive docstring at the top of your plugin files, so they 
register properly and inform users of what they do.

## Testing your plugin during development
```
# In the root folder of the repo
pip install -e .

# Check if plugin installed correctly
otiopluginfo m3u8_adapter
otiopluginfo m3u8d_adapter

# Test an adapter for instance
otioconvert -i some_timeline.otio -o some_timeline.ext
```


### Build your package locally
You might want to build the `otio_m3u8_adapter` package locally to check that everything is behaving
the way you intended.
To do so, simply run `python -m build` in the root of your repo.
This will by default produce wheel and source packages in a "dist" folder.
>**NOTE!** You might need to add the "build" package to your virtualenv (`pip install build`).

For more info on building packages, please refer to the python's 
[packaging](https://packaging.python.org/en/latest/overview/) guide 
and/or the [build](https://pypa-build.readthedocs.io/en/stable/) documentation.


## Unit tests

It's always a good idea to write unit tests for you code.
Please provide tests that run against supported versions of python and 
OpenTimelineIO.


## Github Actions

A set of simple automation scripts are available in the `.github/workflows` folder.
* `ci.yaml` - runs unit tests
* `create_draft_release` - when a tag is pushed, it creates a draft for a release
* `deploy_package.yaml` - simple packing an publishing of a plugin package. 
  Make sure you have a valid token for your PyPi user added to your repos 
  [secrets](https://docs.github.com/es/actions/reference/encrypted-secrets).


## Upload to PyPi

Should you want to release your package to the world and let others reap the 
fruits of your labor, an example "pyproject.toml" is provided which should guide you 
on the way towards publishing your plugin on PyPi.
There's also a sample github-action provided to help automate the process.

Manual steps for creating a simple package and upload to (test)PyPi:
```
# Requires "build" and "twine" package installed in your virtualenv 
python -m build
twine upload --repository testpypi dist/*
```
Please check out python's [docs](https://packaging.python.org/en/latest/overview/) 
for more detailed descriptions on packaging. 


## Let us know about your plugin
If you release your plugin to the public please let us know about it, so we can 
add it to our [list](https://github.com/PixarAnimationStudios/OpenTimelineIO/wiki/Tools-and-Projects-Using-OpenTimelineIO) 
of known plugins.


## Contributions

If you have any suggested changes to the template repository itself, 
please provide them via [pull request](../../pulls) or [create an issue](../../issues) as appropriate. 

All contributions back to the template repository must align with the contribution
[guidelines](https://opentimelineio.readthedocs.io/en/latest/tutorials/contributing.html) 
of the OpenTimelineIO project.
