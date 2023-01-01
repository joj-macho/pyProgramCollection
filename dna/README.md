# DNA Animation

## Description

This program is a simple animation of the DNA molecule.


## How it Works.

- Create a scrolling animation by printing strings from the STRAND list. Where the STRAND is the multiline represenation of a dna molecule.
```python
    STRAND = [

        '         ##',  # Index 0 has no {}.
        '        #{}-{}#',
        '       #{}---{}#',
        '      #{}-----{}#',
        '     #{}------{}#',
        '    #{}------{}#',
        '    #{}-----{}#',
        '     #{}---{}#',
        '     #{}-{}#',
        '      ##',  # Index 9 has no {}.
        '     #{}-{}#',
        '     #{}---{}#',
        '    #{}-----{}#',
        '    #{}------{}#',
        '     #{}------{}#',
        '      #{}-----{}#',
        '       #{}---{}#',
        '        #{}-{}#']
```

- Randomly create the left and the right nucleotide pairs and insert them into the STRAND string using the `format()` string method.
    ```python
    print(STRAND[strandIndex].format(leftNucleotide, rightNucleotide))
    ```


## Program Output

When you run `dna.py`, the output will look like this;

```
DNA Animation

Press Enter To Continue...
        #A-T#
       #G---C#
      #G-----C#
     #C------G#
    #G------C#
    #A-----T#
     #G---C#
     #A-T#
      ##
     #T-A#
     #A---T#
    #T-----A#
    #T------A#
     #A------T#
      #A-----T#
       #G---C#
        #C-G#
         ##
        #A-T#
       #A---T#
      #A-----T#
     #T------A#
    #C------G#
    #C-----G#
     #G---C#
     #G-C#
      ##
     #C-G#
     #T---A#
    #G-----C#
    #T------A#
     #C------G#
      #T-----A#
       #C---G#
        #C-G#
         ##
        #T-A#
       #T---A#
      #G-----C#
     #A------T#
^CGoodbye
```