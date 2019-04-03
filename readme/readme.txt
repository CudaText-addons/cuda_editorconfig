plugin for CudaText.
supports EditorConfig system in editor. it reads/applies EditorConfig files 
for all opened files. supports the following options:

- indent_style
- indent_size; it sets both options "tab_size" and "indent_size"
- tab_width; it sets option "tab_size"

beginning with CudaText 1.77.6:
- end_of_line; it sets option "newdoc_ends" but doesn't change current file newlines
- charset; it sets option "newdoc_encoding" but doesn't change current file encoding
- trim_trailing_whitespace
- insert_final_newline


author: Alexey Torgashin (CudaText)
license: MIT
