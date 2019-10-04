Pacman-progressbar
==================
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FxeBuz%2Fpacman-progressbar.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FxeBuz%2Fpacman-progressbar?ref=badge_shield)

A ProgressBar for Python, based on Arch progressbar, with `ILoveCandy` option enabled.

#### Instalation
```bash
pip install pacmanprogressbar
```


#### Usage


Import the package and create the bar
```python
from pacmanprogressbar import Pacman
 p = Pacman()
```

#### Parameters

| Parameter | Default        | Description                                                     |
| ---       | ---            | ---                                                             |
| start     | 0              | Initial value                                                   |
| end       | 100            | Defines the bar's dimension in an amount of items or "steps"    |
| width     | `console size` | Size (in chars) of the bar, by default is the console size      |
| step      | 0              | Current position in the progressbar                             |
| text      | `None`         | Write some text at the beginning of the line                    |
| encode    | UTF-8          | Encoding                                                        |
    

#### Methods

``` python
p.update([value])
```

Update the progress, incresing the size by 1, or by the "value" parameter

```python
p.progress([value]):
```

Set an specified progress, the parameters is mandatory:


#### Output
----------   
![Alt text](http://i.imgur.com/7oh3T6x.gif)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FxeBuz%2Fpacman-progressbar.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FxeBuz%2Fpacman-progressbar?ref=badge_large)
