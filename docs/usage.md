# Usage

Simple text transport application - probably not useful to many.

## Synopsis

```console
❯ vastaanottaa
usage: vastaanottaa send|recv given text-or-file salt-for-recv
```

## Version

```console
❯ vastaanottaa version
vastaanottaa v2023.6.12+parent.gf1b5cf69
```

## Help

```console
❯ vastaanottaa help
usage: vastaanottaa send|recv given text-or-file salt-for-recv
```

## Send

```console
❯ vastaanottaa send given "my text"
INFO: Loading content from parameter
DEBUG: timestamp embedded:  1686513245 (2023-06-11 19:54:05+00:00)
DEBUG: timestamp extracted: 1686513245 (2023-06-11 19:54:05+00:00)
---- BEGIN VASTAANOTTAA MESSAGE ----
Z0FBQUFBQmtoaVpkNUZfNVBQVm5vSE9jYlBqSEVDZ3pvdnFRZTg4cjZDSTQydnJmcmpTZ0pNanpM
Sm1tZWJpRXlQczc0REVmTGhfbC1rN1NIRkVfbFdxemMwcWF2X2xlVkE9PQ==
---- END VASTAANOTTAA MESSAGE ----

---- BEGIN VASTAANOTTAA SALT ----
b'D5CVqTmQvAfJLn2GIv9YpA==\n'
---- END VASTAANOTTAA SALT ----
```

## Receive

```console
❯ vastaanottaa recv given "Z0FBQUFBQmtoaVpkNUZfNVBQVm5vSE9jYlBqSEVDZ3pvdnFRZTg4cjZDSTQydnJmcmpTZ0pNanpM
Sm1tZWJpRXlQczc0REVmTGhfbC1rN1NIRkVfbFdxemMwcWF2X2xlVkE9PQ==
" 'D5CVqTmQvAfJLn2GIv9YpA==\n'
INFO: Loading content from parameter
my text
```

## Error Messages

Wrong parameter counts or unknown action:

```console
❯ vastaanottaa send given "my text" too many arguments
ERROR: unexpected count of parameters
usage: vastaanottaa send|recv given text-or-file salt-for-recv

❯ vastaanottaa send given
ERROR: unexpected count of parameters
usage: vastaanottaa send|recv given text-or-file salt-for-recv

❯ vastaanottaa unknown given 'some text'
ERROR: unexpected goal/action - use either send or recv
usage: vastaanottaa send|recv given text-or-file salt-for-recv
```


```console
❯ vastaanottaa recv given whatever
ERROR: salt missing for recv
usage: vastaanottaa send|recv given text-or-file salt-for-recv

❯ vastaanottaa send given ''
INFO: Loading content from parameter
ERROR: afraid of the void - content for message has zero bytes
usage: vastaanottaa send|recv given text-or-file salt-for-recv

❯ vastaanottaa send given test/fixtures/basic/empty.src
INFO: Reading content from file
ERROR: afraid of the void - content for message has zero bytes
usage: vastaanottaa send|recv given text-or-file salt-for-recv
```
