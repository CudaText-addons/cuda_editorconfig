plugin for CudaText.
supports EditorConfig system in editor. it reads/applies EditorConfig files 
for all opened files. supports the following options:

- "indent_style"; it sets CudaText option "tab_spaces" in memory
- "indent_size"; it sets CudaText options "tab_size" and "indent_size" in memory
- "tab_width"; it sets CudaText option "tab_size" in memory
- "end_of_line"; it changes line endings on file saving
- "charset"; it sets CudaText option "newdoc_encoding" but doesn't change current file encoding
- "trim_trailing_whitespace"; it's applied on file saving
- "insert_final_newline"; it's applied on file saving


author: Alexey Torgashin (CudaText)
license: MIT
