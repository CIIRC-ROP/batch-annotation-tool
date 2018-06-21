# Annotation tools a.k.a. klikatko

## Features

- Images read from csv file
- Configuration read from JSON file

## Requirements and Installation

- Tested on Ubuntu 16.04, Windows (with anaconda)

### Requirements

 - [Python 3.X](https://www.python.org)
 - [TKinter](https://docs.python.org/3.6/library/tkinter.html), GUI library,  part of standard python library.
 - [pandas](https://pandas.pydata.org/), for faster csv processing.
 - [pillow](http://python-pillow.org/), image processing.

### Installation (Linux, Windows, MacOS)


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
``` shell
pip3 install git+http://gitlab.ciirc.cvut.cz:b635/annotation_tools.git
```

## Usage (Linux)

``` shell
$ klikatko -h
```

## Usage (Windows binary)

The binnary is on grid `/mnt/projects/csbeton/annotation_tools/dist` along with sample input (`../data`) and config files.

```
$ klikatko.exe -h
$ klikatko.exe ../data/test.csv
```

## Configuration file

- Configuration is written in JSON format, with the comment extension.
- Content of the `klikatko.json`:

``` json
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
		"text":"All ok",        //           Text of the button
		"key":""                //           Keyboard shortcut
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

# Development notes

- [TKinter: Get Widget Size](https://stackoverflow.com/questions/3950687/how-to-find-out-the-current-widget-size-in-tkinter)
- [TKinter: Fullscreen](https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter)
- [TKinter: Tutorial](http://zetcode.com/gui/tkinter/)
- [TKinter: Image View Example](https://stackoverflow.com/questions/17504570/creating-simply-image-gallery-in-python-tkinter-pil#17505256)
- [TKinter: Canvas Widgets](https://www.python-course.eu/tkinter_canvas.php)
- [Comment JSON](https://commentjson.readthedocs.io/en/latest/), library for parsing commented json files.
- [Pyton vs MATLAB](https://blog.mide.com/matlab-vs-python-speed-for-vibration-analysis-free-download), read speed of csv.
- [TKinter: Two Frames Stacked](https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter)
- [atexit](https://docs.python.org/3.6/library/atexit.html), library for handling closing of the application.

## Generating windows exe

- using pyinstaller
- 
