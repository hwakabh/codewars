# codewars

Codewars solutions and test codes with Python/Node.js  

## Versioning

As specified with configuration files in each repository, the runtime versions of programming languages are below.  
Note that all the sources would be expected to run only with the specified versions, and we have not tested with other runtimes, which has the other versions.  

| Languages | Versions | Tools | Configurations |
| --- | --- | --- | --- |
| Python | 3.4.3 | pyenv | `./Python/.python-version` |
| Node.js | 13.12.0 | nodenv | `./node/.node-version` |

In this repository, we have expected to use some administration tools for controlling multiple runtime versions, so we need to install them first.  
Please refer the following links if you need further information with administration tools.  

- `pyenv`
  - Installation with OSX
    - `brew install pyenv`
  - For more
    - <https://github.com/pyenv/pyenv>
- `nodenv`
  - Installation with OSX
    - `brew install nodenv`
  - For more
    - <https://github.com/nodenv/nodenv>

***

## Testings

Since all the solutions would be required to be tested in Codewars, we have some container images to testings source codes.  
We could check the testing results after pushing solutions in this repository, with being executed by webhooks with CircleCI.  

- Docker Hub
  - <https://hub.docker.com/repository/docker/wakabh56/codewars-sandbox>

It's recommended to check the test result after you do testings locally.  
