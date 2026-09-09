# PDF/UA run comparison

## Summary

- cases: 180
- comparable: 180
- not_comparable: 0
- new: 0
- persistent: 5408
- no_longer_observed: 0

## Case details

### ua1-heading-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-heading-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-heading-001 --output lab/reproduction.json
```

### ua1-link-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-link-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-link-001 --output lab/reproduction.json
```

### ua1-list-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-list-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-list-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-paragraph-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-paragraph-001 --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:82-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-10:pdfua:5-1; output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.18.3-1; output-10:pdfua:7.18.5-1; output-10:pdfua:7.2-24; output-10:pdfua:7.2-33; output-10:pdfua:7.2-34; output-10:pdfua:7.21.4.2-2; output-10:pdfua:7.21.7-1; output-11:pdfua:5-1; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.2-33; output-11:pdfua:7.2-34; output-11:pdfua:7.21.4.2-2; output-11:pdfua:7.21.7-1; output-12:pdfua:5-1; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.2-33; output-12:pdfua:7.2-34; output-12:pdfua:7.21.4.2-2; output-13:pdfua:5-1; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.2-33; output-13:pdfua:7.2-34; output-13:pdfua:7.21.4.2-2; output-13:pdfua:7.21.7-1; output-14:pdfua:5-1; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.2-33; output-14:pdfua:7.2-34; output-14:pdfua:7.21.4.2-2; output-15:pdfua:5-1; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.2-33; output-15:pdfua:7.2-34; output-15:pdfua:7.21.4.2-2; output-15:pdfua:7.21.7-1; output-16:pdfua:5-1; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.2-33; output-16:pdfua:7.2-34; output-16:pdfua:7.21.7-1; output-17:pdfua:5-1; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.2-33; output-17:pdfua:7.2-34; output-17:pdfua:7.21.7-1; output-18:pdfua:5-1; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.2-33; output-18:pdfua:7.2-34; output-18:pdfua:7.21.7-1; output-19:pdfua:5-1; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.2-33; output-19:pdfua:7.2-34; output-19:pdfua:7.21.4.2-2; output-19:pdfua:7.21.7-1; output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-20:pdfua:5-1; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.2-33; output-20:pdfua:7.2-34; output-20:pdfua:7.21.4.2-2; output-21:pdfua:5-1; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.2-33; output-21:pdfua:7.2-34; output-21:pdfua:7.21.4.2-2; output-22:pdfua:5-1; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.2-33; output-22:pdfua:7.2-34; output-22:pdfua:7.21.4.2-2; output-23:pdfua:5-1; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.2-33; output-23:pdfua:7.2-34; output-23:pdfua:7.21.4.2-2; output-23:pdfua:7.21.7-1; output-24:pdfua:5-1; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.2-33; output-24:pdfua:7.2-34; output-24:pdfua:7.21.4.2-2; output-25:pdfua:5-1; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.2-33; output-25:pdfua:7.2-34; output-25:pdfua:7.21.4.2-2; output-26:pdfua:5-1; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.2-33; output-26:pdfua:7.2-34; output-26:pdfua:7.21.4.2-2; output-27:pdfua:5-1; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.2-33; output-27:pdfua:7.2-34; output-27:pdfua:7.21.4.2-2; output-27:pdfua:7.21.7-1; output-28:pdfua:5-1; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.2-33; output-28:pdfua:7.2-34; output-28:pdfua:7.21.4.2-2; output-29:pdfua:5-1; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.2-33; output-29:pdfua:7.2-34; output-29:pdfua:7.21.4.2-2; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.18.3-1; output-2:pdfua:7.18.5-1; output-2:pdfua:7.2-24; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-30:pdfua:5-1; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.18.3-1; output-30:pdfua:7.18.5-1; output-30:pdfua:7.2-24; output-30:pdfua:7.2-33; output-30:pdfua:7.2-34; output-30:pdfua:7.21.4.2-2; output-30:pdfua:7.21.7-1; output-31:pdfua:5-1; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.18.3-1; output-31:pdfua:7.18.5-1; output-31:pdfua:7.2-24; output-31:pdfua:7.2-33; output-31:pdfua:7.2-34; output-31:pdfua:7.21.4.2-2; output-31:pdfua:7.21.7-1; output-32:pdfua:5-1; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.18.3-1; output-32:pdfua:7.18.5-1; output-32:pdfua:7.2-24; output-32:pdfua:7.2-33; output-32:pdfua:7.2-34; output-32:pdfua:7.21.4.2-2; output-32:pdfua:7.21.7-1; output-3:pdfua:5-1; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.18.3-1; output-3:pdfua:7.18.5-1; output-3:pdfua:7.2-24; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-3:pdfua:7.21.4.2-2; output-3:pdfua:7.21.7-1; output-4:pdfua:5-1; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:5-1; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-5:pdfua:7.21.4.2-2; output-6:pdfua:5-1; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-6:pdfua:7.21.4.2-2; output-6:pdfua:7.21.7-1; output-7:pdfua:5-1; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.18.3-1; output-7:pdfua:7.18.5-1; output-7:pdfua:7.2-24; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-7:pdfua:7.21.4.2-2; output-8:pdfua:5-1; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-8:pdfua:7.21.4.2-2; output-9:pdfua:5-1; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; output-9:pdfua:7.21.4.2-2; output-9:pdfua:7.21.7-1; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:72-&gt;1; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:82-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:73-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.18.1-2; output-10:pdfua:7.18.3-1; output-10:pdfua:7.18.5-1; output-10:pdfua:7.18.5-2; output-10:pdfua:7.2-33; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.2-33; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.2-33; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.2-33; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-33; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.2-33; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-33; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-23:pdfua:7.2-34; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-24:pdfua:7.2-33; output-24:pdfua:7.2-34; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-25:pdfua:7.2-33; output-25:pdfua:7.2-34; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-26:pdfua:7.2-33; output-26:pdfua:7.2-34; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-27:pdfua:7.2-33; output-27:pdfua:7.2-34; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-28:pdfua:7.2-33; output-28:pdfua:7.2-34; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-29:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.18.1-2; output-2:pdfua:7.18.3-1; output-2:pdfua:7.18.5-1; output-2:pdfua:7.18.5-2; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-30:pdfua:7.18.1-2; output-30:pdfua:7.18.3-1; output-30:pdfua:7.18.5-1; output-30:pdfua:7.18.5-2; output-30:pdfua:7.2-34; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-31:pdfua:7.18.1-2; output-31:pdfua:7.18.3-1; output-31:pdfua:7.18.5-1; output-31:pdfua:7.18.5-2; output-31:pdfua:7.2-34; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-32:pdfua:7.18.1-2; output-32:pdfua:7.18.3-1; output-32:pdfua:7.18.5-1; output-32:pdfua:7.18.5-2; output-32:pdfua:7.2-33; output-32:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.18.1-2; output-3:pdfua:7.18.3-1; output-3:pdfua:7.18.5-1; output-3:pdfua:7.18.5-2; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.18.1-2; output-7:pdfua:7.18.3-1; output-7:pdfua:7.18.5-1; output-7:pdfua:7.18.5-2; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:72-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:82-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:73-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-01-magazine-danish / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.18.5-1; output-10:pdfua:7.2-24; output-10:pdfua:7.2-33; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.2-33; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.2-33; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.2-33; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-33; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.2-33; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-33; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-23:pdfua:7.2-34; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-24:pdfua:7.2-33; output-24:pdfua:7.2-34; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-25:pdfua:7.2-33; output-25:pdfua:7.2-34; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-26:pdfua:7.2-33; output-26:pdfua:7.2-34; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-27:pdfua:7.2-33; output-27:pdfua:7.2-34; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-28:pdfua:7.2-33; output-28:pdfua:7.2-34; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-29:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.18.5-1; output-2:pdfua:7.2-24; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-30:pdfua:7.18.5-1; output-30:pdfua:7.2-24; output-30:pdfua:7.2-34; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-31:pdfua:7.18.5-1; output-31:pdfua:7.2-24; output-31:pdfua:7.2-34; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-32:pdfua:7.18.5-1; output-32:pdfua:7.2-24; output-32:pdfua:7.2-33; output-32:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.18.5-1; output-3:pdfua:7.2-24; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.18.5-1; output-7:pdfua:7.2-24; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:72-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-01-magazine-danish --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:5-&gt;0; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:5-&gt;0; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-02-invoice / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:alt_text_count:2-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-02-invoice --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:16-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-2:pdfua:7.21.4.2-2; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:8-&gt;0; structure:role_map_count:16-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:4-&gt;0; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:8-&gt;0; structure:role_map_count:16-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-03-academicabstract / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:4-&gt;0; structure:role_map_count:4-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-03-academicabstract --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:20-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:17-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.7-1; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:12-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-3:pdfua:5-1; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.18.3-1; output-3:pdfua:7.18.5-1; output-3:pdfua:7.2-2; output-3:pdfua:7.2-24; output-3:pdfua:7.2-30; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-4:pdfua:5-1; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.2-30; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:5-1; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.2-30; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-6:pdfua:5-1; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.18.3-1; output-6:pdfua:7.18.5-1; output-6:pdfua:7.2-24; output-6:pdfua:7.2-30; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-7:pdfua:5-1; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.18.3-1; output-7:pdfua:7.18.5-1; output-7:pdfua:7.2-24; output-7:pdfua:7.2-30; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-7:pdfua:7.21.7-1; output-8:pdfua:5-1; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.18.3-1; output-8:pdfua:7.18.5-1; output-8:pdfua:7.2-24; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:4-&gt;1; structure:role_map_count:12-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:20-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:26-&gt;0; structure:role_map_count:17-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.18.1-2; output-3:pdfua:7.18.3-1; output-3:pdfua:7.18.5-1; output-3:pdfua:7.18.5-2; output-3:pdfua:7.2-30; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-30; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-30; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.18.1-2; output-6:pdfua:7.18.3-1; output-6:pdfua:7.18.5-1; output-6:pdfua:7.18.5-2; output-6:pdfua:7.2-30; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.18.1-2; output-7:pdfua:7.18.3-1; output-7:pdfua:7.18.5-1; output-7:pdfua:7.18.5-2; output-7:pdfua:7.2-30; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.18.1-2; output-8:pdfua:7.18.3-1; output-8:pdfua:7.18.5-1; output-8:pdfua:7.18.5-2; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:4-&gt;0; structure:role_map_count:12-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:20-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:26-&gt;0; structure:role_map_count:17-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-04-presentation / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.18.5-1; output-2:pdfua:7.2-24; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.18.5-1; output-3:pdfua:7.2-24; output-3:pdfua:7.2-30; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-30; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-30; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.18.5-1; output-6:pdfua:7.2-24; output-6:pdfua:7.2-30; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.18.5-1; output-7:pdfua:7.2-24; output-7:pdfua:7.2-30; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.18.5-1; output-8:pdfua:7.2-24; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; structure:alt_text_count:15-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:4-&gt;0; structure:role_map_count:12-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-04-presentation --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:9-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:13-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:5-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:5-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-10:pdfua:5-1; output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.2-30; output-10:pdfua:7.2-33; output-10:pdfua:7.2-34; output-10:pdfua:7.21.7-1; output-11:pdfua:5-1; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.18.3-1; output-11:pdfua:7.18.5-1; output-11:pdfua:7.2-24; output-11:pdfua:7.2-30; output-11:pdfua:7.2-33; output-11:pdfua:7.2-34; output-11:pdfua:7.21.4.2-2; output-11:pdfua:7.21.7-1; output-12:pdfua:5-1; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.18.3-1; output-12:pdfua:7.18.5-1; output-12:pdfua:7.2-24; output-12:pdfua:7.2-30; output-12:pdfua:7.2-33; output-12:pdfua:7.2-34; output-12:pdfua:7.21.7-1; output-13:pdfua:5-1; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.18.3-1; output-13:pdfua:7.18.5-1; output-13:pdfua:7.2-24; output-13:pdfua:7.2-30; output-13:pdfua:7.2-33; output-13:pdfua:7.2-34; output-13:pdfua:7.21.4.2-2; output-13:pdfua:7.21.7-1; output-14:pdfua:5-1; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.18.3-1; output-14:pdfua:7.18.5-1; output-14:pdfua:7.2-24; output-14:pdfua:7.2-30; output-14:pdfua:7.2-33; output-14:pdfua:7.2-34; output-14:pdfua:7.21.4.2-2; output-14:pdfua:7.21.7-1; output-15:pdfua:5-1; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.18.3-1; output-15:pdfua:7.18.5-1; output-15:pdfua:7.2-24; output-15:pdfua:7.2-30; output-15:pdfua:7.2-33; output-15:pdfua:7.2-34; output-15:pdfua:7.21.4.2-2; output-15:pdfua:7.21.7-1; output-16:pdfua:5-1; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.2-30; output-16:pdfua:7.2-33; output-16:pdfua:7.2-34; output-16:pdfua:7.21.4.2-2; output-16:pdfua:7.21.7-1; output-17:pdfua:5-1; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.18.3-1; output-17:pdfua:7.18.5-1; output-17:pdfua:7.2-24; output-17:pdfua:7.2-30; output-17:pdfua:7.2-33; output-17:pdfua:7.2-34; output-17:pdfua:7.21.4.2-2; output-17:pdfua:7.21.7-1; output-18:pdfua:5-1; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.2-30; output-18:pdfua:7.2-33; output-18:pdfua:7.2-34; output-18:pdfua:7.21.7-1; output-19:pdfua:5-1; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.2-30; output-19:pdfua:7.2-33; output-19:pdfua:7.2-34; output-19:pdfua:7.21.7-1; output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.7-1; output-20:pdfua:5-1; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.2-30; output-20:pdfua:7.2-33; output-20:pdfua:7.2-34; output-20:pdfua:7.21.7-1; output-21:pdfua:5-1; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.2-30; output-21:pdfua:7.2-33; output-21:pdfua:7.2-34; output-21:pdfua:7.21.7-1; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-2:pdfua:7.21.7-1; output-3:pdfua:5-1; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.2-30; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-3:pdfua:7.21.7-1; output-4:pdfua:5-1; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.18.3-1; output-4:pdfua:7.18.5-1; output-4:pdfua:7.2-24; output-4:pdfua:7.2-30; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-4:pdfua:7.21.7-1; output-5:pdfua:5-1; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.2-30; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-5:pdfua:7.21.4.2-2; output-5:pdfua:7.21.7-1; output-6:pdfua:5-1; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.2-30; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-6:pdfua:7.21.7-1; output-7:pdfua:5-1; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.2-30; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-7:pdfua:7.21.7-1; output-8:pdfua:5-1; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-8:pdfua:7.21.7-1; output-9:pdfua:5-1; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.2-30; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; output-9:pdfua:7.21.7-1; structure:alt_text_count:5-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:22-&gt;1; structure:role_map_count:5-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:9-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:34-&gt;0; structure:role_map_count:13-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.2-30; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.18.1-2; output-11:pdfua:7.18.3-1; output-11:pdfua:7.18.5-1; output-11:pdfua:7.18.5-2; output-11:pdfua:7.2-30; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.18.1-2; output-12:pdfua:7.18.3-1; output-12:pdfua:7.18.5-1; output-12:pdfua:7.18.5-2; output-12:pdfua:7.2-30; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.18.1-2; output-13:pdfua:7.18.3-1; output-13:pdfua:7.18.5-1; output-13:pdfua:7.18.5-2; output-13:pdfua:7.2-30; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.18.1-2; output-14:pdfua:7.18.3-1; output-14:pdfua:7.18.5-1; output-14:pdfua:7.18.5-2; output-14:pdfua:7.2-30; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.18.1-2; output-15:pdfua:7.18.3-1; output-15:pdfua:7.18.5-1; output-15:pdfua:7.18.5-2; output-15:pdfua:7.2-30; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-30; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.18.1-2; output-17:pdfua:7.18.3-1; output-17:pdfua:7.18.5-1; output-17:pdfua:7.18.5-2; output-17:pdfua:7.2-30; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-30; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-30; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-30; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-30; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-30; output-21:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-30; output-2:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.2-30; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.18.1-2; output-4:pdfua:7.18.3-1; output-4:pdfua:7.18.5-1; output-4:pdfua:7.18.5-2; output-4:pdfua:7.2-30; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-30; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.2-30; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.2-30; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-30; output-9:pdfua:7.2-34; structure:alt_text_count:5-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:22-&gt;0; structure:role_map_count:5-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:9-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:34-&gt;0; structure:role_map_count:13-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-05-bookchapter-german / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.2-30; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.18.5-1; output-11:pdfua:7.2-24; output-11:pdfua:7.2-30; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.18.5-1; output-12:pdfua:7.2-24; output-12:pdfua:7.2-30; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.18.5-1; output-13:pdfua:7.2-24; output-13:pdfua:7.2-30; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.18.5-1; output-14:pdfua:7.2-24; output-14:pdfua:7.2-30; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.18.5-1; output-15:pdfua:7.2-24; output-15:pdfua:7.2-30; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-30; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.18.5-1; output-17:pdfua:7.2-24; output-17:pdfua:7.2-30; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-30; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-30; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-30; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-30; output-21:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-30; output-2:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.2-30; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.18.5-1; output-4:pdfua:7.2-24; output-4:pdfua:7.2-30; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-30; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.18.5-1; output-6:pdfua:7.2-24; output-6:pdfua:7.2-30; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.18.5-1; output-7:pdfua:7.2-24; output-7:pdfua:7.2-30; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-30; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-30; output-9:pdfua:7.2-34; structure:alt_text_count:5-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:22-&gt;0; structure:role_map_count:5-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-05-bookchapter-german --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:17-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:4-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.18.3-1; output-2:pdfua:7.18.5-1; output-2:pdfua:7.2-24; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-2:pdfua:7.21.4.2-2; output-2:pdfua:7.21.7-1; structure:alt_text_count:4-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:12-&gt;1; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:17-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:65-&gt;0; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.18.1-2; output-2:pdfua:7.18.3-1; output-2:pdfua:7.18.5-1; output-2:pdfua:7.18.5-2; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; structure:alt_text_count:4-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:12-&gt;0; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:17-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:65-&gt;0; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-06-brochure / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.18.5-1; output-2:pdfua:7.2-24; output-2:pdfua:7.2-30; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; structure:alt_text_count:4-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:12-&gt;0; structure:role_map_count:8-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-06-brochure --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:576-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.7-1; structure:alt_text_count:13-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-10:pdfua:5-1; output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.2-33; output-10:pdfua:7.2-34; output-10:pdfua:7.21.7-1; output-11:pdfua:5-1; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.2-33; output-11:pdfua:7.2-34; output-11:pdfua:7.21.7-1; output-12:pdfua:5-1; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.2-33; output-12:pdfua:7.2-34; output-12:pdfua:7.21.7-1; output-13:pdfua:5-1; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.2-33; output-13:pdfua:7.2-34; output-13:pdfua:7.21.7-1; output-14:pdfua:5-1; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.2-33; output-14:pdfua:7.2-34; output-14:pdfua:7.21.7-1; output-15:pdfua:5-1; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.2-33; output-15:pdfua:7.2-34; output-15:pdfua:7.21.7-1; output-16:pdfua:5-1; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.2-33; output-16:pdfua:7.2-34; output-16:pdfua:7.21.7-1; output-17:pdfua:5-1; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.2-33; output-17:pdfua:7.2-34; output-17:pdfua:7.21.7-1; output-18:pdfua:5-1; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.2-33; output-18:pdfua:7.2-34; output-18:pdfua:7.21.7-1; output-19:pdfua:5-1; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.2-33; output-19:pdfua:7.2-34; output-19:pdfua:7.21.7-1; output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.7-1; output-20:pdfua:5-1; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.2-33; output-20:pdfua:7.2-34; output-20:pdfua:7.21.7-1; output-21:pdfua:5-1; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.2-33; output-21:pdfua:7.2-34; output-21:pdfua:7.21.7-1; output-22:pdfua:5-1; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.2-33; output-22:pdfua:7.2-34; output-22:pdfua:7.21.7-1; output-23:pdfua:5-1; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.2-33; output-23:pdfua:7.2-34; output-23:pdfua:7.21.7-1; output-24:pdfua:5-1; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.2-33; output-24:pdfua:7.2-34; output-24:pdfua:7.21.7-1; output-25:pdfua:5-1; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.2-33; output-25:pdfua:7.2-34; output-25:pdfua:7.21.7-1; output-26:pdfua:5-1; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.2-33; output-26:pdfua:7.2-34; output-26:pdfua:7.21.7-1; output-27:pdfua:5-1; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.2-33; output-27:pdfua:7.2-34; output-27:pdfua:7.21.7-1; output-28:pdfua:5-1; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.2-33; output-28:pdfua:7.2-34; output-28:pdfua:7.21.7-1; output-29:pdfua:5-1; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.2-33; output-29:pdfua:7.2-34; output-29:pdfua:7.21.7-1; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; output-2:pdfua:7.21.7-1; output-30:pdfua:5-1; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.2-33; output-30:pdfua:7.2-34; output-30:pdfua:7.21.7-1; output-31:pdfua:5-1; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.18.3-1; output-31:pdfua:7.18.5-1; output-31:pdfua:7.2-24; output-31:pdfua:7.2-33; output-31:pdfua:7.2-34; output-31:pdfua:7.21.7-1; output-32:pdfua:5-1; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.2-33; output-32:pdfua:7.2-34; output-3:pdfua:5-1; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.2-33; output-3:pdfua:7.2-34; output-3:pdfua:7.21.7-1; output-4:pdfua:5-1; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.2-33; output-4:pdfua:7.2-34; output-4:pdfua:7.21.7-1; output-5:pdfua:5-1; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.2-33; output-5:pdfua:7.2-34; output-5:pdfua:7.21.7-1; output-6:pdfua:5-1; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.2-33; output-6:pdfua:7.2-34; output-6:pdfua:7.21.7-1; output-7:pdfua:5-1; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.2-33; output-7:pdfua:7.2-34; output-7:pdfua:7.21.7-1; output-8:pdfua:5-1; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.2-33; output-8:pdfua:7.2-34; output-8:pdfua:7.21.7-1; output-9:pdfua:5-1; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; output-9:pdfua:7.21.7-1; structure:alt_text_count:13-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:53-&gt;1; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-34; structure:alt_text_count:576-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:373-&gt;0; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-23:pdfua:7.2-34; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-24:pdfua:7.2-34; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-25:pdfua:7.2-34; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-26:pdfua:7.2-34; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-27:pdfua:7.2-34; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-28:pdfua:7.2-34; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-29:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-30:pdfua:7.2-34; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-31:pdfua:7.18.1-2; output-31:pdfua:7.18.3-1; output-31:pdfua:7.18.5-1; output-31:pdfua:7.18.5-2; output-31:pdfua:7.2-34; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-32:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-34; structure:alt_text_count:13-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:53-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-34; structure:alt_text_count:576-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:373-&gt;0; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-08-bookchapter / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-10:pdfua:7.2-34; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-11:pdfua:7.2-34; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-12:pdfua:7.2-34; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-13:pdfua:7.2-34; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-14:pdfua:7.2-34; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-15:pdfua:7.2-34; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-16:pdfua:7.2-34; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-17:pdfua:7.2-34; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-18:pdfua:7.2-34; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-34; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-20:pdfua:7.2-34; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-23:pdfua:7.2-34; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-24:pdfua:7.2-34; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-25:pdfua:7.2-34; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-26:pdfua:7.2-34; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-27:pdfua:7.2-34; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-28:pdfua:7.2-34; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-29:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-30:pdfua:7.2-34; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-31:pdfua:7.18.5-1; output-31:pdfua:7.2-24; output-31:pdfua:7.2-34; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-32:pdfua:7.2-34; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-3:pdfua:7.2-34; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-4:pdfua:7.2-34; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-5:pdfua:7.2-34; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-6:pdfua:7.2-34; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-7:pdfua:7.2-34; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-8:pdfua:7.2-34; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-34; structure:alt_text_count:13-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:53-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-08-bookchapter --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:9-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-10:pdfua:5-1; output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.2-33; output-10:pdfua:7.21.4.2-2; output-11:pdfua:5-1; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.2-33; output-11:pdfua:7.21.4.2-2; output-12:pdfua:5-1; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.2-33; output-12:pdfua:7.21.4.2-2; output-13:pdfua:5-1; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.2-33; output-13:pdfua:7.21.4.2-2; output-14:pdfua:5-1; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.2-33; output-14:pdfua:7.21.4.2-2; output-15:pdfua:5-1; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.2-33; output-15:pdfua:7.21.4.2-2; output-16:pdfua:5-1; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.2-33; output-16:pdfua:7.21.4.2-2; output-17:pdfua:5-1; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.2-33; output-17:pdfua:7.21.4.2-2; output-18:pdfua:5-1; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.2-33; output-18:pdfua:7.21.4.2-2; output-19:pdfua:5-1; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.2-33; output-19:pdfua:7.2-34; output-19:pdfua:7.21.4.2-2; output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.21.4.2-2; output-20:pdfua:5-1; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.2-33; output-20:pdfua:7.21.4.2-2; output-21:pdfua:5-1; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.2-33; output-21:pdfua:7.2-34; output-21:pdfua:7.21.4.2-2; output-22:pdfua:5-1; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.2-33; output-22:pdfua:7.2-34; output-22:pdfua:7.21.4.2-2; output-23:pdfua:5-1; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.2-33; output-23:pdfua:7.21.4.2-2; output-24:pdfua:5-1; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.2-33; output-24:pdfua:7.21.4.2-2; output-25:pdfua:5-1; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.2-33; output-25:pdfua:7.21.4.2-2; output-26:pdfua:5-1; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.2-33; output-26:pdfua:7.21.4.2-2; output-27:pdfua:5-1; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.2-33; output-27:pdfua:7.21.4.2-2; output-28:pdfua:5-1; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.2-33; output-28:pdfua:7.21.4.2-2; output-29:pdfua:5-1; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.2-33; output-29:pdfua:7.21.4.2-2; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-33; output-2:pdfua:7.21.4.2-2; output-30:pdfua:5-1; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.2-33; output-30:pdfua:7.21.4.2-2; output-31:pdfua:5-1; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.2-33; output-31:pdfua:7.21.4.2-2; output-32:pdfua:5-1; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.2-33; output-32:pdfua:7.21.4.2-2; output-33:pdfua:5-1; output-33:pdfua:6.2-1; output-33:pdfua:7.1-10; output-33:pdfua:7.1-11; output-33:pdfua:7.1-3; output-33:pdfua:7.2-33; output-33:pdfua:7.21.4.2-2; output-34:pdfua:5-1; output-34:pdfua:6.2-1; output-34:pdfua:7.1-10; output-34:pdfua:7.1-11; output-34:pdfua:7.1-3; output-34:pdfua:7.2-33; output-34:pdfua:7.21.4.2-2; output-35:pdfua:5-1; output-35:pdfua:6.2-1; output-35:pdfua:7.1-10; output-35:pdfua:7.1-11; output-35:pdfua:7.1-3; output-35:pdfua:7.2-33; output-35:pdfua:7.21.4.2-2; output-36:pdfua:5-1; output-36:pdfua:6.2-1; output-36:pdfua:7.1-10; output-36:pdfua:7.1-11; output-36:pdfua:7.1-3; output-36:pdfua:7.2-33; output-36:pdfua:7.21.4.2-2; output-37:pdfua:5-1; output-37:pdfua:6.2-1; output-37:pdfua:7.1-10; output-37:pdfua:7.1-11; output-37:pdfua:7.1-3; output-37:pdfua:7.2-33; output-37:pdfua:7.21.4.2-2; output-38:pdfua:5-1; output-38:pdfua:6.2-1; output-38:pdfua:7.1-10; output-38:pdfua:7.1-11; output-38:pdfua:7.1-3; output-38:pdfua:7.2-33; output-38:pdfua:7.21.4.2-2; output-39:pdfua:5-1; output-39:pdfua:6.2-1; output-39:pdfua:7.1-10; output-39:pdfua:7.1-11; output-39:pdfua:7.1-3; output-39:pdfua:7.2-33; output-39:pdfua:7.21.4.2-2; output-3:pdfua:5-1; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.2-33; output-3:pdfua:7.21.4.2-2; output-40:pdfua:5-1; output-40:pdfua:6.2-1; output-40:pdfua:7.1-10; output-40:pdfua:7.1-11; output-40:pdfua:7.1-3; output-40:pdfua:7.2-33; output-40:pdfua:7.21.4.2-2; output-41:pdfua:5-1; output-41:pdfua:6.2-1; output-41:pdfua:7.1-10; output-41:pdfua:7.1-11; output-41:pdfua:7.1-3; output-41:pdfua:7.2-33; output-41:pdfua:7.21.4.2-2; output-42:pdfua:5-1; output-42:pdfua:6.2-1; output-42:pdfua:7.1-10; output-42:pdfua:7.1-11; output-42:pdfua:7.1-3; output-42:pdfua:7.2-33; output-42:pdfua:7.21.4.2-2; output-43:pdfua:5-1; output-43:pdfua:6.2-1; output-43:pdfua:7.1-10; output-43:pdfua:7.1-11; output-43:pdfua:7.1-3; output-43:pdfua:7.2-33; output-43:pdfua:7.21.4.2-2; output-44:pdfua:5-1; output-44:pdfua:6.2-1; output-44:pdfua:7.1-10; output-44:pdfua:7.1-11; output-44:pdfua:7.1-3; output-44:pdfua:7.2-33; output-44:pdfua:7.21.4.2-2; output-45:pdfua:5-1; output-45:pdfua:6.2-1; output-45:pdfua:7.1-10; output-45:pdfua:7.1-11; output-45:pdfua:7.1-3; output-45:pdfua:7.2-33; output-45:pdfua:7.21.4.2-2; output-46:pdfua:5-1; output-46:pdfua:6.2-1; output-46:pdfua:7.1-10; output-46:pdfua:7.1-11; output-46:pdfua:7.1-3; output-46:pdfua:7.2-33; output-46:pdfua:7.21.4.2-2; output-47:pdfua:5-1; output-47:pdfua:6.2-1; output-47:pdfua:7.1-10; output-47:pdfua:7.1-11; output-47:pdfua:7.1-3; output-47:pdfua:7.2-33; output-47:pdfua:7.21.4.2-2; output-48:pdfua:5-1; output-48:pdfua:6.2-1; output-48:pdfua:7.1-10; output-48:pdfua:7.1-11; output-48:pdfua:7.1-3; output-48:pdfua:7.2-33; output-48:pdfua:7.21.4.2-2; output-49:pdfua:5-1; output-49:pdfua:6.2-1; output-49:pdfua:7.1-10; output-49:pdfua:7.1-11; output-49:pdfua:7.1-3; output-49:pdfua:7.2-33; output-49:pdfua:7.21.4.2-2; output-4:pdfua:5-1; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.2-33; output-4:pdfua:7.21.4.2-2; output-50:pdfua:5-1; output-50:pdfua:6.2-1; output-50:pdfua:7.1-10; output-50:pdfua:7.1-11; output-50:pdfua:7.1-3; output-50:pdfua:7.2-33; output-50:pdfua:7.21.4.2-2; output-51:pdfua:5-1; output-51:pdfua:6.2-1; output-51:pdfua:7.1-10; output-51:pdfua:7.1-11; output-51:pdfua:7.1-3; output-51:pdfua:7.2-33; output-51:pdfua:7.21.4.2-2; output-52:pdfua:5-1; output-52:pdfua:6.2-1; output-52:pdfua:7.1-10; output-52:pdfua:7.1-11; output-52:pdfua:7.1-3; output-52:pdfua:7.2-33; output-52:pdfua:7.21.4.2-2; output-53:pdfua:5-1; output-53:pdfua:6.2-1; output-53:pdfua:7.1-10; output-53:pdfua:7.1-11; output-53:pdfua:7.1-3; output-53:pdfua:7.2-33; output-53:pdfua:7.21.4.2-2; output-54:pdfua:5-1; output-54:pdfua:6.2-1; output-54:pdfua:7.1-10; output-54:pdfua:7.1-11; output-54:pdfua:7.1-3; output-54:pdfua:7.2-33; output-54:pdfua:7.21.4.2-2; output-55:pdfua:5-1; output-55:pdfua:6.2-1; output-55:pdfua:7.1-10; output-55:pdfua:7.1-11; output-55:pdfua:7.1-3; output-55:pdfua:7.2-33; output-55:pdfua:7.21.4.2-2; output-56:pdfua:5-1; output-56:pdfua:6.2-1; output-56:pdfua:7.1-10; output-56:pdfua:7.1-11; output-56:pdfua:7.1-3; output-56:pdfua:7.2-33; output-56:pdfua:7.21.4.2-2; output-57:pdfua:5-1; output-57:pdfua:6.2-1; output-57:pdfua:7.1-10; output-57:pdfua:7.1-11; output-57:pdfua:7.1-3; output-57:pdfua:7.2-33; output-57:pdfua:7.21.4.2-2; output-58:pdfua:5-1; output-58:pdfua:6.2-1; output-58:pdfua:7.1-10; output-58:pdfua:7.1-11; output-58:pdfua:7.1-3; output-58:pdfua:7.2-33; output-58:pdfua:7.21.4.2-2; output-59:pdfua:5-1; output-59:pdfua:6.2-1; output-59:pdfua:7.1-10; output-59:pdfua:7.1-11; output-59:pdfua:7.1-3; output-59:pdfua:7.2-33; output-59:pdfua:7.21.4.2-2; output-5:pdfua:5-1; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.2-33; output-5:pdfua:7.21.4.2-2; output-60:pdfua:5-1; output-60:pdfua:6.2-1; output-60:pdfua:7.1-10; output-60:pdfua:7.1-11; output-60:pdfua:7.1-3; output-60:pdfua:7.2-33; output-60:pdfua:7.21.4.2-2; output-61:pdfua:5-1; output-61:pdfua:6.2-1; output-61:pdfua:7.1-10; output-61:pdfua:7.1-11; output-61:pdfua:7.1-3; output-61:pdfua:7.2-33; output-61:pdfua:7.21.4.2-2; output-62:pdfua:5-1; output-62:pdfua:6.2-1; output-62:pdfua:7.1-10; output-62:pdfua:7.1-11; output-62:pdfua:7.1-3; output-62:pdfua:7.2-33; output-62:pdfua:7.21.4.2-2; output-63:pdfua:5-1; output-63:pdfua:6.2-1; output-63:pdfua:7.1-10; output-63:pdfua:7.1-11; output-63:pdfua:7.1-3; output-63:pdfua:7.2-33; output-63:pdfua:7.2-34; output-63:pdfua:7.21.4.2-2; output-64:pdfua:5-1; output-64:pdfua:6.2-1; output-64:pdfua:7.1-10; output-64:pdfua:7.1-11; output-64:pdfua:7.1-3; output-64:pdfua:7.2-33; output-64:pdfua:7.21.4.2-2; output-65:pdfua:5-1; output-65:pdfua:6.2-1; output-65:pdfua:7.1-10; output-65:pdfua:7.1-11; output-65:pdfua:7.1-3; output-65:pdfua:7.2-33; output-65:pdfua:7.21.4.2-2; output-66:pdfua:5-1; output-66:pdfua:6.2-1; output-66:pdfua:7.1-10; output-66:pdfua:7.1-11; output-66:pdfua:7.1-3; output-66:pdfua:7.2-33; output-66:pdfua:7.21.4.2-2; output-67:pdfua:5-1; output-67:pdfua:6.2-1; output-67:pdfua:7.1-10; output-67:pdfua:7.1-11; output-67:pdfua:7.1-3; output-67:pdfua:7.2-33; output-67:pdfua:7.21.4.2-2; output-68:pdfua:5-1; output-68:pdfua:6.2-1; output-68:pdfua:7.1-10; output-68:pdfua:7.1-11; output-68:pdfua:7.1-3; output-68:pdfua:7.2-33; output-68:pdfua:7.21.4.2-2; output-69:pdfua:5-1; output-69:pdfua:6.2-1; output-69:pdfua:7.1-10; output-69:pdfua:7.1-11; output-69:pdfua:7.1-3; output-69:pdfua:7.2-33; output-69:pdfua:7.21.4.2-2; output-6:pdfua:5-1; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.2-33; output-6:pdfua:7.21.4.2-2; output-70:pdfua:5-1; output-70:pdfua:6.2-1; output-70:pdfua:7.1-10; output-70:pdfua:7.1-11; output-70:pdfua:7.1-3; output-70:pdfua:7.2-33; output-70:pdfua:7.21.4.2-2; output-71:pdfua:5-1; output-71:pdfua:6.2-1; output-71:pdfua:7.1-10; output-71:pdfua:7.1-11; output-71:pdfua:7.1-3; output-71:pdfua:7.2-33; output-71:pdfua:7.21.4.2-2; output-72:pdfua:5-1; output-72:pdfua:6.2-1; output-72:pdfua:7.1-10; output-72:pdfua:7.1-11; output-72:pdfua:7.1-3; output-72:pdfua:7.2-33; output-72:pdfua:7.21.4.2-2; output-73:pdfua:5-1; output-73:pdfua:6.2-1; output-73:pdfua:7.1-10; output-73:pdfua:7.1-11; output-73:pdfua:7.1-3; output-73:pdfua:7.2-33; output-73:pdfua:7.21.4.2-2; output-74:pdfua:5-1; output-74:pdfua:6.2-1; output-74:pdfua:7.1-10; output-74:pdfua:7.1-11; output-74:pdfua:7.1-3; output-74:pdfua:7.2-33; output-74:pdfua:7.21.4.2-2; output-75:pdfua:5-1; output-75:pdfua:6.2-1; output-75:pdfua:7.1-10; output-75:pdfua:7.1-11; output-75:pdfua:7.1-3; output-75:pdfua:7.2-33; output-75:pdfua:7.21.4.2-2; output-76:pdfua:5-1; output-76:pdfua:6.2-1; output-76:pdfua:7.1-10; output-76:pdfua:7.1-11; output-76:pdfua:7.1-3; output-76:pdfua:7.2-33; output-76:pdfua:7.21.4.2-2; output-77:pdfua:5-1; output-77:pdfua:6.2-1; output-77:pdfua:7.1-10; output-77:pdfua:7.1-11; output-77:pdfua:7.1-3; output-77:pdfua:7.2-33; output-77:pdfua:7.21.4.2-2; output-78:pdfua:5-1; output-78:pdfua:6.2-1; output-78:pdfua:7.1-10; output-78:pdfua:7.1-11; output-78:pdfua:7.1-3; output-78:pdfua:7.2-33; output-78:pdfua:7.2-34; output-78:pdfua:7.21.4.2-2; output-79:pdfua:5-1; output-79:pdfua:6.2-1; output-79:pdfua:7.1-10; output-79:pdfua:7.1-11; output-79:pdfua:7.1-3; output-79:pdfua:7.2-33; output-79:pdfua:7.21.4.2-2; output-7:pdfua:5-1; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.2-33; output-7:pdfua:7.21.4.2-2; output-80:pdfua:5-1; output-80:pdfua:6.2-1; output-80:pdfua:7.1-10; output-80:pdfua:7.1-11; output-80:pdfua:7.1-3; output-80:pdfua:7.2-33; output-80:pdfua:7.21.4.2-2; output-81:pdfua:5-1; output-81:pdfua:6.2-1; output-81:pdfua:7.1-10; output-81:pdfua:7.1-11; output-81:pdfua:7.1-3; output-81:pdfua:7.2-33; output-81:pdfua:7.21.4.2-2; output-82:pdfua:5-1; output-82:pdfua:6.2-1; output-82:pdfua:7.1-10; output-82:pdfua:7.1-11; output-82:pdfua:7.1-3; output-82:pdfua:7.2-33; output-82:pdfua:7.21.4.2-2; output-8:pdfua:5-1; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.2-33; output-8:pdfua:7.21.4.2-2; output-9:pdfua:5-1; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.2-33; output-9:pdfua:7.2-34; output-9:pdfua:7.21.4.2-2; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:320-&gt;3; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; output-1:pdfua:7.2-34; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:320-&gt;0; structure:role_map_count:9-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-33:pdfua:6.2-1; output-33:pdfua:7.1-10; output-33:pdfua:7.1-11; output-33:pdfua:7.1-3; output-33:pdfua:7.1-8; output-34:pdfua:6.2-1; output-34:pdfua:7.1-10; output-34:pdfua:7.1-11; output-34:pdfua:7.1-3; output-34:pdfua:7.1-8; output-35:pdfua:6.2-1; output-35:pdfua:7.1-10; output-35:pdfua:7.1-11; output-35:pdfua:7.1-3; output-35:pdfua:7.1-8; output-36:pdfua:6.2-1; output-36:pdfua:7.1-10; output-36:pdfua:7.1-11; output-36:pdfua:7.1-3; output-36:pdfua:7.1-8; output-37:pdfua:6.2-1; output-37:pdfua:7.1-10; output-37:pdfua:7.1-11; output-37:pdfua:7.1-3; output-37:pdfua:7.1-8; output-38:pdfua:6.2-1; output-38:pdfua:7.1-10; output-38:pdfua:7.1-11; output-38:pdfua:7.1-3; output-38:pdfua:7.1-8; output-39:pdfua:6.2-1; output-39:pdfua:7.1-10; output-39:pdfua:7.1-11; output-39:pdfua:7.1-3; output-39:pdfua:7.1-8; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-40:pdfua:6.2-1; output-40:pdfua:7.1-10; output-40:pdfua:7.1-11; output-40:pdfua:7.1-3; output-40:pdfua:7.1-8; output-41:pdfua:6.2-1; output-41:pdfua:7.1-10; output-41:pdfua:7.1-11; output-41:pdfua:7.1-3; output-41:pdfua:7.1-8; output-42:pdfua:6.2-1; output-42:pdfua:7.1-10; output-42:pdfua:7.1-11; output-42:pdfua:7.1-3; output-42:pdfua:7.1-8; output-43:pdfua:6.2-1; output-43:pdfua:7.1-10; output-43:pdfua:7.1-11; output-43:pdfua:7.1-3; output-43:pdfua:7.1-8; output-44:pdfua:6.2-1; output-44:pdfua:7.1-10; output-44:pdfua:7.1-11; output-44:pdfua:7.1-3; output-44:pdfua:7.1-8; output-45:pdfua:6.2-1; output-45:pdfua:7.1-10; output-45:pdfua:7.1-11; output-45:pdfua:7.1-3; output-45:pdfua:7.1-8; output-46:pdfua:6.2-1; output-46:pdfua:7.1-10; output-46:pdfua:7.1-11; output-46:pdfua:7.1-3; output-46:pdfua:7.1-8; output-47:pdfua:6.2-1; output-47:pdfua:7.1-10; output-47:pdfua:7.1-11; output-47:pdfua:7.1-3; output-47:pdfua:7.1-8; output-48:pdfua:6.2-1; output-48:pdfua:7.1-10; output-48:pdfua:7.1-11; output-48:pdfua:7.1-3; output-48:pdfua:7.1-8; output-49:pdfua:6.2-1; output-49:pdfua:7.1-10; output-49:pdfua:7.1-11; output-49:pdfua:7.1-3; output-49:pdfua:7.1-8; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-50:pdfua:6.2-1; output-50:pdfua:7.1-10; output-50:pdfua:7.1-11; output-50:pdfua:7.1-3; output-50:pdfua:7.1-8; output-51:pdfua:6.2-1; output-51:pdfua:7.1-10; output-51:pdfua:7.1-11; output-51:pdfua:7.1-3; output-51:pdfua:7.1-8; output-52:pdfua:6.2-1; output-52:pdfua:7.1-10; output-52:pdfua:7.1-11; output-52:pdfua:7.1-3; output-52:pdfua:7.1-8; output-53:pdfua:6.2-1; output-53:pdfua:7.1-10; output-53:pdfua:7.1-11; output-53:pdfua:7.1-3; output-53:pdfua:7.1-8; output-54:pdfua:6.2-1; output-54:pdfua:7.1-10; output-54:pdfua:7.1-11; output-54:pdfua:7.1-3; output-54:pdfua:7.1-8; output-55:pdfua:6.2-1; output-55:pdfua:7.1-10; output-55:pdfua:7.1-11; output-55:pdfua:7.1-3; output-55:pdfua:7.1-8; output-56:pdfua:6.2-1; output-56:pdfua:7.1-10; output-56:pdfua:7.1-11; output-56:pdfua:7.1-3; output-56:pdfua:7.1-8; output-57:pdfua:6.2-1; output-57:pdfua:7.1-10; output-57:pdfua:7.1-11; output-57:pdfua:7.1-3; output-57:pdfua:7.1-8; output-58:pdfua:6.2-1; output-58:pdfua:7.1-10; output-58:pdfua:7.1-11; output-58:pdfua:7.1-3; output-58:pdfua:7.1-8; output-59:pdfua:6.2-1; output-59:pdfua:7.1-10; output-59:pdfua:7.1-11; output-59:pdfua:7.1-3; output-59:pdfua:7.1-8; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-60:pdfua:6.2-1; output-60:pdfua:7.1-10; output-60:pdfua:7.1-11; output-60:pdfua:7.1-3; output-60:pdfua:7.1-8; output-61:pdfua:6.2-1; output-61:pdfua:7.1-10; output-61:pdfua:7.1-11; output-61:pdfua:7.1-3; output-61:pdfua:7.1-8; output-62:pdfua:6.2-1; output-62:pdfua:7.1-10; output-62:pdfua:7.1-11; output-62:pdfua:7.1-3; output-62:pdfua:7.1-8; output-63:pdfua:6.2-1; output-63:pdfua:7.1-10; output-63:pdfua:7.1-11; output-63:pdfua:7.1-3; output-63:pdfua:7.1-8; output-63:pdfua:7.2-34; output-64:pdfua:6.2-1; output-64:pdfua:7.1-10; output-64:pdfua:7.1-11; output-64:pdfua:7.1-3; output-64:pdfua:7.1-8; output-65:pdfua:6.2-1; output-65:pdfua:7.1-10; output-65:pdfua:7.1-11; output-65:pdfua:7.1-3; output-65:pdfua:7.1-8; output-66:pdfua:6.2-1; output-66:pdfua:7.1-10; output-66:pdfua:7.1-11; output-66:pdfua:7.1-3; output-66:pdfua:7.1-8; output-67:pdfua:6.2-1; output-67:pdfua:7.1-10; output-67:pdfua:7.1-11; output-67:pdfua:7.1-3; output-67:pdfua:7.1-8; output-68:pdfua:6.2-1; output-68:pdfua:7.1-10; output-68:pdfua:7.1-11; output-68:pdfua:7.1-3; output-68:pdfua:7.1-8; output-69:pdfua:6.2-1; output-69:pdfua:7.1-10; output-69:pdfua:7.1-11; output-69:pdfua:7.1-3; output-69:pdfua:7.1-8; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-70:pdfua:6.2-1; output-70:pdfua:7.1-10; output-70:pdfua:7.1-11; output-70:pdfua:7.1-3; output-70:pdfua:7.1-8; output-71:pdfua:6.2-1; output-71:pdfua:7.1-10; output-71:pdfua:7.1-11; output-71:pdfua:7.1-3; output-71:pdfua:7.1-8; output-72:pdfua:6.2-1; output-72:pdfua:7.1-10; output-72:pdfua:7.1-11; output-72:pdfua:7.1-3; output-72:pdfua:7.1-8; output-73:pdfua:6.2-1; output-73:pdfua:7.1-10; output-73:pdfua:7.1-11; output-73:pdfua:7.1-3; output-73:pdfua:7.1-8; output-74:pdfua:6.2-1; output-74:pdfua:7.1-10; output-74:pdfua:7.1-11; output-74:pdfua:7.1-3; output-74:pdfua:7.1-8; output-75:pdfua:6.2-1; output-75:pdfua:7.1-10; output-75:pdfua:7.1-11; output-75:pdfua:7.1-3; output-75:pdfua:7.1-8; output-76:pdfua:6.2-1; output-76:pdfua:7.1-10; output-76:pdfua:7.1-11; output-76:pdfua:7.1-3; output-76:pdfua:7.1-8; output-77:pdfua:6.2-1; output-77:pdfua:7.1-10; output-77:pdfua:7.1-11; output-77:pdfua:7.1-3; output-77:pdfua:7.1-8; output-78:pdfua:6.2-1; output-78:pdfua:7.1-10; output-78:pdfua:7.1-11; output-78:pdfua:7.1-3; output-78:pdfua:7.1-8; output-78:pdfua:7.2-34; output-79:pdfua:6.2-1; output-79:pdfua:7.1-10; output-79:pdfua:7.1-11; output-79:pdfua:7.1-3; output-79:pdfua:7.1-8; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-80:pdfua:6.2-1; output-80:pdfua:7.1-10; output-80:pdfua:7.1-11; output-80:pdfua:7.1-3; output-80:pdfua:7.1-8; output-81:pdfua:6.2-1; output-81:pdfua:7.1-10; output-81:pdfua:7.1-11; output-81:pdfua:7.1-3; output-81:pdfua:7.1-8; output-82:pdfua:6.2-1; output-82:pdfua:7.1-10; output-82:pdfua:7.1-11; output-82:pdfua:7.1-3; output-82:pdfua:7.1-8; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-34; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:320-&gt;0; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; output-1:pdfua:7.2-34; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:320-&gt;0; structure:role_map_count:9-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-09-scanned / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-10:pdfua:6.2-1; output-10:pdfua:7.1-10; output-10:pdfua:7.1-11; output-10:pdfua:7.1-3; output-10:pdfua:7.1-8; output-11:pdfua:6.2-1; output-11:pdfua:7.1-10; output-11:pdfua:7.1-11; output-11:pdfua:7.1-3; output-11:pdfua:7.1-8; output-12:pdfua:6.2-1; output-12:pdfua:7.1-10; output-12:pdfua:7.1-11; output-12:pdfua:7.1-3; output-12:pdfua:7.1-8; output-13:pdfua:6.2-1; output-13:pdfua:7.1-10; output-13:pdfua:7.1-11; output-13:pdfua:7.1-3; output-13:pdfua:7.1-8; output-14:pdfua:6.2-1; output-14:pdfua:7.1-10; output-14:pdfua:7.1-11; output-14:pdfua:7.1-3; output-14:pdfua:7.1-8; output-15:pdfua:6.2-1; output-15:pdfua:7.1-10; output-15:pdfua:7.1-11; output-15:pdfua:7.1-3; output-15:pdfua:7.1-8; output-16:pdfua:6.2-1; output-16:pdfua:7.1-10; output-16:pdfua:7.1-11; output-16:pdfua:7.1-3; output-16:pdfua:7.1-8; output-17:pdfua:6.2-1; output-17:pdfua:7.1-10; output-17:pdfua:7.1-11; output-17:pdfua:7.1-3; output-17:pdfua:7.1-8; output-18:pdfua:6.2-1; output-18:pdfua:7.1-10; output-18:pdfua:7.1-11; output-18:pdfua:7.1-3; output-18:pdfua:7.1-8; output-19:pdfua:6.2-1; output-19:pdfua:7.1-10; output-19:pdfua:7.1-11; output-19:pdfua:7.1-3; output-19:pdfua:7.1-8; output-19:pdfua:7.2-34; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-20:pdfua:6.2-1; output-20:pdfua:7.1-10; output-20:pdfua:7.1-11; output-20:pdfua:7.1-3; output-20:pdfua:7.1-8; output-21:pdfua:6.2-1; output-21:pdfua:7.1-10; output-21:pdfua:7.1-11; output-21:pdfua:7.1-3; output-21:pdfua:7.1-8; output-21:pdfua:7.2-34; output-22:pdfua:6.2-1; output-22:pdfua:7.1-10; output-22:pdfua:7.1-11; output-22:pdfua:7.1-3; output-22:pdfua:7.1-8; output-22:pdfua:7.2-34; output-23:pdfua:6.2-1; output-23:pdfua:7.1-10; output-23:pdfua:7.1-11; output-23:pdfua:7.1-3; output-23:pdfua:7.1-8; output-24:pdfua:6.2-1; output-24:pdfua:7.1-10; output-24:pdfua:7.1-11; output-24:pdfua:7.1-3; output-24:pdfua:7.1-8; output-25:pdfua:6.2-1; output-25:pdfua:7.1-10; output-25:pdfua:7.1-11; output-25:pdfua:7.1-3; output-25:pdfua:7.1-8; output-26:pdfua:6.2-1; output-26:pdfua:7.1-10; output-26:pdfua:7.1-11; output-26:pdfua:7.1-3; output-26:pdfua:7.1-8; output-27:pdfua:6.2-1; output-27:pdfua:7.1-10; output-27:pdfua:7.1-11; output-27:pdfua:7.1-3; output-27:pdfua:7.1-8; output-28:pdfua:6.2-1; output-28:pdfua:7.1-10; output-28:pdfua:7.1-11; output-28:pdfua:7.1-3; output-28:pdfua:7.1-8; output-29:pdfua:6.2-1; output-29:pdfua:7.1-10; output-29:pdfua:7.1-11; output-29:pdfua:7.1-3; output-29:pdfua:7.1-8; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-30:pdfua:6.2-1; output-30:pdfua:7.1-10; output-30:pdfua:7.1-11; output-30:pdfua:7.1-3; output-30:pdfua:7.1-8; output-31:pdfua:6.2-1; output-31:pdfua:7.1-10; output-31:pdfua:7.1-11; output-31:pdfua:7.1-3; output-31:pdfua:7.1-8; output-32:pdfua:6.2-1; output-32:pdfua:7.1-10; output-32:pdfua:7.1-11; output-32:pdfua:7.1-3; output-32:pdfua:7.1-8; output-33:pdfua:6.2-1; output-33:pdfua:7.1-10; output-33:pdfua:7.1-11; output-33:pdfua:7.1-3; output-33:pdfua:7.1-8; output-34:pdfua:6.2-1; output-34:pdfua:7.1-10; output-34:pdfua:7.1-11; output-34:pdfua:7.1-3; output-34:pdfua:7.1-8; output-35:pdfua:6.2-1; output-35:pdfua:7.1-10; output-35:pdfua:7.1-11; output-35:pdfua:7.1-3; output-35:pdfua:7.1-8; output-36:pdfua:6.2-1; output-36:pdfua:7.1-10; output-36:pdfua:7.1-11; output-36:pdfua:7.1-3; output-36:pdfua:7.1-8; output-37:pdfua:6.2-1; output-37:pdfua:7.1-10; output-37:pdfua:7.1-11; output-37:pdfua:7.1-3; output-37:pdfua:7.1-8; output-38:pdfua:6.2-1; output-38:pdfua:7.1-10; output-38:pdfua:7.1-11; output-38:pdfua:7.1-3; output-38:pdfua:7.1-8; output-39:pdfua:6.2-1; output-39:pdfua:7.1-10; output-39:pdfua:7.1-11; output-39:pdfua:7.1-3; output-39:pdfua:7.1-8; output-3:pdfua:6.2-1; output-3:pdfua:7.1-10; output-3:pdfua:7.1-11; output-3:pdfua:7.1-3; output-3:pdfua:7.1-8; output-40:pdfua:6.2-1; output-40:pdfua:7.1-10; output-40:pdfua:7.1-11; output-40:pdfua:7.1-3; output-40:pdfua:7.1-8; output-41:pdfua:6.2-1; output-41:pdfua:7.1-10; output-41:pdfua:7.1-11; output-41:pdfua:7.1-3; output-41:pdfua:7.1-8; output-42:pdfua:6.2-1; output-42:pdfua:7.1-10; output-42:pdfua:7.1-11; output-42:pdfua:7.1-3; output-42:pdfua:7.1-8; output-43:pdfua:6.2-1; output-43:pdfua:7.1-10; output-43:pdfua:7.1-11; output-43:pdfua:7.1-3; output-43:pdfua:7.1-8; output-44:pdfua:6.2-1; output-44:pdfua:7.1-10; output-44:pdfua:7.1-11; output-44:pdfua:7.1-3; output-44:pdfua:7.1-8; output-45:pdfua:6.2-1; output-45:pdfua:7.1-10; output-45:pdfua:7.1-11; output-45:pdfua:7.1-3; output-45:pdfua:7.1-8; output-46:pdfua:6.2-1; output-46:pdfua:7.1-10; output-46:pdfua:7.1-11; output-46:pdfua:7.1-3; output-46:pdfua:7.1-8; output-47:pdfua:6.2-1; output-47:pdfua:7.1-10; output-47:pdfua:7.1-11; output-47:pdfua:7.1-3; output-47:pdfua:7.1-8; output-48:pdfua:6.2-1; output-48:pdfua:7.1-10; output-48:pdfua:7.1-11; output-48:pdfua:7.1-3; output-48:pdfua:7.1-8; output-49:pdfua:6.2-1; output-49:pdfua:7.1-10; output-49:pdfua:7.1-11; output-49:pdfua:7.1-3; output-49:pdfua:7.1-8; output-4:pdfua:6.2-1; output-4:pdfua:7.1-10; output-4:pdfua:7.1-11; output-4:pdfua:7.1-3; output-4:pdfua:7.1-8; output-50:pdfua:6.2-1; output-50:pdfua:7.1-10; output-50:pdfua:7.1-11; output-50:pdfua:7.1-3; output-50:pdfua:7.1-8; output-51:pdfua:6.2-1; output-51:pdfua:7.1-10; output-51:pdfua:7.1-11; output-51:pdfua:7.1-3; output-51:pdfua:7.1-8; output-52:pdfua:6.2-1; output-52:pdfua:7.1-10; output-52:pdfua:7.1-11; output-52:pdfua:7.1-3; output-52:pdfua:7.1-8; output-53:pdfua:6.2-1; output-53:pdfua:7.1-10; output-53:pdfua:7.1-11; output-53:pdfua:7.1-3; output-53:pdfua:7.1-8; output-54:pdfua:6.2-1; output-54:pdfua:7.1-10; output-54:pdfua:7.1-11; output-54:pdfua:7.1-3; output-54:pdfua:7.1-8; output-55:pdfua:6.2-1; output-55:pdfua:7.1-10; output-55:pdfua:7.1-11; output-55:pdfua:7.1-3; output-55:pdfua:7.1-8; output-56:pdfua:6.2-1; output-56:pdfua:7.1-10; output-56:pdfua:7.1-11; output-56:pdfua:7.1-3; output-56:pdfua:7.1-8; output-57:pdfua:6.2-1; output-57:pdfua:7.1-10; output-57:pdfua:7.1-11; output-57:pdfua:7.1-3; output-57:pdfua:7.1-8; output-58:pdfua:6.2-1; output-58:pdfua:7.1-10; output-58:pdfua:7.1-11; output-58:pdfua:7.1-3; output-58:pdfua:7.1-8; output-59:pdfua:6.2-1; output-59:pdfua:7.1-10; output-59:pdfua:7.1-11; output-59:pdfua:7.1-3; output-59:pdfua:7.1-8; output-5:pdfua:6.2-1; output-5:pdfua:7.1-10; output-5:pdfua:7.1-11; output-5:pdfua:7.1-3; output-5:pdfua:7.1-8; output-60:pdfua:6.2-1; output-60:pdfua:7.1-10; output-60:pdfua:7.1-11; output-60:pdfua:7.1-3; output-60:pdfua:7.1-8; output-61:pdfua:6.2-1; output-61:pdfua:7.1-10; output-61:pdfua:7.1-11; output-61:pdfua:7.1-3; output-61:pdfua:7.1-8; output-62:pdfua:6.2-1; output-62:pdfua:7.1-10; output-62:pdfua:7.1-11; output-62:pdfua:7.1-3; output-62:pdfua:7.1-8; output-63:pdfua:6.2-1; output-63:pdfua:7.1-10; output-63:pdfua:7.1-11; output-63:pdfua:7.1-3; output-63:pdfua:7.1-8; output-63:pdfua:7.2-34; output-64:pdfua:6.2-1; output-64:pdfua:7.1-10; output-64:pdfua:7.1-11; output-64:pdfua:7.1-3; output-64:pdfua:7.1-8; output-65:pdfua:6.2-1; output-65:pdfua:7.1-10; output-65:pdfua:7.1-11; output-65:pdfua:7.1-3; output-65:pdfua:7.1-8; output-66:pdfua:6.2-1; output-66:pdfua:7.1-10; output-66:pdfua:7.1-11; output-66:pdfua:7.1-3; output-66:pdfua:7.1-8; output-67:pdfua:6.2-1; output-67:pdfua:7.1-10; output-67:pdfua:7.1-11; output-67:pdfua:7.1-3; output-67:pdfua:7.1-8; output-68:pdfua:6.2-1; output-68:pdfua:7.1-10; output-68:pdfua:7.1-11; output-68:pdfua:7.1-3; output-68:pdfua:7.1-8; output-69:pdfua:6.2-1; output-69:pdfua:7.1-10; output-69:pdfua:7.1-11; output-69:pdfua:7.1-3; output-69:pdfua:7.1-8; output-6:pdfua:6.2-1; output-6:pdfua:7.1-10; output-6:pdfua:7.1-11; output-6:pdfua:7.1-3; output-6:pdfua:7.1-8; output-70:pdfua:6.2-1; output-70:pdfua:7.1-10; output-70:pdfua:7.1-11; output-70:pdfua:7.1-3; output-70:pdfua:7.1-8; output-71:pdfua:6.2-1; output-71:pdfua:7.1-10; output-71:pdfua:7.1-11; output-71:pdfua:7.1-3; output-71:pdfua:7.1-8; output-72:pdfua:6.2-1; output-72:pdfua:7.1-10; output-72:pdfua:7.1-11; output-72:pdfua:7.1-3; output-72:pdfua:7.1-8; output-73:pdfua:6.2-1; output-73:pdfua:7.1-10; output-73:pdfua:7.1-11; output-73:pdfua:7.1-3; output-73:pdfua:7.1-8; output-74:pdfua:6.2-1; output-74:pdfua:7.1-10; output-74:pdfua:7.1-11; output-74:pdfua:7.1-3; output-74:pdfua:7.1-8; output-75:pdfua:6.2-1; output-75:pdfua:7.1-10; output-75:pdfua:7.1-11; output-75:pdfua:7.1-3; output-75:pdfua:7.1-8; output-76:pdfua:6.2-1; output-76:pdfua:7.1-10; output-76:pdfua:7.1-11; output-76:pdfua:7.1-3; output-76:pdfua:7.1-8; output-77:pdfua:6.2-1; output-77:pdfua:7.1-10; output-77:pdfua:7.1-11; output-77:pdfua:7.1-3; output-77:pdfua:7.1-8; output-78:pdfua:6.2-1; output-78:pdfua:7.1-10; output-78:pdfua:7.1-11; output-78:pdfua:7.1-3; output-78:pdfua:7.1-8; output-78:pdfua:7.2-34; output-79:pdfua:6.2-1; output-79:pdfua:7.1-10; output-79:pdfua:7.1-11; output-79:pdfua:7.1-3; output-79:pdfua:7.1-8; output-7:pdfua:6.2-1; output-7:pdfua:7.1-10; output-7:pdfua:7.1-11; output-7:pdfua:7.1-3; output-7:pdfua:7.1-8; output-80:pdfua:6.2-1; output-80:pdfua:7.1-10; output-80:pdfua:7.1-11; output-80:pdfua:7.1-3; output-80:pdfua:7.1-8; output-81:pdfua:6.2-1; output-81:pdfua:7.1-10; output-81:pdfua:7.1-11; output-81:pdfua:7.1-3; output-81:pdfua:7.1-8; output-82:pdfua:6.2-1; output-82:pdfua:7.1-10; output-82:pdfua:7.1-11; output-82:pdfua:7.1-3; output-82:pdfua:7.1-8; output-8:pdfua:6.2-1; output-8:pdfua:7.1-10; output-8:pdfua:7.1-11; output-8:pdfua:7.1-3; output-8:pdfua:7.1-8; output-9:pdfua:6.2-1; output-9:pdfua:7.1-10; output-9:pdfua:7.1-11; output-9:pdfua:7.1-3; output-9:pdfua:7.1-8; output-9:pdfua:7.2-34; structure:alt_text_count:563-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:320-&gt;0; structure:role_map_count:3-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-09-scanned --output lab/reproduction.json
```

### ua1-ref-2-10-form / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-33; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-33; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-ref-2-10-form / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.4-1; output-1:pdfua:7.2-25; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:6-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-ref-2-10-form --output lab/reproduction.json
```

### ua1-table-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.2-33; output-2:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:2-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-table-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; output-2:pdfua:6.2-1; output-2:pdfua:7.1-10; output-2:pdfua:7.1-11; output-2:pdfua:7.1-3; output-2:pdfua:7.1-8; output-2:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-table-001 --output lab/reproduction.json
```

### ua1-unicode-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-2; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; output-1:pdfua:7.21.4.2-2; output-1:pdfua:7.21.7-1; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations resave --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.2-2; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools ghostscript --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.1-2; output-1:pdfua:7.18.3-1; output-1:pdfua:7.18.5-1; output-1:pdfua:7.18.5-2; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:73-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations resave --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools pymupdf --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.18.5-1; output-1:pdfua:7.2-24; output-1:pdfua:7.2-30; output-1:pdfua:7.2-33; output-1:pdfua:7.2-34; structure:alt_text_count:80-&gt;0; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:73-&gt;0; structure:role_map_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations merge --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations resave --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua1-unicode-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:7.1-10; output-1:pdfua:7.1-11; output-1:pdfua:7.1-3; output-1:pdfua:7.1-8; output-1:pdfua:7.2-34; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:outline_count:1-&gt;0; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua1 --tools qpdf --operations split --fixtures ua1-unicode-001 --output lab/reproduction.json
```

### ua2-heading-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations resave --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations resave --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-heading-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-heading-001 --output lab/reproduction.json
```

### ua2-link-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations resave --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations resave --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-link-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-link-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations resave --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations resave --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-paragraph-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-paragraph-001 --output lab/reproduction.json
```

### ua2-table-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; output-2:pdfua:5-1; output-2:pdfua:6.2-1; output-2:pdfua:8.11.2-1; output-2:pdfua:8.2.1-1; output-2:pdfua:8.2.2-1; output-2:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations resave --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; output-2:pdfua:6.2-1; output-2:pdfua:8.11.1-2; output-2:pdfua:8.11.2-1; output-2:pdfua:8.2.1-1; output-2:pdfua:8.2.2-1; output-2:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations resave --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-table-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; output-2:pdfua:6.2-1; output-2:pdfua:8.11.1-2; output-2:pdfua:8.11.2-1; output-2:pdfua:8.2.1-1; output-2:pdfua:8.2.2-1; output-2:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-table-001 --output lab/reproduction.json
```

### ua2-unicode-001 / ghostscript / merge

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / ghostscript / resave

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations resave --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / ghostscript / split

Status: comparable
Tool version: 10.07.1 → 10.07.1
- new: none
- persistent: output-1:pdfua:5-1; output-1:pdfua:6.2-1; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools ghostscript --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / pymupdf / merge

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / pymupdf / resave

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations resave --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / pymupdf / split

Status: comparable
Tool version: 1.26.4 → 1.26.5
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools pymupdf --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / qpdf / merge

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations merge --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / qpdf / resave

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: none
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations resave --fixtures ua2-unicode-001 --output lab/reproduction.json
```

### ua2-unicode-001 / qpdf / split

Status: comparable
Tool version: qpdf version 12.3.2 → qpdf version 12.3.2
- new: none
- persistent: output-1:pdfua:6.2-1; output-1:pdfua:8.11.1-2; output-1:pdfua:8.11.2-1; output-1:pdfua:8.2.1-1; output-1:pdfua:8.2.2-1; output-1:pdfua:8.4.4-1; structure:document_language_present:True-&gt;False; structure:marked_pdf:True-&gt;False; structure:struct_tree_present:True-&gt;False; structure:title_present:True-&gt;False
- no_longer_observed: none

Reproduce after selecting the recorded tool versions and matching corpus:

```sh
pdfua-bench run --profiles ua2 --tools qpdf --operations split --fixtures ua2-unicode-001 --output lab/reproduction.json
```

Output numbers identify result order, not an inferred PDF page/object location.
No-longer-observed signals describe these two valid runs, not a universal repair claim.
