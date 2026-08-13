# CV source and build

`CV.md` is the editable source for the one-page English CV. The committed PDF is generated with a pinned ReportLab version and invariant PDF metadata.

From the repository root:

```console
python -m pip install -r cv/requirements.txt
python cv/build_cv.py
```

The builder writes `cv/Chih-Kai-Wang-CV.pdf` and fails if the content overflows one page. External links are embedded in the PDF.
