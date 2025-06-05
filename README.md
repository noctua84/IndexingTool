# Indexing Tool
This repository contains a toolset to index markdown files and store the results within mongodb  
It is designed to work with documentation sites like mkdocs and can provide limited search capabilities.  

In addition, there is a small nodejs API written in typescript that offers endpoints to query the indexed article data.  
For more information about the API and its usage refer to its [documentation](./searchtool/README.md)

There is a second SearchTool folder but this is only a rudimentary additional API version written in python, not more than a skeleton.  
Both indextool and searchtool are fully functional and tested.
