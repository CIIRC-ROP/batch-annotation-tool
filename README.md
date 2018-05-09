# Annotation tools a.k.a. klikatko

## Features

- Images read from csv file
- Configuration read from JSON file

## Requirements

- [Python 3.X](https://www.python.org)
- [TKinter](https://docs.python.org/3.6/library/tkinter.html), GUI library,  part of standard python library

## Usage

``` shell
$ klikatko -h
```

## Configuration file

- Configuration is written in JSON format, with the comment extension.
- Content of the `klikatko.json`:

``` json
{
  "column_in":1,
  "column_out":2,
  "zoom_default":1.0,
  "zoom_min":1.0,
  "zoom_max":1.0
}

```

# Development notes

- [TKinter: Get Widget Size](https://stackoverflow.com/questions/3950687/how-to-find-out-the-current-widget-size-in-tkinter)
- [TKinter: Fullscreen](https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter)
- [TKinter: Tutorial](http://zetcode.com/gui/tkinter/)
- [TKinter: Image View Example](https://stackoverflow.com/questions/17504570/creating-simply-image-gallery-in-python-tkinter-pil#17505256)
- [TKinter: Canvas Widgets](https://www.python-course.eu/tkinter_canvas.php)
- [Comment JSON](https://commentjson.readthedocs.io/en/latest/)
- [Pyton vs MATLAB](https://blog.mide.com/matlab-vs-python-speed-for-vibration-analysis-free-download)
