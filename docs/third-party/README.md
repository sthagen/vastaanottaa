# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/vastaanottaa/blob/default/sbom.json) with SHA256 checksum ([2cee74b6 ...](https://git.sr.ht/~sthagen/vastaanottaa/blob/default/sbom.json.sha256 "sha256:2cee74b60d4692f337a3f669e732ac6e0d6a113e5be259fd4e0dd660a3da6061")).
<!--[[[end]]] (checksum: 4f5bce0761bc8a735c4d60feffd811aa)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                                 | License                              | Author                                                                                       | Description (from packaging data)                                                                   |
|:-----------------------------------------------------|:--------------------------------------------------------|:-------------------------------------|:---------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [cryptography](https://github.com/pyca/cryptography) | [41.0.1](https://pypi.org/project/cryptography/41.0.1/) | Apache Software License; BSD License | The Python Cryptographic Authority and individual contributors <cryptography-dev@python.org> | cryptography is a package which provides cryptographic recipes and primitives to Python developers. |
<!--[[[end]]] (checksum: 3699b02c2b519bcec73f6d3a8a8d05bf)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                             | Version                                          | License     | Author                         | Description (from packaging data)                     |
|:-------------------------------------------------|:-------------------------------------------------|:------------|:-------------------------------|:------------------------------------------------------|
| [cffi](http://cffi.readthedocs.org)              | [1.15.1](https://pypi.org/project/cffi/1.15.1/)  | MIT License | Armin Rigo, Maciej Fijalkowski | Foreign Function Interface for Python calling C code. |
| [pycparser](https://github.com/eliben/pycparser) | [2.21](https://pypi.org/project/pycparser/2.21/) | BSD License | Eli Bendersky                  | C parser in Python                                    |
<!--[[[end]]] (checksum: 670b9b7cbd852440c4c48f5792c67d06)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
cryptography==41.0.1
└── cffi [required: >=1.12, installed: 1.15.1]
    └── pycparser [required: Any, installed: 2.21]
````
<!--[[[end]]] (checksum: 5ffa82036ac2e13f4ed564f7f19c4f14)-->
