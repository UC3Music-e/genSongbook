# songbook-tools

Tools for minimally markuped songs, like LaTeX songbook generation and chord transposition.

## Installation

Install dependencies via `pip`:
```bash
pip install -r requirements.txt --user
```

## Contents and Usage

- [examples/](examples/) - Directory with minimally markuped song examples.

- [extra-tools/](extra-tools/) - Directory with extra tools.

- [song-directory-to-songbook.py](song-directory-to-songbook.py) - Given a directory composed by minimally markuped songs, generate a pdf songbook via LaTeX. Parameters (all optional, complementary to CLI queries):
   ```
   -h, --help           show this help message and exit
   --input INPUT        path of the default song input directory (default: "examples/")
   --output OUTPUT      name of the output pdf file [without extension] (default: "songbook")
   --template TEMPLATE  name of the LaTeX template file [specifies language, etc] (default: "template/english.tex")
   --manifest MANIFEST  name of a file-avoiding manifest file [if desired] (default: "")
   --yes [YES]          accept all, skip all queries (default: "NULL")
   ```

- [song-directory-transpose.py](song-directory-transpose.py) - Given a directory composed by minimally markuped songs, create a new directory with transposed chords (by number of semitones and/or capo/drop removal). Parameters (all optional, complementary to CLI queries):
   ```
   -h, --help            show this help message and exit
   --input INPUT         specify the path of the default song input directory
   --output OUTPUT       specify the path of the default song output directory
   --transpose TRANSPOSE  specify half tones of transposition
   --disableCapoDropCorrection [DISABLECAPODROPCORRECTION] specify if automatic capo/drop correction should be disabled
   --yes [YES]           accept all, skip all queries
   ```
