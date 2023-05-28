# codewars-python
Learning and improving Python one kata at a time.

## Build Python 3.11 Docker image
Use the build script in order to build the custom Python 3.11 Docker image
`andrerademacher/codewars-python311`.

```bash
container/build.sh
```

## Run command in container
The `container.sh` script makes running commands in the Docker container easy!
To open a shell, just add the "sh" command:
```bash
container.sh sh
```

The current Python version can be shown like this:
```bash
container.sh python --version
```

The pip binary is already present in the latest version supporting Python 3.11 .
To run any pip command, like `pip list`, just type:
```bash
container.sh pip list
```

After installing the dependencies, the unit test suite can be run
inside the container by calling the run_tests.sh shell script:
```bash
container.sh ./run_tests.sh
```