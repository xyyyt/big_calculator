# bigint_calculator
Big integer calculator supporting very large numbers, complex arithmetic expressions with "+-*/%" operations and parentheses management.

## Dependencies
To compile bigint_calculator project, you need the following packages :
- googletest

```sh
apt-get install googletest
```

## Compilation
Build project by using the "build.sh" script (following example in "release" mode) :

```sh
./build.sh release
```

Then, compile "calculator" binary by using the MakeFile (previously generated with "build.sh" script) :

```sh
make calculator
```

## Run calculator
Execute "calculator" binary (located in "bin/release" directory) :

```sh
./calculator
```

## CRTI mode
CRTI (Calculator Run Time Information) is a mode to send some extra informations to several other local processes (to debug for example).

To do that :

1) Run "calculator" binary directly in project root by using "--local-crti" program option :
```sh
./bin/release/calculator --local-crti
```

2) Run "crti_client.py" script (located in "tools" directory) in project root by using "--local" program option :
```
./tools/crti_client.py --local
```

3) On "calculator" process, type arithmetic expression. You will see extra informations displayed on "crti_client.py" process

## Run tests
a) To execute all unit and integration tests :

```sh
make test
```

b) To execute all functional tests, use "test_launcher.py" script (located in "test/functional" directory) (following example in "release" mode if "calculator" binary was built in release) :

```sh
./test_launcher.py release
```