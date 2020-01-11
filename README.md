# Batch Annotation Tools (klikatko)

A simple tool for fast annotation and reannotation of a large number of images. Written in python using Tk library, thoroughly configurable using JSON file, works on top of SQLite database. The program presents images from the input database to the user together with the original annotation when is defined. The original annotation is read from another input database table. The user can change the annotation of selected images. Then the updated annotation is written into the output database table. Images with annotation written in the output table are no longer presented to the user. Users can break the annotation process and return back to annotate the rest of the images.

![fig](fig/screencap.gif)

## Supported OS

- Tested on Archlinux, Ubuntu 16.04, Windows (with anaconda)

## Requirements

 - [Python 3.X](https://www.python.org)
 - [TKinter](https://docs.python.org/3.6/library/tkinter.html), GUI library,  part of standard python library.
 - [pandas](https://pandas.pydata.org/), for faster csv processing.
 - [pillow](http://python-pillow.org/), image processing.

## Installation (Linux, Windows, MacOS)

From source
```shell
$ git clone https://github.com/CIIRC-ROP/batch-annotation-tool.git
$ cd annotation_tools
$ pip3 install . # normal installation
# or
$ pip3 install -e . # for development
```

Directly from git
```shell
pip3 install git+https://github.com/CIIRC-ROP/batch-annotation-tool.git
```
## Model and structure of data

The program work with three database tables in three databased:

- Image database table - contains the annotated images
- Attribute database table - define original annotation
- Output database table - new user annotation 

The images are read from the image table and presented to the user together with the original annotations. The original annotations are read from the attribute table. The user makes changes of annotations and the results are written as a new annotation into the output table. The images are presented to the user according to the order defined by column "_order" in the output table. The order is generated when annotation of the data are first time started.

Names of the corresponding databases are defined by command line arguments <imfile>, <attfile> and <outfile>. Names of the three tables are partially defined by the command line option "--table TABLE". The TABLE option represents the prefix of the names of the tables. All tables contain the column "id" (integer) which represents a common reference key.

### Structure of the tables:

- Image database table
  - Database name: \<imfile\> (path to the file)
  - Table name: TABLE_images
  - Data column: blob (contains image binary data)
  - Images are read by the pillow module, which implements many types of image files. We usually use JPG and PNG images.
    
- Attribute database table
  - Database name: \<attfile\> (path to the file)
  - Table name: TABLE_attributes
  - Data column: is definde by command line option "--attr ATTR"
  - Type of the ATTR column should be integer.
    
- Output database table
  - Database name: \<outfile\> (path to the file)
  - Table name: TABLE_attributes
  - The table should have the same structure as the attribute database table, but with column "_order".
  - Before the start of the annotation, the output database may not contain the output table. The table will be created and the data will be copied from the attribute database table.
  - When the table has a different structure, the program is not working.

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

The program is fully configurable by the config file. 
The configuration allows us to set user interface default 
parameters, data format parameters, and classes for annotation. 
Multi-class annotation is possible.

- The configuration is written in JSON format, with the comment extension.

Example of the configuration file `klikatko.json` for annotation of two classes:
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

## Acknowledgment

This work was supported by the Ministry of the Interior of the Czech Republic 
under Project VI20172019082 - Smart Camera.

