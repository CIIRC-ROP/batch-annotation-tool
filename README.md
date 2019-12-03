# Batch Annotation Tools (klikatko)

Simple tool for fast annotation and reanotation of large amount of images. Written in python usng Tk library, thoroughly configurable using JSON file, works on top of sqlite database.

![fig](fig/screencap.gif)

## Requirements and Installation

- Tested on Archlinux, Ubuntu 16.04, Windows (with anaconda)

## Requirements

 - [Python 3.X](https://www.python.org)
 - [TKinter](https://docs.python.org/3.6/library/tkinter.html), GUI library,  part of standard python library.
 - [pandas](https://pandas.pydata.org/), for faster csv processing.
 - [pillow](http://python-pillow.org/), image processing.

## Installation (Linux, Windows, MacOS)

From source
```shell
$ git clone git@gitlab.ciirc.cvut.cz:b635/annotation_tools.git
# or
$ git clone http://gitlab.ciirc.cvut.cz/b635/annotation_tools.git
$ cd annotation_tools
$ pip3 install . # normal installation
# or
$ pip3 install -e . # for development
```

Directly from git
```shell
pip3 install git+https://github.com/CIIRC-ROP/batch-annotation-tool.git
```

## Usage (Linux)

- See the [User Guide](user_guide.md)

```
$ klikatko -h

klikatko: Batch Annotation Tool

Usage:
  klikatko -h | --help
  klikatko [options] <imfile> <attfile> <outfile>

Options:
  -h, --help
  --config CONFIG    Specifi config file
  --debug            Run in debug mode
  --fullscreen       Display in fullscreen
  --table TABLE      Table prefix [default: test]
  --attr ATTR        Attribute to edit [default: backpack]
  --filter FILTER    Where query

The filter follows the SQL WHERE syntax, uses a,b prefixes, where a is for the
outpud db and b is for input attribute db. Some examples:

    klikatko im.db att.db out.db --filter b.backpack=1
    klikatko im.db att.db out.db --filter "b.backpack=1 OR a.backpack=1"
```

## Configuration file

- Configuration is written in JSON format, with the comment extension.
- Content of the `klikatko.json`:

```
{

    // User interface
    "zoom_default":0.2, // Default image zoom when the app starts
    "zoom_min":0.1,     // Minimal image zoom
    "zoom_max":1.2,     // Maximal image zoom
    "zoom_step":0.2,    // Zoom step for zoom in and zoom out
    "image_border":2,   // Size of the color border of the image
    "image_padding":2,  // Space between images
    "geometry":"1000x1000+200+200", // Initial geometry of the window (HxH+x+y)
    "background":"black", // Grid background

    // Annotation file
    "csv_sep":";",      // Column separator for cvs parsing
    "csv_decimal":".",  // Decimal separator for cvs parsing
    "column_path":0,    // Column of the image path, starting from 0
    "column_in":1,      // Input columnt for annotation, -1 for none
    "column_out":2,     // Output column for annotation
    "defaul_class":1,   // Value of the default class

    // Annotation
    "classes":[
	{
	    "name":"ok",                // Name of the class
	    "value":1,                  // Value that is used to represent a class
	    "default":true,             // Select default class
	    "color":"green",            // Color used to mark this class
	    "button_all":{              // Optional: Button to mark all visible images by this class
		"text":"All ok",            // Text of the button
		"key":""                    // Keyboard shortcut
	    },
	    "button_select":{
		"text":"Select ok",
		"key":""
	    }

	},
	{
	    "name":"bad",
	    "value":254,
	    "defautl":false,
	    "color":"red",
	    "button_all":{
		"text":"All bad",
		"key":""
	    },
	    "button_select":{
		"text":"Select bad",
		"key":""
	    }
	}
    ]
}

```

