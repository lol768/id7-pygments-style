# -*- coding: utf-8 -*-
"""
    pygments.styles.id7
    ~~~~~~~~~~~~~~~~~~~~~~

    A style based on the University of Warwick's brand.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Whitespace

class IDSevenStyle(Style):
    default_style = ""
    
    aubergine = "#5b3069"
    skyblue = "#204f79" 
    styles = {
        Whitespace:                 '#bbbbbb',
        
        Comment:                    'italic #808080',
        Comment.Preproc:            'noitalic #808080',
        Comment.Special:            'noitalic bold',
        
        Keyword:                    aubergine,
        Keyword.Constant:           '#660E7A',
        Keyword.Type:               "nobold #B00040", 
        Operator.Word:              "bold",
        
        Name.Attribute:             "#0000FF", 
        
        String:                     '#008000',
        String.Escape:              '#000080',
        String.Interpol:            '#00B8BB',
        String.Regex:               '#0000ff',
        Number:                     '#0000ff',
        Generic.Heading:        '#999999',
        Generic.Subheading:     '#aaaaaa',
        Generic.Deleted:        'bg:#ffdddd #000000',
        Generic.Inserted:       'bg:#ddffdd #000000',
        Generic.Error:          '#aa0000',
        Generic.Emph:           'italic',
        Generic.Strong:         'bold',
        Generic.Prompt:         '#555555',
        Generic.Output:         '#888888',
        Generic.Traceback:      '#aa0000',

        Error:                      'bg:#FFCCCC'
    }
